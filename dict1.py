student_data = {
    'id1':{
    'name': ['Sara'],
    'class':['V'], 
    'subject':['English,Math,Science']
    },
    'id2':{
    'name': ['David'],
    'class':['V'], 
    'subject':['English,Math,Science']
    },
    'id3':{
    'name': ['Sara'],
    'class':['V'], 
    'subject':['English,Math,Science']
    },
    'id4':{
    'name': ['Surya'],
    'class':['V'], 
    'subject':['English,Math,Science']
    },
}

result = {}

for key,value in student_data.items():
    if value not in result.values():
        result[key] = value

print(result)

#activity 2
test_dict = {'Codingal': 2,'is': 2,'best': 2,'for': 2,'Coding': 1}

print("The original dictionary : " + str(test_dict))
K = 2

res = 0
for key in test_dict:
    if test_dict[key] == K:
        res = res + 1

print("Frequency of K is : " + str(res))

#activity 3
country_code = {'India' : '0091',
                'Australia' : '0025',
                'Nepal' : '00977'}

print("Country code for India -")
print(country_code.get('India','Not found'))

print("Country code for Japan -")
print(country_code.get('Japan','Not found'))