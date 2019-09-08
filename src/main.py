from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

class AdminUser(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(80), unique=True, nullable=False)
  email = db.Column(db.String(120), unique=True, nullable=False)

  def __repr__(self):
    return '<AdminUser %r>' % self.username

@app.route('/')
def main():
    return '<h1>hola</h1>'

@app.route('/test/<name>')
def test(name):
    return 'Hello %s' %name

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
