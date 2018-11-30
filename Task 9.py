ffile = "file.txt"
option = 0

def printname():
  sentence = ""
  name = input("enter name: ")
  address = input("enter address: ")
  sentence = sentence + name
  sentence = sentence + ", " + address + "\n"
  txtfile=open(ffile, "a")
  txtfile.write(sentence)
  txtfile.close()

def addressname():
  Aname= input("enter name: ")
  txtfile=open(ffile).read()
  for line in open(ffile).readlines():
    name = line.split(", ")[0]
    address = line.split(", ")[1]
    if Aname.lower() == name.lower():
      print(address)

def namecheck():
  exist = 0
  Aname= input("enter name: ")
  txtfile=open(ffile).read()
  for line in open(ffile).readlines():
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

while option != 4:
  print("type 1 to add to file")
  print("type 2 to print user")
  print("type 3 to check name")
  print("type 4 to exit")
  option = int(input(""))
  if option == 1:
    printname()
  elif option == 2:
    addressname()
  elif option == 3:
    namecheck()
