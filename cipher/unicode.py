def show():
     print(["encode","decode","asciiNums","asciiMessage","crack"])

def encode(message,key=0):
     return "".join([chr(ord(n)+int(key)) for n in message])
def decode(message,key=0):
     return "".join([chr(ord(n)-int(key)) for n in message])

def asciiNums(INmessage):
     return " ".join([str(ord(n)) for n in INmessage])
def asciiMessage(INmessage):
     return " ".join([chr(int(n)) for n in INmessage.split(" ")])

def crack(message):
     lowest = 110000
     for n in message:
          if ord(n) < lowest:
               lowest = ord(n)
     for m in range(32,64):
          print("(" + str(lowest-m) + ")-",end=" ")
          for n in message:
               print(chr(ord(n)-lowest+m),end="")
          print("\n")
          if input("Was that the message?\n").lower() == "yes":
               break
