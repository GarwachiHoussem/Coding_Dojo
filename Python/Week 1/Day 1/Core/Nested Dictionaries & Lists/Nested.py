# EX1

x = [ [5,2,3], [10,8,9] ]
students = [
 {'first_name': 'Michael', 'last_name' : 'Jordan'},
 {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
 'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
 'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

x[1][0]=15
students[0]["last_name"]="bryan"
sports_directory['soccer'][0]="Andres"
z[0]["y"]=30


# EX2
students = [
 {'first_name': 'Michael', 'last_name' : 'Jordan'},
 {'first_name' : 'John', 'last_name' : 'Rosales'},
 {'first_name' : 'Mark', 'last_name' : 'Guillen'},
 {'first_name' : 'KB', 'last_name' : 'Tonel'}
 ]
def iterateDictionary(students):
    for i in students:
        for key,value in i.items():
            print(f"{key} - {value}")
    


def iterateDictionary2(key_name, some_list):
    for i in students:
        for key,value in i.items():
            if key==key_name :
                print(value)

# iterateDictionary2('last_name', students)
# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)

dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
 }
def iterateDictionary3(dict):
    for key,value in dict.items():
        print(str(len(value)) + " " + key)
        for i in range (0,len(value)):
            print(value[i])

iterateDictionary3(dojo)
