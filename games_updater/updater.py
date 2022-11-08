from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from games_updater import gs_qua_fin_update, gs_semi_foward_update, gs_close_bets
import ipdb

def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(gs_qua_fin_update.update_quarter_games, 'interval', minutes=1000)
    scheduler.add_job(gs_semi_foward_update.update_semi_foward_games, 'interval', minutes=900)
    scheduler.add_job(gs_close_bets.update_bets, 'interval', minutes=1)
    scheduler.start()