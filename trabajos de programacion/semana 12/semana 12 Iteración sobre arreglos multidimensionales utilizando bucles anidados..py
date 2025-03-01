"""Tarea: Registro de Temperaturas Diarias

Imagina que estás desarrollando una pequeña aplicación para rastrear las temperaturas diarias en diferentes ciudades. Puedes usar una matriz 3D para organizar esta información.

LINK: Abrir matriz Ejemplo

Tarea: Iteración de arreglos multidimensionales con bucles anidados

Crear una matriz 3D que represente los datos de temperaturas diarias en varias ciudades. En una dimensión, puedes tener diferentes ciudades, en otra dimensión, días de la semana (Lunes, Martes, Miércoles, etc.), y en la tercera dimensión, semanas.
Dentro de cada celda de la matriz, puedes almacenar las temperaturas diarias para una ciudad en un día específico de una semana determinada.
Utilizar bucles anidados para calcular el promedio de temperaturas para una ciudad por cada una de las semanas.
Mostrar el promedio de temperaturas para cada ciudad y semana en la pantalla."""
temperaturas= [
   [ #ciudad de manabi
    [ # semana 1
       {"dia": "Lunes", "temperatura":78},
        {"dia":"martes","temperatura":55},
       {"dia":"mircoles","temperatura":100},
       {"dia":"jueves","temperatura":78},
       {"dia":"viernes","temperatura":81},
        {"dia":"sabado","temperatura":80},
        {"dia":"domingo","temperatura":86}
     ],
    [ #semana 2
         {"dia":"luness","temperatura":71},
        {"dia":"martes","temperatura":92},
        {"dia":"mircoles","temperatura":93},
        {"dia":"jueves","temperatura":80},
        {"dia":"viernes","temperatura":79},
        {"dia":"sabado","temperatura":80},
        {"dia":"domingo","temperatura":86}
    ],
    [ #semana 3
        {"dia":"lunes","temperatura":72},
        {"dia":"martes","temperatura":73},
        {"dia":"mircoles","temperatura":74},
        {"dia":"jueves","temperatura":80},
        {"dia":"viernes","temperatura":79},
        {"dia":"sabado","temperatura":80},
        {"dia":"domingo","temperatura":86}
    ],
   [# semana 4
       {"dia":"lunes","temperatura":73},
       {"dia":"martes","temperatura":74},
       {"dia":"mircoles","temperatura":75},
       {"dia":"jueves","temperatura":60},
       {"dia":"viernes","temperatura":79},
       {"dia":"sabado","temperatura":80},
       {"dia":"domingo","temperatura":86}
   ]
],
   [ # ciudad de guayaquil
       [# semana 1
       {"dia":"lunes","temperatura":79},
       {"dia":"martes","temperatura":43},
       {"dia":"mircoles","temperatura":74},
       {"dia":"jueves","temperatura":80},
       {"dia":"viernes","temperatura":99},
       {"dia":"sabado","temperatura":80},
       {"dia":"domingo","temperatura":86}
   ],
    [# semana 2
         {"dia":"lunes","temperatura":72},
         {"dia":"martes","temperatura":93},
         {"dia":"mircoles","temperatura":44},
         {"dia":"jueves","temperatura":80},
         {"dia":"viernes","temperatura":70},
         {"dia":"sabado","temperatura":80},
         {"dia":"domingo","temperatura":66}
    ],
   [ # semana 3
       {"dia":"lunes","temperatura":62},
       {"dia":"martes","temperatura":73},
       {"dia":"mircoles","temperatura":94},
       {"dia":"jueves","temperatura":80},
       {"dia":"viernes","temperatura":79},
       {"dia":"sabado","temperatura":80},
       {"dia":"domingo","temperatura":96}
   ],
   [ #semana 4
       {"dia":"lunes","temperatura":72},
       {"dia":"martes","temperatura":73},
       {"dia":"mircoles","temperatura":74},
       {"dia":"jueves","temperatura":80},
       {"dia":"viernes","temperatura":79},
       {"dia":"sabado","temperatura":80},
       {"dia":"domingo","temperatura":86}
   ],
]
]
#Calcular el promedio de temperaturas para cada ciudad y semana
ciudades = ["Ciudad de manabi", "Ciudad de guayaquil"]
for ciudad_idx, ciudad in enumerate(temperaturas):
    for semana_idx, semana in enumerate(ciudad):
        suma_temperaturas = sum([dia["temperatura"] for dia in semana])
        promedio = suma_temperaturas / len(semana)
        print(f"Promedio de temperaturas en {ciudades[ciudad_idx]}, Semana {semana_idx + 1}: {promedio:.2f} grados")

