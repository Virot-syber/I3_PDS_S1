def electricity_bill (kwh):
    if kwh <0:
        return None
    tier1 = min(kwh, 50)
    tier2 = min(max(kwh - 50,0),150)
    tier3 = max(kwh-200,0)

    total = (tier1 * 480) + (tier2 * 610) + (tier3 * 730)
    total +=2000
    total *=1.1

    return round(total)

for kwh in [0, 35, 50, 120, 200, 350]:
    bill = electricity_bill(kwh)
    usd = bill /4100

    print(f"{kwh} kwh -> {bill} riel =({usd:.2f} USD)")

con = int(input("Enter your moonthly consumption (kwh): "))
bill = electricity_bill(con)

print("\t your electricity bill ","\n","-"*50)

if bill <0:
    print("INVVALID INPUT")
else:
    print ("Your monthly consumption :",con)
    print(f"Your electricity bill is : {bill} riel = {bill/4100:.2f} USd \n")