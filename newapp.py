from flask import Flask,render_template,request
from mysql import connector
 
app=Flask(__name__)





mydb = connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="bankdb")

mycur = mydb.cursor()

        

@app.route('/',methods=['GET','POST'])
def index():
	if request.method=='POST':

	
	 
		name=request.form['name']
		email=request.form['email']
		 
		query="insert into users(name,email) values(%s,%s)"
		val=(name,email)
		mycur.execute(query,val)	
		mydb.commit()
		return'data inserted sucessfuly'
		
	return render_template('index.html')

if __name__ == '__main__':
	app.run(debug=True)
		

