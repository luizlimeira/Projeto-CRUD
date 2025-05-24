import json
import os

ARQUIVO_FICHAS = 'ficha.json'

def carregar_fichas():
    if not os.path.exists(ARQUIVO_FICHAS):
        with open(ARQUIVO_FICHAS, 'w') as f:
            json.dump([], f)
        return []
    
    with open(ARQUIVO_FICHAS, 'r') as f:
        return json.load(f)

def salvar_fichas(fichas):
    with open(ARQUIVO_FICHAS, 'w') as f:
        json.dump(fichas, f, indent=4)

def adicionar_ficha(fichas):
    nova_ficha = {
        'categoria': input("Categoria: ").upper(),
        'nome': input("Nome: ").capitalize(),
        'ingredientes': [],
        'preparo': []
    }
    
    print("\nINGREDIENTES:")
    while True:
        ingred = input("Ingrediente (deixe em branco para parar): ").capitalize()
        if not ingred:
            break
        quant = input("Quantidade: ")
        nova_ficha['ingredientes'].append({'ingrediente': ingred, 'quantidade': quant})
    
    print("\nMODO DE PREPARO:")
    passo_num = 1
    while True:
        descricao = input(f"Passo {passo_num} (deixe em branco para parar): ").capitalize()
        if not descricao:
            break
        nova_ficha['preparo'].append({'passo': passo_num, 'descricao': descricao})
        passo_num += 1
    
    fichas.append(nova_ficha)
    print("\nFicha adicionada com sucesso!")
    salvar_fichas(fichas)
    return fichas

def visualizar_fichas(fichas):
    if not fichas:
        print("\nNenhuma ficha cadastrada ainda!")
        return
    
    for ficha in fichas:
        print("\n" + "=" * 40)
        print(f"Nome: {ficha['nome']}")
        print(f"Categoria: {ficha['categoria']}")
        
        print("\nIngredientes:")
        for ingred in ficha['ingredientes']:
            print(f"- {ingred['quantidade']} de {ingred['ingrediente']}")
        
        print("\nModo de Preparo:")
        for passo in ficha['preparo']:
            print(f"{passo['passo']}. {passo['descricao']}")

def editar_fichas(fichas):
    nome = input("Digite o nome da ficha que deseja editar: ").strip().lower()
    
    for ficha in fichas:
        if ficha['nome'].lower() == nome:
            print(f"\nEditando ficha: {ficha['nome']}")
            ficha['nome'] = input("Novo nome: ").capitalize()
            ficha['categoria'] = input("Nova categoria: ").upper()
            print("Ficha editada com sucesso!")
            salvar_fichas(fichas)
            return
    
    print("Ficha não encontrada.")

def excluir_fichas(fichas):
    nome = input("Digite o nome da ficha que deseja excluir: ").strip().lower()
    
    for ficha in fichas:
        if ficha['nome'].lower() == nome:
            print(f"\nFicha encontrada: {ficha['nome']}")
            if input("Tem certeza que deseja excluir? (s/n): ").lower() == 's':
                fichas.remove(ficha)
                print("Ficha excluída com sucesso.")
            salvar_fichas(fichas)
            return
    
    print("Ficha não encontrada.")

def menu_fichas():
    while True:
        fichas = carregar_fichas()
        
        print("\n--- MENU FICHAS ---")
        print("1. Adicionar Ficha")
        print("2. Visualizar Fichas")
        print("3. Editar Ficha")
        print("4. Excluir Ficha")
        print("0. Voltar")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            fichas = adicionar_ficha(fichas)
        elif opcao == "2":
            visualizar_fichas(fichas)
        elif opcao == "3":
            editar_fichas(fichas)
        elif opcao == "4":
            excluir_fichas(fichas)
        elif opcao == "0":
            return
        else:
            print("\nOpção inválida!")

if _name_ == "_ficha_":
    menu_fichas()