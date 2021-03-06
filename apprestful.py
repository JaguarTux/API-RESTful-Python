#!flask/bin/python
from flask import Flask, request, jsonify
from flask_restful import reqparse, abort, Api, Resource
from functools import wraps
from pymongo import MongoClient

client = MongoClient('localhost',27017)
db = client.Device
collection = db.UsersApp

app = Flask(__name__)
# acepte croos domain
@app.after_request
def after_request(response):
  response.headers.add('Access-Control-Allow-Origin', '*')
  response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization,X-Requested-With')
  response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
  return response
api = Api(app)

# se valida que el usuario y password sean los correctos
def check_auth(username, password):
    return username == 'admin' and password == 'secret'
# metodo para devolver el mesaje de acceso no autorizado
def unauthorized():
    message = {'message': "Unauthorized Access."}
    resp = jsonify(message)
    resp.status_code = 401
    resp.headers['WWW-Authenticate'] = 'Basic realm="restful"'
    return resp
# metodo para leer la autenticacion cuando un cliente hace una peticion
def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        # si no manda credenciales se niega el acceso
        if not auth: 
            return unauthorized()
        # si envian las credenciales de validan que sean correctas si no se niega el acceso 
        elif not check_auth(auth.username, auth.password):
            return unauthorized()
        return f(*args, **kwargs)
    return decorated

# clase para incorporar el oAuth para el api Restful
class Resource(Resource):
    method_decorators = [requires_auth]

parser = reqparse.RequestParser()
parser.add_argument('idUser')
parser.add_argument('UDID')
parser.add_argument('NmbrDisp')
parser.add_argument('Device')
def getUserAll():
    UsersApp=[]
    cursor = collection.find()
    for docUser in cursor:
        UsersApp.append({"idUser": docUser['idUser'],"UDID": docUser['UDID'],"NmbrDisp": docUser['NmbrDisp'],"Device":docUser['Device']})
    return UsersApp
class Users(Resource):
    def get(self):
        # si es por Metodo GET se retorna todos los usuarios
        return getUserAll() 
    def post(self):
        # si es por POST se crea un nuevo usuario
        args = parser.parse_args()
        collection.insert({'idUser': args['idUser'],'UDID': args['UDID'],'NmbrDisp': args['NmbrDisp'],'Device': args['Device']})
        # se retorna un status y el data que se recibio
        return {'status':'OK','data':args},201
# se define route
api.add_resource(Users,'/users')

if __name__ == '__main__':
    app.run(debug=True)




