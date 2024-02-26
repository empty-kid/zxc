import csv
import datetime

with open('songs.csv', 'r', newline='') as f: #открываем исходный файл
    a = csv.reader(f, delimiter=';')
    b = list(a)[1:] #записываем в список все данные
    for i in b: #проходимся по каждой строчке и смотрим, где кол-во прослушиваний равно 0, а затем меняем
        if i[0] == '0':
            ln1 = len(i[1]) #кол-во символов в имени артиста
            ln2 = len(i[2]) #кол-во символов в названии песни
            ln = abs(ln1 + ln2) #общее кол-во
            c = i[3].split('.')
            date1 = datetime.date(year=int(c[2]), month=int(c[1]), day=int(c[0])) #первая дата
            date2 = datetime.date(year=23, month=5, day=12) #вторая дата
            days = abs((date1 - date2).days) #разность между ними в днях
            i[0] = str((days / ln) * 10000) #изменение кол-ва прослушиваний
    for i in b:#проходимся по каждой строчке и смотрим подходит ли она нам по дате
        c = i[3].split('.')
        date1 = datetime.date(year=int(c[2]), month=int(c[1]), day=int(c[0])) #дата из строки
        date2 = datetime.date(year=2002, month=1, day=1) #дата из условия
        if date1 <= date2: #сравнение дат
            print(f'{i[2]}-{i[1]}-{i[0]}')
with open('songs_new.csv', 'w', newline='') as file: #запись в файл
    file.write('streams;artist_name;track_name;date\n')
    for i in b:
        file.write(';'.join(i) + '\n')
