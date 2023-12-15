from flask import render_template, redirect, url_for, abort, request, flash
from app import application, db
from app.models import User
from app import mail
from flask_mail import Message
import datetime

@application.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@application.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        time = datetime.datetime.now()
        name = request.form.get("name")
        course = request.form.get("course")
        faculty = request.form.get("faculty")
        grade = request.form.get("grade")
        email = request.form.get("email")
        _from = request.form.get("from")

        try:
            user = User(time=time, name=name, course=course, faculty=faculty, grade=grade, email=email, reason=_from)
            db.session.add(user)
            db.session.commit()

            url = f"https://api.qrserver.com/v1/create-qr-code/?size=350x350&data={user.id}"

            msg = Message(subject="Приглашение на карьерную неделю", sender="info@sokt-profcom.ru", recipients=[email])
            msg.html = render_template("mail.html", name=name, url=url)
            mail.send(msg)
        except:
            flash("Не удалось оставить заявку на участие! Проверьте корректность введенных данных.")
        else:
            return redirect(url_for("success", name=name))

    return render_template("index.html")

@application.route("/success")
def success():
    name = request.args.get("name")
    return render_template("success.html", name=name)

@application.route("/scanner")
def scanner():
    return render_template("scanner.html")

@application.route("/check", methods=["GET", "POST"])
def check():
    user_id = request.args.get("id")
    user = User.query.get(user_id)

    if request.method == "POST":
        user.visited = True
        user.visited_time = datetime.datetime.now()
        db.session.commit()
        # flash("Пользователь отмечен в системе!")

    return render_template("check_user.html", user=user)