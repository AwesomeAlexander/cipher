import cipher

def show():
     print(["shift","shiftbreak","smartshift","customAlph","flip","keyboardAlph"])

def shift(INmessage,key):
     library = [cipher.alphabet,cipher.capsAlph,cipher.numsAlph,cipher.puncAlph]
     OUTmessage = ""
     for n in INmessage:
          cont = False
          for l in library:
               if cont:
                    continue
               elif l.find(n) != -1:
                    OUTmessage = OUTmessage + l[(l.find(n) + key)%len(l)]
                    cont = True
          if not cont:
               OUTmessage = OUTmessage + n
     return OUTmessage

def shiftbreak(INmessage,returning=False,punctuation=True):
     messages = []
     for n in range(26):
          messages.append( str(n) + "- " + cipher.shift(INmessage,n,punctuation) )
     messages = "\n".join(messages)
     if returning:
          return messages
     else:
          print(messages)

def smartshift(INmessage,key):
     library = [cipher.alphabet,cipher.capsAlph,cipher.numsAlph,cipher.puncAlph]
     OUTmessage = ""
     for n in range(len(INmessage)):
          cont = False
          for l in library:
               if cont:
                    continue
               elif l.find(INmessage[n]) != -1:
                    if key > 0:
                         OUTmessage = OUTmessage + l[int(l.find(INmessage[n]) + (n+1)**key)%len(l)]
                    else:
                         key = abs(key)
                         OUTmessage = OUTmessage + l[int(l.find(INmessage[n]) - (n+1)**key)%len(l)]
                    cont = True
          if not cont:
               OUTmessage = OUTmessage + INmessage[n]
     return OUTmessage

def customAlph(INmessage,newAlph,times=1):
     for t in range(times):
          OUTmessage = ""
          for n in INmessage.lower():
               if newAlph.find(n) != -1:
                    OUTmessage = OUTmessage + cipher.alphabet[newAlph.find(n)]
               else:
                    OUTmessage = OUTmessage + n
          INmessage = OUTmessage
     return OUTmessage
     

def flip(INmessage):
     return cipher.customAlph(INmessage,cipher.backAlph)

def keyboardAlph(INmessage,key=0):
     return cipher.customAlph(INmessage,cipher.keyboard,key+1)

#def punctAlph(INmessage):
#     return cipher.customAlph(INmessage,cipher.puncAlph)
