from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, validators, IntegerField
from wtforms.validators import DataRequired
from application.models import Orders 

class OrderForm(FlaskForm):
        first_name = StringField('First Name',validators=[DataRequired()])
        last_name = StringField('Last Name',validators=[DataRequired()])
        number = StringField('number',validators=[DataRequired()])
        address = StringField('Address',validators=[DataRequired()])
        pizzaid = IntegerField('Pizza',validators=[DataRequired()])
        order_quantity = IntegerField('Quantity',validators=[DataRequired()])
        # last_name = StringField('Last Name', [validators.DataRequired()], [validators.Length(min=2, max=30)])
        # number = StringField('Phone no.', [validators.DataRequired()], [validators.Length(min=2, max=30)])
        # address = StringField('Address', [validators.DataRequired()], [validators.Length(min=2, max=30)])
        # pizza = StringField('Pizza', [validators.DataRequired()], [validators.Length(min=2, max=30)])
        # order_quantity = StringField('Quantity', [validators.DataRequired()], [validators.Length(min=2, max=30)])
        submit = SubmitField("Place Order")
	# last_name = StringField('Last Name',
	# 	validators=[
        #                 DataRequired(),
        #                 Length(min=3, max=30)
        #         ])
	# number = StringField('Phone no.',
	# 	validators=[ 
	# 		DataRequired(),
	# 		Length(min=5, max=20)
	# 	])
	# address = StringField('Address',
        #         validators=[
        #                 DataRequired(),
        #                 Length(min=5, max=140)
	# 	])
	# pizza = StringField('Pizza',
        #         validators=[
        #                 DataRequired(),
        #                 Length(min=5, max=140)
	# 	])
	# quantity = StringField('Quantity',
	# 	StringField=[
	# 		DataRequired()
	# 	])

class StockForm(FlaskForm):
        pizza_name = StringField('Name', validators=[DataRequired()])
        submit = SubmitField('Add')
        #pizzaid = StringField('Pizza',
         #       validators=[
          #              DataRequired(),
           #             Length(min=5, max=140)
            #    ])
	#stock_quantity = StringField('Quantity',
#		 validators=[
#                        DataRequired()
#                ])
#        submitf = SubmitField('Add Stock')
class updateorderform(FlaskForm):
        orderstatus = StringField('order', [validators.DataRequired()])
        submit = SubmitField('Delivered')
#def order_query():
 #       return Orders.query



