from flask import render_template, redirect, url_for, abort, request, flash, send_file
from app import application, db
from app.models import User
from app.forms import UserForm
from app import mail
from flask_mail import Message
import datetime
import qrcode
import io

@application.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@application.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Validate data using UserForm
        form = UserForm(request.form)
        if not form.validate():
            for field, errors in form.errors.items():
                for error in errors:
                    flash(f"Ошибка в поле «{form[field].label.text}»: {error}")
            return render_template("index.html")

        time = datetime.datetime.now()
        name = form.name.data
        course = form.course.data
        faculty = form.faculty.data
        grade = form.grade.data
        email = form.email.data
        reason = form.reason.data

        try:
            user = User(time=time, name=name, course=course, faculty=faculty, grade=grade, email=email, reason=reason)
            db.session.add(user)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            application.logger.error(f"Database error during registration: {e}")
            flash("Не удалось оставить заявку на участие! Проверьте корректность введенных данных.")
            return render_template("index.html")

        # Try sending email, make failures non-blocking
        mail_failed = False
        if application.config.get("MAIL_SERVER") and application.config.get("MAIL_USERNAME"):
            try:
                url = url_for("qr_code", user_id=user.id, _external=True)
                msg = Message(
                    subject="Приглашение на карьерную неделю",
                    sender=application.config.get("MAIL_USERNAME"),
                    recipients=[email]
                )
                msg.html = render_template("mail.html", name=name, url=url)
                mail.send(msg)
            except Exception as e:
                application.logger.error(f"Failed to send email to {email}: {e}")
                mail_failed = True
        else:
            application.logger.warning("SMTP not configured, skipping email.")
            mail_failed = True

        return redirect(url_for("success", name=name, user_id=user.id, mail_failed=1 if mail_failed else 0))

    return render_template("index.html")

@application.route("/success")
def success():
    name = request.args.get("name")
    user_id = request.args.get("user_id")
    mail_failed = request.args.get("mail_failed") == "1"
    return render_template("success.html", name=name, user_id=user_id, mail_failed=mail_failed)

@application.route("/qr/<int:user_id>")
def qr_code(user_id):
    user = User.query.get(user_id)
    if not user:
        abort(404)
    
    qr = qrcode.QRCode(version=1, box_size=10, border=4)
    qr.add_data(str(user.id))
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    
    img_io = io.BytesIO()
    img.save(img_io, 'PNG')
    img_io.seek(0)
    return send_file(img_io, mimetype='image/png')

@application.route("/scanner")
def scanner():
    return render_template("scanner.html")

@application.route("/check", methods=["GET", "POST"])
def check():
    user_id = request.args.get("id")
    user = None
    if user_id:
        try:
            user = User.query.get(int(user_id))
        except (ValueError, TypeError):
            pass

    if request.method == "POST":
        if user:
            user.visited = True
            user.visited_time = datetime.datetime.now()
            db.session.commit()
            flash("Пользователь отмечен в системе!")
        else:
            flash("Пользователь не найден!")
            return redirect(url_for("scanner"))

    return render_template("check_user.html", user=user)