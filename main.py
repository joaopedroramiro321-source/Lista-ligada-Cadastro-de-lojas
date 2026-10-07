from classes import ListaLigada


class Loja:

    def __init__(self, nome, endereco):
        self.nome = nome
        self.endereco = endereco

    def __repr__(self):
        return f"Loja: {self.nome} | Endereço: {self.endereco}"


def criar_loja_usuario():
    print("\n--- Cadastro de Nova Loja ---")
    nome = input("Digite o nome da loja: ").strip()
    endereco = input("Digite o endereço da loja: ").strip()
    return Loja(nome, endereco)


def exibir_menu():
    print("\n====================================")
    print("      GERENCIADOR DE LOJAS          ")
    print("====================================")
    print("1 - Inserir no início")
    print("2 - Inserir no fim")
    print("3 - Inserir em posição específica")
    print("4 - Listar todas as lojas")
    print("5 - Consultar item por posição")
    print("6 - Pesquisar loja por nome")
    print("7 - Remover do início")
    print("8 - Remover de posição específica")
    print("9 - Limpar toda a lista")
    print("0 - Sair")
    print("====================================")


def main():
    lista = ListaLigada()

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip()

        try:
            if opcao == "1":
                loja = criar_loja_usuario()
                lista.inserir_no_inicio(loja)
                print("Loja inserida no início com sucesso!")

            elif opcao == "2":
                loja = criar_loja_usuario()
                lista.inserir_no_fim(loja)
                print("Loja inserida no fim com sucesso!")

            elif opcao == "3":
                posicao = int(input(f"Digite a posição (0 até {lista.quantidade}): "))
                loja = criar_loja_usuario()
                lista.inserir(posicao, loja)
                print(f"Loja inserida na posição {posicao} com sucesso!")

            elif opcao == "4":
                print(f"\nTotal de elementos: {lista.quantidade}")
                lista.imprimir()

            elif opcao == "5":
                posicao = int(input("Digite a posição que deseja consultar: "))
                loja = lista.item(posicao)
                print(f"\nItem na posição {posicao}:\n{loja}")

            elif opcao == "6":
                termo = input("Digite o nome ou parte do nome da loja: ").strip()
                posicao, loja = lista.pesquisar(termo)
                if posicao != -1:
                    print(f"\nLoja encontrada na posição [{posicao}]:\n{loja}")
                else:
                    print("\nNenhuma loja encontrada com esse nome.")

            elif opcao == "7":
                removido = lista.remover_do_inicio()
                print(f"\nLoja removida do início:\n{removido}")

            elif opcao == "8":
                posicao = int(input("Digite a posição da loja a ser removida: "))
                removido = lista.remover(posicao)
                print(f"\nLoja removida da posição [{posicao}]:\n{removido}")

            elif opcao == "9":
                confirmacao = input("Tem certeza que deseja apagar toda a lista? (s/n): ").strip().lower()
                if confirmacao == 's':
                    lista.limpar()
                    print("\nLista limpa com sucesso!")

            elif opcao == "0":
                print("\nEncerrando o programa... Até logo!")
                break

            else:
                print("\nOpção inválida! Tente novamente.")

        except ValueError:
            print("\n[Erro] Digite apenas números inteiros válidos para opções/posições.")
        except IndexError as e:
            print(f"\n[Erro de Índice] {e}")
        except Exception as e:
            print(f"\n[Erro Inesperado] {e}")


if __name__ == "__main__":
    main()