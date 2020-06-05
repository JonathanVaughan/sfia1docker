from application import db
from application.models import Orders, Stock

db.drop_all()
db.create_all()
