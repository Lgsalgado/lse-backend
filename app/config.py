import os

class Settings:
    DB_URL = os.getenv("DATABASE_URL", "postgresql://postgre:admin@localhost:5432/lse")

settings = Settings()
