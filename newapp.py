from flask import Flask,render_template,request
from mysql import connector

app=Flask(__name__)





mydb = connector.connect(
    host="localhost",
    user="root",
    passwd="9960551687",
    database="bankdb")

mycur = mydb.cursor()

        

@app.route('/')
def index():
	
	 
	name='name'
	email='email'
	 
	query="insert into users(name,email) values(%s,%s)"
	val=(name,email)
	mycur.execute(query,val)	
	mydb.commit()
		
		
	return render_template('index.html')

if __name__ == '__main__':
	app.run(debug=True)
		

