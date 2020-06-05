from flask import render_template, redirect, url_for, request
from application import app, db
from application.models import Orders, Stock
from application.forms import OrderForm, StockForm, updateorderform


@app.route('/')
@app.route('/home')
def home():
	OrderData = Orders.query.all()
	Stockdata = Stock.query.all()
	return render_template('home.html', title="Home Page", orders=OrderData)

@app.route('/about')
def about():
	return render_template('about.html', title='about')

@app.route('/menu')
def menu():
	StockData = Stock.query.all()
	return render_template('menu.html', title="Home Page", stocks=StockData)

@app.route('/order', methods=['GET', 'POST'])
def order():	
	form = OrderForm()
	if request.method == 'POST':
		if form.validate_on_submit():
			orderData = Orders(
				first_name=form.first_name.data,
				last_name=form.last_name.data,
				number=form.number.data,
				address=form.address.data,
				pizzaid=form.pizzaid.data,
				order_quantity=form.order_quantity.data
			)
			
			db.session.add(orderData)
			db.session.commit()
			return redirect(url_for('home'))
		
	return render_template('order.html', title='Order', form=form)

@app.route('/stock', methods=['GET', 'POST'])
def stock():
	form = StockForm()
	if request.method == 'POST':
		if form.validate_on_submit():
			stockData = Stock(
				pizza_name=form.pizza_name.data
			)
			db.session.add(stockData)
			db.session.commit()
			return redirect(url_for('menu'))
	return render_template('stock.html', title='stock', form=form)
	
@app.route('/updateorder/<id>/', methods=['GET', 'POST'])
def updateorder(id):
	print("hello")
	form = updateorderform()
	orderstatus = Orders.query.filter_by(orderid=id).first()
	if form.validate_on_submit():
		orderstatus.orderstatus = form.orderstatus.data
		db.session.commit()
		return redirect(url_for('home'))
	return render_template('orderstatus.html', title='orderstatus', form=form)

@app.route('/updateorder/<id>/delete', methods=['GET', 'POST'])
def deleteorder(id):
	delorder = Orders.query.filter_by(orderid=id).first()
	db.session.delete(delorder)
	db.session.commit()
	return redirect(url_for('home'))


