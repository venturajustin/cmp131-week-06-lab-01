#Justin ventura week 6 lab 1 phone bill 10/1/26
packageprice = 99
packagessold = int(input("How many packages have been sold: "))
packagestotal = packageprice * packagessold
if packagessold <= 9:
    print("there is no discount")
elif packagessold >=10 and packagessold <= 19:
    print("there is a 20 percent discount")
    packagesdiscountprice = packagestotal / 0.20
    print("the total price after discount is:" , packagesdiscountprice)
elif packagessold >=20 and packagessold <= 49:
    print("there is a 30 percent discount")
    packagesdiscountprice = packagestotal / 0.30
    print("the total price after discount is:" , packagesdiscountprice)
elif packagessold >=50 and packagessold <= 99:
    print("there is a 40 percent discount")
    packagesdiscountprice = packagestotal / 0.40
    print("the total price after discount is:" , packagesdiscountprice)
elif packagessold >= 100:
    print("there is a 50 percent discount")
    packagesdiscountprice = packagestotal / 0.50
    print("the total price after discount is:" , packagesdiscountprice)


