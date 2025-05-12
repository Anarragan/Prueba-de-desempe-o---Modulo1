# Prueba de desempeño - Modulo1

Programa para la gestion de inventarios

Este programa permite la administracion de un inventario de productos que puede crecer de forma dinamica y cuenta con 7 funciones que se describen acontinuacion, no se necesita el uso de ninguna libreria externa:

__-Add_product:__ Esta funcion recibe 3 parametros (name, price, amount). El primer argumento es de tipo string, el segundo de tipo float y el tercero de tipo int; usa ciclos para determinar la existencia de un producto, si ya está muestra el mensaje con la aclaracion. Si el producto no se encuentra verifica que los valores ingresados sean numeros positivos y crea un diccionario para el producto, luego el diccionario lo agrega como elemento a la variable global de tipo lista llamada inventory.

__-Search_product:__ Recibe un solo parametro que es el nombre del producto, usa un ciclo para recorrer la lista global, si el nombre del producto se encuentra en la lista muestra detalles como el nombre, el precio y la cantidad; si no se encuentra el producto lo muestra de froma clara.

__-Update_price:__ Recibe 2 parametros (name, new_price), el primero de tipo string y el segundo de tipo float. Verifica que el nuevo precio ingresado sea un numero positivo y si el producto se encuentra, si es asi busca el nombre del producto y accede a su valor, en este caso una tupla(price, amount). Se toma solo la cantidad de la tupla asosiada al nombre y se ignora su precio, luego se crea una variable llamada new_tup y se iguala al nuevo precio ingresado (new_price) y se conserva el valor de la cantidad anterior, la tupla anterior se reemplaza por la nueva tupla creada y se muestra un mensaje con la actualizacion y el nuevo precio.

__-Delete_product:__ Se recibe un solo parametro llamado name, busca el producto dentro de la lista inventory y si está lo elimina, si no está, señala que el producto no se encuentra.

__-Calculate_total_price:__ Usa una funcion lambda para calcular el precio total del inventario, hace un ciclo para recorrer cada producto en la lista inventario y toma sus valores asociados, cada elemento se puede ver como un Xi, lo que hace la funcion es una sumatoria de price*amount para cada Xi.

__-Show_menu:__ Solo muestra un menu al usuario

__-main:__ Es la funcion principal en donde se hace el llamado a todas las funciones dependiendo de la opcion seleccionada, valida los datos de entrada y verifica que las opciones selecionadas esten disponibles. Pide los datos dependiendo de la opcion y los pasa como parametros a las funciones ya establecidas. Si se selecciona 1 Llama a la funcion add_product y si los productos de la lista global (inventory) son menores a 5 pide los 5 que se necesitan como minimo, si hay mas de 5 hace el proceso normal. Si se seleciona 2 llama a la funcion search_product y se le pasa el parametro de nombre. Si se selecciona 3 llama a la funcion update_price y se pide el nombre y el nuevo precio para pasarlos como parametros a la funcion. Si se selecciona 4 llama a la funcion delete_product pide el nombre y se le pasa como parametro. Si se selleciona 5 llama a la funcion anonima calculate_total_price y esta realiza el calculo y lo muestra. Si se selecciona 6 sale del programa.

__-if _name_ == "__main__":__ Hace que el archivo ejecute solo lo que hay en el y no lo ejecuta en caso de que se importe como modulo en otro archivo, pero se puede hacer el llamado tradicional de main() sin ningun problema.


