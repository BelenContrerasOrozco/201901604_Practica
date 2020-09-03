import json
salir = False

print("")
print("-----------------BIENVENIDO A SimpleQL-----------------")
print("")
print("Primero que nada debes cargar unos archivos: ")
print(" archivo1 \n archivo2 \n archivo3 \n archivo4 \n archivo5 \n archivo6 \n archivo7 \n archivo8 \n archivo9 \n archivo10 \n ... \n archivoN")
opciones_cargar = input("CARGAR: ")
cadena1 = opciones_cargar.lower().split(sep=', ')

for i in range(len(cadena1)): 
    print("Se cargo el archivo "+cadena1[i])

while not salir:

    print("")
    print("Elija una opción:")
    print("  1. Cargar \n  2. Seleccionar \n  3. Máximo \n  4. Mínimo \n  5. Suma \n  6. Cuenta \n  7. Reportar \n  8. Salir")
    opcion = input("Ingrese la opcion que eligio: ")

#CARGAR LISTO
    if opcion== "1" or opcion.lower() == "cargar" or opcion.lower() == "1. cargar" or opcion.lower()=="1.cargar":
        print("")
        print("-----Opción de 'Cargar'-----")
        print("Archivos que puede cargar:")
        print("archivo1 \n archivo2 \n archivo3 \n archivo4 \n archivo5 \n archivo6 \n archivo7 \n archivo8 \n archivo9 \n archivo10 \n ... \n archivoN")
        opciones_cargar1 = input("CARGAR: ")
        cadena1 = opciones_cargar1.lower().split(sep=', ') + opciones_cargar.lower().split(sep=', ')

        for i in range(len(cadena1)): 
            print("Se cargo el archivo "+cadena1[i])

#SELECCIONAR LISTO  
    elif opcion== "2" or opcion.lower() == "seleccionar" or opcion.lower() == "2. seleccionar" or opcion.lower()=="2.seleccionar":
        print("")
        print("-----Opción de 'Seleccionar'-----")
        print("Atributos que puede seleccionar para ver:")
        print(" nombre \n edad \n activo \n promedio")
        select = input("SELECCIONAR: ")
        selecccion= select.replace(', ', ' ')
        cadena2 = selecccion.lower().split(sep=' ')
        #print(cadena2)

        for i in range(len(cadena2)):
            if cadena2[i] == "donde":
                clave = i

        tipo = (cadena2[clave+1])
        condicion = (cadena2[clave+3])

        if clave == 3:
            buscar1 = cadena2[clave-3]
            buscar2 = cadena2[clave-2]
            buscar3 = cadena2[clave-1]
        elif clave ==2:
            buscar1 = cadena2[clave-2]
            buscar2 = cadena2[clave-1]
        elif clave == 1:
            buscar1 = cadena2[clave-1]
      
        if tipo == "nombre":
            def cargar_json(ruta):
                with open(ruta) as contenido:
                    archivo = json.load(contenido)
                    for element in archivo:
                        encontrado = (element.get('nombre'))
                        if encontrado.lower() == condicion or ('"'+encontrado.lower()+'"')==condicion:
                            if clave == 3:
                                print(buscar1 + ": " + str(element.get(buscar1)))
                                print(buscar2 + ": " + str(element.get(buscar2)))
                                print(buscar3 + ": " + str(element.get(buscar3)))
                            elif clave==2:
                                print(buscar1 + ": " + str(element.get(buscar1)))
                                print(buscar2 + ": " + str(element.get(buscar2)))
                            elif clave==1:
                                if buscar1 =="*":
                                    print(element)
                                else:
                                    print(buscar1 + ": " + str(element.get(buscar1)))

            for i in range(len(cadena1)): 
                ruta = '201901604_Practica/'+cadena1[i]+'.json'
                cargar_json(ruta)

        elif tipo == "edad":
            def cargar_json(ruta):
                with open(ruta) as contenido:
                    archivo = json.load(contenido)
                    for element in archivo:
                        encontrado = (element.get('edad'))
                        if encontrado == int(condicion):
                            if clave == 3:
                                print(buscar1 + ": " + str(element.get(buscar1)))
                                print(buscar2 + ": " + str(element.get(buscar2)))
                                print(buscar3 + ": " + str(element.get(buscar3)))
                            elif clave==2:
                                print(buscar1 + ": " + str(element.get(buscar1)))
                                print(buscar2 + ": " + str(element.get(buscar2)))
                            elif clave==1:
                                if buscar1 =="*":
                                    print(element)
                                else:
                                    print(buscar1 + ": " + str(element.get(buscar1)))

            for i in range(len(cadena1)): 
                ruta = '201901604_Practica/'+cadena1[i]+'.json'
                cargar_json(ruta)

        elif tipo == "activo":
            def cargar_json(ruta):
                with open(ruta) as contenido:
                    archivo = json.load(contenido)
                    for element in archivo:
                        encontrado = (element.get('activo'))
                        if encontrado == condicion.lower():
                            if clave == 3:
                                print(buscar1 + ": " + str(element.get(buscar1)))
                                print(buscar2 + ": " + str(element.get(buscar2)))
                                print(buscar3 + ": " + str(element.get(buscar3)))
                            elif clave==2:
                                print(buscar1 + ": " + str(element.get(buscar1)))
                                print(buscar2 + ": " + str(element.get(buscar2)))
                            elif clave==1:
                                if buscar1 =="*":
                                    print(element)
                                else:
                                    print(buscar1 + ": " + str(element.get(buscar1)))

            for i in range(len(cadena1)): 
                ruta = '201901604_Practica/'+cadena1[i]+'.json'
                cargar_json(ruta)

        elif tipo == "promedio":
            def cargar_json(ruta):
                with open(ruta) as contenido:
                    archivo = json.load(contenido)
                    for element in archivo:
                        encontrado = (element.get('promedio'))
                        if encontrado == float(condicion):
                            if clave == 3:
                                print(buscar1 + ": " + str(element.get(buscar1)))
                                print(buscar2 + ": " + str(element.get(buscar2)))
                                print(buscar3 + ": " + str(element.get(buscar3)))
                            elif clave==2:
                                print(buscar1 + ": " + str(element.get(buscar1)))
                                print(buscar2 + ": " + str(element.get(buscar2)))
                            elif clave==1:
                                if buscar1 =="*":
                                    print(element)
                                else:
                                    print(buscar1 + ": " + str(element.get(buscar1)))

            for i in range(len(cadena1)): 
                ruta = '201901604_Practica/'+cadena1[i]+'.json'
                cargar_json(ruta)

        elif select == "*":
            def cargar_json(ruta):
                with open(ruta) as contenido:
                    archivo = json.load(contenido)
                    for element in archivo:
                        print(element)

            for i in range(len(cadena1)): 
                print("Datos del "+cadena1[i])
                ruta = '201901604_Practica/'+cadena1[i]+'.json'
                cargar_json(ruta)

#MAXIMO LISTO
    elif opcion== "3" or opcion.lower() == "máximo" or opcion.lower() == "maximo" or opcion.lower()=="3. máximo" or opcion.lower() == "3. maximo" or opcion.lower() == "3.máximo" or opcion.lower()=="3.maximo":
        print("")
        print("-----Opción de 'Máximo'-----")
        print("Atributos que puede seleccionar para ver el valor máximo de los archivo:")
        print(" edad \n promedio")
        maxximo = input("MÁXIMO: ")
        maximo = 0
        maximo_final =0 

        if (maxximo.lower()) == "edad":
            def cargar_json(ruta):
                mayor=0
                with open(ruta) as contenido:
                    archivo = json.load(contenido)
                    for element in archivo:
                        edad = (element.get('edad'))
                        if edad>mayor:
                            mayor = edad
                        else:
                            mayor = mayor
                    return mayor

            for i in range(len(cadena1)): 
                ruta = '201901604_Practica/'+cadena1[i]+'.json'
                maximo = (cargar_json(ruta))
                if maximo>maximo_final:
                    maximo_final = maximo
                else:
                    maximo_final = maximo_final
            print("La edad más grande es: "+str(maximo_final))

        elif (maxximo.lower()) == "promedio":
            def cargar_json(ruta):
                mayor = 0
                with open(ruta) as contenido:
                    archivo = json.load(contenido)
                    for element in archivo:
                        promedio = (element.get('promedio'))
                        if promedio>mayor:
                            mayor = promedio
                        else:
                            mayor = mayor
                    return mayor

            for i in range(len(cadena1)): 
                ruta = '201901604_Practica/'+cadena1[i]+'.json'
                maximo = (cargar_json(ruta))
                if maximo>maximo_final:
                    maximo_final = maximo
                else:
                    maximo_final = maximo_final
            print("El promedio más grande es: "+str(maximo_final))

#MINIMO LISTO
    elif opcion== "4" or opcion.lower() == "mínimo" or opcion.lower() == "minimo" or opcion.lower()=="4. mínimo" or opcion.lower() == "4. minimo" or opcion.lower() == "4.mínimo" or opcion.lower()=="4.mínimo":
        print("")
        print("-----Opción de 'Mínimo'-----")
        print("Atributos que puede seleccionar para ver el valor mínimo de los archivo:")
        print(" edad \n promedio")
        mini = input("MINIMO: ")
        menor = 0
        minimo_final = 0

        if (mini.lower()) == "edad":
            def cargar_json(ruta):
                minimo=0
                with open(ruta) as contenido:
                    archivo = json.load(contenido)
                    for element in archivo:
                        edad = (element.get('edad'))
                        if minimo==0:
                            minimo = edad
                        elif edad>minimo:
                            minimo = minimo
                        else:
                            minimo = edad

                    return minimo

            for i in range(len(cadena1)): 
                ruta = '201901604_Practica/'+cadena1[i]+'.json'
                menor = (cargar_json(ruta))
                if minimo_final == 0:
                    minimo_final = menor
                elif menor>minimo_final:
                    minimo_final = minimo_final
                else:
                    minimo_final = menor
            print("La menor edad es: "+str(minimo_final))

        elif (mini.lower()) == "promedio":
            def cargar_json(ruta):
                minimo=0
                with open(ruta) as contenido:
                    archivo = json.load(contenido)
                    for element in archivo:
                        promedio = (element.get('promedio'))
                        if minimo==0:
                            minimo = promedio
                        elif promedio>minimo:
                            minimo = minimo
                        else:
                            minimo = promedio

                    return minimo

            for i in range(len(cadena1)): 
                ruta = '201901604_Practica/'+cadena1[i]+'.json'
                menor = (cargar_json(ruta))
                if minimo_final == 0:
                    minimo_final = menor
                elif menor>minimo_final:
                    minimo_final = minimo_final
                else:
                    minimo_final = menor
            print("El promedio más bajo es: "+str(minimo_final))

#SUMA LISTO
    elif opcion== "5" or opcion.lower() == "suma" or opcion.lower() == "5. suma" or opcion.lower()=="5.suma":
        print("")
        print("-----Opción de 'Suma'-----")
        print("Atributos que puede seleccionar para sumar todos los valores de todos los archivo:")
        print(" edad \n promedio")
        sumar = input("SUMAR: ")
        total_final = 0

        if sumar.lower() == "edad":
            def cargar_json(ruta):
                subtotal = 0 
                with open(ruta) as contenido:
                    archivo = json.load(contenido)
                    for elemento in archivo:
                        edad_obtenida = elemento.get('edad')
                        subtotal = subtotal + edad_obtenida
                    return subtotal

            for i in range(len(cadena1)): 
                ruta = '201901604_Practica/'+cadena1[i]+'.json'
                total =(cargar_json(ruta))
                total_final = total_final+ total
            print("Suma de edades: "+ str(total_final))

        elif sumar.lower() == "promedio":
            def cargar_json(ruta):
                subtotal = 0 
                with open(ruta) as contenido:
                    archivo = json.load(contenido)
                    for elemento in archivo:
                        promedio_sumado = elemento.get('promedio')
                        subtotal = subtotal + promedio_sumado
                    return subtotal

            for i in range(len(cadena1)): 
                ruta = '201901604_Practica/'+cadena1[i]+'.json'
                total =(cargar_json(ruta))
                total_final = total_final+ total
            print("Suma de promedios: "+ str(total_final))

#CUENTA LISTO
    elif opcion== "6" or opcion.lower() == "cuanta" or opcion.lower() == "6. cuenta" or opcion.lower()=="6.cuenta":
        print("")
        print("-----Opción de 'Cuenta'-----")
        print("La cantidad de objetos que se cargaron fueron: " + str(len(cadena1)*2))

#REPORTAR
    elif opcion== "7" or opcion.lower() == "reportar" or opcion.lower() == "7. reportar" or opcion.lower()=="7.reportar":
        print("")
        print("-----Opción de 'Reportar'-----")
        print("")
        print("Esta opción aun no esta disponible")
        print("")
        


#SALIR LISTO
    elif opcion== "8" or opcion.lower() == "salir" or opcion.lower() == "8. salir" or opcion.lower()=="8.salir":
        salir= True
    
    else:
        print(" \n Ese numero no es una opción!")

print("")
print("Ten un buen día!")
print("")
