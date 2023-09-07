# write your code here
person = {
    'name': "asmaa" ,
    'age' : 16 ,
    'hobbies' : ['drawing' , 'swimming' , 'reading']
}

print(person.get('name'))
print(person.get('age'))

person['age']= 17
print(person)

person['country'] = 'syria'
print(person)
print(len(person))

person['hobbies'].append('skating')
print(person)

def check_hobbies(person) :
    if len(person['hobbies']) >= 3 :
        print('wow you are amazing !!')
    else :
        print('try to do something new !! ')
check_hobbies(person)