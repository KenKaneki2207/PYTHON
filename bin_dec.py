#BASE TO DECIMAL

def base_dec(num):
    #length of the number
    #convert to string
    to = int(input("Enter the base number to be converted :"))
    num = str(num)
    length = len(num)
    l=[]
    for k in range(length):
        l.append(num[k])
    print(l)

    #converting to decimal
    dec = 0
    for j in range(len(l)):
        dec = dec + (to**j)*int(l[len(l)-j-1])
    print("DECIMAL EQUIVALENT OF BASE",to,"IS :",dec,sep=' ')
base_dec(11010111)
