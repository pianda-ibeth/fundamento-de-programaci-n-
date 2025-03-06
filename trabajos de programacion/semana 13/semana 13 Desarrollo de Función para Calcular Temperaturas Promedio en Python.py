#Tarea Individual: Desarrollo de Función para Calcular Temperaturas Promedio en Python

Objetivo: Practicar la definición y uso de funciones en Python para calcular temperaturas promedio y utilizar la plataforma GitHub para compartir el desarrollo de código. En esta tarea, utilizarás los datos de temperaturas de clases anteriores.

Instrucciones:

Recuperación del Repositorio en GitHub:

Accede al repositorio en GitHub que creaste previamente en una tarea anterior.
Desarrollo de la Función:

Desarrolla una función en Python que calcule la temperatura promedio de una ciudad durante un período de tiempo. La función debe ser capaz de manejar datos de temperaturas de múltiples ciudades y semanas.

Utiliza como base el ejemplo anterior, donde tenías datos de 3 ciudades durante 4 semanas.

Tu función debe recibir estos datos como parámetros y calcular la temperatura promedio de cada ciudad.

Subida del Nuevo Código:

Una vez que hayas probado y verificado que la función funciona correctamente en tu entorno local, agrega y haz commit de los cambios en tu repositorio local.

Utiliza el comando git commit and push para enviar los cambios al repositorio en GitHub existente. Esto actualizará el código en GitHub con la nueva función que has desarrollado.

Documentación:

Agrega comentarios al código para explicar cómo funciona tu función.

Pruebas y Verificación:

Realiza pruebas para verificar que la función calcule las temperaturas promedio correctamente.





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
def  temperaturas_promedio(ciudades_temperaturas):
ciudades = ["Ciudad de manabi", "Ciudad de guayaquil"]
for ciudad_idx, ciudad in enumerate(temperaturas):
    for semana_idx, semana in enumerate(ciudad):
        suma_temperaturas = sum([dia["temperatura"] for dia in semana])
        promedio = suma_temperaturas / len(semana)
        print(f"Promedio de temperaturas en {ciudades[ciudad_idx]}, Semana {semana_idx + 1}: {promedio:.2f} grados")

 return