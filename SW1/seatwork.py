def conv(dollar):
    pesoRate = 56.95
    yenRate = 147.15
    
    peso = dollar * pesoRate
    yen = dollar * yenRate
    return peso, yen

print()
print("Dollar($)      Peso(P)          Yen(Y)")
convert = [59, 200, 500]
for dol in convert:
    peso, yen = conv(dol)
    print(f"{dol:<14} {peso:<16.2f} {yen:<16.2f}")
    
def main ():
    
    try:
        currency = input("Enter currency in Dollar($): ")
        dollarAmount = float(currency.replace(",", ""))
        pesoAmount, yenAmount = conv(dollarAmount)
        
        print(f"\t\t{dollarAmount:,.2f} US dollar")
        print(f"\t\t{pesoAmount:,.2f} in Philippine Peso")
        print(f"\t\t{yenAmount:,.2f} in Japanese Yen")
    except ValueError:
        print("Invalid!, Please Enter Valid currency!")
        return

if __name__ =="__main__":
    main()