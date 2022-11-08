from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from games_updater import games_updater
import ipdb

def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(games_updater.update_games, 'interval', minutes=1)
    scheduler.start()