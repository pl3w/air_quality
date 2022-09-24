import client
import typing
from sqlalchemy import engine

class Router:
    def __init__(self,):
        # 建立 connection
        self._mysql_aqidb_conn = (
            client.get_airquality_conn()
        )


    def check_mysql_conn_alive(self,):

        self._mysql_aqidb_conn = check_connect_alive(
            self._mysql_aqidb_conn,
            client.get_airquality_conn()
        )
        
        return (
            self._mysql_aqidb_conn
        )
    

    def mysql_aqidb_conn(self):

        # 拿取 connect 前先檢查連線是否 alive
        return (
            self.check_mysql_conn_alive()
        )


# 從新建立連線
def reconnect(
    conn_func: typing.Callable
):

    try:
        connect = conn_func()

    except Exception as e:
        f"{conn_func.__name__} reconnect error:{e}"

    return connect


def check_connect_alive(
    conn: engine.base.Connection,
    conn_func: typing.Callable,
):
    if conn:
        try:
            # alive
            conn.execute("select 1 + 1")
            return conn

        except Exception as e:
            # dead
            conn = reconnect(conn_func)

            return check_connect_alive(
                conn, conn_func,
            )

    else:
        conn = reconnect(conn_func)

        return check_connect_alive(
            conn, conn_func,
        )
