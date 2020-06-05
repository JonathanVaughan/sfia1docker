from application import db
from datetime import datetime
from sqlalchemy import ForeignKey

class Orders(db.Model):
	orderid = db.Column(db.Integer, primary_key=True)
	first_name = db.Column(db.String(30), nullable=False)
	last_name = db.Column(db.String(30), nullable=False)
	number = db.Column(db.String(30), nullable=False)
	address = db.Column(db.String(100), nullable=False)
	pizzaid = db.Column(db.Integer, db.ForeignKey('stock.pizza_num')) # should this be stock
	order_quantity = db.Column(db.Integer, nullable=False) ####### integer
	#price = db.Column(db.Integer, nullable=True) ######## times by price per pizza
	orderstatus = db.Column(db.String(5), nullable=True, server_default='No') 
	
	

class Stock(db.Model):
	pizza_num = db.Column(db.Integer, primary_key=True)
	pizza_name = db.Column(db.String(40), nullable=False) ###########)
	#priceperpizza = db.Column(db.Integer, nullable=False)
	pizza = db.relationship('Orders', backref='nameofpizza', lazy=True)

