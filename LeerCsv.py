import csv

def leer_archivo(name):
  datos = []
  with open(name) as f:
    reader = csv.reader(f)
    entro = False #Esto porque comienza con un x,y en el excel
    for fila in reader:
      if entro == True:
        punto = (int(fila[0]),int(fila[1]))
        datos.append(punto)
      entro = True
  return datos
