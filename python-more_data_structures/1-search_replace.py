#!/usr/bin/python3
def search_replace(my_list, search, replace):
    # Crear una nueva lista para almacenar los elementos reemplazados
    new_list = []
    for element in my_list:
        # Verificar si el elemento coincide con el elemento de búsqueda
        if element == search:
            # Reemplazar el elemento con el nuevo elemento
            new_list.append(replace)
        else:
            # Mantener el elemento tal como está
            new_list.append(element)
    
    return new_list
