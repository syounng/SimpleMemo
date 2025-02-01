people = [{'name': 'bob', 'age': 20}, 
          {'name': 'carry', 'age': 38},
          {'name': 'john', 'age': 7},
          {'name': 'smith', 'age': 17},
          {'name': 'ben', 'age': 27}]

def getAgeByName(name):
    for x in people:
            if x['name']==name:
                a = x['name'] + ' is ' + str(x['age']) + ' years old'
                return a
    return 'this name does not exist'

def setNameAndAge(name, age):
     x = {name:age}
     people.append(x)
     return people

print(setNameAndAge('chloe', 27))