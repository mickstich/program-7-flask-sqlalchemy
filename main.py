from flask import Flask,request,redirect,url_for
from flask_migrate import Migrate
from flask_sqlalchemy import  SQLAlchemy
from flask.templating import render_template
from sqlalchemy import create_engine,MetaData,Column,Integer,String,Float,PrimaryKeyConstraint
a=Flask(__name__)
a.debug=True
a.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:12345@localhost:5432/db'
db = SQLAlchemy(a)
migrate=Migrate(a,db)

class table(db.Model):
    user_id=db.Column(db.Integer,primary_key=True)
    user_name = db.Column(db.String(20),nullable=False,unique=True)
    password = db.Column(db.String(20), nullable=False, unique=True)
    company_name = db.Column(db.String(20), nullable=False)
    phone_no = db.Column(db.String(50), nullable=False)
    status = db.Column(db.Boolean)

    def __repr__(self):
        return f"Name : {self.user_name}, password: {self.password},company: {self.company_name},number: {self.phone_no}"
@a.route('/')
def details():
    s=table.query.all()
    return render_template('details.html', s=s)
@a.route('/add')
def add():
    return render_template('add_details.html')

@a.route('/data',methods=["POST"])
def data():
          user_name = request.form.get("user_name")
          password = request.form.get("password")
          company_name = request.form.get("company_name")
          phone_no= request.form.get("phone_no")
          if user_name !='' and  password !='' and  company_name !='' and phone_no is not None:
              p=table(user_name=user_name,password=password,company_name=company_name,phone_no=phone_no)
              db.session.add(p)
              db.session.commit()
              return redirect('/')
          else:
              return redirect('/')
@a.route('/delete/<int:id>')
def erase(user_id):
    data = table.query.get(user_id)
    db.session.delete(data)
    db.session.commit()
    return redirect('/')










if __name__=='__main__':
    a.run(host="localhost",port=8000)
