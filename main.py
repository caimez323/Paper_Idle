import threading
import os

from shop_scripts import display_shop_items
from common import clear, arrond, display_ressources, end_game
from items import get_items_shop, reset_inventory, get_multiplier_dict

#Addition and ascention
addition = 1
fold = 1
piles = 1
sleepTime = 2

bonusMulti = 1
bonusTimer = 0

manual_multiplier = 1

#Get all usefull dicts
dict_shop = get_items_shop()
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


def enter_shop():
  global DISPLAY
  global prec_bought_string
  DISPLAY = False
  clear()
  print("Welcome to the shop : \n")
  print(prec_bought_string)
  display_shop_items(inventory, dict_shop)
  print("\nEnter what you want : id * qqt (or 'max')")
  id_in = input("id : ")
  if (id_in == "xs" or id_in == "xshop"):
    id_in = 0
    exit_shop()
    display_ressources(inventory,item_mutli_dict,bonusMulti)
    return
  #Id
  id_in = int(id_in)
  id_data = dict_shop.get(id_in)
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
    inventory[id_in][0] += qqt_in
    prec_bought_string = "+{} {}".format(qqt_in, id_name)
    inventory[0][0] -= priceToPay
    inventory[0][0] = arrond(inventory[0][0])
    #new price
    dict_shop[id_in][0] = arrond(id_price * id_increase**qqt_in)
    enter_shop()
  else:
    print("Not enough paper or wrong id\n")
    enter_shop()


def exit_shop():
  global DISPLAY
  global user_input
  DISPLAY = True
  clear()
  user_input = '\0'


def gain_function():
  global bonusTimer
  global bonusMulti
  if DISPLAY:
    clear()
    display_ressources(inventory,item_mutli_dict,bonusMulti)
  reward = 1
  for id, itemCoef in item_mutli_dict.items():
    reward += addition * (itemCoef * inventory[id][0])
  #Asc multi
  reward = reward * (piles**fold)
  #Bonus mutli 
  if bonusTimer > 0:
    reward *= bonusMulti
    bonusTimer-=1
  else:
    bonusMulti = 1
  inventory[0][0] += arrond(reward)
  timer = threading.Timer(sleepTime, gain_function)
  timer.daemon = True
  timer.start()


#============MAIN=============

timer = threading.Timer(sleepTime, gain_function)
timer.start()

try :
  while True:
    user_input = input("")
    if user_input == "shop" or user_input == "s":
      enter_shop()
    elif user_input == "cut" and inventory[3][0]>0:
      if(bonusMulti<=inventory[3][0]):
        bonusMulti += 2
      bonusTimer += 5
    elif user_input == "paper" or user_input =="pp":
      #A revoir ptet
      inventory[0][0] += max(inventory[1][0] * manual_multiplier /2 ,1)
      
except KeyboardInterrupt:
  timer.cancel()
  end_game(inventory)