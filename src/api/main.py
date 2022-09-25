from fastapi import FastAPI
import datetime
import pandas as pd
from asyncio.log import logger
from sqlalchemy import create_engine, engine


app = FastAPI()


# Connect db.
def get_conn():
    address = "mysql+pymysql://pl3w:Pbw101031@mysql:3306/aqidb"
    engine = create_engine(address)
    return engine.connect()


# Set current time.
def current_time():
    # 每小時10分前資料庫尚未更新至最新資料
    if(datetime.datetime.now().minute <= 10):
        dt1 = datetime.datetime.utcnow().replace(tzinfo=datetime.timezone.utc)
        dt2 = dt1.astimezone(datetime.timezone(datetime.timedelta(hours=7)))

    else:
        dt1 = datetime.datetime.utcnow().replace(tzinfo=datetime.timezone.utc)
        dt2 = dt1.astimezone(datetime.timezone(datetime.timedelta(hours=8)))

    return datetime.datetime.strptime(dt2.strftime("%Y-%m-%d %H"), "%Y-%m-%d %H")


# Transfer eng site name to chinese site name.
def get_sitename(
    sitename: str,
    conn: engine.base.Connection
):

    string = f"""
    select sitename from site
    where sitename = '{sitename}'
    or eng_name = '{sitename}'
    """
    site = pd.read_sql(string, conn)
    return site.to_dict("records")


# Dict to json
def serializer(data):
    json_data = []

    for row in data:
        json_data.append(row[0])

    return json_data


@app.get('/')
def index():
    return {"result": "root"}


@app.get('/api/v1/{sitename}/{option}')
def get_site_special_data(
    sitename: str,
    option: str
):

    conn = get_conn()

    site = get_sitename(sitename, conn)

    # Current time
    date = current_time()

    string = f"""
    select sitename, {option}, publishtime from `sitedata` 
    where publishtime = '{date}' 
    and sitename = '{site[0]['sitename']}' 
    """

    try:
        data_df = pd.read_sql(string, con=conn)
        data = data_df.to_dict("records")

    except Exception as e:
        data = logger.info(e)

    return{
        'data': data
    }


@app.get('/api/v1/{sitename}/{option}/{start_time}/{end_time}')
def get_site_data_with_time_interval(
    sitename: str,
    option: str,
    start_time: str,
    end_time: str
):

    conn = get_conn()
    
    site = get_sitename(sitename, conn)

    start = datetime.datetime.strptime(start_time, "%Y%m%d%H")
    end = datetime.datetime.strptime(end_time, "%Y%m%d%H")

    string = f"""
    select sitename, {option}, publishtime from `sitedata`
    where sitename = '{site[0]['sitename']}'
    and publishtime between '{start}'
    and '{end}'
    """

    try:
        data_df = pd.read_sql(string, con=conn)
        data = data_df.to_dict("records")

    except Exception as e: 
        data = logger.info(e)

    return{
        'data': data
    }

