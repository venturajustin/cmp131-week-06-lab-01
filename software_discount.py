#justin ventura 10/1/2026 week 6 lab assigment 2 
package = input("what Package have you purchased A,B,C(please enter in uppercase and nothing else: )")
minutesused = int(input("How many minutes have you used: "))
if package == "A" :
    print("package A Price is 39.99 450 min limit extra is 0.45 per min")
    extraminpriceA = 0.45
    priceA = 39.99
    if minutesused > 450:
        minextraused = minutesused - 450
        print("the extra minutes used is:",minextraused)
        totalbill = priceA + (minextraused + extraminpriceA)
    else:
        totalbill = priceA
    print("Total amount due is $", totalbill)

elif package == "B" :
    print("package B Price is 59.99 900 min limit extra is 0.40 per min")
    extraminpriceB = 0.40
    priceB = 59.99
    if minutesused > 900:
        minextraused = minutesused - 900
        print("the extra minutes used is:",minextraused)
        totalbill = priceB + (minextraused + extraminpriceB)
    else:
        totalbill = priceB
    print("Total amount due is $", totalbill)

elif package == "C" :
    print("package is C")
    priceC = 69.99
    totalbill = priceC
    print("Total amount due is $", totalbill)