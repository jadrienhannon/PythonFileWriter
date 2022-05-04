import random
myList=[random.randint(1, 6) for _ in range(6)]
for element in myList:
   if element == 3:
      print("element = 3")
   else:
      print("element != 3")
