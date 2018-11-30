exist = 0
Aname= input("enter name: ")
txtfile=open("text.txt").read()
for line in open("text.txt").readlines():
  name = line.split(", ")[0]
  address = line.split(", ")[1]
  if Aname.lower() == name.lower():
    exist = exist + 1
if exist > 1:
   print("names found")
   print("there are " +str(exist), " names in the file")
elif exist == 1:
  print("name found")
  print("There is " +str(exist), "name in the file")
else:
   print("no names found.")
