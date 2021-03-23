from blog.service import requests_favqs_quote, send_email
from siteblog.celery import app
from django.core.cache import cache


@app.task
def set_quote_in_cache():
    """
    Task get quote end set it in cache  for 1 minute
    :return: dict with keys:
    text - quote text
    author - quote author
    """
    quote = requests_favqs_quote()
    cache.set('quote', quote, 60)
    return quote


@app.task
def send_subscribe_email(user_mail):
    """
    Task send email about subscription on user_mail
    :param user_mail: email for registration subscription
    """
    send_email(user_mail)
