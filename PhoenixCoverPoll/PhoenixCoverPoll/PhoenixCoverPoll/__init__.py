from flask import Flask
from PhoenixCoverPoll.models import db

app = Flask(__name__)


app.secret_key = 'development key'
 
app.config["MAIL_SERVER"] = "smtp.yandex.com"
app.config["MAIL_PORT"] = 465
app.config["MAIL_USE_SSL"] = True
app.config["MAIL_USERNAME"] = 'test@fenixrostov.ru'
app.config["MAIL_PASSWORD"] = 'test'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

from PhoenixCoverPoll.views import mail
mail.init_app(app)
 
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://rootroot:12345@portal/pcp_base'

db.init_app(app)


