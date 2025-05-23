import json
import os


ARQUIVO_CARDAPIO = os.path.join(os.path.dirname(__file__), 'cardapio.json')


def carregar_cardapio():
    if not os.path.exists(ARQUIVO_CARDAPIO):
        with open(ARQUIVO_CARDAPIO, 'r', encoding='utf-8') as f:
            json.dump([], f, indent=4)
    with open(ARQUIVO_CARDAPIO, 'r' , encoding='utf-8') as f:
        return json.load(f)
    
def salvar_cardapio(cardapio):
    with open(ARQUIVO_CARDAPIO, 'w', encoding='utf-8') as f:
        json.dump(cardapio, f, indent=4, ensure_ascii=False)