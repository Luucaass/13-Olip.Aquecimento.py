#A entrada consiste em vários casos de teste. Cada caso contém um valor real V e um valor inteiro N, representando o valor que uma figurinha rara foi vendida, e a quantidade de integrantes do grupo de Charlinho, incluindo ele. Todos os valores serão possiveis de fazer 
#uma divisao por igual entre os membros do grupo.

#A saida imprima o valor que cada integrante ira receber


v,n = input().split()

div = float(v) / int(n)

result = "{:.2f}".format(div)

print(result)




