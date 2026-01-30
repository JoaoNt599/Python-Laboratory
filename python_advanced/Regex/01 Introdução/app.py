import re 

string = 'Este é um teste de um teste inicial.'

print(re.search(r'teste', string)) # busca ocorrencia 
print(re.findall(r'teste', string)) # busca quantas ocorrencias existem 
print(re.sub(r'teste', 'ABC', string)) # substitui a palavra por outra
print(re.sub(r'teste', 'ABC', string, count=1)) # substitui a primeira ocorrencia

# compile
regexp = re.compile(r'teste')
print (regexp.search(string))
print (regexp.findall(string))
print (regexp.sub('DEF', string))