import requests
from bs4 import BeautifulSoup
import pprint

res = requests.get('https://news.ycombinator.com')
soup = BeautifulSoup(res.text, 'html.parser')
links = soup.select('.titlelink')
# votes = soup.select('.score')
subtext = soup.select('.subtext')

# --------254-----
res2 = requests.get('https://news.ycombinator.com/news?p=2')
soup2 = BeautifulSoup(res2.text, 'html.parser')
links2 = soup.select('.titlelink')
subtext2 = soup.select('.subtext')

mega_links = links + links2
mega_subtext = subtext + subtext2

def sort_stories_by_votes(hnlist):
    return sorted(hnlist, key= lambda k:k['votes'], reverse=True)

# 254
def create_custom_hn(links, subtext):
    hn = []
    for idx, item in enumerate(links):
        title = item.getText()
        href = item.get('href', None)
        vote = subtext[idx].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace('points', ' '))
            if points > 99:
                hn.append({'title': title, 'link': href, 'votes': points})
    # return hn
    return sort_stories_by_votes(hn)
# 254
# pprint.pprint(create_custom_hn(links, subtext))
pprint.pprint(create_custom_hn(mega_links, mega_subtext))





# def create_custom_hn(links, votes):
#     hn = []
#     for idx, item in enumerate(links):
#         title = links[idx].getText()
#         href = links[idx].get('href', None)
#
#         points = (votes[idx].getText().replace('points', ''))
#         hn.append({'title': title, 'link': href})
#     return hn
# print(create_custom_hn(links, votes)) #tested this for printing the votes but some links dont have votes at all(comes a conditiion)



# def create_custom_hn(links, subtext):
#     hn = []
#     for idx, item in enumerate(links):
#         title = item.getText()
#         href = item.get('href', None)
#         vote = subtext[idx].select('.score')
#
#         if len(vote):
#             points = int(vote[0].getText().replace('points', ' '))
#             print(points)
#             hn.append({'title': title, 'link': href, 'votes': points})
#     return hn
# print(create_custom_hn(links,subtext))












