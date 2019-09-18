from flask import Blueprint, render_template
import models

edit = Blueprint("edit", __name__)


@edit.route("/edit/<page>")
def main(page):
    return render_template('edit.html', page=page)
