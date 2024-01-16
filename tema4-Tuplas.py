'''
Las tuplas son inmutables
'''

tupla=("uno", "dos", "tres")
print(tupla)
tuplasVariosDatos=(12,True,23.5, "el gato", 12+4j)
print(tuplasVariosDatos)

tuplasconTuplas=(1,2,3,4,(1,2,3))
print(tuplasconTuplas)

print(tuplasVariosDatos[3])
print(tuplasVariosDatos[-2])
print(tuplasconTuplas[0:2])

a,b,c=tupla
print(a)
print(b)
print(c)

tuplaNueva=tupla+tuplasVariosDatos

print(tuplaNueva)