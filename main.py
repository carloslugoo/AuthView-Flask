from flask import Flask, url_for, redirect, render_template, request, session
import mysql.connector
from flask import flash
from config import DevConfig
from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash
import userform

app = Flask(__name__)

app.config.from_object(DevConfig)

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="test"
)



@app.route('/bienvenido')
def bienvenido():
  datos = session['username']
  print(datos)
  return render_template('bienvenido.html', datos = datos)


@app.route('/', methods = ['GET', 'POST'])
def login():
  user = userform.User(request.form)
  username = user.username.data
  password = user.password.data
  if request.method == 'POST':
    mycursor = mydb.cursor()
    mycursor.execute('SELECT * FROM user WHERE username = %(username)s', {'username': username})
    data = mycursor.fetchall()
    if data:
      userdata = data[0]
      if userdata:
        passcheck = userdata[3]
    if userdata and check_password_hash(passcheck, password):
      return redirect(url_for('bienvenido'))
    else:
      flash("", "error")
  return render_template('login.html', user = user)

@app.route('/registro', methods = ['GET', 'POST'])
def registro():
  user = userform.User(request.form)
  if request.method == 'POST' and user.validate():
    password = createpassword(user.password.data)
    mycursor = mydb.cursor()
    sql = "SELECT * FROM user WHERE username = %s"
    val = [user.username.data]
    mycursor.execute(sql, val)
    data = mycursor.fetchall()
    create = True
    if data:
      flash("User existente", "existe_us")
      create = False
      print("a")
    elif not data:
      sql = "SELECT * FROM user WHERE email = %s"
      val = [user.email.data]
      mycursor.execute(sql, val)
      coe = mycursor.fetchall()
      if coe:
        create = False
        print("a")
        flash("Correo existente", "existe_co")
      elif user.password.data == user.confirmpassword.data and create == True:
        mycursor.execute('INSERT INTO user (username, email, password) VALUES (%s, %s, %s)',
                           (user.username.data,
                            user.email.data, password))
        mydb.commit()
        flash("Correcto", "success")
        return redirect(url_for('login'))
      else:
        flash("Error", "psw")
  return render_template('register.html', user = user)

def createpassword(password):
  return generate_password_hash(password)

if __name__=='__main__':
    app.run(debug = True, port= 8000)
