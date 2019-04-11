import re
import requests
from bs4 import BeautifulSoup

SPORT1 = ["basketball", "badminton", "archery", "baseball", "volleyball", 
"bmx", "bobsleigh", "canoe", "equestrian", "football", "soccer", "golf", "hockey", "judo", 
"karate", "luge", "pentathlon", "rugby",  "softball",  "table tennis", "taekwondo", "tennis", 
"trampoline", "triathlon", "water polo"]

SPORT2 = ["gymnast", "ski", "swimm", "box", "curl", "dive", "fenc", "figure skat", "mountain bik", "cycl", 
"speed skat", "row", "sail", "shoot", "ski jump", "snow board", "surf", "weightlift", "wrestl", "driv", "rac", "sprint", "runn"]
def repl_func(m):
    """process regular expression match groups for word upper-casing problem"""
    return m.group(1) + m.group(2).upper()


def find_occupations(wiki_data):
    output = {}
    for indx, result in enumerate(wiki_data):
        name = result[1][0]
        wiki_desc = result[2][0]
        wiki_url = result[3][0]
        wiki_html = requests.get(wiki_url).content
        wiki_page = BeautifulSoup(wiki_html, features="html.parser")

        occupations = []
        # Actor and Muscians
        info_card = wiki_page.find("td", {"class": "role"})
        if info_card is not None:
            for occ in info_card.findChildren('li'):
                occ = re.sub("(^|\s)(\S)", repl_func, occ.contents[0])
                occupations.append(occ)

        # Politicians
        if 'politic' in wiki_desc.lower():
            if 'president' in wiki_desc.lower():
                pres= re.search("[\w]+ (president of the united states)", wiki_desc.lower())
                occupations.append(pres.title())
            else:
                occupations.append('Politician')

        # Athletes
        for sport in SPORT1:
            if sport in wiki_desc.lower():
                athlete_type= 'Professional ' + sport.title() + ' Player'
                occupations.append(athlete_type)
        for sport in SPORT2:
            if sport in wiki_desc.lower():
                if(sport != "gymnast"):
                    if(sport != "dive"):
                        sport= sport + 'er'
                    else:
                        sport= sport + 'r'
                athlete_type= 'Professional ' + sport.title()
                occupations.append(athlete_type)
        output[name] = occupations

    return output
