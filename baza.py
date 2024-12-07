import time
from helpers import *
from  data import *
for i in History['start'] :
    print(i)
    time.sleep(5.5)  
name = input("Как будут звать их спасителя - ")
player['name'] = name
print(f'{player["name"]}, Хорошо ')
time.sleep(1)
menu()
  