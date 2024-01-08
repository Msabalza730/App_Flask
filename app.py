from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:password@localhost/contacts'

db = SQLAlchemy(app)

class Contacts(db.Model):
    __tablename__ = 'contacts'
    id=db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    phone = db.Column(db.String(15))
    email = db.Column(db.String(50))

    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

with app.app_context():
    db.create_all()

@app.route('/')
def Index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def add_contact():
    name = request.form['name']
    phone = request.form['phone']
    email = request.form['email']

    contact = Contacts(name, phone, email)
    db.session.add(contact)
    db.session.commit()


    #fetch a certain student2
    contactResult=db.session.query(Contacts).filter(Contacts.id==1)
    for result in contactResult:
        print(result.name)

    return render_template('success.html', data=name)

if __name__ == '__main__':
    app.run(debug=True)