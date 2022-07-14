from flask import Flask, render_template, request
from flask_mail import Mail, Message

app = Flask(__name__)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'leofonsil@gmail.com'
app.config['MAIL_PASSWORD'] = 'ozvfmchzicnvlyug'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

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

# recipient = email que vai receber o email
  msg = Message(sender= email, recipients= ['leo.fonseca1337@icloud.com'])
  msg.html = "<small>Mensagem enviada pelo formulário do site</small><br/><strong>Enviado por:.</strong> " + nome + ".<br/><strong>Mensagem:. </strong>" + mensagem
  msg.subject = assunto
  mail.send(msg)
  return render_template('mensagem.html')

app.run()