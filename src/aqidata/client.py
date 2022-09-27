from sqlalchemy import create_engine, engine
from config import (
    MYSQL_DATA_HOST,
    MYSQL_DATA_USER,
    MYSQL_DATA_PASSWORD,
    MYSQL_DATA_PORT,
    MYSQL_DATA_DATABASE
)

def get_airquality_conn():

    global engine
    # MySQL Address
    address = (
        f"mysql+pymysql://{MYSQL_DATA_USER}:{MYSQL_DATA_PASSWORD}"
        f"@{MYSQL_DATA_HOST}:{MYSQL_DATA_PORT}/{MYSQL_DATA_DATABASE}"
    )

    engine = create_engine(address)
    return engine.connect()

