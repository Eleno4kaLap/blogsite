import os

import requests
from django.core.mail import send_mail

from external_urls import favqs_quote_url


def requests_favqs_quote():
    """
    Function get quote from public api https://favqs.com/api/qotd
    :return: dict with keys:
    text - quote text
    author - quote author
    """
    response = requests.get(url=favqs_quote_url, timeout=2, verify=False)
    if response.status_code == 200:
        quote = response.json()
        return {'text': quote['quote']['body'], 'author': quote['quote']['author']}


def send_email(user_email):
    """
    Function send email to user about subscription
    :param user_email: email for subscription
    """
    send_mail(
        'You subscribed to new posts on blogsite',
        "Don't worry! There will be no more emails :)",
        os.environ.get('EMAIL_HOST_PASSWORD'),
        [user_email],
        fail_silently=False,
    )

