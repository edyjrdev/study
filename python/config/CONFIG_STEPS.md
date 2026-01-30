# Comandos de Ambiente
conferir pythons da maquina
```
where.exe python 
python --version
```

``` 
pyenv install --list
pyenv install 3.11.5
pyenv install 3.13.11
pyenv versions
pyenv local 3.11.5
pyenv global 3.13.11
```

Global isola Python do Sistema.

Path do pyenv deve ser superior ao Path do Python do Sistema.

No Powershell criar Profile
```
notepad $PROFILE
$env:PYENV_ROOT = "$env:USERPROFILE\.pyenv\pyenv-win"
$env:Path = "$env:PYENV_ROOT\bin;$env:PYENV_ROOT\shims;$env:Path"
```
No windows configurar Path subindo variaveis de ambiente do pyenv acima do Python do Sistema.

Atualizar pip da versão do pyenv
 C:\Users\S836491661\.pyenv\pyenv-win\versions\3.11.5\python.exe -m pip install --upgrade pip

Instalar pipx
```
pip install pipx
```

Instalar poetry
```
pipx install poetry
```

Inicializar o poetry

```
poetry init
poetry config virtualenvs.in-project true
poetry env use python
```