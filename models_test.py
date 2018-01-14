from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey
#from yourapplication.database import Base


app = Flask (__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bank.db'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root@localhost/bankDB'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:123@localhost/bankDB'
db = SQLAlchemy(app)

class Customer(db.Model):
	__tablename__ = 'customer'
	id = db.Column (db.Integer)
	name = db.Column (db.String(60))
	email = db.Column(db.String(60), primary_key=True)
	password = db.Column(db.String(60))
	address = db.Column (db.String(60))
	aadhar = db.Column (db.Integer)
	pan = db.Column (db.Integer)
	contact = db.Column (db.Integer)
	amount = db.Column (db.Float)


	def __init__(self, name, email, password, address, aadhar, pan, contact, amount):
		self.name = name
		self.email = email
		self.password = password
		self.address = address
		self.aadhar = aadhar
		self.pan = pan
		self.contact = contact
		self.amount = amount


class Transaction(db.Model):
	__tablename__ = 'transaction'
	trans_id = db.Column(db.Integer, primary_key = True)
	cust_name = db.Column(db.String(60))
	cust_email = db.Column(db.String(60), ForeignKey('customer.email'))
	account = db.Column(db.Integer)
	deposit = db.Column(db.Integer)
	withdrawal = db.Column(db.Integer)


	def __init__(self, cust_name, cust_email, account, deposit, withdrawal):
		self.cust_name = cust_name
		self.cust_email = cust_email
		self.account = account
		self.deposit = deposit
		self.withdrawal = withdrawal

		
try:
	print"************************************* CREATE_ALL *****************************************"
	db.create_all()
except Exception as exp:
	print "exp:", exp

"""
print "saving"
customer = Customer('John', 'John Avenue', 98765, 5678, 1234)
	#save = Customer(name, address, aadhar, pan, phone)
db.session.add(customer)
db.session.commit() 

print "done"
"""


