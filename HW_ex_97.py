file = open('C:\\Users\\ACER\\Documents\\HW_3\\mail.txt')
#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
dic = dict()
for line in file:
    #print(line.split())
    word = line.split()[0]
    day = line.split()[2]
    if word == 'From':
        if day not in dic:
            dic[day] = 1
        else:
            dic[day]+=1
    else: continue
print(dic)

