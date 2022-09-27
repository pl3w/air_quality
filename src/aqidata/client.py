from sqlalchemy import create_engine, engine

def get_airquality_conn():

    global engine
    # MySQL Address
    address = "" 

    engine = create_engine(address)
    return engine.connect()

