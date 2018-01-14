from flask import Flask
from flask_mail import Mail, Message
app = Flask(__name__)

app.config['MAIL_SERVER'] = 'gaurav3.weavebytes@gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
app.config.from_pyfile('config.cfg')

mail = mail(app)


@app.route('/')
def index():
    msg = message('hello', sender='gauravkumarall@gmail.com', recipients=['13mcl007@'])
    mail.send(msg)
    return 'Message Send!'


if __name__ == '__main__':
    app.run(debug=True)
