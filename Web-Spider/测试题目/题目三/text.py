import re


list = ['\n        ', '5.4', '\n        ', '\n            ', '有迹可循', '\n            ', '90分钟 - ', '爱情', ' / ', '悬疑', '\n                ', '1家影院上映1场', '\n            ', '查影讯', '\n        ', '\n    ']
for i in list:
    result = re.findall(r'映1场',i)
print(result)