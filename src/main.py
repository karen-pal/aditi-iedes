import datetime

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:////tmp/test.db"
db = SQLAlchemy(app)


class BaseModel(db.Model):
    __abstract__ = True
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=True)
    active = db.Column(db.Boolean, default=True)

    def __repr__(self):
        return "<{}: {}>".format(self.__class__.__name__, self.id)


class AdminUser(BaseModel):
    __tablename__ = 'admin'
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)


class Page(BaseModel):
    __tablename__ = 'page'
    title = db.Column(db.Text)
    cards = db.relationship("Card", backref="page", lazy=True)


class Card(BaseModel):
    __tablename__ = 'card'
    card_type = db.Column(db.String(80))
    page_id = db.Column(db.Integer, db.ForeignKey("page.id"))
    content = db.Column(db.Text)


class Tag(BaseModel):
    __tablename__ = 'tag'
    tag_name = db.Column(db.String(80))


tags = db.Table(
    "tags",
    db.Column("tag_id", db.Integer, db.ForeignKey("tag.id"), primary_key=True),
    db.Column("page_id", db.Integer, db.ForeignKey("page.id"), primary_key=True),
    db.Column("card_id", db.Integer, db.ForeignKey("card.id"), primary_key=True),
)


@app.route("/")
def main():
    return "<h1>hola</h1>"


@app.route("/test/<name>")
def test(name):
    return "Hello %s" % name


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
