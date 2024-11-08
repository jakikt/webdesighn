import random

teller_rett = 0

for i in range(0,10):
    riktig_tall = random.randint(1,10)

    gjett = str(input("gjett et tall mellon 1 og 10:"))
    if gjett = riktig_tall:
        print("riktig!")
        teller_rett = teller_rett + 1
    else:
        print("feil! det riktige tallet var", riktig_tall)

print("du klarte", teller_rett, "rette på 10 forsøk")