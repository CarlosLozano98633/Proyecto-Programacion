with open(r"C:\Users\edloz\Proyecto-Programación\J. K. Rowling - Harry Potter 1 - Sorcerer's Stone (1).txt", "r") as archivo:
    texto = archivo.read()
palabras = texto.split()
total_palaras=len(palabras)
conteo = dict()
for palabra in palabras:
    if palabra in conteo:
        conteo[palabra] += 1
    else:
        conteo[palabra] = 1
c_espacios = len(texto)
num_espacios = 0
for espacio in texto:
    if espacio == "\n" or espacio == " " or espacio == "\t":
        num_espacios += 1
sin_espacios = c_espacios - num_espacios

    

