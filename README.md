# API-Restful-Python #

## Introduction ##

Este es un ejemplo basico para la creción de un API Restful usando Python con 
el framework [Flask][1] y [Flask-RESTful][2], se utiliza dos EndPoint HTTP (GET y POST).

Este docuemento contiene instrucciones breves sobre la instalación de requerimientos,
instalación de los framework [Flask][1] y [Flask-RESTful][2]

For more information, see the

  * [Flask][1],
  * [Flask-RESTful][2],

[1]: http://flask.pocoo.org
[2]: http://flask-restful-cn.readthedocs.org/en/0.3.4/

## Installing ##

    sudo easy_install pip
    sudo pip install virtualenv

## Ejecutar el APPI RESTful ##

Primer paso, se debe acceder a nuestro proyecto 

    cd API-Restful-Python

A continuacion ejecutamos virtualenv:
    
    virtualenv flask

procedemos a instalar Flask y Flask-RESTful en nuestro proyecto

    flask/bin/pip install flask
    flask/bin/pip install flask-restful

asignamos permiso de ejecucion a nuestro archivo apprestful.py:
    
    chmod a+x apprestful.py

ejecutamos nuestro archivo:

    ./apprestful.py

Debe indicarnos que esta en ejecución nuestra API RESTful

    * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
    * Restarting with stat
    * Debugger is active!
    * Debugger pin code: 378-764-549

## Otras Configuraciones ##

si requieres de cambiar el puerto (default = 5000) por el puerto 9001:

abrimos el archivo apprestful.py y cambiamos esta linea:
      
      app.run(debug=True)

por esta otra:
      
      app.run(port = 9001, debug=True)


## Contact ##

Abel Mejía Hernández <abel.mejia.hdz@gmail.com>