from flask import Flask
from flask import render_template
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)


dbconn = 'wojak:piwo@localhost:5432/cebula'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://'+str(dbconn)
db = SQLAlchemy(app)




@app.route("/")
def hello(): 
	# BEGIN equals largest key in db...
	query = "SELECT id FROM borrower ORDER BY id DESC LIMIT 1;"
	current = db.engine.execute(query)
	for c in current:
	    BEGIN = c[0]
	    return(str(BEGIN))


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
