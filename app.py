import json
import uuid
from flask import Flask, render_template, url_for, request, redirect
from datetime import datetime
from forms import ContatoForm
from flask_wtf.csrf import CSRFProtect
from config import Config
from flask_mongoengine import MongoEngine

app = Flask(__name__)
app.config.from_object(Config) #pega todas as configurações da classe Config
app.debug = True

db = MongoEngine(app) # Conexao do banco

@app.route('/', methods=['POST', 'GET'])
def index():
	from models import Post

	posts = Post.objects
	print(Post.objects)

	if request.method == 'POST':
		hoje = datetime.now()
		p = Post(	
			content = request.values['content'],
			date = hoje.strftime('%d/%m/%Y %H:%M'),
		)
		p.save()
	# Buscando a lista de post
	posts = Post.objects.all()
	return render_template('index.html', titulo='Bonfim Blog', posts=posts)

@app.route('/contato/', methods=['GET', 'POST'])
def contato():
	form = ContatoForm(csrf_enabled=False)
	if form.validate_on_submit():
		print(form.data)
		return redirect('/')

	return render_template('contato.html', form=form)

@app.route('/sobre/')
def sobre():
	return 'Meu primeiro projeto Flask'

@app.route('/sobre/<nome>/')
def sobre_autor(nome):
	return 'Esse artigo foi escrito por %s' % nome 