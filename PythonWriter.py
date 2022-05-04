'''
Jadrien Hannon
7/3/2019
'''

import os
filepath = os.getcwd()
def CreateFile(file_name):
    #temp_path = filepath + file_name
    with open(file_name, 'w') as f:
        f.write("import random\n")
        f.write("myList=[random.randint(1, 6) for _ in range(6)]\n")
        f.write("for element in myList:\n")
        f.write("   if element == 3:\n")
        f.write("      print(\"element = 3\")\n")
        f.write("   else:\n")
        f.write("      print(\"element != 3\")\n")

CreateFile("writer.py")
