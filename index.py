from flask import Flask
from flask import render_template, request, redirect
from flaskext.mysql import MySQL

app = Flask(__name__)

mysql = MySQL()
app.config['MYSQL_DATABASE_HOST']='localhost'
app.config['MYSQL_DATABASE_USER']='root'
app.config['MYSQL_DATABASE_PASSWORD']=''
app.config['MYSQL_DATABASE_DB']='viveregistro'
mysql.init_app(app)


@app.route('/')
def index():
    sql = "SELECT * FROM `plantas`"
    conexion = mysql.connect()
    cursor = conexion.cursor()
    cursor.execute(sql)
    plantas = cursor.fetchall()
    conexion.commit()
    return render_template('plantas/index.html', plantas = plantas)


@app.route('/crear')
def vistaCrear():
    return render_template('plantas/crear.html')

@app.route('/guardarUsuario', methods=['POST'])
def crearUsuario():
    _nombrePlanta = request.form['txtNombrePlanta']
    _descripcionPlanta = request.form['txtDescripcionPlanta']

    if(_nombrePlanta != '' or _descripcionPlanta != ''):
        sql = "INSERT INTO `plantas` (`id_planta`, `nombre_planta`, `descripcion_planta`) VALUES (NULL, %s, %s);"
        datosUsuario = (_nombrePlanta,_descripcionPlanta)
        conexion = mysql.connect()
        cursor = conexion.cursor()
        cursor.execute(sql, datosUsuario)
        conexion.commit()
        return redirect("/")
    else:
        return redirect("/crear")

@app.route('/eliminar/<int:id>')
def eliminarPlanta(id):
    conexion = mysql.connect()
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM `plantas` WHERE id_planta = %s",(id))
    conexion.commit()
    return redirect("/")

@app.route('/editar/<int:id>')
def editar(id):
    conexion = mysql.connect()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM `plantas` WHERE id_planta = %s",(id))
    planta = cursor.fetchall()
    conexion.commit()
    return render_template('plantas/editar.html', planta=planta)
    


@app.route('/editarUsuario', methods=['POST'])
def editarUsuario():
    _id_planta= request.form['txtId']
    _nombrePlanta = request.form['txtNombrePlanta']
    _descripcionPlanta = request.form['txtDescripcionPlanta']

    sql = "UPDATE plantas SET nombre_planta = %s , descripcion_planta = %s WHERE id_planta = %s"

    datosUsuario = (_nombrePlanta,_descripcionPlanta, _id_planta)
    conexion = mysql.connect()
    cursor = conexion.cursor()
    cursor.execute(sql, datosUsuario)
    conexion.commit()
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True, port=8005)