from fastapi import FastAPI
import datetime
import psycopg2
from asyncio.log import logger


app = FastAPI()


# Connect to db.
conn = psycopg2.connect(database="postgres", user="postgres", password="Pbw101031", host="airqualitydbv2.ccy27k19fmyr.ap-northeast-1.rds.amazonaws.com", port="5432")
cur = conn.cursor()

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
def get_sitename(sitename: str):

    string = f"""
    select sitename from site
    where sitename = '{sitename}'
    or eng_name = '{sitename}'
    """
    cur.execute(string)
    return cur.fetchall()


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
def get_site_special_data(sitename: str, option: str):

    site = get_sitename(sitename)

    # Current time
    date = current_time()

    string = f"""
    select json_build_object('sitename', sitename, '{option}', {option}, 'publishtime', publishtime) from sitedata
    where publishtime = '{date}'
    and sitename = '{site[0][0]}'
    """

    try:
        cur.execute(string)
        data = serializer(cur.fetchall())

    except Exception as e:
        cur.execute("ROLLBACK;")
        data = logger.info(e)

    return{
        'data': data
    }


@app.get('/api/v1/{sitename}/{option}/{start_time}/{end_time}')
def get_site_data_with_time_interval(sitename: str, option: str, start_time: str, end_time: str):
    
    site = get_sitename(sitename)

    start = datetime.datetime.strptime(start_time, "%Y%m%d%H")
    end = datetime.datetime.strptime(end_time, "%Y%m%d%H")

    print(start, end)

    string = f"""
    select json_build_object('sitename', sitename, '{option}', {option}, 'publishtime', publishtime) from sitedata
    where sitename = '{site[0][0]}'
    and publishtime between '{start}'
    and '{end}'
    """

    try:
        cur.execute(string)
        data = serializer(cur.fetchall())

    except Exception as e: 
        cur.execute("ROLLBACK;")
        data = logger.info(e)

    return{
        'data': data
    }


# Insert user linenotify token into db.
@app.get('/api/v1/{token}/{sitename}/{elements}/{limit_value}/')
def create_alert_message(token: str, sitename: str, elements: str, limit_value: float):

    string = f"""
    insert into linenotify (usertoken, sitename, elements, limitvalue) VALUES ('{token}', '{sitename}', '{elements}', '{limit_value}')
    """

    try:
        cur.execute(string)
        conn.commit()
        data = {"Successful"}

    except:
        cur.execute("ROLLBACK;")
        data = {"error"}

    return{
        'data': data
    }


#  Delete user linenotify token from db. 
@app.get('/api/v1/{token}')
def delete_alert_message(token: str):

    string = f"""delete from linenotify where usertoken = '{token}'"""


    try:
        cur.execute(string)
        conn.commit()
        data = {'Successful'}
    
    except:
        cur.execute("ROLLBACK;")
        data = {'error'}

    return{
        'data': data
    }