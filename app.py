from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from send_email import send_mail

app = Flask(__name__)


ENV = 'prod'

if ENV == 'dev':
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Samyto06@localhost/ToyotaRentDB'
else:
    app.debug = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://zvcgebxcdnutma:9a4cea7a41e491a6c362225819e558890ec1ca6ea834d85dfb9273fb02087147@ec2-107-21-120-104.compute-1.amazonaws.com:5432/d8v7mbo54m4b2i'


app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Feedback(db.Model):
    _tablename_ = 'feedback'
    id = db.Column(db.Integer, primary_key = True)
    costumer = db.Column(db.String(200), unique = True)
    comments = db.Column(db.Text(), unique = True)
    dealer = db.Column(db.String(200))
    rate = db.Column(db.Integer)
    
    def __init__(self, customer, dealer, comments, rate):
        self.costomer = customer
        self.comments = comments
        self.dealer = dealer
        self.rate = rate




@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        customer = request.form['customer']
        dealer = request.form['dealer']
        rate = request.form['rating']
        comments = request.form['comments']
        if customer == '' or dealer == '':
            return render_template('index.html', message='please fill the required fields')
        if db.session.query(Feedback).filter(Feedback.costumer == customer).count() == 0:
            data = Feedback(customer, dealer, comments, rate)
            db.session.add(data)
            db.session.commit()
            send_mail(customer, dealer,rate, comments)
            return render_template('success.html')
        return render_template('index.html', message='You already submitted the feedback')

if __name__ == '__main__':
    app.debug = True
    app.run()