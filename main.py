from flask import Flask, render_template, redirect, request, session, url_for, flash
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
import os
import random
from werkzeug.security import generate_password_hash, check_password_hash
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
from flask_login import  LoginManager, current_user, login_user, UserMixin, logout_user, login_required
from flask_paginate import Pagination, get_page_parameter
from datetime import datetime
import requests




app = Flask(__name__)
bootstrap = Bootstrap(app)
login = LoginManager(app)
app.config['SECRET_KEY']='gvpTrsDaf5vgzIzdzC2XKA'

#DATABASE location
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///webshopDB.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False #kako bi se koristilo manje memorije
app.config['SQLALCHEMY_ECHO'] = True
#db je objekt instanciran od klase SQLAlchemy, predstavlja bazu i pruza
#pristup svim funkcijama flask sqlalchemya
db = SQLAlchemy(app)



#DATABASE
class Category(db.Model):
   __tablename__= "category"
   id = db.Column(db.Integer, primary_key=True)
   name = db.Column(db.String, nullable=False)
   products = db.relationship("Product", backref="category", lazy="dynamic" )
  # image = db.Column(db.String, nullable=False)

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
 # color = db.Column(db.String, nullable=True)
   shopping_cart = db.relationship('Shopping_cart', backref='product',)
  

class ProductImage(db.Model):
   __tablename__= "product_image"
   id = db.Column(db.Integer, primary_key=True)
   product_id = db.Column(db.Integer, db.ForeignKey('product.id'))
   image = db.Column(db.String, nullable=False)
   

class Customer (UserMixin, db.Model):
   __tablename__= "customer"
   id = db.Column(db.Integer, primary_key=True)
   name = db.Column(db.String(100), nullable=False)
   surname = db.Column(db.String(100), nullable=False)
   email = db.Column(db.String, nullable=False)
   password = db.Column(db.Integer, nullable=False)
   telephone = db.Column(db.String, nullable=False)
   address = db.Column(db.String(200))
   shopping_cart = db.relationship('Shopping_cart', backref='customer', uselist=False)
   # order = db.relationship('Order', backref='customer')


   def check_password(self, password):
      return check_password_hash(self.password, password)

class Shopping_cart(db.Model):
   __tablename__= "shopping_cart"
   id = db.Column(db.Integer, primary_key=True)
   quantity = db.Column(db.Integer, nullable=False) 
   customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable=False)
   product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False,)


class Order(db.Model):
   __tablename__= "order"
   id = db.Column(db.Integer, primary_key=True)
   create_date = db.Column(db.Date)
   update_date = db.Column(db.Date)
   payment_method = db.Column(db.String, nullable=False)
   total = db.Column(db.Numeric(3,2), nullable=False)
   order_number = db.Column(db.Integer, nullable=False)
   customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable=False)
   products = db.relationship('Product', secondary=order_product, backref=db.backref('orders', lazy='dynamic'))

   
class RegistrationForm(FlaskForm):
   name = StringField('Name', validators=[DataRequired()])
   surname = StringField('Surname', validators=[DataRequired()])
   email = StringField('Email', validators=[DataRequired(), Email()])
   password = PasswordField('Password', validators=[DataRequired()])
   telephone =StringField('Telephone', validators=[DataRequired()])
   address = StringField('Addresse',validators=[DataRequired()])
   submit = SubmitField('Register', validators=[DataRequired()])

   def validate_email(self, email):
      customer = Customer.query.filter_by(email=email.data).first()
      if customer is not None:
         raise ValidationError('Please use a different email address.')

class LoginForm(FlaskForm):
   email = StringField('Email', validators=[DataRequired()])
   password = PasswordField('Password', validators=[DataRequired()])
   remember_me = BooleanField('Remember me')
   submit = SubmitField('Login')


class EditProfileForm(FlaskForm):
   name = StringField('Ime')
   surname = StringField('Prezime')
   telephone =StringField('Broj telefona')
   address = StringField('Adresa za dostavu')
   submit = SubmitField('Ažuriraj podatke')




@login.user_loader
def load_user(id):
    return Customer.query.get(int(id))

@app.route('/')
def index():
   #postavljanje vrijednosti brojača košarice(ikona)
   session["cartQuantity"]=0
   if current_user.is_authenticated:
     result=Shopping_cart.query.filter(Shopping_cart.customer_id==current_user.id).all()
     for i in result:
        session["cartQuantity"]= int(session["cartQuantity"]) + int(i.quantity )
      
   categories = Category.query.all()
   products =Product.query.all()
   productRandom = random.sample(products, k=16)
   return render_template('index.html', categories=categories, products=products, productRandom=productRandom)
 

@app.route('/product', methods=["GET","POST"] )
@app.route('/product/<id>', methods=["GET","POST"])
def product(id=None):
   page = request.args.get('page', 1, type=int)
   categories = Category.query.all()
   if request.method == "POST":
      search_word=request.form.get('keyword')
      # result = Product.query.filter(Product.web_name == search_word).order_by(Product.price.desc()).paginate(page=page, per_page=16)
      result = Product.query.filter(Product.web_name == search_word).paginate(page=page, per_page=16)
      return render_template('product.html', categories=categories, productList = result)  
   
   if id is None:
      result = Product.query.order_by(Product.price.desc()).paginate(page=page, per_page=16)
      return render_template('product.html', categories=categories, productList = result)   
   result = Product.query.filter(Product.category_id==id).paginate(page=page, per_page=16)
   return render_template('product.html', categories=categories, productList = result)


@app.route('/product_detail/<id>', methods=["GET","POST"])
def product_detail(id): 
   if request.method =="POST": 
      productId= request.form.get('productId')
      if current_user.is_authenticated:
         quantity = request.form.get('quantity')
         customer_id = current_user.id  

         #dohvacanje kosarice trenutnog kupca    
         shopping_cart_customer = Shopping_cart.query.filter(Shopping_cart.customer_id==customer_id, Shopping_cart.product_id==productId).first()
         if shopping_cart_customer is None:
            shopping_cart = Shopping_cart(quantity=quantity, customer_id = customer_id, product_id=productId)
            db.session.add(shopping_cart)
            db.session.commit()           
         else:
            # azuriranje kolicine dohvacene kosarice
            shopping_cart_customer.quantity= int(shopping_cart_customer.quantity)+ int(quantity)   
            db.session.add(shopping_cart_customer)
            db.session.commit()

         session["cartQuantity"] = int(session["cartQuantity"]) + int(quantity)        
      result = Product.query.filter(Product.id==productId).first()
      # images=ProductImage.query.filter(ProductImage.product_id==productId)
      return render_template('product_detail.html', product = result)

   else:
      result = Product.query.filter(Product.id==id).first()
      images=ProductImage.query.filter(ProductImage.product_id==id)
      return render_template('product_detail.html', product = result, images = images)


@app.route('/register', methods=['GET','POST'])
def register():
   if current_user.is_authenticated:
      return redirect(url_for('index'))
   form = RegistrationForm()
   if form.validate_on_submit():
      customer = Customer(name=form.name.data, surname=form.surname.data,email=form.email.data,  password=generate_password_hash(form.password.data), telephone=form.telephone.data, address=form.address.data)
      db.session.add(customer)
      db.session.commit()

      flash('Uspješno ste registrirani!')
      return redirect(url_for('login'))

   return render_template('register.html', title='Register', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
   if current_user.is_authenticated:
      return redirect(url_for('index'))
      
   form = LoginForm()
   if form.validate_on_submit():
      customer = Customer.query.filter_by(email=form.email.data).first()
      if customer is None or not customer.check_password(form.password.data):
         flash('Invalid email or password')
         return redirect(url_for('login'))
      login_user(customer, remember=form.remember_me.data)
      return redirect(url_for('index'))     
   return render_template('login.html', title='Sign in', form=form)


@app.route('/profile/<email>')
@login_required
def profile(email):
   customer = Customer.query.filter_by(email=email).first()
   result = Order.query.filter(Order.customer_id==customer.id).first() 
   return render_template('profile.html', customer=customer, result=result)


@app.route('/shopping_cart')
def shopping_cart():  
   if current_user.is_authenticated:
      result= db.session.query(Shopping_cart).join(Product).filter(Shopping_cart.customer_id==current_user.id).all()  
      total_amount= 0
      for i in result:
         total_amount= total_amount+(i.quantity*i.product.price)

      return render_template('shopping_cart.html', result=result, total_amount = total_amount)
   return render_template('shopping_cart.html')
   

@app.route('/logout')
def logout():
   logout_user()
   return redirect(url_for('index'))


@app.route('/order', methods=['GET','POST'])
@login_required
def order():  
   result= db.session.query(Shopping_cart).join(Product).filter(Shopping_cart.customer_id==current_user.id).all()   
   total_amount= 0
   if result  != None:
      for i in result:
         total_amount= total_amount+(i.quantity*i.product.price)

   
   form = EditProfileForm()
   
   if form.validate_on_submit():      
      current_user.name= form.name.data
      current_user.surname = form.surname.data
      # current_user.email = form.email.data
      current_user.telephone = form.telephone.data
      current_user.address = form.address.data
      # db.session.add(current_user)
      
      db.session.add(current_user._get_current_object())
      db.session.commit()
      # flash('Profil je ažuriran')
      return render_template('order.html', title='Podaci za dostavu', form=form, result=result, total_amount=total_amount)
   elif request.method == 'GET':
      form.name.data = current_user.name
      form.surname.data = current_user.surname
      # form.email.data = current_user.email
      form.telephone.data = current_user.telephone
      form.address.data = current_user.address

   return render_template('order.html', form=form, result=result, total_amount=total_amount)



@app.route('/order_complete')
def completeOrder():
   result= db.session.query(Shopping_cart).join(Product).filter(Shopping_cart.customer_id==current_user.id).all()  
   order_number = db.session.query(Order.order_number).count()
   total_amount= 0
   order_number = order_number + 1
   for i in result:
      total_amount= total_amount+(i.quantity*i.product.price) 

   order = Order(create_date=datetime.now(), update_date=datetime.now(), payment_method="Plaćanje pouzećem", total=total_amount, order_number=order_number, customer_id=current_user.id)
   db.session.add(order)
   db.session.commit()
 
   #povezivanje veze "many to many" tabele order sa tabelom product preko  relacijske tabele order_product

   for i in result:
       p = i.product
       order.products.append(p)

   db.session.commit()
      
   customer =  Customer.query.filter(Customer.id==current_user.id).first()
   send_simple_message(customer, result,order_number, total_amount)

   #brisanje košarice

   shopping_cart=Shopping_cart.query.filter(Shopping_cart.customer_id==current_user.id).delete()
   db.session.commit()

   session["cartQuantity"]=0
   
   return render_template('order.html')


# napravljeno samo za testiranje izgleda template-a koji korisniku stiže na mail za potvrdu narudzbe

@app.route('/orderOnmail')
def orderOnmail():
   result= db.session.query(Shopping_cart).join(Product).filter(Shopping_cart.customer_id==current_user.id).all()  
   total_amount= 0
   delivery_cost =30
   for i in result:
      total_amount= total_amount+(i.quantity*i.product.price)+ delivery_cost

   customer =  Customer.query.filter(Customer.id==current_user.id).first()
   # form = EditProfileForm()
   # form.name.data = current_user.name
   # form.surname.data = current_user.surname
   # # form.email.data = current_user.email
   # form.telephone.data = current_user.telephone
   # form.address.data = current_user.address

   return render_template('orderOnmail.html', form=customer, result=result, total_amount=total_amount)




def send_simple_message(customer, result, order_number, total_amount):


   ix_html = render_template("orderOnmail.html", form=customer, result=result, order_number=order_number, total_amount=total_amount ) 
   return requests.post(
      "https://api.mailgun.net/v3/sandbox94f4a2d744044e6d8531292a69293626.mailgun.org/messages",
		auth=("api", "847133b294adba022303af05788f4ca5-7cd1ac2b-df76f17b"),
		data={
         "from": "Tanja <mailgun@sandbox94f4a2d744044e6d8531292a69293626.mailgun.org>",
			"to": [customer.email],
			"subject": "Hello",
			"html": ix_html
       
      })


@app.route('/deleteItem/<id>')
def deleteItem(id):
   result=Shopping_cart.query.filter(Shopping_cart.id==id).first()
   db.session.delete(result)
   db.session.commit()

   session["cartQuantity"]=0
   result=Shopping_cart.query.filter(Shopping_cart.customer_id==current_user.id).all()
   for i in result:
      session["cartQuantity"]= int(session["cartQuantity"]) + int(i.quantity )

   return redirect(url_for('shopping_cart'))


@app.route('/about')
def about():  
   return render_template('about.html')

@app.route('/contact')
def contact():  
   return render_template('contact.html')




if __name__ == "__main__":
   app.run()


