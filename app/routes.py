from flask import render_template, redirect, url_for, abort, request, flash
from app import application, db
from app.models import User, Company
from app import mail
from flask_mail import Message
import datetime

@application.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@application.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")

@application.route("/reg-clients", methods=["GET", "POST"])
def clients():
    if request.method == "POST":
        time = datetime.datetime.now()
        name = request.form.get("name")
        university = request.form.get("university")
        course = request.form.get("course")
        faculty = request.form.get("faculty")
        grade = request.form.get("grade")
        email = request.form.get("email")
        vk = request.form.get("vk")
        tg = request.form.get("tg")
        _from = request.form.get("from")

        try:
            user = User(time=time, university=university, name=name, course=course, faculty=faculty, grade=grade, email=email, vk_ref=vk, tg_ref=tg, reason=_from)
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
    
    return render_template("reg-clients.html")

@application.route("/reg-company", methods=["GET", "POST"])
def companies():
    if request.method == "POST":
        time = datetime.datetime.now()
        name = request.form.get("name")
        contact = request.form.get("contact")
        comp_name = request.form.get("comp_name")
        description = request.form.get("description")

        comp = Company(time=time, name=name, contact=contact, comp_name=comp_name, description=description)
        db.session.add(comp)
        db.session.commit()

        return redirect(url_for("success_comp", comp_name=comp_name))
    
    return render_template("reg-company.html")

@application.route("/success")
def success():
    name = request.args.get("name")
    return render_template("success.html", name=name)

@application.route("/success-comp")
def success_comp():
    name = request.args.get("comp_name")
    return render_template("success-comp.html", name=name)

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