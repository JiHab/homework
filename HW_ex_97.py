file = open('C:\\Users\\ACER\\Documents\\HW_3\\mail.txt')
#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
mail_adr_dic = dict()
dic = dict()
for line in file:
    word = line.split()[0]
    day = line.split()[2]
    mail_adr = line.split()[1]
    if word == 'From':
        if day not in dic:
            dic[day] = 1
        else:
            dic[day]+=1
        if mail_adr not in mail_adr_dic:
            mail_adr_dic[mail_adr] = 1
        else:
            mail_adr_dic[mail_adr]+=1

    else: continue
print(dic)

