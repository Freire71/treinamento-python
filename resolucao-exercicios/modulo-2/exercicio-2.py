# NÃO ALTERAR ============================================
from random import choice
comida = choice(['uva', 'caqui', 'bacon', 'filé',
                 'minhoca', 'aranha', 'leite', 'queijo', ''])
# NÃO ALTERAR =============================================

print(f"A comida escolhida foi: {comida}")

if comida == "uva" or comida == "caqui":
    print("Essa comida pertence ao grupo das frutas")
elif comida == "bacon" or comida == "filé":
    print("Essa comida pertence ao grupo das carnes")
elif comida == "queijo" or comida == "bacon": 
    print("Essa comida pertence ao grupo dos laticínios")
else: 
    print("Eca! Isso é comestível?!")
