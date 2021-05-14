from sqlalchemy import create_engine

engine = create_engine('sqlite:///basepaises.db')

from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


from sqlalchemy import Column, Integer, String, Float

class Pais(Base):
    __tablename__ = 'paises'
    
    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    capital = Column(String)
    continente = Column(String)
    dial = Column(String)
    geonameId = Column(Float)
    itu = Column(String)
    lenguajes = Column(String)
    esIndependiente = Column(String)

    def __repr__(self):
        return "Pais: nombre=%s capital=%s continente:%s dial:%s geonameId:%.1f itu:%s lenguajes:%s esIndependiente:%s" % (
                          self.nombre, 
                          self.capital, 
                          self.continente,
                          self.dial,
                          self.geonameId,
                          self.itu,
                          self.lenguajes,
                          self.esIndependiente)


Base.metadata.create_all(engine)