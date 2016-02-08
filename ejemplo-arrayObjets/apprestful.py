#!flask/bin/python
from flask import Flask, request, jsonify
from flask_restful import reqparse, abort, Api, Resource
from functools import wraps

app = Flask(__name__)
# acepte croos domain
@app.after_request
def after_request(response):
  response.headers.add('Access-Control-Allow-Origin', '*')
  response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization,X-Requested-With')
  response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
  return response
api = Api(app)

UsersApp = [
    {
        'idUser': 1,
        'UDID': u'APA91BFCTY-UWGZYWSS2D3QTXO7VUBTAE1EUSON1BY9PY6K7M5VPXFSLL-JEBWYLPFFBCBFX_FBB6J0N1KRZX61WRQBKNX-AAUHZNKKWVSIV8D_GDOCSWIUDIYSVHL4JI3D7AEJLIU21',
        'NmbrDisp': u'iPhone 6s',
        'Device': u'iOS'
    },
    {
        'idUser': 2,
        'UDID': u'APA91BGZHYFQWUZMDS9S8FPGAC8W_8TO86W9E-BEZJ26PJLJDS8W8MB1ECBRBOFIQ3T9Z9ZDXFZK8GUQKBQT_J_JCODDLO75CNEYAONRTC0MVRVQGVVCI2I91YYKBBGEQ_IJK2KKFMGA',
        'NmbrDisp': u'Sony xperia Z1',
        'Device': u'Android'
    },
    {
        'idUser': 3,
        'UDID': u'APA91BF_EKVRMNRIVZUHZDMVS8XY3MDN9GC1ZMB_5R5UT55WP08HG3AGB4VJVSQE0IA7OY_IK8VNOR6EV_I-ZWRTPDJRHA7AQQ8215-T-IRKLVMDKUPAG6___6ZMOPGIPU8UKQDYTZ1P',
        'NmbrDisp': u'Motorola G3',
        'Device': u'Android'
    }
]

# se valida que el usuario y password sean los correctos
def check_auth(username, password):
    return username == 'admiin' and password == 'secret'
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

class Users(Resource):
    def get(self):
        # si es por Metodo GET se retorna todos los usuarios
        return UsersApp
    def post(self):
        # si es por POST se crea un nuevo usuario
        args = parser.parse_args()
        UsersApp.append({
            'idUser': args['idUser'],
            'UDID': args['UDID'],
            'NmbrDisp': args['NmbrDisp'],
            'Device': args['Device']}
        )
        # se retorna un status y el data que se recibio
        return {'status':'OK','data':args},201
# se define route
api.add_resource(Users,'/users')

if __name__ == '__main__':
    app.run(debug=True)




