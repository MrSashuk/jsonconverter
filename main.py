import json

a = open('data.json', 'r')
data = json.load(a)

first_name = sorted([value for dictionary in data for key, value in dictionary.items() if key == 'first_name' ])
lastname = sorted([value for i in data for key, value in i.items() if key == 'last_name' ])
email = sorted([value for o in data for key, value in o.items() if key == 'email'])
ip_adress = sorted([value for y in data for key, value in y.items() if key == 'ip_address'])


f_n = open('first_name.txt', 'w')
f_n.write(str(first_name))

l_n = open('lastname.txt', 'w')
l_n.write(str(lastname))

m_n = open('email.txt', 'w')
m_n.write(str(email))


m_t = open('ip_adress.txt', 'w')
m_t.write(str(ip_adress))



















