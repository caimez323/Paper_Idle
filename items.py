
paper = 65


#Ajouter des upgrades en % /passif /jsp quoi


#scissors
#basic
scissors_multiplier = 0.7
scissors_price = 5
scissors_incr = 1.2
scissors_name = "Auto scissors"
scissors_number = 0

#knife
#bit better
knife_multiplier = 1.7
knife_price = 10
knife_incr = 1.35
knife_name = "Knife"
knife_number = 0

#cutting pliers
#not that good but have a bonus multiplier keyword
cutting_pliers_multiplier = 2.6
cutting_pliers_price = 75
cutting_pliers_incr = 1.6
cutting_pliers_name = "Cutting pliers"
cutting_pliers_number = 0

#
#costly but good base stats



#
#same price than before but increase how many reward you get by a %
#high price increase


#
#average but multiplies manual cutting with scissors

#
#huge stats

#
#new keyword

#++prestige items : 



def get_items_shop():
  dict_shop = {\
    0: [None, "DEBUG"],\
    1: [scissors_price, scissors_name, scissors_incr],\
    2: [knife_price,knife_name, knife_incr],\
    3: [cutting_pliers_price,cutting_pliers_name,cutting_pliers_incr]}
  
  return dict_shop
  
def reset_inventory():
  inventory = {\
    0: [paper, "Paper"],\
    1: [scissors_number, scissors_name],\
    2: [knife_number,knife_name],\
    3: [cutting_pliers_number,cutting_pliers_name]}
  
  return inventory


def get_multiplier_dict():
  item_mutli_dict = {0: 0, \
    1: scissors_multiplier,\
    2: knife_multiplier,\
    3: cutting_pliers_multiplier}

  return item_mutli_dict
