#Programita para chequear si dos palabras son anagramas

a=list('albert einstein')
b=list('entre tinieblas')
print(a)
print(b)

#Ordeno cada una
a.sort()
b.sort()
print(a)
print(b)

anagram = True

#Comparo letra por letra
for i in range(len(a)):
	if (a[i] != b[i]):
		anagram = False
		break

print('Anagram is ', anagram)
