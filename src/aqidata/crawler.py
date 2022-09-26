from asyncio.log import logger
import requests
import datetime
import time
import pandas as pd

from router import Router


def check_data_isexist(current: str):

    string = f"""
    select count(*) from sitedata
    where publishtime = '{current}'
    """

    db_router = Router()
    
    try:
        site = pd.read_sql(
            string,
            db_router.mysql_aqidb_conn()
        )
        count = site.to_dict("records")

        if count[0]['count(*)'] == 0:
            return False
        
        else:
            return True

    except Exception as e:
        logger.info(e)
        return 0
        

# Get AQI data
def get_data():
    # Request data
    response = requests.get("https://data.epa.gov.tw/api/v2/aqx_p_432?format=json&api_key=2cb603b2-1507-46c8-85c0-93e5107d773d")

    # Check error.
    try:
        response.json()
    except Exception as e:
        logger.info(e)

    df = pd.DataFrame(response.json()['records']).set_index("sitename")
    df = clear_data(df)

    store_data(df)


# Clean unuseful data column.
def clear_data(df):
    df = df.drop('county', axis=1)
    df = df.drop('longitude', axis=1)
    df = df.drop('latitude', axis=1)
    df = df.drop('siteid', axis=1)
    df.rename(columns = {"pm2.5": "pm25", "pm2.5_avg": "pm25_avg"}, inplace=True)
    df.replace('-', 0, inplace=True)
    df.replace('', 0, inplace=True)
    return df


# Store data to SQL.
def store_data(df):

    db_router = Router()

    # If data not exist -> Store
    if check_data_isexist(df['publishtime'][0]) == False:
        try:
            df.to_sql(
                name = 'sitedata', 
                con = db_router.mysql_aqidb_conn(), 
                if_exists="append",
            )
            logger.info("Store successful.")
            print("Store successful.")

            return {
                "result": "Successful"
            }

        except Exception as e:
            logger.info("Store error.")
            print("Store error.")

            return {
                "result": "Error",
                "Error_fuc": e
            }

    # If data already exist -> wait 30 min
    else:
        if datetime.datetime.now().minute < 35:
            time.sleep(300)
            get_data()

        else:
            return{
                "result": "Data already exist"
            }


if __name__ == "__main__":
    get_data()