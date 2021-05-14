from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from crear_base import Pais

import json
import requests

# se genera en enlace al gestor de base de
# datos
# para el ejemplo se usa la base de datos
# sqlite
engine = create_engine('sqlite:///basepaises.db')


Session = sessionmaker(bind=engine)
session = Session()

# se crean objetos de tipo Pesona

# leer el archivo de datos

archivo = requests.get('https://pkgstore.datahub.io/core/country-codes/country-codes_json/data/616b1fb83cbfd4eb6d9e7d52924bb00a/country-codes_json.json') 

datos_json = archivo.json()
#print(datos_json)


for a in datos_json:
    #print(a)
    #print("1: %s 2: %s" % (a['CLDR display name'] , a['Capital']))
    p = Pais(nombre=a['CLDR display name'], capital=a['Capital'], continente=a['Continent'], \
        dial=a['Dial'], geonameId = a['Geoname ID'], itu = a['ITU'], lenguajes = a['Languages'], \
        esIndependiente = a['is_independent'])
    session.add(p)

# confirmar transacciones

session.commit()

