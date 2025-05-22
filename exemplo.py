from utils import carregar_dados, salvar_dados

CAMINHO = "cardapio.json"

def listar_cardapio():
    return carregar_dados(CAMINHO)

def adicionar_item(nome, descricao, preco):
    dados = carregar_dados(CAMINHO)
    dados.append({"nome": nome, "descricao": descricao, "preco": preco})
    salvar_dados(CAMINHO, dados)