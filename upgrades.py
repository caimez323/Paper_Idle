##upgrades

#Augemntation en %
#pp bonus en fonction de ?
#mltiplicateur de keyword ?


#sharpening tools 
#same price than before but increase auto reward you get by 2%
#high price increase
sharpening_tool_price = 700
sharpening_tool_incr = 3
sharpening_tool_name = "Sharpening tool"
sharpening_tool_number = 0



def get_upgrades_shop():
  upgrades_shop_dict = {
    0:  [None, "DEBUG"],\
    -1: [sharpening_tool_price, sharpening_tool_name, sharpening_tool_incr]}
  
  return upgrades_shop_dict