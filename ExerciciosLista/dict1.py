# dic = {'nome': 'beto', 'banda': 'U2'}
# print(dic['nome'])
# # adiciona elemento no dic
# dic['album'] = 'Version 2.0'
# # apaga elemento do dic
# del dic ['album']
# print(dic)
# item = dic.items()
# chaves = dic.keys()
# print(chaves)
# print(item)
# valores = dic.values()
# print(valores)
progs = {'yes': ['Foxtrot', 'Sierra', 'key'], 'Gta6': ['Echo', 'Cobra'], 'key': 'ioa'}
progs['King Crimson'] = ['Red', 'Discipline']
print(progs.items())
if progs.has_key('Gta6'):
    del progs['Cobra']

