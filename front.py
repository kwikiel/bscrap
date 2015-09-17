from flask import Flask
from flask import render_template
from flask.ext.sqlalchemy import SQLAlchemy
from myspider import Borrower
app = Flask(__name__)


dbconn = 'wojak:piwo@localhost:5432/cebula'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://'+str(dbconn)
db = SQLAlchemy(app)

@app.route("/")
def hello(): 
	# BEGIN equals largest key in db...
	brw = Borrower.query.limit(5)
	return render_template("index.html", borrowers = brw)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
