import random
import json
import sys

# Função para carregar palavras de um arquivo JSON
def carregar_palavras_do_json(arquivo):
    with open(arquivo, 'r', encoding='utf-8') as f:
        return json.load(f)

# Carregar a lista de palavras corretas do arquivo JSON
palavras_corretas = carregar_palavras_do_json('palavras.json')

# Funções para criar os erros com base nas regras
def gerar_substituicao(palavra):
    pos = random.randint(0, len(palavra) - 1)
    letra_errada = random.choice('abcdefghijklmnopqrstuvwxyz'.replace(palavra[pos], ''))
    return palavra[:pos] + letra_errada + palavra[pos+1:]

def gerar_omissao(palavra):
    if len(palavra) > 2:
        pos = random.randint(0, len(palavra) - 2)
        return palavra[:pos] + palavra[pos+1:]
    return palavra  # Não omitir palavras muito curtas

def gerar_acrescimo(palavra):
    pos = random.randint(1, len(palavra) - 1)
    letra_extra = random.choice('abcdefghijklmnopqrstuvwxyz')
    return palavra[:pos] + letra_extra + palavra[pos:]

# Função para gerar o dataset sem duplicatas
def gerar_dataset(tamanho):
    dataset = []
    exemplos_unicos = set()  # Usar um conjunto para armazenar tuplas únicas
    print("Gerando dataset...\n")
    
    for i in range(tamanho):
        palavra = random.choice(palavras_corretas)
        tipo_erro = random.choice(["Substituição", "Omissão", "Acréscimo"])
        
        if tipo_erro == "Substituição":
            erro = gerar_substituicao(palavra)
        elif tipo_erro == "Omissão":
            erro = gerar_omissao(palavra)
        else:
            erro = gerar_acrescimo(palavra)
        
        # Criar uma tupla para verificar duplicidade
        tupla_erro = (palavra, erro, tipo_erro)
        
        if tupla_erro not in exemplos_unicos:
            exemplos_unicos.add(tupla_erro)  # Adicionar tupla ao conjunto
            dataset.append({
                "correta": palavra,
                "erro": erro,
                "tipo_erro": tipo_erro
            })

            # Exibir o progresso a cada 100 iterações
            if (i + 1) % 100 == 0 or (i + 1) == tamanho:
                sys.stdout.write(f'\rProgresso: {i + 1}/{tamanho} exemplos gerados')
                sys.stdout.flush()  # Forçar a atualização da linha

    print("\n\nDataset gerado com sucesso!")
    return dataset

# Gerar dataset com 50 mil palavras sem duplicatas
dataset = gerar_dataset(50000)

# Salvar em arquivo JSON
with open('dislalia_dataset_sem_duplicatas.json', 'w') as f:
    json.dump(dataset, f, ensure_ascii=False, indent=4)

print("Arquivo 'dislalia_dataset_sem_duplicatas.json' salvo com sucesso!")