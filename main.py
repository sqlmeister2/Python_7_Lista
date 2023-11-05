zmienna = 1
zmienna2 = "A"

#lista jest to odpowiednik tablicy z javy
lista = [] #stworzenie pustej listy
print(lista)
lista = [1, 2, "c", "d", "haha"]
print(lista)

print("Długośc listy: {}".format(len(lista)))

#odwołanie się do konkretnego elementu w lisćie
print(lista[2])

#nadpisanie elementu listy nową wartością
lista[2] = "Ada"
print(lista)

#odwoływanie się do jednego znaku stringa. Zachowuje się jak lista
tekst = "Hello world"
print(tekst[2])

#można dołączać elementy do listy
print(lista + ["f", 'g'])

#mnożenie listy
print(lista * 3)

#dlugość listy za pomocą funkcji len
print("Ilość elementow listy ", len(lista))

#jako że lista jest obiektem możemy odwołać się po kropce do jej metod
#append dołącza do listy element umiejscawiająć go na końcu listy
lista.append("f")
print(lista)

#dodanie listy do listy
lista.append(["g", "h"])
print(lista)
#odwołanie się do "zagnieżdzonej listy"
print(lista[6][0])

#dołącza element we wskazanym przez nas miejscu
lista.insert(3, "x") # pierwszy argument to miejsce gdzie chcemy umiejscowic
print(lista)

#metoda count
print("Ilość wystąpeiń znaku w danej liscie ", lista.count(1))

#metoda index daje pierwszy indeks wystąpienia zadanego elementu
print("Index ", lista.index("d"))

#funkcje działające tylko na liczbach
lista2 = [1, 20, 35, -5, 0]

print("Minimum: ", min(lista2))
print("Maksimum: ", max(lista2))

#sortowanie listy
print("\nSortowanie listy")
print(f"Nieposortowana lista: {lista2}")
print(f"Lista posortowana jednorazowo bez zapamiętania {sorted(lista2)}") #sortowanie nietrwałe
print(f"Ta sama lista po raz kolejny {lista2}")
lista2.sort() #sortowanie trwałe
print(f"Lista po sortowaniu trwałym: {lista2}")

#odwrócenie kolejności listy
lista2.reverse()
print(lista2)

#czyszczenie listy, by była pusta
lista2.clear()
print(lista2)

print(lista)
for i in lista:
    print(i)

#odwracanie listy
lista.reverse()
print(lista)

#wycinanie listy
print(lista[0:3])
print(lista[2:])
#bez wybranej ilosci ostatniego elementu
print("Bez wybranej ilości ostatniego elementu")
print(lista[:-1])

#łaczenie list
lista3 = [50, 60]
lista4 = lista + lista3
print(lista4)
lista4 = lista + lista3*2
print(lista4)

#długośc listy
print(len(lista4))


print(10 in lista4)

#list comprehension
#uproszczona składnia list, szybkie wypełenienie list wartościami
my_list = [i for i in range(10)] # można tu dodać ifa
print(my_list)

#usuniecie elementu z listy o danej wartości
print(lista)
lista.remove("f")
print(lista)

#usuniecie ostatniego elementu z listy i z wybranego miejsca (indeksu)
print("\n",my_list)
print("Usuniecie ostatniego elementu z listy")
my_list.pop()
my_list.pop(4)
deleted = my_list.pop()
print(f"Usunięty, ale zapamiętany pod zmienną element to {deleted}")
print(my_list)
print("_---")

#zamiana warości w wybranym fragmencie listy
my_list[1 : 3] = [ "A", "B"]
print(my_list)

#wyzerowanie listy od wybranego miejsca
my_list[5:] = []
print(my_list)

print(my_list.index("B"))

print(my_list.count("A"))

my_list2 = ["FR", "GR"]
newList = my_list + my_list2
print(newList)
my_list.extend(my_list2)
print(my_list)

print("-----")
#kopiowanie i usuwanie listy
listCopy = newList
print(newList)
newList.clear() #czyszczenie listy. Niestey listCopy i newList to te same obiekty, tak więc obie zostały wyczyszczone
print(listCopy)
print(newList)

#trzeba użyć metody copy, aby skopiowała się w nowe miejsce w pamięci
newList = ["AU", "BE", "DE"]
print(newList)
listCopy = newList.copy()
print(id(listCopy)) #sprawdzenie czy te dwie listy to te same obiekty
print(id(newList))
newList.clear()
print(listCopy)




