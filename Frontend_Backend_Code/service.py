#Importing the neccessary libraries
import mysql.connector
from flask import Flask, request, redirect,render_template,url_for, session,jsonify,escape
from random import randint
import json

#Create an app instance
app = Flask(__name__)
#Creating a secret key for Flask-sessions
app.secret_key = 'secret_key'

#At the end point '/'
#Call the method main
#Which renders index.html
@app.route('/')
def main():
        return render_template('index.html')

#At the end point '/login.html/'
#Call the method login
#Which renders login.html
@app.route('/login.html/')
def login():
        return render_template('login.html')

#At the endpoint '/register.html/'
#Call method register
#Which renders register.html
@app.route('/register.html/')
def register():
        return render_template('register.html')

#At the end point '/customer_login/'
#Call method customer_login which uses both GET and POST requests
#Which renders 'login.html'
@app.route('/customer_login/',methods=['GET','POST'])
def customer_login():
        msg =""
        #Check if "username" and "password" POST requests exist (user submitted form)
        if request.method =='POST' and  'username' in request.form and 'password' in request.form:
                #Creating variables for easy access and session data for access in other routes
                session['loginID'] = request.form['username']
                password = request.form['password']
                #Connecting to the database
                mydb = mysql.connector.connect(host="project.ckvyrailz12q.us-east-1.rds.amazonaws.com",user="tcss545",password="databaseproject",database="SQLProject",auth_plugin='mysql_native_password')
                #Created a cursor in our database
                mycursor = mydb.cursor()
                #Executing the query
                mycursor.execute('SELECT * FROM Customer WHERE CustomerID = %s AND Password=%s', (session['loginID'],password,));
                #Fetch one record
                account = mycursor.fetchone()
                #Check if account exists using MySQL server and rendering the template
                if account:
                   return render_template('Customer.html')
                else:
                   return "Invalid Creditianls"
        return render_template('login.html',msg=session['loginID'])

#At the end point '/manager_login/'
#Call method manager_login which uses both GET and POST requests
@app.route('/manager_login/',methods=['GET','POST'])
def manager_login():
        msg =""
        #Check if "username" and "password" POST requests exist (user submitted form) 
        if request.method =='POST' and  'username' in request.form and 'password' in request.form:
                #creating variables for easy access and session data for access in other routes   
                session['loginID'] = request.form['username']
                password = request.form['password']
                #connecting to the database     
                mydb = mysql.connector.connect(host="project.ckvyrailz12q.us-east-1.rds.amazonaws.com",user="tcss545",password="databaseproject",database="SQLProject",auth_plugin='mysql_native_password')
                #created a cursor in our database       
                mycursor = mydb.cursor()
                #executing the query     
                mycursor.execute('SELECT * FROM Manager WHERE ManagerID = %s AND Password=%s', (session['loginID'],password,));
                #fetch one record   
                account = mycursor.fetchone()
                #check if account exists using MySQL server and rendering the template              
                if account:
	                return render_template('Manager.html',msg=msg)
                else:
                    return "Invalid Crediantials"
            
#At end point '/manager_home/'
#Call method manager_home 
#Which renders 'Manager.html'
@app.route('/manager_home/',methods=['GET','POST'])
def manager_home():
            ManagerID = session['loginID']
            return render_template('Manager.html',msg=ManagerID)

#At end point '/customer_home/'                                                                                                                                                                                   #Call method customer_home  
#Which renders 'Customer.html' 
@app.route('/customer_home/',methods=['GET','POST'])
def customer_home():
            customerID = session['loginID']
            return render_template('Customer.html',msg=customerID)
        
#At end point '/customer_registration/'
#Call method customer_registration which uses both GET and POST requests
#Which renders 'register.html'
@app.route('/customer_registration/',methods=['GET','POST'])
def customer_registration():
        msg =""
        #Check if "country" and "password" POST requests exist (user submitted form)          
        if request.method =='POST' and 'country' in request.form and 'password' in request.form:
        #creating variables for easy access and session data for access in other routes                
            cust=randint(22222,99999)
            country = request.form['country']
            password = request.form['password']
            #Connecting to the database  
            mydb = mysql.connector.connect(host="project.ckvyrailz12q.us-east-1.rds.amazonaws.com",user="tcss545",password="databaseproject",database="SQLProject",auth_plugin='mysql_native_password')
            #Created a Cursor on Database
            mycursor = mydb.cursor()
            #Execting the Query
            mycursor.execute('CALL SQLProject.CustomerData(%s,%s,%s)',(cust,country,password,))
            #Updating the changes in our DB using Commit
            mydb.commit()
            msg = "Successfully Registered!Please notE your ID - "+str(cust)+". Please Login with your registered password and ID"
            return msg
        return render_template('register.html',msg=msg)

#At end point '/customer_update_password/'
#Call method customer_update_password which uses both GET and POST requests
#Which renders 'updateCustomerPassword.html'
@app.route('/customer_update_password/',methods=['GET','POST'])
def customer_update_password():
        msg=""
        #Check if "customerid" and "password" POST requests exist (user submitted form)  
        if request.method =='POST' and  'customerid' in request.form and 'password' in request.form :
                #Creating variables for easy access and session data for access in other routes                
                customerID = request.form['customerid']
                password = request.form['password']
                #Connecting to database
                if(customerID != "" and password != ""):
                    mydb = mysql.connector.connect(host="project.ckvyrailz12q.us-east-1.rds.amazonaws.com",user="tcss545",password="databaseproject",database="SQLProject",auth_plugin='mysql_native_password')
                    #Created a cursor Database
                    mycursor = mydb.cursor()
                    #Executing the Query
                    mycursor.execute('UPDATE Customer SET Password= %s WHERE CustomerID= %s',(password,customerID,));
                    #Commiting the changes
                    mydb.commit()
                    return "Successfully updated"
                else:
                    return "Please enter all the fields"
        return render_template('updateCustomerPassword.html',msg=msg)
        
#At the end point '/customer_update_country/'
#Call method customer_update_country which uses GET and POST requests
#Which renders 'updateCustomerCountry.html'
@app.route('/customer_update_country/',methods=['GET','POST'])
def customer_update_country():
        msg =""
        #Check if "customerid" and "country" POST requests exist (user submitted form)                   
        if request.method =='POST' and  'customerid' in request.form and 'country' in request.form:
                #Creating variables for easy access and session data for access in other routes 
                customerID = request.form['customerid']
                country = request.form['country']
                #Connecting to database
                if(customerID != "" and country != ""):
                    mydb = mysql.connector.connect(host="project.ckvyrailz12q.us-east-1.rds.amazonaws.com",user="tcss545",password="databaseproject",database="SQLProject",auth_plugin='mysql_native_password')
                    #Created a cursor on Database
                    mycursor = mydb.cursor()
                    #Executing the Query
                    mycursor.execute('UPDATE Customer SET Country= %s WHERE CustomerID= %s',(country,customerID,));
                    #Committing the changes
                    mydb.commit()
                    return "Successfully updated"
        return render_template('updateCustomerCountry.html',msg=msg)
        
#At the end point '/shop/'
#Call method shop which uses GET requests
#Which renders show.html
@app.route('/shop/',methods=['GET'])
def shop():
        #Connecting to the Database
        mydb = mysql.connector.connect(host="project.ckvyrailz12q.us-east-1.rds.amazonaws.com",user="tcss545",password="databaseproject",database="SQLProject",auth_plugin='mysql_native_password')
        #Created a cursor on Database
        mycursor = mydb.cursor()
        #Executing the query
        mycursor.execute('SELECT * FROM Item');
        #Fetching all the records
        items = mycursor.fetchall()
        return render_template('show.html', data=items)

#At the end point '/order_history/'
#Call method order_history which uses both GET and POST requests
#Which renders 'orderlist.html'
@app.route('/order_history/',methods=['GET','POST'])
def order_history():
        #Connecting to the Database
        mydb = mysql.connector.connect(host="project.ckvyrailz12q.us-east-1.rds.amazonaws.com",user="tcss545",password="databaseproject",database="SQLProject",auth_plugin='mysql_native_password')
        customerID = session['loginID']
        #Created cursor on Database
        mycursor = mydb.cursor()
        #Calling the method for getting the order details
        items = findHistory(customerID)
        #Passing the order details to the html page 
        return render_template('orderlist.html',data=items)

#At the end point '/manager_delete_customer/'
#Call method manager_delete_customer which uses both GET and POST
@app.route('/manager_delete_customer/',methods=['GET','POST'])
def manager_delete_customer():
        #Creating variables for easy access
        customerID = request.form['customerid']
        #Connecting to the Database
        mydb = mysql.connector.connect(host="project.ckvyrailz12q.us-east-1.rds.amazonaws.com",user="tcss545",password="databaseproject",database="SQLProject",auth_plugin='mysql_native_password')
        #Created a cursor on Database
        mycursor = mydb.cursor()
        #Executing the Query
        mycursor.execute('DELETE FROM Customer WHERE CustomerID=%s',(customerID,));
        #Committing the changes
        mydb.commit()
        return "successfully deleted"

#At the end point '/view_customer_details/'
#Call method view_customer_details which uses both GET and POST requests
#Which renders 'viewCustomer.html'
@app.route('/view_customer_details/',methods=['GET','POST'])
def view_customer_details():
        #Creating variables for easy access
        customerID = session['loginID']
        #Connecting to the Database
        mydb = mysql.connector.connect(host="project.ckvyrailz12q.us-east-1.rds.amazonaws.com",user="tcss545",password="databaseproject",database="SQLProject",auth_plugin='mysql_native_password')
        #Created a cursor on Database
        mycursor = mydb.cursor()
        #Executing the Query
        mycursor.execute('SELECT * FROM Customer WHERE CustomerID=%s',(customerID,));
        #Fetch all records
        user_details = mycursor.fetchall()
        return render_template('viewCustomer.html', data=user_details)

#At the end point '/view_manager_details/'
#Call method view_manager_details which uses both GET and POST requests
#Which renders 'viewManager.html'
@app.route('/view_manager_details/',methods=['GET','POST'])
def view_manager_details():
        #Creating variables for easy access  
        managerID = session['loginID']
        #Connecting to the Database
        mydb = mysql.connector.connect(host="project.ckvyrailz12q.us-east-1.rds.amazonaws.com",user="tcss545",password="databaseproject",database="SQLProject",auth_plugin='mysql_native_password')
        #Created a cursor on Database
        mycursor = mydb.cursor()
        #Executing the Query
        mycursor.execute('SELECT * FROM Manager WHERE ManagerID=%s',(managerID,));
        #Fetching all records
        user_details = mycursor.fetchall()
        return render_template('viewManager.html', data=user_details)
       
#At the end point '/manager_add_item/'
#Call method manager_add_item which uses both GET and POST requests
@app.route('/manager_add_item/',methods=['GET','POST'])
def manager_add_item():
        #Creating variables for easy access  
        unitPrice = request.form['unitprice']
        description = request.form['description']
        itemID=randint(100,666666)
        #Connecting to the Database 
        mydb = mysql.connector.connect(host="project.ckvyrailz12q.us-east-1.rds.amazonaws.com",user="tcss545",password="databaseproject",database="SQLProject",auth_plugin='mysql_native_password')
        #Created a cursor on Database   
        mycursor = mydb.cursor()
        #Executing the query using stored procedures
        mycursor.execute('CALL SQLProject.ItemData(%s,%s,%s)',(itemID,description,unitPrice,))
        #Commiting the changes
        mydb.commit()
        return "Item successfully addded , ItemCode : " +str(itemID)

#At end point '/manager_delete_item/'
#Call method manager_delete_item which uses both GET and POST requests
@app.route('/manager_delete_item/', methods=['GET', 'POST'] )
def manager_delete_item():
        #Creating variables for easy access   
        itemID = request.form['stockcode']
        #Connecting to the Database  
        mydb = mysql.connector.connect(host="project.ckvyrailz12q.us-east-1.rds.amazonaws.com",user="tcss545",password="databaseproject",database="SQLProject",auth_plugin='mysql_native_password')
        #Created a cursor on Database        
        mycursor = mydb.cursor()
        #Executing the query
        mycursor.execute('DELETE FROM Item WHERE StockCode = %s', (itemID, ))
        #Commiting the changes    
        mydb.commit()
        return "Item successfully deleted , ItemCode : " +str(itemID)

#At the end point '/viewAllCustomers/'
#Call method viewAllCustomers which uses GET and POST requests
#Which renders 'viewAllCustomers.html'
@app.route('/viewAllCustomers/',methods=['GET','POST'])
def viewAllCustomers():
        #Creating variables for easy access      
        managerID = session['loginID']
        #Connecting to the Database     
        mydb = mysql.connector.connect(host="project.ckvyrailz12q.us-east-1.rds.amazonaws.com",user="tcss545",password="databaseproject",database="SQLProject",auth_plugin='mysql_native_password')
        #Created a cursor on Database 
        mycursor = mydb.cursor()
        #Executing the query
        mycursor.execute('SELECT * FROM CustomerView');
        #Fetching all records
        user_details = mycursor.fetchall()
        return render_template('viewAllCustomers.html', data=user_details)

#At the end point '/viewNewCustomers/'
#Call method viewNewCustomers which uses GET and POST requests
#Which renders viewAllCustomers.html
@app.route('/viewNewCustomers/',methods=['GET','POST'])
def viewNewCustomers():
        #Creating variables for easy access         
        managerID = session['loginID']
        #Connecting to the Database  
        mydb = mysql.connector.connect(host="project.ckvyrailz12q.us-east-1.rds.amazonaws.com",user="tcss545",password="databaseproject",database="SQLProject",auth_plugin='mysql_native_password')
        #Created a cursor on Database  
        mycursor = mydb.cursor()
        #Executing the query             
        mycursor.execute('SELECT * FROM ConfirmationtoManager');
        #Fetching all records      
        user_details = mycursor.fetchall()
        return render_template('viewAllCustomers.html', data=user_details)

#At end point '/viewAllItems/'
#Call method viewAllItems which uses GET and POST requests
#Which renders 'viewAllItems.html'
@app.route('/viewAllItems/',methods=['GET','POST'])
def viewAllItems():
        #Creating variables for easy access 
        managerID = session['loginID']
        #Connecting to the Database         
        mydb = mysql.connector.connect(host="project.ckvyrailz12q.us-east-1.rds.amazonaws.com",user="tcss545",password="databaseproject",database="SQLProject",auth_plugin='mysql_native_password')
        #Created a cursor on Database   
        mycursor = mydb.cursor()
         #Executing the query         
        mycursor.execute('SELECT * FROM Item');
        #Fetching all records      
        user_details = mycursor.fetchall()
        return render_template('viewAllItems.html', data=user_details)

#This is a helper function for getting
#Stock Description,InvoiceNo for a particular customerID
def findHistory(*args):
        customerID = args[0]
        #Connecting to the Database  
        mydb = mysql.connector.connect(host="project.ckvyrailz12q.us-east-1.rds.amazonaws.com",user="tcss545",password="databaseproject",database="SQLProject",auth_plugin='mysql_native_password')
        #Created a cursor on Database     
        mycursor = mydb.cursor()
        #Executing the query        
        mycursor.execute('SELECT * FROM Invoice WHERE InvoiceNo IN (SELECT InvoiceNo FROM Customer_Invoice WHERE InvoiceNo=Invoice.InvoiceNo AND CustomerID=%s)',(customerID,));
        #Fetching all records     
        user_details = mycursor.fetchall()
        invnum = []
        for i in user_details:
            invnum.append(i[0])
        temp = {}
        for j in range(len(invnum)):
                #Executing the query and fetching the records
            mycursor.execute('SELECT StockCode FROM InvoiceDetails det, Invoice i WHERE det.InvoiceNo=i.InvoiceNo AND i.InvoiceNo=%s',(invnum[j],));
            code = mycursor.fetchall()
            arr = []
            for k in code:
                arr.append(k)
            temp[invnum[j]] = arr
            arr = []
        combineInvDes = {}
        for i,j in temp.items():
            linkStcDes = []
            for k in range(len(j)):
                for n in range(len(j[k])):
                        #Executing the query and fetching the records  
                    mycursor.execute('SELECT i.Description FROM Item i WHERE i.StockCode=%s',(j[k][n],));
                    details = mycursor.fetchall()
                    for l in details:
                        linkStcDes.append(l)
            combineInvDes[i] = linkStcDes
        return combineInvDes
                    
#Run the Flask APP on port=30036
app.run(debug=True, host='127.0.0.1', port=30036)
