import csv
russian_artists = []
foreign_artists = []
with open('songs.csv', 'r', newline='') as f: #открываем исходный файл
    a = csv.reader(f, delimiter=';')
    b = list(a)[1:]
    for i in b: #проходимся по строчкам и смотрим на имя автора
        fl = False
        for j in i[1]: #проходимся по каждой букве и проверяем ее
            if not(j.isascii()) and j != 'ñ' and j != 'é': #проверяем букву
                fl = True
                break
        if fl and i[1] not in russian_artists: #если в слове хоть 1 буква русская, то относем ее к списку русских артистов
            russian_artists.append(i[1])
        if not fl and i[1] not in foreign_artists: #если в слове нет русскиз букв, то относем ее к списку иностранных артистов
            foreign_artists.append(i[1])
print(f'Количество российских исполнителей: {len(russian_artists)}') #выводим кол-во русских артистов
print(f'Количество иностранных исполнителей: {len(foreign_artists)}') #выводим кол-во иностранных артистов
#далее данные из списков записываем в файлы
f1 = open('russian_artists.txt', 'w')
for i in russian_artists:
    f1.write(i + '\n')
f2 = open('foreign_artists.txt', 'w')
for i in foreign_artists:
    f2.write(i + '\n')