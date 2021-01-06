from celery import Celery

# پارامتر اول
# نام ماژولی که تسک ها در داخل آن تعریف می شود( یا همان نمونه در داخل آن تعریف می شود)
# اگر خالی باشد، به صورت اتوماتیک به فایلی که نمونه در آن تعریف می شود اشاره می کند
# پارامتر دوم، ادرس بروکر است که باید مشخص شود
# اگر بروکر ردیس باشد، به صورت زیر مقدار دهی می شود


# run command: celery -A tasks worker --loglevel=INFO --concurrency 1 -P solo

app = Celery('tasks')

#
# app.conf.task_serializer = 'json'
# app.conf.result_serializer = 'json'
# app.conf.update(
#     accept_content=['json'],
#     timezone='Asia/Tehran',
#     enable_utc=True,
# )

app.config_from_object('celeryconfig')


# app=Celery('tasks',broker='amqp://localhost')
#

# متد هایی که قرار است در سلری صف شوند از دکوراتور زیر قبل از آنها استفاده می کنیم
@app.task
def add(x, y):
    return x + y


@app.task
def divide(x, y):
    return x / y
    # print('hello world')
