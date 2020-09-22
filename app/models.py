from datetime import datetime
from app import db
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
from flask_login import  LoginManager, current_user, login_user, UserMixin, logout_user, login_required
from flask_paginate import Pagination, get_page_parameter
from werkzeug.security import generate_password_hash, check_password_hash

class Category(db.Model):
   __tablename__= "category"
   id = db.Column(db.Integer, primary_key=True)
   name = db.Column(db.String, nullable=False)
   products = db.relationship("Product", backref="category", lazy="dynamic" )
 

order_product = db.Table('order_product',  
   db.Column('order_id', db.Integer, db.ForeignKey('order.id')),
   db.Column('product_id', db.Integer, db.ForeignKey('product.id')))

class Product(db.Model):
   __tablename__= "product"
   id = db.Column(db.Integer, primary_key=True)
   name = db.Column(db.String, unique=True, nullable=False)
   web_name = db.Column(db.String, unique=True)
   category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=True)
   price = db.Column(db.Numeric(3,2), nullable=False)
   image = db.Column(db.String, nullable=False)
   images = db.relationship('ProductImage', backref='product')
   shopping_cart = db.relationship('Shopping_cart', backref='product',)
  

class ProductImage(db.Model):
   __tablename__= "product_image"
   id = db.Column(db.Integer, primary_key=True)
   product_id = db.Column(db.Integer, db.ForeignKey('product.id'))
   image = db.Column(db.String, nullable=False)
   

class User (UserMixin, db.Model):
   __tablename__= "user"
   id = db.Column(db.Integer, primary_key=True)
   name = db.Column(db.String(100), nullable=False)
   surname = db.Column(db.String(100), nullable=False)
   email = db.Column(db.String, nullable=False)
   password = db.Column(db.Integer, nullable=False)
   telephone = db.Column(db.String, nullable=False)
   address = db.Column(db.String(200))
   shopping_cart = db.relationship('Shopping_cart', backref='user', uselist=False)
   # order = db.relationship('Order', backref='user')


   def check_password(self, password):
      return check_password_hash(self.password, password)

class Shopping_cart(db.Model):
   __tablename__= "shopping_cart"
   id = db.Column(db.Integer, primary_key=True)
   quantity = db.Column(db.Integer, nullable=False) 
   user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
   product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False,)


class Order(db.Model):
   __tablename__= "order"
   id = db.Column(db.Integer, primary_key=True)
   create_date = db.Column(db.Date)
   update_date = db.Column(db.Date)
   payment_method = db.Column(db.String, nullable=False)
   total = db.Column(db.Numeric(3,2), nullable=False)
   order_number = db.Column(db.Integer, nullable=False)
   user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
   products = db.relationship('Product', secondary=order_product, backref=db.backref('orders', lazy='dynamic'))