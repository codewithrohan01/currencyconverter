 # currency  convert from INR to AED                                              83.66 INR = 1 USD 

curr1 = str(input("which currency you want's to convert : "))

if curr1 == "dollar" :
    dollar = int(input("amount in USD :"))
    ininr = dollar*83.66
    print(ininr)

elif curr1 == "INR" :
    rupee = int(input("Amount in INR :"))
    inusd = rupee/83.66
    print(inusd)

else:
     print("invalid")
