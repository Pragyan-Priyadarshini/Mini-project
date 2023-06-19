with open('currency values.txt') as f:
    lines=f.readlines()
currencyDict={}
for line in lines:
    a=line.split('\t')
    currencyDict[a[0]] = a[1]
amount = int(input("Enter Amount:\n"))    
print("Enter the name of the currency you want to it to.\n Available options are :")
[print(item) for item in currencyDict.keys()]
currency = input("Please enter one of these options: \n")
print(f"{amount} INR is equal to {amount *float(currencyDict[currency])} {currency}")