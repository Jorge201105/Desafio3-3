import sys

with open("lorem_ipsum.txt","r") as file:
    texto=file.read()

numero_caracteres=len(set(texto))
# Se realiza el chequeo de los caracteres encontrados y después se deja como comentario
# print(set(texto))
#print(numero_caracteres)


palabras = texto.split(" ")

#Se chequea el número de palabras encontradas con print pero despues se deja como comentario
# print(palabras)
numero_palbras = len(set(palabras))
#print(numero_palbras)

print(f"El número de carcateres distintos son : {numero_caracteres}")
print(f"El número de palabras distintas es : {numero_palbras}")