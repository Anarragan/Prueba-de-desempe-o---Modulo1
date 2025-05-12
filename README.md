# Prueba de desempeño - Modulo1

Programa para la gestion de inventarios

Este programa permite la administracion de un inventario de productos que puede crecer de forma dinamica y cuenta con 7 funciones que se describen acontinuacion:

-Add_product: Esta funcion recibe 3 parametros (name, price, amount). El primer argumento es de tipo string, el segundo de tipo float y el tercero de tipo int; usa ciclos para determinar la existencia de un producto, si ya está muestra el mensaje con la aclaracion. Si el producto no se encuentra verifica que los valores ingresados sean numeros positivos y crea un diccionario para el producto, luego el diccionario lo agrega como elemento a la variable global de tipo lista llamada inventory.

-Search_product: Recibe un solo parametro que es el nombre del producto, usa un ciclo para recorrer la lista global, si el nombre del producto se encuentra en la lista muestra detalles como el nombre, el precio y la cantidad; si no se encuentra el producto lo muestra de froma clara.

-Update_price: Recibe 2 parametros (name, new_price), el primero de tipo string y el segundo de tipo float. Verifica que el nuevo precio ingresado sea un numero positivo y si el producto se encuentra, si es asi busca el nombre del producto y accede a su valor, en este caso una tupla(price, amount). Se toma solo la cantidad de la tupla asosiada al nombre y se ignora su precio, luego se crea una variable llamada new_tup y se iguala al nuevo precio ingresado (new_price) y se conserva el valor de la cantidad anterior, la tupla anterior se reemplaza por la nueva tupla creada y se muestra un mensaje con la actualizacion y el nuevo precio.

-Delete_product: Se recibe un solo parametro llamado name, busca el producto dentro de la lista inventory y si está lo elimina, si no está, señala que el producto no se encuentra.

-Calculate_total_price: 
