#Exercise 1
#
#Create a program that asks the user to enter their name and their age. Print out a 
#message addressed to them that tells them the year that they will turn 100 years old.
#
#Extras:
#
#1. Add on to the previous program by asking the user for another number and printing 
#out that many copies of the previous message. (Hint: order of operations exists in 
#Python)

#2. Print out that many copies of the previous message on separate lines. (Hint: the 
#string "\n is the same as pressing the ENTER button)


name = input("Nombre: ")    # En python 2.7 funciona con raw_input()
				# En python 3 se usa input() supuestamente
age = int(input("Edad: "))

print("Tu nombre es " + name)
print("Tu edad es " + str(age))

print("Vas a cumplir 100 años en el ano " + str(100-age+2018))

times = int(input("Cuantas veces queres imprimir lo anterior? "))

for i in range(times):
	print("Tu nombre es " + name)
	print("Tu edad es " + str(age) + "\n")
