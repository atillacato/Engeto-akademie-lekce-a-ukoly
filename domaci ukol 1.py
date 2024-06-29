mesta = ["Praha", "Viden", "Olomouc", "Svitavy", "Zlin", "Ostrava"]
ceny = [150, 200, 120, 120, 100, 180]
cara = "=" * 35
nabidka = """
1 - Praha   | 150
2 - Viden   | 200
3 - Olomouc | 120
4 - Svitavy | 120
5 - Zlin    | 100
6 - Ostrava | 180
"""
print(cara)
print ("VITEJTE U NASI APLIKACE DESTINATIO!")
print ("nejlevnější portál nabídky jízdenek")
print(cara)
destinace = input("CISLO DESTINACE:")
jmeno = input("JMENO:")
prijmeni = input("PRIJMENI:")
email = input("EMAIL:")
spravna_destinace = mesta[int(destinace) - 1]
cena = ceny[int(destinace) - 1]
print (cara)
print (f"""Děkuji, {jmeno}  za objednávku, Cílová destinace: {spravna_destinace} 
Cena jízdného: {cena}, na tvuj email {email} jsem ti poslal jízdenky. """)