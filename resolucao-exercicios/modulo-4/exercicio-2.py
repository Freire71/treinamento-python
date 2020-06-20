amigos = ["Michaela", "Joaquim", "Marcela", "Jaqueline", "Bruno"]
bebidas = ["Vodka", "Licor de Café", "Rum de Coco", "Tequila", "Whiskey"]

amigos.remove("Marcela")
bebidas.pop(2)

print(f"Tamanho lista de amigos: {len(amigos)}")
print(f"Tamanho lista de bebidas: {len(bebidas)}")

amigos.insert(0, "Thiago")
bebidas.insert(2, "Gim")

amigos.sort()
print(amigos)
bebidas.reverse()
print(bebidas)

i = 0
while i < len(amigos):
    print(f"{amigos[i]} irá trazer {bebidas[i]}")
    i += 1

amigos.clear()
bebidas.clear()
print(amigos)
print(bebidas)    
