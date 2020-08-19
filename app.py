from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from send_mail import send_mail

app = Flask(__name__)

ENV = 'dev'

if ENV == 'dev':
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://dmiyqajkecepak:ed9c11db5ee9ca1b806f04a17e5b0586eb19d81565915925367f5cdafe55529c@ec2-54-91-178-234.compute-1.amazonaws.com:5432/de40acr4p2215n'
else:
    app.debug = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://dmiyqajkecepak:ed9c11db5ee9ca1b806f04a17e5b0586eb19d81565915925367f5cdafe55529c@ec2-54-91-178-234.compute-1.amazonaws.com:5432/de40acr4p2215n'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Feedback(db.Model):
    __tablename__ = 'feedback'
    id = db.Column(db.Integer, primary_key=True)
    customer = db.Column(db.String(200))
    comments = db.Column(db.Text())

    def __init__(self, customer, comments):
        self.customer = customer
        self.comments = comments

'''   
db.create_all()
db.session.commit()
'''

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        customer = request.form['customer']
        comments = request.form['comments']
        if customer == '' :
            return render_template('index.html', message='Please enter required fields')
        else:
            data = Feedback(customer,comments)
            db.session.add(data)
            db.session.commit()
            send_mail(customer, comments)
            return render_template('success.html')


if __name__ == '__main__':
    app.run()
