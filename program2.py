from collections import Counter

count_f=0
count_m=0
count_a=0
x=0
all_names = []
all_un_age = []
all_names_age35_male = []

persons = [
    {
        "name": "Anna",
        "age": 31,
        "gender": "female"
    }, {
        "name": "Feris",
        "age": 36,
        "gender": "male"
    }, {
        "name": "Keanu",
        "age": 57,
        "gender": "male"
    }, {
        "name": "Angelina",
        "age": 46,
        "gender": "female"
    }, {
        "name": "Alex",
        "age": 42,
        "gender": "male"
    }, {
        "name": "Cortana",
        "age": 17,
        "gender": "female"
    }, {
        "name": "Jason",
        "age": 54,
        "gender": "male"
    }, {
        "name": "Oliver",
        "age": 50,
        "gender": "male"
    }, {
        "name": "Oliver",
        "age": 45,
        "gender": "male"
    }, {
        "name": "Harry",
        "age": 30,
        "gender": "male"
    }, {
        "name": "Harry",
        "age": 45,
        "gender": "male"
    }, {
        "name": "Harry",
        "age": 41,
        "gender": "male"
    }, {
        "name": "Alex",
        "age": 15,
        "gender": "male"
    }, {
        "name": "Alex",
        "age": 15,
        "gender": "male"
    }, {
        "name": "Alex",
        "age": 15,
        "gender": "male"
    }, {
        "name": "Federrico",
        "age": 40,
        "gender": "male"
    }

] 

def get_unique(l_in):
    l_out = list(set(l_in))
    return l_out

while len(persons)> x:
    if persons[x]['gender'] == 'female':
       count_f += 1
    if persons[x]['gender'] == 'male':
       count_m += 1
       if persons[x]['age'] > 35:
           if persons[x]['name'][0] == 'F':
               all_names_age35_male.append(persons[x]['name'])
    if persons[x]['age'] > 18:
       count_a += 1  
    all_names.append(persons[x]['name'])  
    all_un_age.append(persons[x]['age'])  
    x+=1   

print('Количество всех людей :',len(persons))
print('Женщин :',count_f)
print('Мужчин :',count_m)
print('Совершеннолетний персон :',count_a)

print('\nСписок всех имен: ')
for y in all_names:
    print(y)

all_un_age = get_unique(all_un_age)
all_un_age.sort()
print("\nСписок всех возрастов без повторений:", all_un_age)    


c = Counter(all_names)

print("\n3 Самых встречающих имён:")    
for y in c.most_common(3):
    print(y[0],' кол-во:',y[1])

print("\nИмена мужчин старше 35, имя которого начинается с F:")   
for aln in all_names_age35_male:
    print(aln)