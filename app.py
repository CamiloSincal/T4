from userdata import userdata
from flask import Flask,request,json,jsonify
from flask_cors import CORS,cross_origin
import json
import os


app = Flask(__name__)
CORS(app)

#Arreglo para almacenar los pacientes
arregloUsuarios = []
#Datos del administrador
adminUser = {
    "nombre":"Ingrid",
    "apellido":"Perez",
    "nombre_usuario":"admin",
    "contrasena":"1234"
}

@app.route('/',methods=['GET'])
def datos():
    return{
            "nombre" : 'Camilo Sincal',
            "carnet" : '202000605',
        }

@app.route('/login',methods=['GET'])
def metodo_Principal():
    user = request.args.get("nombre_usuario")
    userPassword = request.args.get("contrasena")
    if not validateUser(user):
        return jsonify({'state': 0, 'message':'Este usuario no existe'})
    if verifyUser(user,userPassword):
        return jsonify({'state': 1, 'message':'Sesion iniciada'})
    return jsonify({'state': 0, 'message':'Contrasena incorrecta'})

@app.route('/registro',methods=['POST'])
def reg_Pacientes():
    global arregloUsuarios
    content = request.get_json()
    name = content['nombre']
    lastname = content['apellido']
    bornDate = content['fecha_nacimiento']
    genre = content['sexo']
    username = content['nombre_usuario']
    if(validateUser(username)):
        return jsonify({'added':0,'message':'Este usuario ya existe'})
    password = content['contrasena']
    phoneNumber = content['telefono']
    n_Paciente = userdata(name,lastname,bornDate,genre,username,password,phoneNumber)
    arregloUsuarios.append(n_Paciente)
    return jsonify({'added':1,'message':'Su usuario ha sido registrado con exito'})

@app.route('/usuarios',methods=['GET'])
def obPacientes():
    arreglojson = []
    global arregloUsuarios
    for usuario in arregloUsuarios:
        arreglojson.append(usuario.get_json())
    return jsonify(arreglojson)

#Métodos de validación
def validateUser(username):
    global arregloUsuarios
    for usuario in arregloUsuarios:
        if usuario.username == username:
            return True
    return False

def verifyUser(username,password):
    global arregloUsuarios
    for usuario in arregloUsuarios:
        if usuario.username == username and usuario.password == password:
            return True
    return False
    

if __name__ == '__main__':
    puerto = int(os.environ.get('PORT',3000))
    app.run(host='0.0.0.0',port = puerto)