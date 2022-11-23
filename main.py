# Importa nosso arquivo Pessoa.py no diretório model
from model.Pessoa import Pessoa

# Exemplo de uso
lafuente = Pessoa(1, "Felipe Luiz Lafuente")
print(lafuente)

# Quero mostrar só o nome
print(lafuente.nome)