from app import db

class User(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    time = db.Column(db.DateTime())
    name = db.Column(db.String())
    course = db.Column(db.Integer())
    faculty = db.Column(db.String())
    grade = db.Column(db.String())
    email = db.Column(db.String())
    reason = db.Column(db.Text())

    visited = db.Column(db.Boolean(), default=False)
    visited_time = db.Column(db.DateTime())

    def __repr__(self):
        return f"{self.name}"