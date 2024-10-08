import json

# Lista de palavras usuais (exemplo inicial, pode adicionar mais)
palavras_base = [
    "abacate", "abacaxi", "abelha", "aberto", "abismo", "abobora", "abraço", 
    "abre", "abrigado", "absoluto", "absorver", "abundância", "acabamento", 
    "academia", "acelerar", "acender", "acento", "aceptar", "acesso", "acidez",
    "afastado", "afeto", "afinidade", "aflição", "água", "aguardar", "agudo", 
    "alavanca", "alegria", "algodão", "alimentação", "alma", "amarelo", 
    "ambiente", "amizade", "amplo", "analisar", "andar", "anel", "anexo", 
    "aniversário", "antigo", "anular", "apagado", "aparelho", "apetite", 
    "apontar", "aprender", "aproximado", "árvore", "asfalto", "asilo", 
    "aspirar", "astronauta", "atitude", "ato", "atraente", "através", "atual", 
    "aumento", "aura", "auxiliar", "avançar", "avenida", "aventura", "avisar", 
    "axioma", "azar", "azeite", "azul", "bacia", "bailarino", "balanço", 
    "bandeira", "barato", "barco", "barriga", "base", "batata", "beber", 
    "beijo", "beliscar", "beleza", "bendito", "bento", "bicho", "bicicleta",
    "bilhete", "bloco", "bolo", "bolsa", "bomba", "borboleta", "bordado", 
    "branco", "bravo", "breve", "brilho", "brinquedo", "broto", "bruto", 
    "bucha", "buscar", "cabide", "cabra", "cabeça", "cabelo", "cabide", 
    "cabo", "cabresto", "cacau", "cadeado", "cadeira", "caixa", "cajado", 
    "calçada", "calcular", "calor", "cama", "camisa", "campo", "canção", 
    "cansaço", "cantar", "capacidade", "capaz", "caracol", "caramelo", 
    "caravana", "carbono", "cardápio", "caridade", "carnaval", "caro", 
    "carregar", "carro", "carta", "casar", "cascata", "castelo", "catálogo", 
    "causa", "cebola", "cedo", "célebre", "cenário", "censura", "centro", 
    "cercado", "certa", "cerveja", "chão", "chapéu", "charme", "cheio", 
    "cheiro", "chiclete", "chifre", "chocolate", "choque", "chuva", "círculo",
    "citadino", "civilização", "clareza", "clássico", "claro", "cliente", 
    "clima", "coado", "cobertor", "cobra", "cobre", "cobrir", "coelho", 
    "coerente", "cofre", "cogumelo", "colher", "colina", "colocar", "colorir",
    "combater", "comer", "cometa", "comida", "comida", "compaixão", 
    "compasso", "comportamento", "comprar", "computador", "comum", "conceito", 
    "conclusão", "conduzir", "conectar", "confiança", "conflito", "conforto", 
    "conhecer", "conquista", "conseguir", "consistência", "consultar", 
    "consumir", "conta", "contar", "contento", "contornar", "contratar", 
    "controle", "convencer", "conversar", "convidado", "coragem", "corda", 
    "corpo", "corrente", "cortar", "costura", "crânio", "cravo", "crédito", 
    "crescimento", "criação", "criança", "crítica", "cruz", "cruzeiro", 
    "cuidadoso", "culminar", "cultura", "cúpula", "curioso", "curto", "custo"
    # Adicione mais palavras à lista
]

# Multiplicar palavras ou gerar combinações para criar 100 mil palavras
palavras_100mil = []

for i in range(5000):  # Supondo que tenha 20 palavras base, multiplicando até ter 100 mil
    for palavra in palavras_base:
        nova_palavra = f"{palavra}{i}"  # Variando as palavras, você pode melhorar isso
        palavras_100mil.append(nova_palavra)

# Garantir que temos 100 mil palavras
palavras_100mil = palavras_100mil[:100000]  # Cortar a lista para ter 100 mil palavras exatas

# Salvar a lista em um arquivo JSON
with open('palavras_100mil.json', 'w') as f:
    json.dump(palavras_100mil, f, ensure_ascii=False, indent=4)

print("Arquivo com 100 mil palavras salvo como 'palavras_100mil.json'")
