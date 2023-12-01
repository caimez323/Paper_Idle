import threading
import os

from shop_scripts import display_shop_items
from common import clear, arrond, display_ressources, end_game
from items import get_items_shop, reset_inventory, get_multiplier_dict
from upgrades import get_upgrades_shop


#TODOLISt
#Fix bug with too high qqt
#Cannot see the error line when wrong id




#Addition and ascention
addition = 1
fold = 1
piles = 1
sleepTime = 2

bonusMulti = 1
bonusTimer = 0

manual_multiplier = 1

#Get all usefull dicts
dict_shop_items = get_items_shop()
dict_shop_upgrades = get_upgrades_shop()
inventory = reset_inventory()
item_mutli_dict = get_multiplier_dict()

DISPLAY = True
user_input = '\0'
prec_bought_string = ""


def calculate_max_units(budget, initial_cost, increase_factor):
  max_units = 0
  remaining_budget = budget

  while remaining_budget >= initial_cost:
    remaining_budget -= initial_cost
    initial_cost *= increase_factor
    initial_cost = arrond(initial_cost)
    max_units += 1
  return max_units


def enter_shop(inShop="i"):
  global DISPLAY
  global prec_bought_string
  DISPLAY = False
  clear()
  print("Welcome to the shop : \n")
  print(prec_bought_string)
  if inShop == "i":
    display_shop_items(inventory, dict_shop_items)
  elif inShop == "u":
    display_shop_items(inventory, dict_shop_upgrades)
  print("\nEnter what you want : id * qqt (or 'max')")
  id_in = input("id : ")
  if (id_in == "xs" or id_in == "xshop"):
    id_in = 0
    exit_shop()
    display_ressources(inventory, item_mutli_dict, bonusMulti)
    return
  elif (id_in == "upgrades" or id_in == "up"):
    return enter_shop("u")
  #Id
  id_in = int(id_in)
  id_data = None
  if inShop == "i":
    id_data = dict_shop_items.get(id_in)
  elif inShop == "u":
    id_data = dict_shop_upgrades.get(id_in)
    
  if id_data is None :
    print("Not enough paper or wrong id\n")
    enter_shop(inShop)
  #else
  id_price, id_name, id_increase = id_data
    
  #QQT
  qqt_in = input("qqt : ")
  if qqt_in == "max":
    qqt_in = calculate_max_units(inventory[0][0], id_price, id_increase)
  else:
    qqt_in = int(qqt_in)
  
  #Price to pay
  priceToPay = 0
  for i in range(qqt_in):
    priceToPay += arrond(id_price * id_increase**i)
  if id_price is not None and inventory[0][0] >= priceToPay:
    #reward
    if not inventory.get(id_in) :
      inventory[id_in] = [qqt_in,id_name]
    else:
      inventory[id_in][0] += qqt_in
    prec_bought_string = "+{} {}".format(qqt_in, id_name)
    inventory[0][0] -= priceToPay
    inventory[0][0] = arrond(inventory[0][0])
    #new price
    if inShop == "i":
      dict_shop_items[id_in][0] = arrond(id_price * id_increase**qqt_in)
    elif inShop == "u":
      dict_shop_upgrades[id_in][0] = arrond(id_price * id_increase**qqt_in)
    enter_shop(inShop)
  else:
    print("Not enough paper or wrong id\n")
    enter_shop(inShop)


def exit_shop():
  global DISPLAY
  global user_input
  global prec_bought_string
  DISPLAY = True
  clear()
  user_input = '\0'
  prec_bought_string = ""


def gain_function():
  global bonusTimer
  global bonusMulti
  if DISPLAY:
    clear()
    display_ressources(inventory, item_mutli_dict, bonusMulti)
  reward = 1
  for id, itemData in inventory.items():
    if id < 0 :continue
    itemNumber = itemData[0]
    reward += addition * (item_mutli_dict[id] * itemNumber)
  #Asc multi
  reward = reward * (piles**fold)
  #Sharpening tool
  #reward = (reward/100) * (100+2*inventory[5][0])
  #Bonus mutli
  if bonusTimer > 0:
    reward *= bonusMulti
    bonusTimer -= 1
  else:
    bonusMulti = 1
  inventory[0][0] += arrond(reward)
  timer = threading.Timer(sleepTime, gain_function)
  timer.daemon = True
  timer.start()


#============MAIN=============

timer = threading.Timer(sleepTime, gain_function)
timer.start()

try:
  while True:
    user_input = input("")
    if user_input == "shop" or user_input == "s":
      enter_shop()
    elif user_input == "cut" and inventory[3][0] > 0:
      if (bonusMulti <= inventory[3][0]):
        bonusMulti += 2
      bonusTimer += 5
    elif user_input == "paper" or user_input == "pp":
      #A revoir ptet
      inventory[0][0] += max(inventory[1][0] * manual_multiplier / 2, 1)

except KeyboardInterrupt:
  timer.cancel()
  end_game(inventory)
