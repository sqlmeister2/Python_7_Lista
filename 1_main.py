zmienna = 1
zmienna2 = "A"

#lista jest to odpowiednik tablicy z javy
lista = [] #stworzenie pustej listy
print(lista)
lista = [1, 2, "c", "d", "haha"]
print(lista)


# uzycie funkcji len do dostania dlugosci (ilosci) elementów listy
# oraz sformatowanie tekstu, aby wyswietlic we wskazanym miejscu wskazany obiekt
print("Długośc listy: {}".format(len(lista)))

# #odwołanie się do konkretnego elementu w liście
print(lista[2])

#nadpisanie elementu listy nową wartością
lista[2] = "Ada"
print(lista)

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

#dodanie listy do listy. Zagniezdza się lista w liscie
lista.append(["g", "h"])
print(lista)
#odwołanie się do "zagnieżdzonej listy"
print(lista[6][0])

#dołącza element we wskazanym przez nas miejscu
lista.insert(3, "x") # pierwszy argument to miejsce gdzie chcemy umiejscowic
print(lista)

#metoda count czyli tutaj ile jest elementów równych 1
print("Ilość wystąpeiń znaku w danej liscie ", lista.count(1))

#metoda index daje pierwszy indeks wystąpienia zadanego elementu
print("Index ", lista.index("d"))


#funkcje działające tylko na liczbach
lista2 = [1, 20, 35, -5, 0]

print("Minimum: ", min(lista2))
print("Maksimum: ", max(lista2))

# max, min też można stosować na listach tekstowych, ale musza byc jednorodne typem, a nie mieszane.
print(max(["a", "b"]))

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



print(lista)
#wyswietlanie elementow listy za pomoca petli
for i in lista:
    print(i)

#wycinanie listy
print(lista[0:3])
print(lista[2:])
#bez wybranej ilosci ostatniego elementu
print("Bez wybranej ilości ostatniego elementu")
print(lista[:-1])


# zwraca wartosc logiczna czy podana wartosc jest w liscie
print(10 in lista)

#list comprehension
#uproszczona składnia list, szybkie wypełenienie list wartościami
my_list = [i for i in range(10)] # można tu dodać ifa
print(my_list)

#zamiana warości w wybranym fragmencie listy
my_list[1 : 3] = [ "A", "B"]
print(my_list)


# # Nie zadziała podmiana 3 wybranych elementów jedna wartoscia
# # my_list[1:4] = 'C'
# # print(my_list)

#Nalezy to zrobić za pomocą listy. 
# Zadziałało to tak, że 3 elemnty zostały zamienione jednym  
# Aby zamienić 3 elementy trzema elementami "C", trzeba by stworzyć jakąs metodę z pętlą
my_list[1:4] = ['C']
print(my_list)


#Łączenie list
lista3 = [50, 60]
lista4 = lista + lista3
print(lista4)
lista4 = lista + lista3*2
print(lista4)
# Rozszerzanie listy za pomocą metody extend
# my_list2 = ["FR", "GR"]
# my_list.extend(my_list2)
# print(my_list)




# #Kopiowanie i usuwanie listy
# print("-----")
# listCopy = newList
# print(newList)
# newList.clear() #czyszczenie listy. Niestey listCopy i newList to te same obiekty, tak więc obie zostały wyczyszczone
# print(listCopy)
# print(newList)

# #trzeba użyć metody copy, aby skopiowała się w nowe miejsce w pamięci
# newList = ["AU", "BE", "DE"]
# print(newList)
# listCopy = newList.copy()
# print(id(listCopy)) #sprawdzenie czy te dwie listy to te same obiekty
# print(id(newList))
# newList.clear()
# print(listCopy)


