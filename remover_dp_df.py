import json

# Carregar o arquivo JSON
with open('dislalia_dataset.json', 'r') as f:
    dataset = json.load(f)

# Usar um conjunto para armazenar tuplas únicas
tuplas_unicas = set()
dataset_sem_duplicatas = []

# Verificar e remover duplicidade
for item in dataset:
    tupla = (item['correta'], item['erro'], item['tipo_erro'])
    if tupla not in tuplas_unicas:
        tuplas_unicas.add(tupla)
        dataset_sem_duplicatas.append(item)  # Adicionar apenas itens únicos

# Salvar o dataset sem duplicatas de volta em um novo arquivo JSON
with open('dislalia_dataset_sem_duplicatas.json', 'w') as f:
    json.dump(dataset_sem_duplicatas, f, ensure_ascii=False, indent=4)

print(f"Dataset original: {len(dataset)} entradas.")
print(f"Dataset sem duplicatas: {len(dataset_sem_duplicatas)} entradas.")
print("As duplicatas foram removidas e o arquivo foi salvo como 'dislalia_dataset_sem_duplicatas.json'.")
