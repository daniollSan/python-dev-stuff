#Prosty kalkulator

print("\t\t\t \\ \\ \\ \\ \\ \\ \\ \\ \\")
print("\t\t\t Prosty kalkulator")
print("\t\t\t \\ \\ \\ \\ \\ \\ \\ \\ \\")
print("\nWitaj w programie \"Prosty kalkulator\"" , end=" ")
print("\nJakie działanie chcesz wykonać:")

dzialanie = input("\n0-dodawanie\n1-odejmowanie\n2-mnożenie\n3-dzielenie\n")
print("Wybrałeś ", dzialanie) 

liczba1 = int(input("Podaj pierwszą liczbe do działania"))
liczba2 = input("Podaj drugą liczbe do działania")
liczba2 = int(liczba2)
wynik = liczba1 + liczba2

print("Wynik dodawania liczb ", liczba1, "+", liczba2, "=", wynik)

input("\n\nAby zakończyć naciśnij Enter!")
      
