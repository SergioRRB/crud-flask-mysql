from flask import Flask, render_template, request, redirect, url_for
import os
import database as db

template_dir = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
template_dir = os.path.join(template_dir, 'src', 'views')

app = Flask(__name__, template_folder=template_dir)

# Rutas de la app 
@app.route('/')
def home():
    cursor = db.database.cursor()
    cursor.execute("SELECT * FROM users")
    myresult = cursor.fetchall()
    # Convertir los datos a diccionarios
    insertObject = []
    columnNames = [column[0] for column in cursor.description]
    for record in myresult:
        insertObject.append(dict(zip(columnNames, record)))
    cursor.close()
    return render_template('index.html', data=insertObject)

# Ruta para guardar usuarios en la BDD
@app.route('/user', methods=['POST'])
def addUser():
    usuario = request.form['usuario']
    nombre = request.form['nombre']
    contrasena = request.form['contrasena']

    if usuario and nombre and contrasena:
        cursor = db.database.cursor()
        sql = "INSERT INTO users (usuario, nombre, contraseña) VALUES (%s,%s,%s)"
        data = (usuario, nombre, contrasena)
        cursor.execute(sql, data)
        db.database.commit()
    return redirect(url_for('home'))

@app.route('/delete/<string:id>')
def delete(id):
    cursor = db.database.cursor()
    sql = "DELETE FROM users WHERE id=%s"
    data = (id,)

    cursor.execute(sql, data)
    db.database.commit()
    return redirect(url_for('home'))

@app.route('/edit/<string:id>', methods=['POST'])
def edit(id):
    usuario = request.form['usuario']
    nombre = request.form['nombre']
    contrasena = request.form['contrasena']

    if usuario and nombre and contrasena:
        cursor = db.database.cursor()
        sql = "UPDATE users SET usuario=%s, nombre=%s, contraseña=%s WHERE id=%s"
        data = (usuario, nombre, contrasena, id)
        cursor.execute(sql, data)
        db.database.commit()
    return redirect(url_for('home'))

if __name__ == '__main__':
    # Para correr el servidor en
    app.run(debug=True, port=4000)
