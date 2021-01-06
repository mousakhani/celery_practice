broker_url = 'redis://localhost:6379'
result_backend = 'mongodb://localhost:27017/'
task_serializer = 'json'
result_serializer = 'json'
timezone = 'Asia/Tehran'
accept_content = ['json']
enable_utc = True

# برای محدود کردن تعداد اجرای یک تسک بر حسب زمان
#برای تسک های سنگین می تواند مفید باشد
#rate_limit اگر تنظیم شود، از اجرا جلوگیری می کند. یعنی تسک دریافت می شود اما اجرا نمی شود. چون یک دقیقه باید به تعداد محدودیت تعریف شده تقسیم شود.
# m= minute
# s= second
# h= hour
#اگر بیشتر از محدودیتی که تعریف شده است، تسک دریافت شود، تسک های اضافی وارد صف می شوند و بعد اجرا خواهند شد.
# task_annotations={
#     'tasks.add':{'rate_limit':'1/m'},
# }
