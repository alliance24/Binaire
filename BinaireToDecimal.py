
def signe(liste_binary):
	signe=""
	if liste_binary[0]=="0":
		signe="+"
	else:
		signe="-"
	return signe

def exposant(exposant_lenght, liste_binary):
	result=0
	for i in range(1, exposant_lenght+1, -1):
		result += liste_binary[i]*(base**i)
	
	if bits==32:
		result-=127
	elif bits==64:
		result-=1023
	return result




bits = int(input("Sur combien de bits ?\n"))

if bits==32:
	exposant_lenght = 8
elif bits==64:
	exposant_lenght = 11

base = int(input("Sur quelle base ?\n"))

binary = str(input("Entrez le nombre binaire...\n"))
liste_binary = []

liste_binary=list(str(binary))
for k in range(len(liste_binary)):
	liste_binary[k]=int(liste_binary[k])
print(liste_binary)
print(exposant(exposant_lenght, liste_binary))
# 010000000111



