from datetime import datetime
import time
# import re
from urllib.request import urlopen
f=urlopen('https://forbes.kz/news/2023/02/28/newsid_296112')
f = urlopen('https://www.zakon.kz/6385814-sozdateli-filma-532-proigrali-delo-o-plagiate.html')
f = urlopen('https://www.inform.kz/ru/pochemu-podtopleniya-proishodyat-na-ezhegodnoy-osnove-ob-yasnil-senator_a4041331')


i=f.info()
print(i)
print(i['Date'])
d = datetime.strptime(i['Date'], '%a, %d %b %Y %X %Z')
print(d)
print(type(d))
print(int(time.mktime(d.timetuple())))


dict = {
    "1": "one",
    "2": "two",
    "3": "three"
}

for v in dict.values():
    print(v)