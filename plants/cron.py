from django_cron import CronJobBase, Schedule
from moisture import *


class MyCronJob(CronJobBase):
    RUN_EVERY_MINS = 1  # every minute

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'plants.cron'    # a unique code

    def do(self):
        print "run chronjob"
        get_moisture(0, 140, 1023)
