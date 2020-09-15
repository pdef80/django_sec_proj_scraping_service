from bs4 import BeautifulSoup as BS
import requests
import codecs
from random import randint


__all__ = ('work', "rabota", 'dou', "djinny")


headers = [{'User-Agent': 'Mozilla/5.0 (Windows NT 5.1; rv:47.0) Gecko/20100101 Firefox/47.0',
           'Accept': 'text/html, application/xhtml+xml, application/xml;q=0.9,*/*;q=0.8'},
           {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36",
           'Accept': 'text/html, application/xhtml+xml, application/xml;q=0.9,*/*;q=0.8'},
           {"User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.5) Gecko/20091102 Firefox/3.5.5 (.NET CLR 3.5.30729)",
            'Accept': 'text/html, application/xhtml+xml, application/xml;q=0.9,*/*;q=0.8'}
]


jobs = []
errors = []

def work(url):
    domain = 'https://www.work.ua'
    # url = 'https://www.work.ua/ru/jobs-kyiv-python/'
    resp = requests.get(url, headers=headers[randint(0, 2)])
    jobs = []
    errors = []

    if resp.status_code == 200:
        soup = BS(resp.content, 'html.parser')
        main_div = soup.find('div', attrs={'id': 'pjax-job-list'})
        if main_div:
            div_list = main_div.find_all('div', attrs={'class': 'job-link'})
            for div in div_list:
                title = div.find('h2')
                href = title.a['href']
                content = div.p.text
                company = 'No name'
                logo = div.find('img')
                if logo:
                    company = logo['alt']
                jobs.append({'title': title.text, 'url': url, 'href': domain + href, 'description': content, 'company': company})
        else:
            errors.append({'url': url, 'title': 'Div does not exists'})
    else:
        errors.append({'url': url, 'title': 'Page do not response'})

    return jobs, errors


def rabota(url):
    domain = 'https://rabota.ua'
    resp = requests.get(url, headers=headers[randint(0, 2)])
    jobs = []
    errors = []
    if resp.status_code == 200:
        soup = BS(resp.content, 'html.parser')
        new_jobs = soup.find('div', attrs={'class': 'card-body'})
        if not new_jobs:
            table = soup.find('table', attrs={'id': 'ctl00_content_vacancyList_gridList'})
            if table:
                tr_list = table.find_all('tr', attrs={'id': True})
                for tr in tr_list:
                    div = tr.find('div', attrs={'class': 'card-body'})
                    if div:
                        title = div.find('p', attrs={'class': 'card-title'})
                        href = title.a['href']
                        content = div.p.text
                        company = 'No name'
                        p = div.find('p', attrs={'class': 'company-name'})
                        if p:
                            company = p.a.text
                    jobs.append({'title': title.text, 'url': url, 'href': domain + href, 'description': content, 'company': company})
            else:
                errors.append({'url': url, 'title': 'Table does not exists'})
        else:
            errors.append({'url': url, 'title': 'Page is empty'})
    else:
        errors.append({'url': url, 'title': 'Page do not response'})

    return jobs, errors


def dou(url):
    # domain = 'https://www.work.ua'
    # url = 'https://www.work.ua/ru/jobs-kyiv-python/'
    resp = requests.get(url, headers=headers[randint(0, 2)])
    jobs = []
    errors = []

    if resp.status_code == 200:
        soup = BS(resp.content, 'html.parser')
        main_div = soup.find('div', attrs={'id': 'vacancyListId'})
        if main_div:
            li_list = main_div.find_all('li', attrs={'class': 'l-vacancy'})
            for li in li_list:
                if '__hot' not in li['class']:
                    title = li.find('div', attrs={'class': 'title'})
                    href = title.a['href']
                    cont = li.find('div', attrs={'class': 'sh-info'})
                    content = cont.text
                    company = 'No name'
                    a = title.find('a', attrs={'class': 'company'})
                    if a:
                        company = a.text
                    jobs.append({'title': title.text, 'url': url, 'href': href, 'description': content, 'company': company})
        else:
            errors.append({'url': url, 'title': 'Div does not exists'})
    else:
        errors.append({'url': url, 'title': 'Page do not response'})

    return jobs, errors


def djinny(url):
    domain = 'https://djinni.co'
    # url = 'https://www.work.ua/ru/jobs-kyiv-python/'
    resp = requests.get(url, headers=headers[randint(0, 2)])
    jobs = []
    errors = []

    if resp.status_code == 200:
        soup = BS(resp.content, 'html.parser')
        main_ul = soup.find('ul', attrs={'class': 'list-jobs'})
        if main_ul:
            li_list = main_ul.find_all('li', attrs={'class': 'list-jobs__item'})
            for li in li_list:
                if '__hot' not in li['class']:
                    title = li.find('div', attrs={'class': 'list-jobs__title'})
                    href = title.a['href']
                    cont = li.find('div', attrs={'class': 'list-jobs__description'})
                    content = cont.text
                    company = 'No name'
                    comp = li.find('div', attrs={'class': 'list-jobs__details__info'})
                    if comp:
                        company = comp.text
                    jobs.append({'title': title.text, 'url': url, 'href': domain + href, 'description': content, 'company': company})
        else:
            errors.append({'url': url, 'title': 'Div does not exists'})
    else:
        errors.append({'url': url, 'title': 'Page do not response'})

    return jobs, errors


if __name__ == '__main__':
    url = 'https://djinni.co/jobs/keyword-python/kyiv/'
    jobs, errors = djinny(url)
    h = codecs.open('../work.txt', 'w', 'utf-8')
    h.write(str(jobs))
    h.close()