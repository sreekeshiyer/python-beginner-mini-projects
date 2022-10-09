
# https://en.wikipedia.org/wiki/Hill_cipher

def split(a): # splitting the string into its arbitary characters
    return [char for char in a]

def arbitaryNumbers(list): # returning the arbitary value of the alphabets
    list_arb=[]
    for i in list:
        list_arb.append(ord(i)-96)
    return list_arb

def remove(string): # removing all spaces
    return string.replace(" ", "")

def divide_chunks(l, n): # dividing lists into 2 each
    # looping till length l
    for i in range(0, len(l), n): 
        yield l[i:i + n]

def arbChar(list):
    chars=[]
    for i in list:
        chars.append(chr(i))
    return chars

cipherText=input()
cipherText=cipherText.lower()
cipherTextNew=remove(cipherText)

if len(cipherTextNew)%2!=0: # addition of dummy letter in case it is odd
    cipherTextNew+='a'


list_aplha=split(cipherTextNew)
arbNum=arbitaryNumbers(list_aplha) 

# [4, 15, 14, 15, 20, 20, 15, 21, 3, 8]

# matrix=[1,2,0,3]
matrix=[1,24,8,19] 
x=list(divide_chunks(arbNum,2))

cipherNum=[]

for i in range(len(x)):
    sum1=0
    sum2=0 
    sum1=x[i][0]*matrix[0]+x[i][1]*matrix[1]
    sum2=x[i][0]*matrix[2]+x[i][1]*matrix[3]
    cipherNum.append(sum1)
    cipherNum.append(sum2)

cipherNumArb=[]

for i in cipherNum:
    cipherNumArb.append((i%26)+96)

hillcipher=arbChar(cipherNumArb)

finalHillCipher=""

for i in hillcipher:
    finalHillCipher+=i

finalHillCipher=finalHillCipher.upper()
print(finalHillCipher)

