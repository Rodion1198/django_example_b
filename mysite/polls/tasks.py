from bs4 import BeautifulSoup

from celery import shared_task

from django.core.mail import send_mail as django_send_mail   # noqa: F821

from polls.models import Quot, QuoteAuthor

import requests


@shared_task
def send_mail(subject, message, from_email):
    django_send_mail(subject, message, from_email, ['admin@example.com'])


@shared_task
def parse_quote():
    page = 1
    last_page = False
    already_saved_quotes = 1
    LINK = 'https://quotes.toscrape.com'

    while not last_page:
        url = f'{LINK}/page/{page}'
        r = requests.get(url)
        soup = BeautifulSoup(r.content, 'html.parser')
        quotes = soup.findAll('div', {'class': 'quote'})

        for item in quotes:
            if already_saved_quotes > 5:
                break
            else:
                title = item.select('.text')[0].contents[0]
                if Quot.objects.exists(title=title):
                    continue
                else:
                    author = item.select('.author')[0].contents[0]
                    if QuoteAuthor.objects.exists(author=author):
                        saved_author = QuoteAuthor.objects.get(author=author)
                    else:
                        link_author = LINK + item.find_all('a')[0].get('href')
                        r = requests.get(link_author)
                        soup = BeautifulSoup(r.content, 'html.parser')
                        date_of_birth = soup.find('span', {'class': 'author-born-date'}).contents[0]
                        born_in = soup.find('span', {'class': 'author-born-location'}).contents[0]
                        description = soup.find('div', {'class': 'author-description'}).contents[0]
                        saved_author: QuoteAuthor = QuoteAuthor(author=author, date_of_birth=date_of_birth,
                                                                born_in=born_in, description=description)
                        saved_author.save()
                    quote_record: Quot = Quot(title=title, author=saved_author)
                    quote_record.save()
                    already_saved_quotes += 1
        if already_saved_quotes < 5:
            if soup.find('li', {'class': 'next'}) is None:
                last_page = True
            else:
                page += 1
        else:
            break
        if last_page is True:
            django_send_mail('Quotes is over!', 'All quotes added!', 'rodion@test.com', ['admin@example.com'])
