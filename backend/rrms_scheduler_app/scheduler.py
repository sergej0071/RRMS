from apscheduler.schedulers.background import BackgroundScheduler

def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(lambda : print("Do schedule job!"), 'interval', seconds=2.0, name='do-some', jobstore='default')
    scheduler.start()