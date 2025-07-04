from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import Base

class Usuario(Base):
    __tablename__ = 'usuarios'
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    tipo_usuario = Column(String(20), nullable=False)
    fecha_registro = Column(DateTime, default=datetime.utcnow)

    resultados = relationship('Resultado', back_populates='usuario')

class Senal(Base):
    __tablename__ = 'senales'
    id = Column(Integer, primary_key=True, index=True)
    descripcion = Column(Text)
    url_video = Column(Text)
    fecha_captura = Column(DateTime, default=datetime.utcnow)

    resultados = relationship('Resultado', back_populates='senal')

class Resultado(Base):
    __tablename__ = 'resultados'
    id = Column(Integer, primary_key=True, index=True)
    usuario_id = Column(Integer, ForeignKey('usuarios.id'))
    senal_id = Column(Integer, ForeignKey('senales.id'))
    texto_traducido = Column(Text)
    fecha_procesamiento = Column(DateTime, default=datetime.utcnow)

    usuario = relationship('Usuario', back_populates='resultados')
    senal = relationship('Senal', back_populates='resultados')
