from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base

from configs.database_config import username, password, ip, port

db_name = "conti_db"
table_name = "conti_gpt"

engine = create_engine(f"mysql+pymysql://{username}:{password}@{ip}:{port}")

Base = declarative_base()
