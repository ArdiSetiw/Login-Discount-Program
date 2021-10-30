# Program Diskon
import secrets as gaca

print("="*57)
print("""\033[36m                  Menu Cafe PostTest 3
            > Beverages Menu
                - Teh           = Rp 5000
                - Kopi          = Rp 5000
                - Air           = Rp 2000
                - JusBuah       = Rp 10000
                - EnergyDrink   = Rp 10000
            > Food Menu
                - FrenchFries   = Rp 10000
                - NasiAyam      = Rp 15000
                - Pizza         = Rp 20000
                - Borger        = Rp 15000
                - Pudding       = Rp 5000\033[39m  """)
print("="*57)

# Hari beli 
day = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
hari = gaca.choice(day)
print("\033[32m            Hey you order this on",hari,"\033[39m")
print("="*57)

# Proses Input Minuman
x = 1
hargaMn = []    #List untuk harga minuman
Minum = []      #List minuman
print("-- Beverages --")
print(" Type your order as in menu\n Type end if you finish ordering")
while x > 0 :
    mn = str(input("> Beverages Order = "))
    if mn == "Teh" or mn == "teh" :
        price_mn = 5000
        hargaMn.append(price_mn)
        Minum.append(mn)
    elif mn == "Kopi" or mn == "kopi" :
        price_mn = 5000
        hargaMn.append(price_mn)
        Minum.append(mn)
    elif mn == "Air" or mn == "air" :
        price_mn = 2000
        hargaMn.append(price_mn)
        Minum.append(mn)
    elif mn == "JusBuah" or mn == "jusbuah" :
        price_mn = 10000
        hargaMn.append(price_mn)
        Minum.append(mn)
    elif mn == "EnergyDrink" or mn == "energydrink" :
        price_mn = 10000
        hargaMn.append(price_mn)
        Minum.append(mn)
    elif mn == "End" or mn == "end" :
        print("-"*57)
        break
    else :
        print(" Sorry We don't have that in the Menu")
    
total_mn = sum(hargaMn)

# Proses Input Makanan
y = 1
hargaMk = [] # List Harga Makanan
makan = []   # List Makanan
print("-- Food --")
print(" Type your order as in menu\n Type end if you finish ordering")
while y > 0 :
    mk = str(input("> Food Order = "))
    if mk == "FrenchFries" or mk == "frenchfries" :
        price_mk = 10000
        hargaMk.append(price_mk)
        makan.append(mk)
    elif mk == "NasiAyam" or mk == "nasiayam" :
        price_mk = 5000
        hargaMk.append(price_mk)
        makan.append(mk)
    elif mk == "Pizza" or mk == "pizza" :
        price_mk = 20000
        hargaMk.append(price_mk)
        makan.append(mk)
    elif mk == "Burger" or mk == "burger" :
        price_mk = 15000
        hargaMk.append(price_mk)
        makan.append(mk)
    elif mk == "Pudding" or mk == "pudding" :
        price_mk = 10000
        hargaMk.append(price_mk)
        makan.append(mk)
    elif mk == "End" or mk == "end" :
        break
    else :
        print(" Sorry We don't have that in the Menu")
    
total_mk = sum(hargaMk)

# Diskon Minuman
if len(Minum) >= 3 :
    print("="*57)
    print("\033[36mYour Beverages Order")
    for d in Minum :
        print("\033[36m-",d,"\033[39m")
    print("\033[32m| Beverages Prices = Rp",total_mn,"\033[39m")
    print("| You got 10% discount for ordering at least 3 beverages")
    total_mn = total_mn - (total_mn*10/100)
    print("\033[32m| Beverages Prices After Discount = ","Rp",total_mn,"\033[39m")
else : 
    print("\033[36mYour Beverages Order")
    for d in Minum :
        print("\033[36m-",d,"\033[39m")
    print("\033[32m| Beverages Prices = Rp",total_mn,"\033[39m")
print("="*57)

# Diskon Makanan
if len(makan) >= 2 :
    print("\033[36mYour Food Order")
    for f in makan :
        print("\033[36m-",f,"\033[39m")
    print("\033[32m| Food's Prices = Rp ",total_mk,"\033[39m")
    print("| You got 5% discount for ordering at least 2 foods ")
    total_mk = total_mk - (total_mk*5/100)
    print("\033[32m| Food's Prices After Discount = ","Rp",total_mk,"\033[39m")
else :
    print("\033[36mYour Food Order")
    for f in makan :
        print("\033[36m-",f,"\033[39m")
    print("\033[32m| Food's Prices = Rp",total_mk,"\033[39m")
price = total_mn + total_mk
print("="*57)
print("\033[32mBeverages and Food's Prices = Rp",price,"\033[39m")
print("="*57)

# Diskon Hari
if hari == "Saturday" or hari == "Sunday" :
    print("Since you order this on",hari,"you got 5% discount")
    price = price - (price * 5/100)
    print("\033[32mPrice After Weekend's Discount = Rp",price,"\033[39m")
else :
    print("you came to our shop at",hari,"here 10% discount")
    price = price - (price * 10/100)
    print("\033[32mPrice After Weekday's Discount = Rp",price,"\033[39m")

# Pembayaran and The End of the program
print("="*57)
print("""how would you like to pay
> Cash
> CC Card
> eMoney""")
print("="*57)
bayar = str(input("Payment = "))
if bayar == "eMoney" or bayar == "emoney" :
    print("eMoney Payment, you got 5% discount")
    price = price - (price * 5/100)
    print("\033[32mFinal Price = Rp",price,"\033[39m")
    print("="*57)
else : 
    print("\033[32mFinal Price = Rp",price,"\033[39m")
    print("="*57)