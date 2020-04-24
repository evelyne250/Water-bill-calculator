print("Please Enter The Initial number of m3 after the last bill payment")
initial = float(input())

print("Please Enter The Current number of m3 on the meter")
current = float(input())
print("1: Public Tap")
print("2: Residential")
print("3: Non Residential")
print("4: Industries")
inp = int(input("Enter a number of your category: "))
diff = current - initial
if inp == 1:
  print( "Public Tap")
elif inp == 2:
  print( "Residential")
elif inp == 3:
  print( "Non Residential")
else:
  print( "Industries") 
if initial <= 0:
  print('Invalid Number of Initial consumption')
elif current <= 0:
  print('Invalid Number of Current consumption')
elif current < initial:
  print('Current consumption can not be under the initial consumption')
elif inp == 1:
  amt = diff * 323
  print('The amount is', round(amt), ' Rwanda Francs')
elif inp == 2 and diff < 6:
  amt = diff * 340 
  print('The amount is', round(amt), ' Rwanda Francs')
elif inp == 2 and diff < 21:
  amt = diff * 720 
  print('The amount is', round(amt), ' Rwanda Francs')
elif inp == 2 and diff < 51:
  amt = diff * 845
  print('The amount is', round(amt), ' Rwanda Francs')
elif inp == 2 and diff >= 51:
  amt = diff * 877
  print('The amount is', round(amt), ' Rwanda Francs')
elif inp == 3 and diff < 51:
  amt = diff * 877 
  print('The amount is', round(amt), ' Rwanda Francs')
elif inp == 3 and diff >= 51:
  amt = diff * 895
  print('The amount is', round(amt), ' Rwanda Francs' )
else:
  amt = diff * 736 
  print('The amount is', round(amt), ' Rwanda Francs')