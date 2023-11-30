

def display_shop_items(inventoryDict,shopDict):
  print("Paper : {}".format(inventoryDict[0][0]))
  for id,item_data in shopDict.items():
    if id == 0: 
      continue
    print("{} : {} : {}".format(id,item_data[1],item_data[0]))
