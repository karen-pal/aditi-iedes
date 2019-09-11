import datetime

from slugify import slugify
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, abort

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
    __tablename__ = "admin"
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)


class Page(BaseModel):
    __tablename__ = "page"
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
    __tablename__ = "card"
    card_type = db.Column(db.String(80))
    page_id = db.Column(db.Integer, db.ForeignKey("page.id"))
    content = db.Column(db.Text)


class Tag(BaseModel):
    __tablename__ = "tag"
    tag_name = db.Column(db.String(80))


tags = db.Table(
    "tags",
    db.Column("tag_id", db.Integer, db.ForeignKey("tag.id"), primary_key=True),
    db.Column("page_id", db.Integer, db.ForeignKey("page.id"), primary_key=True),
    db.Column("card_id", db.Integer, db.ForeignKey("card.id"), primary_key=True),
)


def _page_to_ctx(page):
    return {
        "title": page.title,
        "id": page.id,
        "slug": page.slug,
        "created": page.created_at,
        "cards": [
            {
                "content": card.content,
                "created": card.created_at,
                "tags": ['definicion', 'historia', 'biografia'],
            }
            for card in page.cards
        ],
    }


@app.route("/")
def home():
    pages = Page.query.order_by(Page.id.desc()).all()
    context = [_page_to_ctx(page) for page in pages]
    return render_template("home.html", pages=context)


@app.route("/article/<slug>")
def article(slug):
    page = Page.query.filter_by(_slug=slug).first()
    if not page:
        abort(404)
    context = _page_to_ctx(page)
    return render_template("content.html", **context)

@app.route('/edit/<int:_id>')
def edit(_id):
    page = Page.query.get_or_404(_id)
    return render_template('edit.html', page=page)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
