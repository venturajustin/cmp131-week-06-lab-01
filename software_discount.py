#justin ventura 10/1/2026 week 6 lab assigment 2 
package = input("what Package have you purchased A,B,C(please enter in uppercase and nothing else: )")
minutesused = int(input("How many minutes have you used: "))
if package == "A" :
    print("package is A Price is 39.99 450 min limit extra is 0.45 per min")
    extraminpriceA = 0.45
    priceA = 39.99
    if minutesused > 450:
        minextraused = minutesused - 450
        print("the extra minutes used is:",minextraused)

elif package == "B" :
    print("package is B")
elif package == "C" :
    print("package is C")