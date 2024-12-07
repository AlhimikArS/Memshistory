import time
import random
from math import *
from data import *

def who():
    for x in History['who']:
            print(x)
            time.sleep(5)


def fight(current_enemy):
    round_f = random.randint(1,2)
    enemy = enemies[current_enemy]
    enemy_hp = enemies[current_enemy]["hp"]
    low = enemy["low_reward"]
    high = enemy["high_reward"]
    
    while player["hp"] > 0 and enemy_hp> 0: 
        #Атака игрока
        if round_f % 2 == 1:
            print(f'{player["name"]} атакует {enemy["name"]}')
            crit = random.randint(1, 100)
            if crit <= player['luck']:
                enemy_hp -= player['damage'] * 3
            else:
                enemy_hp -= player['damage']  
            time.sleep(1.5)
            print(f''' {player["name"]} - {player["hp"]}
{enemy["name"]} - {enemy_hp}''')
            print()
           #Атака NPC
        else:
            print(f"{enemy['name']} атакует {player['name']}")
            if enemy["damage"] <= player["armor"]:
              player["hp"] -= 0
            else:  
                player["hp"] -= (enemy["damage"] - player["armor"])
            time.sleep(1.5)
            print(f''' {player["name"]} - {player["hp"]}
{enemy["name"]} - {enemy_hp}''')
            print()
        round_f = round_f + 1
    
        
       
    if player["hp"] > 0:
        print(f'{enemy["win"]}')
        
        payout = (random.randint(low,high))
        if "счастливый кулон" in player['inventory']:
            payout = round(payout * 1.5, 0)
            payout = trunc(payout)
            player['money'] += payout 
            print(f'вы получили  {payout} робуксов, теперь у вас {player["money"]}')    
        else:
            player['money'] += payout 
            print(f'вы получили  {payout} робуксов, теперь у вас {player["money"]}')
        enemy["kill"] += 1
        
        
        if current_enemy == 2 and enemy["kill"] == 1 :
            print(History['end'][0])
            items[str(len(items)+1)] = {
    "name" : 'Большой взрыв', 
    "price" : 100000,
    "description" : '"вернет все на место"'  
                
            }
            
            time.sleep(1)
            print(f'Тут же к вам подешел незнакомец и сказал: ')
            who()
    else:
        print(f'{enemy["lose"]}')   
    player['hp'] = player['true_hp'] 
    
    
    
    
def training():
            training_type = input(''' 1 - атака 2 - защита ''')
            if items['2']['name'] in player['inventory'] :
                print() 
            
            else:
                for i in range(0,101,20):
                    print(f"тренировка завершена на {i}% ")
                    time.sleep(1.5)
           
            if training_type == '1':
                if 'Амулет ниндзи' in player['inventory']:
                    player['damage'] += 2*5 
                else:
                  player['damage'] += 2  
                print(f'Тренировка закончена! теперь вы наносите - {player["damage"]} урона')
            
            elif training_type == '2':
                if 'Амулет ниндзи' in player['inventory']:
                    player["armor"] += 3*5  
                else:
                    player["armor"] += 3
                print(f'Тренировка закончена! теперь вы поглощаете - {player["armor"]} урона')
            
            else: 
                print("такой тренировки несуществует! Вы тренировались зря")

def display_player():
    print(f"Игрок - {player['name']} ")
    
    print(f"Урон - {player['damage']} , шанс критического урона {player['luck']}% ")
    print(f'броня поглощает - {player["armor"]} урона')


def display_enemy(current_enemy):
    enemy = enemies[current_enemy]
    print(f" противник- {enemy['name']}")
    print(f"Урон - {enemy['damage']}")
    print(f"Здоровье - {enemy['hp']}")
    print(f"{enemy['description']}")
    print(f"Вы победили врага - {enemy['kill']}")
    
def shop():
    print(f''' Не Добро пожаловать в Toxic Синдрию
ваши робуксы - {player['money']}''')
    # 1 - предметы на покупку
    for key, value in items.items():
        print(f'{key} - {value["name"]}: {value["price"]}, описание - {value["description"]}')
    print('Выход - остальные цифры')

# - 2 логика транзакции
    item = input()
    item_int = int(item)
    
    if item_int <= len(items) and item_int > 0:            
        if items[item]['name'] in player['inventory']:
            print(f"у тебя уже есть {items[item]['name']} ") 
        
        elif player['money'] >= items[item]['price']:
            print(f"Ты успешно приобрел {items[item]['name']}")      
            player['money'] -= items[item]['price']
            player['inventory'].append(items[item]['name'])
        else:
            print('у вас нет столько денег, вам нужно идти и заработать их , лол')
            
        if 'Большой взрыв' in player['inventory']:
            for y in History['real_end']:
                print(y)
                time.sleep(2.5)
            exit(0)
            
    
    print("Не приходи сюда больше")
    
    
def dispaly_inventory():
    for value in player['inventory']:
        print(value)
    print(f"Ваши робуксы - {player['money']}")
    print()
    if 'зелье удачи' in player['inventory']:
        drink_potion = input("Хотите петь зелье 1 - да 2 - нет ")
        if drink_potion == '1':
            player['luck'] += 5
            print(f"Теперь твой крит шанс {player['luck']}%")
            player['inventory'].remove("зелье удачи")
        else:
            print("Как хочешь")
    
    
    
def menu():
    
    while True:
        action = input('''Выбери действие :
1 -  в бой 
2 - тренировка 
3 - статы игрока
4 - Статы противника
5 - Магазин
6 - Инвентарь
''')
        if action == '1':
            enemy_input = (input('С кем будет битва  0 - пикми 1 - палитра(требуется"разведка") 2 - Босс КФС(нужно купить "КФС") '))
            
            if enemy_input == '0' or enemy_input == '1' or enemy_input == '2' :
                
                if enemy_input == '0':
                    enemy_input = int(enemy_input)
                    fight(enemy_input)       
                
                
                elif  enemy_input == '1':
                    
                    if 'разведка палитр' in player['inventory']:
                        enemy_input = int(enemy_input)
                        fight(enemy_input)
                        
                    else:
                        print("А где они?!")
                        
                elif enemy_input == '2':
                    if 'КФС' in player['inventory']:
                        enemy_input = int(enemy_input)
                        fight(enemy_input)
                    else:
                        print("У вас нет кфс чтоб поймать его босса")    
            else:
                print("такого врага нет")
                
        elif action == '2':
            training()
        elif action == '3':
            display_player()
        elif action == "4":
            enemy_stats = int(input('о ком хотите узнать  0 - пикми 1 - палитра 2 - Босс КФС '))
            if enemy_stats == 0 or enemy_stats == 1 or enemy_stats == 2 :
                display_enemy(enemy_stats)
            else:
                print("Такая информация не найдена :(")
        elif action == "5":
            shop()
        elif action == "6":
            dispaly_inventory()    
        else:
            print(random.choice(scripts_menu))
            
        print()
              
            

                
            
        