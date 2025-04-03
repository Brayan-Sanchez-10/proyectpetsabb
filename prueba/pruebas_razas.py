lista = ("pitbull","pastor","labrador","cazador","cazador","pitbull","pastor","pastor")
razas = {}
def listar_mascotas():
    for x in lista:
        if x in razas:
            razas[x] += 1
        else:
            razas[x] = 1
    return razas

print(listar_mascotas())
