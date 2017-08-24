import cipher

def show(connector=", "):
     returnmessage = []
     for d in dir(cipher):
          if d[0] != "_":
               if "Alph" not in d and "alph" not in d and d != "cipher":
                    returnmessage.append(d+"()")
               else:
                    returnmessage.append(d)
     print(connector.join(returnmessage))

#Full operating system
def operate(operation=""):
     output = ""
     #Inputs,help,failsafes
     if operation == "":
          operation=input("What would you like to do?\n")
     while " - " not in operation:
          operation=input("INVALID, please enter the input like this: (coding-type) (encode/decode):(key) - (message)\n").lower()
          if operation in ["exit",""," ","no thanks","let me out"]:
               print("Exiting...")
               return
          elif operation in ["help","suggestions","options","explain","what"]:
               explanation = input("What do you need help on?\n")
               if explanation in ["coding-type","codingtype","codes","(coding-type)"]:
                    print("You can do any of these as your coding type:\n unicode, ascii, shift, flip, or customAlphabet")
               elif explanation in ["encode","decode","encode/decode","(encode/decode)"]:
                    print("Choose whether you want to encode a message or decode a message.")
               elif explanation in ["key","(key)"]:
                    print("Whatever 'key' you want to use to encode or decode your message.")
               elif explanation in ["message","(message)"]:
                    print("Whatever message you want to encode or decode.")
               else:
                    print("Sorry I didn't understand")
               operation = input("What would you like to do?\n")
     #Breaking up 'operation' into operation and message
     operation = operation.split(" - ")
     message = " - ".join(operation[1:])
     #Breaking up 'operation' into different parts
     operation = operation[0].split(" ")
     encoder = operation[0]
     if ":" in operation[1]:
          #if key
          operation = operation[1].split(":")
          key = operation[1]
          operation = operation[0]
          haskey = True
     else:
          #no key
          operation = operation[1]
          haskey = False
     #Running the different ciphers
     if operation == "encode":
          #all encode operations
          if haskey:
               #all ciphers that have a key
               if encoder == "unicode":
                    output = cipher.encode(message,int(key))
               elif encoder == "shift":
                    output = cipher.shift(message,int(key))
               elif encoder == "customAlphabet":
                    output = cipher.customAlph(message,key)
          else:
               #all ciphers that dont have a key
               if encoder == "ascii":
                    output = cipher.asciiNums(message)
               elif encoder == "flip":
                    output = cipher.flip(message)
     elif operation == "decode":
          #all encode operations
          if haskey:
               #all ciphers that have a key
               if encoder == "unicode":
                    if key == "crack" or key == "break":
                         output = cipher.crack(message)
                    else:
                         output = cipher.decode(message,-int(key))
               elif encoder == "shift":
                    if key == "crack" or key == "break":
                         output = cipher.shiftbreak(message)
                    else:
                         output = cipher.shift(message,-int(key))
               elif encoder == "customAlphabet":
                    output = cipher.customAlph(message,key)
          else:
               #all ciphers that dont have a key
               if encoder == "ascii":
                    output = cipher.asciiMessage(message)
               elif encoder == "flip":
                    output = cipher.flip(message)
     else:
          print("INVALID Operation")
     #Output
     print("Your message is:\n" + output)
     return
