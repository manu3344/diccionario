import string
import time

def generate_combinations(length, charset, prefix=""):
    if length == 0:
        yield prefix
    else:
        for char in charset:
            yield from generate_combinations(length - 1, charset, prefix + char)

def main():

    start_time = time.time()#Registro del tiempo de inicio

    # Crear un archivo de texto
    with open("wordsCombination.txt", "w") as file:
        # Crear una lista con las letras del abecedario y los dígitos numéricos
        charset = list(string.ascii_lowercase + "ñ" + string.digits)
        charset = [letter.encode('utf-8').decode('latin-1') for letter in charset]

        # Definir la longitud de las combinaciones
        length = 4

        # Generar todas las posibles combinaciones de la longitud especificada
        combinations = generate_combinations(length, charset)

        # Iterar sobre todas las combinaciones
        for combination in combinations:
            # Escribir la cadena en el archivo
            file.write(combination + "\n")
    end_time = time.time()
    elapsed_time = end_time-start_time
    print("Tiempo transcurrido: ",elapsed_time, "segundos")

main()
