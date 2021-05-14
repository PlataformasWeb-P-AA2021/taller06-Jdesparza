from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_, or_ # se importa el operador and y or

# se importa la clase(s) del 
# archivo genera_tablas
from crear_base import Pais

# se genera enlace al gestor de base de
# datos
# para el ejemplo se usa la base de datos
# sqlite
engine = create_engine('sqlite:///basepaises.db')


Session = sessionmaker(bind=engine)
session = Session()

# Obtener todos los registros de 
# la entidad paises 
#paises = session.query(Pais).all()

#consulta de los paises del continente americano
#para lo cual se consultara tando del conteniente norte americano y sudamericano para sacar todos los paises
print("====================================================================")
consulta1 = session.query(Pais).filter(or_(Pais.continente=="NA", Pais.continente=="SA")).all()
print(consulta1)
print("====================================================================")
