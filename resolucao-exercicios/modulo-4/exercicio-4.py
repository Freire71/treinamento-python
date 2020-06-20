a = [1, 2, 3, 4]
b = [3, 4, 5, 6]


x = [num for num in a if num in b]
print(x)


heroinas = ["Capitã Marvel", "Mulher Maravilha", "Feiticeira Escarlate"]

sanioreh = [ heroina[::-1].lower() for heroina in heroinas ]
print(sanioreh)
