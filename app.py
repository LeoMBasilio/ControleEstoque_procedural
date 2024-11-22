import os
from time import sleep
import banco

def main():
    banco.create_table()

    while True:
        print( '''
        ################################################################
        # ███████╗███████╗████████╗ ██████╗  ██████╗ ██╗   ██╗███████╗ #
        # ██╔════╝██╔════╝╚══██╔══╝██╔═══██╗██╔═══██╗██║   ██║██╔════╝ #
        # █████╗  ███████╗   ██║   ██║   ██║██║   ██║██║   ██║█████╗   #
        # ██╔══╝  ╚════██║   ██║   ██║   ██║██║▄▄ ██║██║   ██║██╔══╝   #
        # ███████╗███████║   ██║   ╚██████╔╝╚██████╔╝╚██████╔╝███████╗ #
        # ╚══════╝╚══════╝   ╚═╝    ╚═════╝  ╚══▀▀═╝  ╚═════╝ ╚══════╝ #
        ################################################################ ''')                                                   
        print("Menu:")
        print("1. Adicionar produto")
        print("2. Remover produto")
        print("3. Atualizar produto")
        print("4. Listar produtos")
        print("5. Sair")
        
        escolha = input("Escolha uma opção: ")
        
        if escolha == '1':
            nome = input("Nome: ")
            quantidade = input("Quantidade: ")
            valor = input("Valor: ")
            print("Produto adicionado",banco.insert(nome, quantidade, valor))
        elif escolha == '2':
            nome = input("Nome ou id: ")
            banco.delete(nome)
            print("Produto removido")
        elif escolha == '3':
            nome = input("Nome: ")
            quantidade = input("Quantidade: ")
            valor = input("Valor: ")
            id = input("Id: ")
            banco.update(nome, quantidade, valor, id)
            print("Produto atualizado com sucesso!", banco.select(id))
        elif escolha == '4':
            if banco.select_all():
                print("Produtos:\n")
                print(f"{"ID".ljust(36)} | {"Nome".ljust(25)} | {"Quantidade".ljust(25)} | Valor")
                for produto in banco.select_all():
                    print(f"{produto[0]} | {produto[1].ljust(25)} | {produto[2].ljust(25)} | R$ {produto[3]}")
        elif escolha == '5':
            break
        else:
            print("Opção inválida. Tente novamente.")
        
        input("Pressione Enter para continuar...")
        os.system('cls')
        sleep(3)

if __name__ == "__main__":
    main()