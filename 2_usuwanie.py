lista2 = ['a', "b", 2, 3, 4, "sześć", "b"]
print(lista2)

#czyszczenie listy, by była pusta
# Jest to metoda, dlatego nie potrzebuje przypisania do zmiennej na nowo
lista2.clear()
print(lista2)

#usuniecie elementu z listy o danej wartości
lista2 = ['a', "b", 2, 3, 4, "sześć", "b"]
print(lista2)
#usuneło tylko pierwszy jeden element z listy
lista2.remove("b")
print(lista2)

# jeżeli c nie istnieje w liście to rzuci błędem
# lista2.remove("c")

# Usuniecie z listy zadanego zakresu elementow. 
print(lista2)
lista2[1:3] = []
print(lista2)

# to samo co powyżej tylko do końca listy
lista2[2:] = []
print(lista2)

# Odejmowanie listy od listy nie zadziała
lista3 = [element for element in range(9)]
print(lista3)
# print(lista3 - lista3[1:4])

# #usuniecie ostatniego elementu z listy i z wybranego miejsca (indeksu)
lista3 = [element for element in range(9)]
print("\n",lista3)
print("Usuniecie ostatniego elementu z listy")
lista3.pop()
lista3.pop(4)
deleted = lista3.pop()
print(f"Usunięty, ale zapamiętany pod zmienną element to {deleted}")
print(lista3)
print("_---")