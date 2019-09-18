import datetime
from flask_sqlalchemy import SQLAlchemy


from flask_admin.contrib.sqla import ModelView
from flask_admin.contrib.sqla.form import InlineModelConverter
from slugify import slugify

db = SQLAlchemy()


class PageModelView(ModelView):

    def on_model_change(self, form, model, is_created):
        model.slug = model.title

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
    page_id = db.Column(db.Integer, db.ForeignKey("page.id"))
    category_id = db.Column(db.Integer, db.ForeignKey("category.id"))
    content = db.Column(db.Text)

    def __repr__(self):
        return self.content[0:27] + '...'


class Category(BaseModel):
    __tablename__ = "category"
    tag_name = db.Column(db.String(80))
    cards = db.relationship("Card", backref="category", lazy=True)

    def __repr__(self):
        return self.tag_name
