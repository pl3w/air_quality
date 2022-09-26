from sqlalchemy import create_engine, engine

def get_airquality_conn():

    global engine
    address = "mysql+pymysql://pl3w:Pbw101031@mysql:3306/aqidb"
    #address = "mysql+pymysql://pl3w:Pbw101031@139.162.119.7:3306/aqidb"

    engine = create_engine(address)
    return engine.connect()

