# 파이썬 300제
# https://wikidocs.net/7023

import time
import datetime
import numpy as np
import pandas as pd

# start on 2022. 05. 23
# -------- 051 ~ 070 리스트
# 052
movie_rank = ["닥터 스트레인지", "스플릿", "럭키"]
movie_rank.append("배트맨")
movie_rank

# 053
movie_rank.insert(1, "슈퍼맨")
movie_rank

# 054
movie_rank.remove("럭키")
movie_rank

# 056
lang1 = ["C", "C++", "JAVA"]
lang2 = ["Python", "Go", "C#"]

langs = lang1 + lang2
langs

# 057
nums = [1, 2, 3, 4, 5, 6, 7]
min(nums), max(nums)
np.mean(nums)

# 062, 063, 064
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
nums[::2]
nums[1::2]
nums[::-1]

# 065
interest = ['삼성전자', 'LG전자', 'Naver']
interest[::2]
interest[0], interest[2]

# 067. 068 join
interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
"/".join(interest)
print("\n".join(interest))

# 069
string = "삼성전자/LG전자/Naver"
string.split("/")

# 070
data = [2, 4, 3, 1, 5, 10, 9]
data.sort()
data

# -------- 071 ~ 080 튜플
# 071
my_variable = ()
my_variable

# 075
t = 1, 2, 3, 4
type(t)

# 076
t = ('a', 'b', 'c')
t = ('A', 'b', 'c')
t

# 리스트와 비교
l = ['a', 'b', 'c']
# 방법1)
l = ['A'] + l[1:]
l
# 방법2)
l[0] = 'A'
l

# 079 unpacking
temp = ('apple', 'banana', 'cake')
a, b, c = temp
a
b
c

# 080
a = tuple(range(2, 100, 2))
a

# -------- 080 ~ 100 딕셔너리
# 081, 083 star expression
scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
*valid_score, x, y = scores
valid_score

_, *valid_score, _ = scores
valid_score

# tuple
a, b, *c = (0, 1, 2, 3, 4, 5)
print(a, b, c, sep="\n")

# 084
temp = {}
type(temp)

# 085
icecream = {'메로나': 1000, '폴라포': 1200, '빵빠레': 1800}
icecream

# 086
icecream['죠스바'] = 1200
icecream['월드콘'] = 1500
icecream

# 087
icecream['메로나']

# 088
icecream['메로나'] = 1300
icecream

# 089
del icecream['메로나']
icecream

# 092, 093
inventory = {"메로나": [300, 20],
             "비비빅": [400, 3],
             "죠스바": [250, 100]}
inventory['메로나'][0]
inventory['메로나'][1]

# 094
inventory['월드콘'] = [500, 7]
inventory

# 095, 096, 097
icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
list(icecream.keys())
list(icecream.values())
sum(list(icecream.values()))
sum(icecream.values())

# 098
new_product = {'팥빙수': 2700, '아맛나': 1000}
icecream.update(new_product)
icecream

# 099
keys = ("apple", "pear", "peach")
vals = (300, 250, 400)

result = dict(zip(keys, vals))
result

# 100
date = ['09/05', '09/06', '09/07', '09/08', '09/09']
close_price = [10500, 10300, 10100, 10800, 11000]

close_table = dict(zip(date, close_price))
close_table

# -------- 121 ~ 130 조건문
# 121
a = input("영문자를 입력하시오: ")
if a.islower():
    print(a.upper())
else:
    print(a.lower())

# # 124
# num1 = input("number1: ")
# num2 = input("number2: ")
# num3 = input("number3: ")
#
# arr = [int(num1), int(num2), int(num3)]
# print(max(arr))

# 129 주민등록번호 유효성 체크
id_nums = input("주민등록 번호를 입력하세요: 예)890319-1000000")
nums = []
test = np.array([2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 4, 5, 1])
for _ in id_nums.split("-"):
    for num in _:
        nums.append(int(num))
check = np.array(nums) * test
if 11 - sum(check[:len(check1) - 1]) % 11 == nums[len(nums) - 1]:
    print("유효한 주민등록번호입니다.")
else:
    print("유효하지 않은 주민등록번호입니다.")

# -------- 191 ~ 200 반복문
# 191, 192, 193
data = [
    [2000,  3050,  2050,  1980],
    [7500,  2050,  2050,  1980],
    [15450, 15050, 15550, 14900]
]
result = []

for prices in data:
    for price in prices:
        result.append(price * (1 + 0.014 / 100))
        print(price * (1 + 0.014 / 100))
    print('----')
result

# 195
ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]
for price in ohlc[1:]:
    print(price[3])

# 196
for price in ohlc[1:]:
    if price[3] > 150:
        print(price[3])

# 197
for price in ohlc[1:]:
    if price[3] >= price[0]:
        print(price[3])

# 198
volatility = []
for price in ohlc[1:]:
    volatility.append(abs(price[2] - price[1]))
volatility

# 200
profit = 0
for price in ohlc[1:]:
    profit += price[3] - price[0]
profit

# -------- 231 ~ 240 함수
# 232


def make_url(arg):
    print("www.{}.com".format(arg))


data = input("문자열 입력하세요: ")
make_url(data)

# 233


def make_list(x: str):
    mlist = []
    for _ in x:
        mlist.append(_)
    return mlist


make_list("abcd")

# 234


def pickup_even(numbers):
    mlist = []
    for number in numbers:
        if number % 2 == 0:
            mlist.append(number)
    return mlist


pickup_even([3, 4, 5, 6, 7, 8])

# 235


def convert_int(number: str):
    return int(number.replace(",", ""))


convert_int("1,234,567")


# -------- 241 ~ 250 모듈
# 241, 242
now = datetime.datetime.now()
print(now)
type(now)

# 243
for day in range(5, 0, -1):
    print(now - datetime.timedelta(days=day))

# 244
now.strftime("%H:%M:%S")
# now.strftime("%h:%m:%s")

# 245
date = "2020-05-04"
result = datetime.datetime.strptime(date, "%Y-%m-%d")
print(result)

# 246

count = 0
while count < 10:
    now = datetime.datetime.now()
    print(now)
    count += 1
    time.sleep(1)

# 250
for num in np.arange(0, 5, 0.1):
    print(round(num, 1))

np.arange(0, 5, 0.1)

# update on 2022. 10. 19
# -------- 251 ~ 290 클래스
# 252 ~ 259


class Human:
    def __init__(self, name, age, sex):
        # print("응애응애")
        self.name = name
        self.age = age
        self.sex = sex

    def __del__(self):
        print("나의 죽음을 알리지마라")

    def who(self):
        print('이름: {}, 나이: {}, 성별: {}'.format(self.name, self.age, self.sex))

    def setInfo(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex


# areum = Human("이름", 25, "여자")
# print(areum.age)
areum = Human("불명", "미상", "모름")
areum.who()
areum.setInfo("이름", 25, "여자")
areum.who()

del areum

# 260


class OMG:
    def print(self):
        print('oh no')


mystock = OMG()
mystock.print()


class OMG:
    def print():
        print('oh no')


mystock = OMG()
OMG.print()


# 261 ~ 270
