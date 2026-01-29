# string - '' ou "" ou """ """

nome_completo = 'Edy Epumuceno Rodrigues Junior'

nome_completo_quebra = 'Edy Epumuceno' \
    'Rodrigues Junior'
print(nome_completo)

emoji_heart = '❤️'
print(emoji_heart)
# paragrafo com quebra de linha

paragrafo = """Ouviram do Ipiranga,
as margens plácidas
de um povo heróico, bravo, retumbante"""

print(paragrafo)

# formatacao de string
print('Nome completo (1a forma):', nome_completo)
print('Nome completo (2a forma):' + nome_completo) # concatenacao
# fstring
print(f'Nome completo (3a forma): {nome_completo}') 
print('Nome completo (4a forma):' + nome_completo_quebra) 

# metodos de string
print(nome_completo.upper())
print(nome_completo.lower())
print(nome_completo.title())
print('tamanho', len(nome_completo))

nome_sujo = '    Edy E Rodrigues Junior         '
print(nome_sujo)
print(nome_sujo.strip())

print('quantos e =', nome_completo.lower().count('e'))
print('J em', nome_completo.find('J'))
print(nome_completo[24])

# encode e decode
print(nome_completo.encode()) # byte por padrão
print(nome_completo.encode('utf-8'))
print(nome_completo.encode().decode('utf-8')) # byte -> string

# replace
print(nome_completo.replace('E','&'))

telefone = '(61) 98252-0611'
telefone_limpo = telefone.replace('(','').replace(')','').replace(' ','').replace('-','')
print(telefone, telefone_limpo)  

# join
print('-'.join(nome_completo))
print(''.join(nome_completo))

# split
print(nome_completo.split())

# strip
nome_hifen = '-----Edy Junior-----'
print(nome_hifen, nome_hifen.strip('-'))

# indexacao
print(nome_completo[0])
print(nome_completo[0:3])

# verificacaoes
print(nome_completo.startswith('Ed'))
print(nome_completo.endswith('Jr'))
print('mu'in nome_completo)
print('@' not in nome_completo)