import logging
import time
from threading import Thread
from crontab import CronTab

FORMAT = '%(asctime)-15s %(function)s %(message)s'
logging.basicConfig(format=FORMAT)
LOGGER = logging.getLogger(__name__)


def execute_with_log(f):
    def wrapper(*args, **kwargs):
        LOGGER.warning('has started.', extra={'function': f.__name__})
        f(*args, **kwargs)
        LOGGER.warning('has finished.', extra={'function': f.__name__})

    return wrapper


def scheduler():
    registry = {}

    def cron(cr):
        def registrar(f):
            registry[f.__name__] = {'function': f, 'cron': cr}
            return f

        return registrar

    cron.tasks = registry
    return cron


schedule = scheduler()


class TaskTrigger(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.start()

    def run(self):
        while True:
            for task, kwargs in schedule.tasks.items():
                entry = CronTab(kwargs['cron'])
                nxt = entry.next()
                if 0.0 < nxt < 1.0:
                    func = lambda: execute_with_log(kwargs['function'])
                    Thread(target=func()).start()
            time.sleep(0.9)


TaskTrigger()
