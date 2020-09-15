from scraping.parsers import *
import codecs


parsers = (
            (work, 'https://www.work.ua/ru/jobs-kyiv-python/'),
            (rabota, 'https://rabota.ua/zapros/python/%d0%ba%d0%b8%d0%b5%d0%b2'),
            (dou, 'https://jobs.dou.ua/vacancies/?category=Python&city=%D0%9A%D0%B8%D0%B5%D0%B2'),
            (djinny, 'https://djinni.co/jobs/keyword-python/kyiv/')
)


jobs, errors = [], []
for func, url in parsers:
    j, e = func(url)
    jobs += j
    errors += e

h = codecs.open('work.txt', 'w', 'utf-8')
h.write(str(jobs))
h.close()
