from datetime import datetime 
from app import db

#modelos
class Referencia(db.Model):
    #modelos ern singular y creacion de tablas en plural
    __tablename__="referencias"
    idReferencia = db.Column(db.Integer, primary_key = True )
    nombre=db.Column(db.String(100), unique = True)
    descripcion=db.Column(db.String(120), unique = True)
    referencia=db.Column(db.String(128), unique = True) 
    imagen=db.Column(db.String(100))
    
class Prenda(db.Model):
    __tablename__="prendas"
    idPrenda = db.Column(db.Integer, primary_key = True )
    idVenta= db.Column(db.Integer, db.ForeignKey('ventas.idVenta')) 
    idReferencia= db.Column(db.Integer, db.ForeignKey('referencias.idReferencia')) 
    talla = db.Column(db.String(120), unique = True)
    fecha=db.Column(db.DateTime, default = datetime.utcnow)
    estado=db.Column(db.String(120), unique = True)
    color=db.Column(db.String(120), unique = True)
    precio=db.Column(db.Double(120), unique = True)

class Venta(db.Model):
    __tablename__="ventas"
    idVenta = db.Column(db.Integer, primary_key = True )
    idPrenda= db.Column(db.Integer, db.ForeignKey('prendas.idPrenda')) 
    idPreventa= db.Column(db.Integer, db.ForeignKey('preventas.idPreVenta')) 
    fecha=db.Column(db.DateTime, default = datetime.utcnow)
    codigo=db.Column(db.Integer(100))
    estado=db.Column(db.String(60), unique = True)
    

class PreVenta(db.Model):
    __tablename__="preventas"
    idPreVenta = db.Column(db.Integer, primary_key = True )
    idPrenda= db.Column(db.Integer, db.ForeignKey('prendas.idPrenda')) 
    fecha=db.Column(db.DateTime, default = datetime.utcnow)
    fechaEnvio=db.Column(db.DateTime, default = datetime.utcnow)
    estado=db.Column(db.String(60), unique = True)

class Administrador(db.Model):
    __tablename__="administradores"
    idAdmin= db.Column(db.Integer, primary_key = True )
    nombre=db.Column(db.String(100), unique = True)
    apellido=db.Column(db.String(100), unique = True)
    usuario=db.Column(db.String(100), unique = True)
    contrasena=db.Column(db.String(100), unique = True)
    compContrasena=db.Column(db.String(100), unique = True)

