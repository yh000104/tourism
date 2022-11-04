import requests
from bs4 import BeautifulSoup
import re
# import urllib.request as req

#헤더 키 설정
header = {'User-agent' : 'Mozila/2.0'}
# text = 'data.txt'
# output_text = 'clean_data.txt'
# f = open('data.txt', 'wb')

# url = "https://korean.visitkorea.or.kr/list/ms_list.do?areacode=All"
# res = req.urlopen(url, headers=header)

# def clean_text(text):
#     cleaned_text = re.sub('[a-zA-Z]' , '', text)
#     cleaned_text = re.sub('[\{\}\[\]\/?.,;:|\)*~`!^\-_+<>@\#$%&\\\=\(\'\"]',
#                           '', cleaned_text)

#     return cleaned_text 

#크롤링
response = requests.get("http://www.koreatriptips.com/tourist-attractions.html", headers=header)
html = response.text
soup = BeautifulSoup(html, 'html.parser')
# soup = BeautifulSoup(res, 'html.parser', from_encoding='eur-kr')
names = soup.select('div.row div.col-sm-8')

# 크롤링 파일화
with open('data.txt', 'w', encoding='utf-8') as f:
    f.write(str(names))
f.close

# read_file = open('data.txt', 'r')
# write_file = open(output_text, 'w')
# data = read_file.read()
# data = clean_text(text)
# write_file.write(data)
# read_file.close()
# write_file.close()


# for name in names:
#     data = name.SaveFormat()

#     f.write(data)
#     f.write('\n')

# f.close()

#화편에 표시
for name in names:
    print(name.text.strip())

# names = soup.find_all('a', attrs={'class':'tit'})

# for name in names:
#     tit = name.get_text()

# for name in names:
#     try:
#         print(name.text.strip())

#     except IndexError:
#         pass