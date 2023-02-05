import requests
from bs4 import BeautifulSoup
from bs4 import SoupStrainer

URL = 'https://isport.blesk.cz/vysledky/hokej/liga?action=season&season=3089'


def get_soup():
    page = requests.get(URL)
    page.raise_for_status()
    body = page.content
    table = SoupStrainer(id='leftPane')
    soup = BeautifulSoup(body, 'html.parser', parse_only=table)
    return soup


def win_fav_team(soup, fav_team):
    # pokud zadám class_="team-name", vezme to všechny zápasy
    all_matches = soup.find_all("div", class_="team-name")
    all_fav_team = [name.text for name in all_matches].count(fav_team)
    team_loser = soup.find_all("div", class_="team-name team-looser")
    fav_team_loser = [name.text for name in team_loser].count(fav_team)
    count_win = all_fav_team - fav_team_loser
    return f'Tým {fav_team} vyhrál v Generali Play-off 2017/2018 {count_win}x.'


def losses(soup):
    dates = soup.find_all("div", class_="datetime-container")
    day = []
    for date in dates:
        # vezme datum, oddělí celý text "•", vezme jen první část
        # datum se zobrazoval '6.\xa03.', takže .replace() v UTF-8 kódování
        full = date.text.split("•")[0].replace(u'\xa0', u' ')
        day.append(f'{full}')
    team_names = soup.find_all("div", class_="team-name team-looser")
    team = [name.text for name in team_names]
    losses = dict(zip(day, team))
    return losses


print('\n###\n')
print(win_fav_team(get_soup(), "Brno"))
print('\n###\n')
loss_in_date = losses(get_soup())
for k, v in loss_in_date.items():
    print(f'V zápase ze dne {k}je poraženým týmem {v}.')
