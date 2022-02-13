import os
from urllib.parse import quote_plus
from requests import get
from flask_cors import CORS, cross_origin
from flask_migrate import Migrate
from flask import Flask, jsonify, redirect, render_template, request, url_for, abort
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
load_dotenv()

app=Flask(__name__)#creer une instance de l'application
motdepasse="root"

app.config['SQLALCHEMY_DATABASE_URI']="postgresql://postgres:{}@localhost:5432/projetflask".format(motdepasse)
#connexion a la base de données
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db=SQLAlchemy(app)#creer une instance de Dase de données
#migrate =Migrate(app,db)
#migrate = Migrate(app, db)


class Categorie(db.Model):
    __tablename__='categories'
    id=db.Column(db.Integer,primary_key=True)
    libelle_categorie=db.Column(db.String(100),nullable=False)

    def __init__(self,libelle_categorie) :
         self.libelle_categorie=libelle_categorie
    
    def __init__(self,identity,libelle_categorie) :
         self.id=identity
         self.libelle_categorie=libelle_categorie
         
    def insert(self):
        db.session.add(self)
        db.session.commit()
  
    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
        'id': self.id,
        'libelle_categorie': self.libelle_categorie,
        }

db.create_all()
db.session.commit()
class Livre(db.Model):
    __tablename__='livres'
    id=db.Column(db.Integer, primary_key=True)
    isbn=db.Column(db.String(100),nullable=False)
    titre=db.Column(db.String(100),nullable=False)
    date_publication=db.Column(db.Date(),nullable=False)
    auteur=db.Column(db.String(100),nullable=False)
    editeur=db.Column(db.String(100),nullable=False)
    categorie_id=db.Column(db.Integer,db.ForeignKey('categories.id'),nullable=False)
    
    def __init__(self,isbn,titre,date_publication,auteur,editeur,categorie_id):
        self.isbn=isbn
        self.titre=titre
        self.date_publication=date_publication
        self.auteur=auteur
        self.editeur=editeur
        self.categorie_id=categorie_id
    
    def insert(self):
        db.session.add(self)
        db.session.commit()
  
    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
        'id': self.id,
        'isbn':self.isbn,
        'titre':self.titre,
        'date_publication':self.date_publication,
        'auteur':self.auteur,
        'editeur':self.editeur,
        'categorie_id': self.categorie_id,
        }


db.create_all()
db.session.commit()

def paginate(request):
    items = [item.format() for item in request]
    return items
   
   

@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Headers',
                            'Content-Type,Authorization,true')
    response.headers.add('Access-Control-Allow-Methods',
                            'GET,PUT,POST,DELETE,OPTIONS')
    return response


@app.route('/livres/<string:word>')
def search_book(word):
    mot = '%'+word+'%'
    livre = Livre.query.filter(Livre.titre.like(mot)).all()
    livre = paginate(livre)
    return jsonify({
        'livre': livre
    })
@app.route('/categories/<string:word>')
def search_categorie(word):
    mot = '%'+word+'%'
    categorie = Categorie.query.filter(Categorie.libelle_categorie.like(mot)).all()
    categorie = paginate(categorie)
    return jsonify({
        'livre': categorie
    })
@app.route('/categories')
def get_categories():
    categories = Categorie.query.all()
    categories = paginate(categories)
    return jsonify({
        'success': True,
        'Categorie': categories,
        'total_categories': len(categories)
    })
@app.route('/livres')
def get_livres():
    livres= Livre.query.all()
    livres= paginate(livres)
    return jsonify({
        'success':True,
        'Livres':livres,
        'total_livres': len(livres)
    })
@app.route('/categories/<int:id>')
def get_categorie(id):
    categorie = Categorie.query.get(id)
    if categorie is None:
        abort(404)
    else:
        return categorie.format()

@app.route('/livres/<int:id>')
def get_livre(id):
    livre = Livre.query.get(id)
    if livre is None:
        abort(404)
    else:
        return livre.format()

@app.route('/categories/<int:id>',methods=['DELETE'])
def delete_categorie(id):
    categorie = Categorie.query.get(id)
    categorie.delete()
    return jsonify({
        'success': True,
        'delete successfully': id,
    })

@app.route('/livres/<int:id>',methods=['DELETE'])
def delete_livres(id):
    livre =Livre.query.get(id)
    livre.delete()
    return jsonify({
        'success': True,
        'delete successfully': id,
    })

@app.route('/categories/<int:id>',methods=['PATCH'] )
def update_categorie(id):
    data = request.get_json()
    categorie= Categorie.query.get(id)
    if 'libelle_categorie' in data:
        categorie.libelle_categorie = data['libelle_categorie']
        #query.libelle_categorie = input()
        categorie.update()
    return jsonify({
        'success modify': True,
        'categorie': categorie.format(),
    })

@app.route('/livres/<int:id>',methods=['PATCH'] )
def update_livres(id):
    data = request.get_json()
    livre = Livre.query.get(id)
    try:
            if 'titre' in data and 'auteur' in data and 'editeur' in data:
                livre.titre = data['titre']
                livre.auteur = data['auteur']
                livre.editeur = data['editeur']
            livre.update()
    except:
            abort(404)
    return jsonify({
        'success modify': True,
        'livre': livre.format(),
    })

@app.route('/categories', methods=['POST'])
def add_categorie():
    data = request.get_json()
    idtf=libtf=False
    if 'id' in data :
        idt=data['id']
        idtf=True
    if 'libelle_categorie' in data:
        libelle = data['libelle_categorie']
        libtf=True
    if libtf and  idtf==False:
      categorie= Categorie(libelle)
    else:
        categorie= Categorie(idt,libelle)
    categorie.insert()
    count = categorie.query.count()
    return jsonify({
        'success': True,
        'added': categorie.format(),
        'total_categorie': count,
    })

@app.route('/livres', methods=['POST'])
def add_livre():
    data = request.get_json()
    isbn = data['isbn']
    titre = data['titre']
    date= data['date_publication']
    auteur = data['auteur']
    editeur = data['editeur']
    cateId = data['categorie_id']
    livre= Livre(isbn,titre,date,auteur,editeur,cateId)
    livre.insert()
    count = Livre.query.count()
    return jsonify({
        'success': True,
        'added': livre.format(),
        'total_livre': count,
    })

@app.route('/livres/categories/<int:id>')
def get_livre_from_categorie(id):
    books=db.session.query(Livre).join(Categorie).filter(Livre.categorie_id==id)
    books= paginate(books)
    return jsonify({
        'success':True,
        'Livres':books,
        'total_livres': len(books)
    })    
