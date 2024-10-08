import json

# Carregar o arquivo JSON
with open('dislalia_dataset.json', 'r') as f:
    dataset = json.load(f)

# Usar um conjunto para armazenar tuplas únicas
tuplas_unicas = set()
duplicatas = set()

# Verificar duplicidade
for item in dataset:
    tupla = (item['correta'], item['erro'], item['tipo_erro'])
    if tupla in tuplas_unicas:
        duplicatas.add(tupla)
    else:
        tuplas_unicas.add(tupla)

# Exibir duplicatas, se houver
if duplicatas:
    print(f"Encontrado {len(duplicatas)} entradas duplicadas:")
    for dup in duplicatas:
        print(dup)
else:
    print("Nenhuma duplicata encontrada!")
