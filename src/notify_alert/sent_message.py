from email import message
import requests
import datetime
import psycopg2
import sys


# Set current time.
def current_time():
    dt1 = datetime.datetime.utcnow().replace(tzinfo=datetime.timezone.utc)
    dt2 = dt1.astimezone(datetime.timezone(datetime.timedelta(hours=8)))

    return datetime.datetime.strptime(dt2.strftime("%Y-%m-%d %H"), "%Y-%m-%d %H")


def sent_message(token, element, site, limit_value, current_value):

    message = "\n當前 " + element + " 數值為：" + str(current_value)
    message += "\n已大於" + "您所設定的數值：" + str(limit_value)
    message += "\n請注意身體健康且待在室內。"

    # HTTP 標頭參數與資料
    headers = { "Authorization": "Bearer " + token }
    data = { 'message': message }

    # 以 requests 發送 POST 請求
    requests.post("https://notify-api.line.me/api/notify", headers = headers, data = data)


def main(conn):
    cur = conn.cursor()
    now = current_time()

    # 取得待通知清單
    cur.execute("select * from linenotify")
    rows = cur.fetchall()

    for row in rows:
        # 取得設定條件當下空氣數值
        string = "select " + row[2] + " from sitedata where sitename = %s and publishtime = %s"
        cur.execute(string, (row[1], now,))
        value = cur.fetchall()
        

        # 比較設定條件值與當下空氣數值
        if(value[0][0] >= row[3]):
            sent_message(row[0], row[2], row[1], row[3], value[0][0])


if __name__ == '__main__':
    database , user, pwd, host = sys.argv[1:]

    # 連接資料庫
    conn = conn = psycopg2.connect(database=database, user = user, password = pwd, host = host, port = "5432")
    main(conn)