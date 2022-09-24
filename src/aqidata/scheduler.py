import time
import datetime
from loguru import logger
from apscheduler.schedulers.background import BackgroundScheduler

from crawler import get_data


def main():
    scheduler = BackgroundScheduler(
        timezone="Asia/Taipei"
    )

    scheduler.add_job(get_data, 'cron', minute="10")

    logger.info("sent_crawler_task")
    scheduler.start()


def sent_crawler_task():
    get_data()
    logger.info("Sent Task!")


if __name__ == "__main__":
    main()

    while True:
        logger.info(datetime.datetime.now())
        time.sleep(600)