import os
import platform

OS_SYSTEM = platform.system()


def clear():
  global OS_SYSTEM
  os.system("clear" if OS_SYSTEM == "Linux" else "cls") 
  print("=== PAPER IDLE === Cutting paper...\n")

def end_game(theInventory):
  clear()
  print("End of PAPER IDLE")
  print("Paper : {}".format(theInventory[0][0]))



def arrond(n):
  toReturn = round(n,2)
  #Since python is bad at calculating things, toReturn could be higher than n
  if toReturn >n:
    toReturn -= 0.01
  return toReturn


def get_items_contribution(theInventory,theMulti):
  itemContributionSum = {}
  theSum = 0
  for theID,theIDData in theInventory.items():
    if theID < 0 : 
      itemContributionSum[theID] = 0
      continue
    itemContributionSum[theID] = theIDData[0] * theMulti[theID]
    theSum += itemContributionSum[theID]
  if theSum == 0 : theSum =1
  itemContribution = {id:arrond((value/theSum)*100) for id,value in itemContributionSum.items()}
  return itemContribution
  


def display_ressources(theInventory,theMulti,bonusMulti):
  #TODO PRINT DANS L ORDRE QUAND MEME
  itemContr = get_items_contribution(theInventory,theMulti)
  print("Bonus multiplier : {}\n".format(bonusMulti))
  for id, ressources_data in theInventory.items():
    if type(ressources_data[0]) == float and not ressources_data[0].is_integer():
      print("{} : {:.2f} ({})".format(ressources_data[1], ressources_data[0],itemContr[id]))
    else:
      print("{} : {:.0f} ({})".format(ressources_data[1], ressources_data[0],itemContr[id]))
  print("= = = = = = = = = = = = = =")