# pyscheduler
Task Scheduler

Create scheduled tasks at runtime easily.

# Installation

```bash
pip install python-scheduler
```

# Example

```bash
from pyscheduler import schedule

# crawl_task runs in every 2 minutes
@schedule('*/2 * * * *')
def crawl_task():
    print 'crawl task'

```

# Important

It won't definitely create any cronjob on the os level. All tasks will be executed on runtime.

Every cron syntax can be used.