from flask import Blueprint, render_template, abort
from models import Page

home = Blueprint("home", __name__)

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


@home.route("/")
@home.route("/home.html")
def home_main():
    pages = Page.query.order_by(Page.id.desc()).all()
    context = [_page_to_ctx(page) for page in pages]    
    return render_template('home.html', pages=context)


@home.route("/article/<slug>")
def article(slug):
    page = Page.query.filter_by(_slug=slug).first()
    if not page:
        abort(404)
    context = _page_to_ctx(page)
    return render_template("content.html", **context)
