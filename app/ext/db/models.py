from app.ext.db import db, init_app


class Comentario(db.Model):
    __tablename__ = "comentario"
    
    id = db.Column(db.Integer(), primary_key=True)
    nome = db.Column(db.String(80), nullable=False)
    comentario = db.Column(db.String(100), nullable=False)

    