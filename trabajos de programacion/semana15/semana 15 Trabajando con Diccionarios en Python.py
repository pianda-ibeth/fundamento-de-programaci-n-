"""Crear un Diccionario:

Crea un diccionario llamado informacion_personal que contenga información ficticia sobre una persona, incluyendo al menos las claves "nombre", "edad", "ciudad" y "profesion".
Acceder y Modificar Valores:

Accede al valor asociado con la clave "ciudad" y modifícalo con una ciudad diferente.
Agrega una nueva clave-valor al diccionario que represente la "profesion" de la persona.
Verificar Existencia de Claves:

Verifica si la clave "telefono" existe en el diccionario. Si no existe, agrégala con un número de teléfono ficticio.
Eliminar una Clave:

Elimina la clave "edad" del diccionario, ya que esa información no es necesaria.
Imprimir el Diccionario Final:

Imprime el diccionario resultante después de realizar todas las operaciones."""

# Crear el diccionario con información ficticia
informacion_personal = {
    "nombre": "denny peñafiel",
    "edad": 24,
    "ciudad": "manabi",
    "profesion": "Ingeniero"
}

# Acceder y modificar el valor de "ciudad"
informacion_personal["ciudad"] = "guayaquil"

# Agregar una nueva clave-valor para "profesion"
informacion_personal["profesion"] = "licenciado"

# Verificar si "telefono" existe, si no, agregarlo
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "099469341"

# Eliminar la clave "edad"
del informacion_personal["edad"]

# Imprimir el diccionario final
print(informacion_personal)
