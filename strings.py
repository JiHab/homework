fruit  = 'banana'
letter = fruit[1]
print(letter)

letter = fruit[0]
print(letter)

print(len(fruit))

length = len(fruit)
last = fruit[length-1]
print(last)

index = 0
while index < len(fruit):
    letter = fruit[index]
    print(letter)
    index = index+1

for char in fruit:
    print(char)

s = 'Monty Python'
print(s[0:5])
print(s[6:12])

fruit = 'banana'
print(fruit[:3])
print(fruit[3:])

greeting = 'Hello, wold!'
new_greeting = 'J'+greeting[1:]
print(new_greeting)

word = 'banana'
count = 0
for letter in word:
    if letter=='a':
        count = count+1
print(count)

print('a' in 'banana')
print('seed' in 'banana')

if word =='banana':
    print('All right, bananas.')

if word < 'banana':
    print('Your word, ' + word + ', comes before banana')
elif word > 'banana':
    print('Your word, ' + word + ', comes after banana')
else:
    print('All right, bananas.')

stuff = 'Hello word'
print(type(stuff))
print(dir(stuff))
print(help(str.capitalize))

new_word = word.upper()
print(new_word)

print(word.find('a'))
print(word.find('na'))
print(word.find('na',3))

line = ' here we go '
print(line.strip())
line = 'Please have a nice day'
print(line.startswith('Please'))
print(line.startswith('p'))

print(line.lower().startswith('p'))

data = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
atpos = data.find('@')
print(atpos)
sppos = data.find(' ',atpos)
print (sppos)
host = data[atpos+1:sppos]
print(host)

camels = 42
print('%d' % camels)
print(type('%d' % camels))

print('I have supported %d camels. '% camels )

print('In %d years I have spotted %g %s.' % (3, 0.1, 'camels'))

str = 'X-DSPAM-Confidence: 0.8475'
a = str.find(':')+2
b = str[a:]
print(b)
fl = float(b)
print(fl)
