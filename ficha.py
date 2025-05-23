def carregar_fichas():
    return []

def salvar_fichas(fichas):
    pass

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
    print("Função de editar fichas")

def excluir_fichas(fichas):
    nome = input("Digite o nome da ficha que deseja excluir: ").strip().lower()
    
    for ficha in fichas:
        if ficha['nome'].lower() == nome:
            print(f"\nFicha encontrada: {ficha['nome']}")
            if input("Tem certeza que deseja excluir? (s/n): ").lower() == 's':
                fichas.remove(ficha)
                print("Ficha excluída com sucesso.")
            return
    
    print("Ficha não encontrada.")