from pydantic import BaseModel
from datetime import datetime
from typing import Optional

# ==== USUARIO ====

class UsuarioBase(BaseModel):
    nombre: str
    tipo_usuario: str  # 'sordo', 'oyente', etc.

class UsuarioCreate(UsuarioBase):
    pass

class Usuario(UsuarioBase):
    id: int
    fecha_registro: datetime

    class Config:
        orm_mode = True


# ==== SEÑAL ====

class SenalBase(BaseModel):
    descripcion: Optional[str] = None
    url_video: str

class SenalCreate(SenalBase):
    pass

class Senal(SenalBase):
    id: int
    fecha_captura: datetime

    class Config:
        orm_mode = True


# ==== RESULTADO ====

class ResultadoBase(BaseModel):
    usuario_id: int
    senal_id: int
    texto_traducido: str

class ResultadoCreate(ResultadoBase):
    pass

class Resultado(ResultadoBase):
    id: int
    fecha_procesamiento: datetime

    class Config:
        orm_mode = True
