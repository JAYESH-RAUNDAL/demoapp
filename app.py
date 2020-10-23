from flask import Flask,render_template,request
from flask_mysqldb import MySQL 	
 
app=Flask(__name__)



app.config['MySQL_HOST']='localhost'
app.config['MySQL_USER']='root'                 
app.config['MySQL_PASSWORD']='' 
app.config['MySQL_DB']='bankdb'
mysql=MySQL(app)
mycur=mysql.connection.cursor() 
        

@app.route('/',methods=['GET',' POST'])
def index():
	if request.method=='POST':
		userdetails=request.form
		name=userdetails['name']
		email=userdetails['email']
		mycur.execute("insert into users(name,email) values(%s,%s)"(name,email))
		mydb.commit()
		mycur.close()
		return 'success'
	return render_template('index.html')

if __name__ == '__main__':
	app.run(debug=True)
		

