import random as rn

B, M = {}, {}
msg = 'Group No,Roll No,Name,Subject\n'

with open('BIO102.csv') as f :
    lst = f.read().splitlines()[1:]

for student in lst :
    data = student.split(',')
    if data[2] == 'yes' :
        B[data[0]] = data[1]
    elif data[2] == 'no' :
        M[data[0]] = data[1]

for n in range(1,13) :
    bio = rn.sample(list(B.keys()),5)
    math = rn.sample(list(M.keys()),1)

    msg += f'{n}'
    for s in bio : msg += f',{s},{B[s]},Bio\n'
    for s in math : msg += f',{s},{M[s]},Math\n'

    [B.pop(key) for key in bio]
    [M.pop(key) for key in math]

for n in range(13,39) :
    bio = rn.sample(list(B.keys()),4)
    math = rn.sample(list(M.keys()),2)

    msg += f'{n}'
    for s in bio : msg += f',{s},{B[s]},Bio\n'
    for s in math : msg += f',{s},{M[s]},Math\n'

    [B.pop(key) for key in bio]
    [M.pop(key) for key in math]

for n in range(39,41) :
    bio = rn.sample(list(B.keys()),5)
    math = rn.sample(list(M.keys()),2)

    msg += f'{n}'
    for s in bio : msg += f',{s},{B[s]},Bio\n'
    for s in math : msg += f',{s},{M[s]},Math\n'

    [B.pop(key) for key in bio]
    [M.pop(key) for key in math]


with open('BIO102 Groups.csv', 'w+') as f :
    f.truncate(0)
    f.write(msg)

print(B)