import numpy as np
import pandas as pd
import timeit

animais = ["Pato", "Cachorro", "Gato"] #criando uma lista
serie_animais = pd.Series(animais) #criando uma série a partir de uma lista
serie_animais

"""A série serie_animais tem os **índices** 0, 1 e 2 para acessar os animais Pato,   Cachorro e Gato.

É possível acessar a informação dessa série pelos índices usando **serie_animais.iloc[*índice*]**.
"""

print(serie_animais.iloc[0]) #acessando o primeiro indice
print(serie_animais.iloc[1]) #acessando o segundo indice
print(serie_animais.iloc[2]) #acessando o terceiro indice

#notar que o primeiro indice não é o 1 e sim o 0

"""Quando a série é criada a partir de um dicionário, pode-se usar outro método para acessar valores:"""

dicionario = {"Gabriela" : "Amarelo", "Leonardo": "Roxo", "Joao" : "Vermelho"} #criando uma dicionario
serie_dic = pd.Series(dicionario) #criando uma série a partir de um dicionário
serie_dic

"""Repare que agora temos um novo tipo de índice. Diferente da série anterior, os novos índices são **strings** que representam o **nome** de uma pessoa. Portanto, chamamos o método **.loc["*nome*"]**.

Mesmo com o novo índice sendo uma **string**, o **índice numérico** continua "escondido" por trás dessa estrutura de dados.


Sendo assim, é possível acessar as informações pelo **nome** ou pelo **índice numérico**.

Logo, quando se deseja saber o valor de um **nome** na série serie_dic, usa-se a função **serie_dic.loc["*nome*"]** e o acesso pelo **índice numérico** continua sendo feito pela função **serie_dic.iloc[*índice*]**.
"""

print(serie_dic.loc["Gabriela"]) #printando pelo nome
print("\n")
print(serie_dic.iloc[0]) #printando pelo índice

"""Note que executando o comando **serie_dic[0]** acessamos o mesmo valor de **serie_dic.iloc[0]**."""

print(serie_dic[0])
print("\n")
print(serie_dic.iloc[0])

"""O mesmo vale para **serie_dic["Gabriela"]** e **serie_dic.loc["Gabriela"]**."""

print(serie_dic["Gabriela"])
print("\n")
print(serie_dic.loc["Gabriela"])

"""Mas essa síntaxe não é a mais indicada pois alguns "acidentes" podem acontecer dependendo de como a estrutura da série está organizada."""

dic = {200 : "Tijolo", 4 : "Saco de cimento", 2 : "Martelo", 0 : "Chave de fenda"}
materiais = pd.Series(dic)
print(materiais)

"""Para o exemplo acima, tentando acessar **materiais[0]** e **materiais.iloc[0]** vamos ter valores diferentes."""

print(materiais[0])
print("\n")
print(materiais.iloc[0])

"""Nesse caso, acessar **materiais[0]** retorna o mesmo valor de **materiais.loc[0]**"""

print(materiais[0])
print("\n")
print(materiais.loc[0])

"""Portanto, para fugir dessa ambiguidade, é recomendado se acostumar com as funções **.iloc** e **.loc**.

Outra maneira de criar uma série:

Vamos supor que já existe uma lista com os índices e uma lista com os valores.
"""

lista_indice = ["Gabriela","Leonardo","Joao"]
print(lista_indice)
lista_valores = ["Amarelo","Roxo","Vermelho"]
print(lista_valores)

serie_2 = pd.Series(lista_valores, index = lista_indice)
print("\n")
print(serie_2)
print("-------"*3)
print(serie_dic) #obtemos o mesmo resultado passando parametros diferentes

"""#Índices da lista

A maneira mais otimizada para retornar os índices de uma série é chamando o método **.index**.
"""

lista_indice = serie_2.index
print(lista_indice)

print("\nTipo da variavel 'lista_indice':")
print(type(lista_indice))

"""Vale a pena lembrar que a função **.index** não retorna uma lista convencional mas é possível percorre-la com um laço de maneira semelhante."""

for i in lista_indice:
  print(i)

"""#Percorrendo uma série

É possível percorrer uma série usando um laço **for**:
"""

for i in serie_2: #somente os valores da serie
  print(i)

print("\n")

for k in serie_2.iteritems():
  aux = k
  print(k)

print(type(aux))

"""Exemplos de iteração:"""

serie_3 = pd.Series([0,1,2])
aux = 0

for i in serie_3:
  aux += i

print(aux)

#aux = 0 nao funciona
#for k in serie_2.iteritems():
#  aux += k

"""Sempre existirão métodos nativos de bibliotecas que otimizarão a iteração.

Uma alternativa para percorrer uma série e somar valor por valor é usar o método **.sum()** da biblioteca NumPy.
"""

#criando uma serie com 100000 numeros entre 0 e 100
serie_4 = pd.Series(np.random.randint(0,100,100000))
print(serie_4)
print("\n")

# Commented out IPython magic to ensure Python compatibility.
# %%timeit -n 100
# aux = 0
# for i in serie_4:
#   aux += i

# Commented out IPython magic to ensure Python compatibility.
# %%timeit -n 100
# np.sum(serie_4)

"""Comparando o laço com o método **.sum()**, é possível ver nitidamente a diferença no tempo de execução de um para outro.


Artigo sobre o uso de laços em Python: https://medium.com/python-pandemonium/never-write-for-loops-again-91a5a4c84baf

#Adicionando um novo elemento em uma série

Vamos supor que queremos adicionar mais uma pessoa e sua cor favorita em nossa tabela.

Basta usar a função **.loc["*novo_nome*"] = "*nova_cor*"**.
"""

print(serie_2)

serie_2.loc["Lucas"] = "Cinza"
print(serie_2)

"""Também podemos usar a função **.append()** para juntarmos uma nova série à outra:"""

serie_5 = pd.Series(["Marrom","Verde"], index = ["Florenza","Sergio"])
print(serie_5)
print("\n")
serie_2 = serie_2.append(serie_5)
print(serie_2)
