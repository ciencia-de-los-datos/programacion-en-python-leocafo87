"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------
Este archivo contiene las preguntas que se van a realizar en el laboratorio.
No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.
Utilice el archivo `data.csv` para resolver las preguntas.
"""

def pregunta_01():
    """    Retorne la suma de la segunda columna.
    Rta/
    214
    """
    total = 0
    with open('./data.csv', 'r') as archivo:
        for linea in archivo.readlines():
            columnas = linea.split('\t')
            valor = int(columnas[1])
            total += valor
    archivo.close()
    return(total)
    

def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]

    """
    with open('./data.csv', 'r') as archivo:
        conteos = {}
        result=[]

        for linea in archivo.readlines():
            columnas = linea.strip().split('\t')
            valor_variable = columnas[0]
            if valor_variable not in conteos:
                conteos[valor_variable] = 1
            else:
                conteos[valor_variable] += 1
        for element in conteos:
            result.append((element,conteos.get(element)))
            result.sort()
    archivo.close()
    return(result)


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]

    """
    with open('./data.csv', 'r') as archivo:
        sumas = {}
        result=[]

        for linea in archivo.readlines():
            columnas = linea.strip().split('\t')
            valor_variable = columnas[0]
            if valor_variable not in sumas:
                sumas[valor_variable] = int(columnas[1])
            else:
                sumas[valor_variable] = sumas[valor_variable] + int(columnas[1])
        for element in sumas:
                result.append((element,sumas.get(element)))
                result.sort()
        archivo.close()
    return(result)


def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]

    """
    with open('./data.csv', 'r') as archivo:
        conteos_mes = {}
        result=[]

        for linea in archivo.readlines():
            columnas = linea.strip().split('\t')
            col_fecha = columnas[2]
            col_fecha = col_fecha.split('-')
            mes = col_fecha[1]
            if mes not in conteos_mes:
                conteos_mes[mes] = 1
            else:
                conteos_mes[mes] += 1
        for element in conteos_mes:
                result.append((element,conteos_mes.get(element)))
                result.sort()
        archivo.close()
    return(result)


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """
    with open('./data.csv', 'r') as archivo:
        conteos_max_min ={}
        resultado=[]

        for linea in archivo.readlines():
            columnas = linea.strip().split('\t')
            variable = columnas[0]
            valor = columnas[1]
            if variable not in conteos_max_min:
                conteos_max_min[variable] = []
            conteos_max_min[variable].append(int(valor))

        
        for variable, valor in conteos_max_min.items():
            max_val = max(valor)
            min_val = min(valor)
            resultado.append((variable,max_val,min_val))
            resultado.sort()
        archivo.close()
    return(resultado)


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """
    with open('./data.csv', 'r') as archivo:
        cont_max_min ={}
        result=[]

        for linea in archivo.readlines():
            columnas = linea.strip().split('\t')
            diccionario = columnas[4]

            for item in diccionario:
                valores = diccionario.strip().split(',')
            
            for par in valores:
                clave = par.split(':')

                if clave[0] not in cont_max_min:
                    cont_max_min[clave[0]] = []
                cont_max_min[clave[0]].append(int(clave[1]))
        
        for variable, valor in cont_max_min.items():
            max_val = max(valor)
            min_val = min(valor)
            result.append((variable,min_val,max_val))
            result.sort()
        archivo.close()

    return(result)


def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """
    with open('./data.csv', 'r') as archivo:
        lista = {}
        resultado=[]

        for linea in archivo.readlines():
            columnas = linea.strip().split('\t')
            numeros = columnas[1]
            letra = columnas[0]

            if numeros not in lista:
                lista[numeros] = []
            lista[numeros].append(letra)

        for numero in lista:
            num = int(numero)
            resultado.append((num,lista.get(numero)))
        resultado.sort()
        archivo.close()
    return(resultado)


def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """
    with open('./data.csv', 'r') as archivo:
        lista = {}
        resultado=[]

        for linea in archivo.readlines():
            columnas = linea.strip().split('\t')
            numeros = columnas[1]
            letra = columnas[0]

            if numeros not in lista:
                lista[numeros] = []
            if letra not in lista[numeros]:
                lista[numeros].append(letra)
                lista[numeros].sort()

        for numero in lista:
            num = int(numero)
            resultado.append((num,lista.get(numero)))
        resultado.sort()
        archivo.close()
    return(resultado)


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """
    with open('./data.csv', 'r') as archivo:
        cont_max_min ={}
        result=[]
        dic_res={}

        for linea in archivo.readlines():
            columnas = linea.strip().split('\t')
            diccionario = columnas[4]

            for item in diccionario:
                valores = diccionario.strip().split(',')
            
            for par in valores:
                clave = par.split(':')

                if clave[0] not in cont_max_min:
                    cont_max_min[clave[0]] = []
                cont_max_min[clave[0]].append(int(clave[1]))
        
        for variable , valor in cont_max_min.items():
            cant_entradas = len(valor)
            result.append((variable,cant_entradas))
            dic_res[variable] = cant_entradas
        orderdic = dict(sorted(dic_res.items()))            
        archivo.close()

    return(orderdic)


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]
    """
    with open('./data.csv', 'r') as archivo:
        
        result=[]

        for linea in archivo.readlines():
            columnas = linea.strip().split('\t')
            letra = columnas[0]
            col4 = columnas[3]
            col5 = columnas[4]

            for item in col4:
                entidades = len(col4.strip().split(','))
                parejas = len(col5.strip().split(','))
            result.append((letra,entidades,parejas))
        archivo.close()
 
    return(result)


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }


    """
    with open('./data.csv', 'r') as archivo:
        
        sumas = {}

        for linea in archivo.readlines():
            columnas = linea.strip().split('\t')
            cadena = columnas[3]
            valor= columnas[1]

            for item in cadena:
                letra = cadena.split(',')
            for caracter in letra:
                if caracter not in sumas:
                    sumas[caracter] = int(valor)
                else:
                    sumas[caracter] = sumas[caracter] + int(valor)
        orderdic = dict(sorted(sumas.items()))
        archivo.close()
 
    return(orderdic)


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """
    with open('./data.csv', 'r') as archivo:
        
        sumas = {}

        for linea in archivo.readlines():
            columnas = linea.strip().split('\t')
            cadena = columnas[4]
            letra= columnas[0]

            for item in cadena:
                tupla = cadena.split(',')
            for cadena in tupla:
                var1=cadena.split(':')
                if letra not in sumas:
                    sumas[letra] = int(var1[1])
                else:
                    sumas[letra] = sumas[letra] + int(var1[1])
        orderdic = dict(sorted(sumas.items()))    

        archivo.close()
 
    return(orderdic)
