# requests
# powershell cd .\python\projeto01\
# gitbash cd python/projeto01/
# poetry env activate
# poetry add requests
# pip list
# pip freeze > requirements.txt
# Forçar pyenv
# pyenv shell 3.11.5

import requests

print('Utilizando modulo requests de terceiros.')

url = 'https://www.google.com'
response = requests.get(url)
print(f'Requisição de {url} retornou {response.status_code}')

