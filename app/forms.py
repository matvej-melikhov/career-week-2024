from wtforms import Form, StringField, SelectField, TextAreaField
from wtforms.validators import DataRequired

class UserForm(Form):
    name = StringField("Фамилия Имя", description="Фамилия Имя", validators=[DataRequired()])
    course = SelectField("Курс", choices=[1, 2, 3, 4], description="Курс", validators=[DataRequired()])
    faculty = SelectField(
        "Факультет",
        choices=["ФКТИ", "ФРТ", "ФЭЛ", "ФЭА", "ФИБС", "ГФ", "ИНФРОТЕХ"],
        description="Факультет",
        validators=[DataRequired()]
    )
    grade = SelectField(
        "Направление подготовки",
        choices=["Бакалавриат", "Магистратура", "Аспирантура"],
        description="Направление подготовки",
        validators=[DataRequired()]
    )
    email = StringField("Почтовый адрес", description="Почтовый адрес", validators=[DataRequired()])
    reason = TextAreaField("Откуда узнали о мероприятии", description="Откуда узнали о нас?", validators=[DataRequired()])