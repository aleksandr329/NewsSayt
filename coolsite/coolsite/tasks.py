from celery import shared_task
import time
from coolsite.accounts.forms import CustomSignupForm
@shared_task
def hello():
    time.sleep(10)
    print("Hello, i task of celery!")





@shared_task
def frech_news():
    CustomSignupForm.mailing_list()
