from app.ext.db import db
from app.ext.db.models import Comentario
from flask import Blueprint, current_app, redirect, render_template, request

blueprint = Blueprint('home', __name__, url_prefix='/')


@blueprint.route('/')
def index():
    # return 'Hello, Mundaoo!'
    # return render_template('index.html')
    return render_template(
            "index.html",
            comments = Comentario.query.order_by(
                Comentario.id.desc()).limit(20).all()
        ) 

@blueprint.route('/post', methods=['POST'])  
def post():
    form = request.form
    comment = Comentario(
        nome=form["nome"],
        comentario=form["comentario"]
    )
    db.session.add(comment)
    db.session.commit()

    return redirect('/')  
    


