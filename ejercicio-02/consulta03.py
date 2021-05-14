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

#consulta de los lenguajes de cada pais
print("====================================================================")
consulta3 = session.query(Pais.nombre, Pais.lenguajes).all()
print(consulta3)
print("====================================================================")