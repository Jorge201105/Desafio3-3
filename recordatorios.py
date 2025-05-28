recordatorios = [['2021-01-01', "11:00", "Levantarse y ejercitar"],
 ['2021-05-01', "15:00", "No trabajar"],
 ['2021-07-15', "13:00", "No hacer nada es feriado"],
 ['2021-09-18', "16:00", "Ramadas"],
 ['2021-12-25', "00:00", "Navidad"]]


# se ingresa el día 2 de febrero como fecha de empezar el año, en las respuestas aparece el 01 de Febrero pero la pregunta habla del 02 de Febrero(detalle)
empezar_año= ["2021-02-02","06:00","Empezar el año"]
recordatorios.insert(1,empezar_año)

# Se cambia día en el indice 3 de la lista
recordatorios[3] = ["2021-07-16","13:00","No hacer nada es feriado"]

# Se comprueba que lo que estamos borrando sea el ía del trabajo y después lo dejamos como comentario
# print(recordatorios[2])
recordatorios.pop(2)

# Se agregan ambas cenas en las posiciones según orden de fecha.
cena_navidad = ["2021-12-24","22:00","Cena de Navidad"]
cena_año_nuevo = ["2021-12-31","22:00","Cena de año nuevo"]

recordatorios.insert(4,cena_navidad)
recordatorios.insert(6,cena_año_nuevo)



# Output, imprime a lo largo, pero coincidiendo con la respuesta (se deja como comentario, ya que, se determino hacer un for para presentar respuesta)
## print(recordatorios)
# con este for se deja el listado de elementos dispuesto hacia abajo como esta en la respuesta del apunte
for elemento in recordatorios:
    print(elemento)