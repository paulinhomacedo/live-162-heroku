from flask import Flask, redirect, render_template, request

from app.ext import config

# from flask_migrate import Migrate
# from flask_sqlalchemy import SQLAlchemy


# db = SQLAlchemy()
# migrate = Migrate()

# class Comentario(db.Model):
#     __tablename__ = "comentario"
    
#     id = db.Column(db.Integer(), primary_key=True)
#     nome = db.Column(db.String(80), nullable=False)
#     comentario = db.Column(db.String(100), nullable=False)

def create_app():
    app = Flask(__name__)
    
    config.init_app(app)      
     

    # app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://iaruekluxvivvw:fc6de78932d36f9a5b445be932df26cf0161548c6199bb50d227ef89f3664b52@ec2-107-22-245-82.compute-1.amazonaws.com:5432/d619ea6dvsk702'
    # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    # app.db = db.init_app(app)
    # Migrate(app,db)



    

    # @app.route('/')
    # def index():
    #     #return "ola liveeeeeeex"
    #     return render_template(
    #         "index.html",
    #         comments = Comentario.query.order_by(
    #             Comentario.id.desc()).limit(20).all()
    #     )

    # @app.route('/post', methods=['POST'])  
    # def post():
    #     form = request.form
    #     comment = Comentario(
    #         nome=form["nome"],
    #         comentario=form["comentario"]
    #     )
    #     db.session.add(comment)
    #     db.session.commit()

    #     return redirect('/')

    
    return app     
    

