f = open('C:\\Users\\ACER\\Documents\\romeo.txt')
l2=[]
for line in f:
    l2 = l2 + line.replace('\n','').split(' ')
l2.sort()
print(l2)

l_or = []
l_or = [c for c in l2 if c not in l_or]
#for word in l2:
 #   if word in l_or:
  #      q = 1+2
   # else:
    #    l_or.append(word)

print(l_or)
#f2= open('C:\\Users\\ACER\\Documents\\romeo.txt').read()
#print(f2.read())
#for word in f2:
#    print(word)
#

    #print(line)
    #print(line.replace('\n',' '))

    #line.split(' ')
    #print(line.split(' '))