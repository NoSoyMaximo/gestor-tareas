tareas = []

def agregar_tarea(titulo):
    if not titulo.strip():
        raise ValueError ('El titulo no puede estar vacio')
    tareas.append(titulo.strip())

def lista_tareas():
    return tareas

def eliminar_tarea(indice):
    return tareas.py(indice)
