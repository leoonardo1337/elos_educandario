from flask import Flask, render_template, request
from flask_mail import Mail, Message

app = Flask(__name__)

app.config['MAIL_SERVER']='smtp.educandarioelos.com.br'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = 'noreply@educandarioelos.com.br'
app.config['MAIL_PASSWORD'] = 'NoEdu@2022'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_DEBUG'] = True
app.config['MAIL_SUPPRESS_SEND'] = False
app.config['TESTING'] = False
app.config['DEBUG'] = False

mail = Mail(app)

@app.route('/')
def root():
    return render_template('index.html')

@app.route("/mensagem")
def mensagem():
  nome = request.args.get('name')
  assunto = request.args.get('subject')
  email = request.args.get('email')
  mensagem = request.args.get('message')
  sender = 'noreply@educandarioelos.com.br'

  msg = Message(sender= sender, recipients= ['contato@educandarioelos.com.br'])
  msg.html = "<small>Mensagem enviada pelo formulário do site</small><br/><br/><strong>Enviado por:.</strong> " + nome + ".<br/><strong>Email:.</strong> "+ email +"<br/><strong>Mensagem:. </strong>" + mensagem
  msg.subject = assunto
  mail.send(msg)
  return render_template('mensagem.html')

app.run()