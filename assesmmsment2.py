##Vending machine
water = {"Al ain(01)":"1 dhs","Masafi(02)":"1 dhs","Oasis(03)":"1 dhs","Aquafina(04)":"1 dhs","Arwa(05)":"1 dhs"} ##The menu
drinks = {"Coca cola(06)":" 2.5 dhs","7 up(07)":"2.5 dhs","Pepsi(08)":"2.5 dhs","Mountain dew(09)":"2.5 dhs","Fanta(10)":"2.5 dhs"} 
jelly = {"Fruit jelly(11)":"0.5 dhs","Gummy bears(12)":"1 dhs","Jelly beans(13)":"5 dhs","Soda jelly(14)":"0.5 dhs","Sour jelly(15)":"1 dhs"}
juices = {"Apple juice(16)":"2 dhs","Mango juice(17)":"2 dhs","Orange juice(18)":"2 dhs","Grape juice(19)":"2 dhs","Mix fruit juice(20)":"2 dhs"}
chips_small = {"Lays(Salt)(21)":"1 dhs","Lays(Cheese)(22)":"1 dhs","Lays(Tomato)(23)":"1 dhs","Lays(Chilli)(24)":"1 dhs","Lays(Salt & Vinger)(25)":"1 dhs"}
chips_big = {"takis(26)":"3 dhs","Doritos(27)":"3 dhs","Pringle(28)":"3 dhs","Buggles(29)":"3 dhs","Cheetos(30)":"3 dhs"}
items = [water,drinks,jelly,juices,chips_small,chips_big] ## storing the Menu
print("Below are the items present in the vending machine:-") ##Displaying the menu in neat form
print("- Al ain(01):1 dhs - Masafi(02):1 dhs - Oasis(03):1 dhs - Aquafina(04):1 dhs - Arwa(05):1 dhs.")
print("- Coca cola(06):2.5 dhs - 7 up(07):2.5 dhs - Pepsi(08):2.5 dhs - Mountain dew(09):2.5 dhs - Fanta(10):2.5 dhs.")
print("- Fruit jelly(11):0.5 dhs - Gummy bears(12):1 dhs - Jelly beans(13):5 dhs - Soda jelly(14):0.5 dhs - Sour jelly(15):1 dhs.")
print("- Apple juice(16):2 dhs - Mango juice(17):2 dhs - Orange juice(18):2 dhs - Grape juice(19):2 dhs - Mix fruit juice(20):2 dhs.")
print("- Lays(Salt)(21):1 dhs - Lays(Cheese)(22):1 dhs - Lays(Tomato)(23):1 dhs - Lays(Chilli)(24):1 dhs - Lays(Salt & Vinger)(25):1 dhs")
print("- takis(26):3 dhs - Doritos(27):3 dhs - Pringle(28):3 dhs - Buggles(29):3 dhs - Cheetos(30):3 dhs")
addi = 0 #declared variable
finished_order = [] ##list for the ordered items
while True: ##Taking the money as input
  money = float(input("Enter the money: "))
  i = str(input("Would you like to add more?(YES OR NO): "))
  addi += money
  if i == 'YES' or i == 'yes' or i == 'Yes':
    continue
  elif i == 'NO' or i == 'no' or i == 'No':
    break
  else:
    print("Wrong entry...")       
print("The amount you have entered is: ",addi) ##initial ammount
while True: ##Loop for the order
    if addi>0: ##While the balance is above 0 
      print("Your balance:",addi)
      order = str(input("Please choose the item by entering its numeric code:"))
      if order=='01' or order=='1' and addi>=1: ## each order having same line of codes
        print("You chose Al Ain water,here are some recommended items:")
        addi -= 1 ##reducting from actual value
        finished_order.append('Al Ain') ##storing ordered item in a list 
        print(chips_small)## recommending items to customer
        j = str(input("Would you like to continue?(YES or NO): "))##continuing to order or exiting the program
        if j=='YES' or j=='yes' or j=='Yes':
          continue
        elif j=='NO' or j=='no' or j=='No':
          break  
      elif order=='02' or order=='2' and addi>=1: ## same applied codes for 29 more orders as above
        print("You chose Masafi water,here are some recommended items:")
        addi -= 1
        finished_order.append('Masafi')
        print(chips_small)
        j = str(input("Would you like to continue?(YES or NO): "))
        if j=='YES' or j=='yes' or j=='Yes':
          continue
        elif j=='NO' or j=='no' or j=='No':
          break 
      elif order=='03' or order=='3' and addi>=1:
        print("You chose Oasis water,here are some recommended items:")
        addi -= 1
        finished_order.append('Oasis')
        print(chips_small)
        j = str(input("Would you like to continue?(YES or NO): "))
        if j=='YES' or j=='yes' or j=='Yes':
          continue
        elif j=='NO' or j=='no' or j=='No':
          break 
      elif order=='04' or order=='4' and addi>=1:
        print("You chose Aquafina water,here are some recommended items:")
        addi -= 1
        finished_order.append('Aquafina')
        print(chips_small)
        j = str(input("Would you like to continue?(YES or NO): "))
        if j=='YES' or j=='yes' or j=='Yes':
          continue
        elif j=='NO' or j=='no' or j=='No':
          break   
      elif order=='05' or order=='5' and addi>=1:
        print("You chose Arwa water,here are some recommended items:")
        addi -= 1
        finished_order.append('Arwa')
        print(chips_small)
        j = str(input("Would you like to continue?(YES or NO): "))
        if j=='YES' or j=='yes' or j=='Yes':
          continue
        elif j=='NO' or j=='no' or j=='No':
          break 
      elif order=='06' or order=='6' and addi>=2.5:
        print("You chose Coca Cola,here are some recommended items:")
        addi -= 2.5
        finished_order.append('Coca Cola')
        print(chips_big)
        j = str(input("Would you like to continue?(YES or NO): "))
        if j=='YES' or j=='yes' or j=='Yes':
          continue
        elif j=='NO' or j=='no' or j=='No':
          break  
      elif order=='07' or order=='7' and addi>=2.5:
        print("You chose 7 up,here are some recommended items:")
        addi -= 2.5
        finished_order.append('7 up')
        print(chips_big)
        j = str(input("Would you like to continue?(YES or NO): "))
        if j=='YES' or j=='yes' or j=='Yes':
          continue
        elif j=='NO' or j=='no' or j=='No':
          break 
      elif order=='08' or order=='8' and addi>=2.5:
        print("You chose Pepsi,here are some recommended items:")
        addi -= 2.5
        finished_order.append('Pepsi')
        print(chips_big)
        j = str(input("Would you like to continue?(YES or NO): "))
        if j=='YES' or j=='yes' or j=='Yes':
          continue
        elif j=='NO' or j=='no' or j=='No':
          break 
      elif order=='09' or order=='9' and addi>=2.5:
        print("You chose Mountain Dew,here are some recommended items:")
        addi -= 2.5
        finished_order.append('Mountain Dew')
        print(chips_big)
        j = str(input("Would you like to continue?(YES or NO): "))
        if j=='YES' or j=='yes' or j=='Yes':
          continue
        elif j=='NO' or j=='no' or j=='No':
          break
      elif order=='10' and addi>=2.5:
        print("You chose Fanta,here are some recommended items:")
        addi -= 2.5
        finished_order.append('Fanta')
        print(chips_big)
        j = str(input("Would you like to continue?(YES or NO): "))
        if j=='YES' or j=='yes' or j=='Yes':
          continue
        elif j=='NO' or j=='no' or j=='No':
          break
      elif order=='11' and addi>=0.5:
        print("You chose Fruit Jelly,here are some recommended items:")
        addi -= 0.5
        finished_order.append('Fruit Jelly')
        print(juices)
        j = str(input("Would you like to continue?(YES or NO): "))
        if j=='YES' or j=='yes' or j=='Yes':
          continue
        elif j=='NO' or j=='no' or j=='No':
          break
      elif order=='12' and addi>=1:
        print("You chose Gummy bears,here are some recommended items:")
        addi -= 1
        finished_order.append('Gummy bears')
        print(juices)
        j = str(input("Would you like to continue?(YES or NO): "))
        if j=='YES' or j=='yes' or j=='Yes':
          continue
        elif j=='NO' or j=='no' or j=='No':
          break
      elif order=='13' and addi>=5:
        print("You chose Jelly Beans,here are some recommended items:")
        addi -= 5
        finished_order.append('Jelly Beans')
        print(juices)
        j = str(input("Would you like to continue?(YES or NO): "))
        if j=='YES' or j=='yes' or j=='Yes':
          continue
        elif j=='NO' or j=='no' or j=='No':
           break
      elif order=='14' and addi>=0.5:
        print("You chose Soda Jelly,here are some recommended items:")
        addi -= 0.5
        finished_order.append('Soda Jelly')
        print(juices)
        j = str(input("Would you like to continue?(YES or NO): "))
        if j=='YES' or j=='yes' or j=='Yes':
          continue
        elif j=='NO' or j=='no' or j=='No':
          break
      elif order=='15' and addi>=1:
        print("You chose Sour Jelly,here are some recommended items:")
        addi -= 1
        finished_order.append('Sour Jelly')
        print(juices)
        j = str(input("Would you like to continue?(YES or NO): "))
        if j=='YES' or j=='yes' or j=='Yes':
          continue
        elif j=='NO' or j=='no' or j=='No':
          break
      elif order=='16' and addi>=2:
        print("You chose Apple Juice,here are some recommended items:")
        addi -= 2
        finished_order.append('Apple Juice')
        print(jelly)
        j = str(input("Would you like to continue?(YES or NO): "))
        if j=='YES' or j=='yes' or j=='Yes':
          continue
        elif j=='NO' or j=='no' or j=='No':
          break
      elif order=='17' and addi>=2:
        print("You chose Mango Juice,here are some recommended items:")
        addi -= 2
        finished_order.append('Mango Juice')
        print(jelly)
        j = str(input("Would you like to continue?(YES or NO): "))
        if j=='YES' or j=='yes' or j=='Yes':
          continue
        elif j=='NO' or j=='no' or j=='No':
          break
      elif order=='18' and addi>=2:
        print("You chose Orange Juice,here are some recommended items:")
        addi -= 2
        finished_order.append('Orange Juice')
        print(jelly)
        j = str(input("Would you like to continue?(YES or NO): "))
        if j=='YES' or j=='yes' or j=='Yes':
          continue
        elif j=='NO' or j=='no' or j=='No':
          break
      elif order=='19' and addi>=2:
        print("You chose Grape Juice,here are some recommended items:")
        addi -= 2
        finished_order.append('Grape Juice')
        print(jelly)
        j = str(input("Would you like to continue?(YES or NO): "))
        if j=='YES' or j=='yes' or j=='Yes':
          continue
        elif j=='NO' or j=='no' or j=='No':
          break
      elif order=='20' and addi>=2:
        print("You chose Mix Fruit Juice,here are some recommended items:")
        addi -= 2
        finished_order.append('Mix Fruit Juice')
        print(jelly)
        j = str(input("Would you like to continue?(YES or NO): "))
        if j=='YES' or j=='yes' or j=='Yes':
          continue
        elif j=='NO' or j=='no' or j=='No':
          break
      elif order=='21' and addi>=1:
        print("You chose Lays(Salt),here are some recommended items:")
        addi -= 1
        finished_order.append('Lays(Salt)')
        print(water)
        j = str(input("Would you like to continue?(YES or NO): "))
        if j=='YES' or j=='yes' or j=='Yes':
          continue
        elif j=='NO' or j=='no' or j=='No':
          break
      elif order=='21' and addi>=1:
        print("You chose Lays(Salt),here are some recommended items:")
        addi -= 1
        finished_order.append('Lays(Salt)')
        print(water)
        j = str(input("Would you like to continue?(YES or NO): "))
        if j=='YES' or j=='yes' or j=='Yes':
          continue
        elif j=='NO' or j=='no' or j=='No':
          break
      elif order=='22' and addi>=1:
        print("You chose Lays(Cheese),here are some recommended items:")
        addi -= 1
        finished_order.append('Lays(Cheese)')
        print(water)
        j = str(input("Would you like to continue?(YES or NO): "))
        if j=='YES' or j=='yes' or j=='Yes':
          continue
        elif j=='NO' or j=='no' or j=='No':
          break
      elif order=='23' and addi>=1:
        print("You chose Lays(Tomato),here are some recommended items:")
        addi -= 1
        finished_order.append('Lays(Tomato)')
        print(water)
        j = str(input("Would you like to continue?(YES or NO): "))
        if j=='YES' or j=='yes' or j=='Yes':
          continue
        elif j=='NO' or j=='no' or j=='No':
          break
      elif order=='24' and addi>=1:
        print("You chose Lays(Chilli),here are some recommended items:")
        addi -= 1
        finished_order.append('Lays(Chilli)')
        print(water)
        j = str(input("Would you like to continue?(YES or NO): "))
        if j=='YES' or j=='yes' or j=='Yes':
          continue
        elif j=='NO' or j=='no' or j=='No':
          break
      elif order=='25' and addi>=1:
        print("You chose Lays(Salt & Vinger),here are some recommended items:")
        addi -= 1
        finished_order.append('Lays(Salt)')
        print(water)
        j = str(input("Would you like to continue?(YES or NO): "))
        if j=='YES' or j=='yes' or j=='Yes':
          continue
        elif j=='NO' or j=='no' or j=='No':
          break
      elif order=='26' and addi>=3:
        print("You chose Takis,here are some recommended items:")
        addi -= 3
        finished_order.append('Takis')
        print(drinks)
        j = str(input("Would you like to continue?(YES or NO): "))
        if j=='YES' or j=='yes' or j=='Yes':
          continue
        elif j=='NO' or j=='no' or j=='No':
          break
      elif order=='27' and addi>=3:
        print("You chose Doritos,here are some recommended items:")
        addi -= 3
        finished_order.append('Doritos')
        print(drinks)
        j = str(input("Would you like to continue?(YES or NO): "))
        if j=='YES' or j=='yes' or j=='Yes':
          continue
        elif j=='NO' or j=='no' or j=='No':
          break
      elif order=='28' and addi>=3:
        print("You chose Pringle,here are some recommended items:")
        addi -= 3
        finished_order.append('Pringle')
        print(drinks)
        j = str(input("Would you like to continue?(YES or NO): "))
        if j=='YES' or j=='yes' or j=='Yes':
          continue
        elif j=='NO' or j=='no' or j=='No':
          break 
      elif order=='29' and addi>=3:
        print("You chose Buggles,here are some recommended items:")
        addi -= 3
        finished_order.append('Buggles')
        print(drinks)
        j = str(input("Would you like to continue?(YES or NO): "))
        if j=='YES' or j=='yes' or j=='Yes':
          continue
        elif j=='NO' or j=='no' or j=='No':
          break
      elif order=='30' and addi>=3:
        print("You chose Cheetos,here are some recommended items:")
        addi -= 3
        finished_order.append('Cheetos')
        print(drinks)
        j = str(input("Would you like to continue?(YES or NO): "))
        if j=='YES' or j=='yes' or j=='Yes':
          continue
        elif j=='NO' or j=='no' or j=='No':
          break                                                                                                           
      elif order>='30' or order<'0':## for wrong entry or having insufficient balance
        print("Insufficient Balance...")
        print("OR")
        print("Wrong entry...")
        l = str(input("Would you like to continue?(YES or NO): ")) ##choice for continuing or exiting 
        if l=='YES' or l=='yes' or l=='Yes':
          m = str(input("Would you like to add more money?(YES or NO): "))## adding more money after balance is low
          if m=='YES' or m=='yes' or m=='Yes':
            exmoney = float(input("The extra amount: "))
            addi += exmoney ## final balance
            continue
          elif m=='NO' or m=='no' or m=='No':
            continue
        elif l=='NO' or l=='no' or l=='No':
          break  
    elif addi<=0: ## final lines of codes for balance reaching 0 
      print("Oops,looks like you ran out of money")
      k = str(input("Would you like to add more?(YES or NO)"))
      if k=='YES' or k=='yes' or k=='Yes':
        extra = float(input("The extra amount: "))
        addi = addi + extra
        continue
      elif k=='NO' or k=='no' or k=='No':
        break  
print("Your order:-") ## display order and reciept
print(finished_order)
print("Your spare change:",addi)      
print("Thank you for the purchase.")