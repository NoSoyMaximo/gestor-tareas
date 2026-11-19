from tareas import agregar_tarea,lista_tareas,eliminar_tarea

agregar_tarea('Configurar git')
print( lista_tareas() )

eliminar_tarea(0)
print(lista_tareas())