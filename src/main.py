import datetime

from flask import Flask, render_template
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
    _slug = db.Column(db.String(150), nullable=False)
    @property
    def slug(self):
        return self._slug
    @slug.setter
    def slug(self, value):
        self._slug = slugify(value)

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


@app.route("/article/<int:_id>")
def test(_id):
    page = Page.query.get_or_404(_id)
    context = {
        'title': page.title,
        'cards': [
            {'content': card.content, 'created': card.created_at, 'tags': ['definicion', 'trivia', 'historia de vida', 'ques eyo']}
        for card in page.cards]
    }
    return render_template('content.html', **context)



if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
