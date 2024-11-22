import os
from time import sleep
import banco


def main():
    banco.create_table()

    while True:
        print('''
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
        print("5. Buscar produto")
        print("0. Sair")

        escolha = input("Escolha uma opção: ")

        match escolha:
            case '1':
                nome = input("Nome: ")
                quantidade = input("Quantidade: ")
                valor = input("Valor: ")
                print("Produto adicionado", banco.insert(
                    nome, quantidade, valor))
            case '2':
                nome = input("Nome ou id: ")
                banco.delete(nome)
                print("Produto removido")
            case '3':
                nome = input("Nome: ")
                quantidade = input("Quantidade: ")
                valor = input("Valor: ")
                id = input("Id: ")
                banco.update(nome, quantidade, valor, id)
                print("Produto atualizado com sucesso!", banco.select(id))
            case '4':
                produtos = banco.select_all()
                if produtos:
                    print("Produtos:\n")
                    print(f"{"ID".ljust(36)} | {"Nome".ljust(25)} | {
                        "Quantidade".ljust(25)} | Valor")
                    for produto in produtos:
                        print(f"{produto[0]} | {produto[1].ljust(25)} | {
                            produto[2].ljust(25)} | R$ {produto[3]}")
                        
            case '5':
                nome = input("Nome ou id: ")
                produtos = banco.select(nome)
                if produtos:
                    print("Produto encontrado:")
                    print(f"{"ID".ljust(36)} | {"Nome".ljust(25)} | {"Quantidade".ljust(25)} | Valor")
                    for produto in produtos:
                         print(f"{produto[0]} | {produto[1].ljust(25)} | {produto[2].ljust(25)} | R$ {produto[3]}")
                else:
                    print("Produto não encontrado.")

            case '0':
                break
            case _:
                print("Opção inválida. Tente novamente.")

        input("Pressione Enter para continuar...")
        os.system('cls')
        sleep(1)


if __name__ == "__main__":
    main()
