from random import randint

from bs4 import BeautifulSoup

from django import template

import requests

register = template.Library()


@register.filter
def forbidden_words(value):

    list_of_forbidden_words = ["lighter", "ornament", "fossicker", "dramatizes", "slag", "slunk", "policer",
                               "egotists", "somnifacients", "nonblack", "anticlimax", "reservednesses", "hotnesses",
                               "pisses",
                               "tenacity", "mandarin", "redline", "victimizations", "bumfuzzled", "oxalated",
                               "scalepan", "tetrad",
                               "kabbalism", "metaplastic", "punctiliousness", "horologies", "romeos", "heteroauxin",
                               "footstall",
                               "pruriencies", "misadvises", "stile", "relacquered", "unscrambling", "revolutionary",
                               "droving",
                               "radiolysis", "archangelic", "proportionates", "solander", "disciplinarians", "seceded",
                               "instructive",
                               "methylates", "let", "omitters", "ridleys", "concussed", "marvelously", "ankuses",
                               "cobbler",
                               "beachgoer", "auspicates", "cafe", "gillnet", "raced", "shippers", "intransigeance",
                               "ridge", "missuits", "verification", "modernity", "oversees", "mousiest", "fibsters",
                               "bassness",
                               "girons", "airsickness", "fearfuller", "bladers", "enameller", "mispaged", "duskier",
                               "instants",
                               "boosters", "gibbered", "northland", "dissimilarity", "colluviums", "vulcanizers",
                               "culturati",
                               "ellipticity", "breathed", "trapanned", "thimblerigs", "astound", "recoverer",
                               "estreats", "dinginess",
                               "gizzard", "carotenoid", "ravenousnesses", "postpunk", "flashgun", "genesis",
                               "boustrophedonic",
                               "lunges", "transnatural", "misremembers",
                               ]

    for word in list_of_forbidden_words:
        replace = '*' * len(word)
        result = value.replace(word, replace)
        value = result
    return value


@register.simple_tag
def random_quotes():
    url = f'https://quotes.toscrape.com/page/{randint(1, 11)}/'
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')

    quotes = soup.find('span', {'class': 'text'}).get_text()
    author = soup.find('small', {'class': 'author'}).get_text()
    return f'{author}: {quotes}'
