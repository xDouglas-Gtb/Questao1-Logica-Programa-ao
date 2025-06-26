print("---Seja bem-vindo,Douglas Guimarães---")

funcionarios_lista = []  # guarda os funcionarios
global_id = 21246       # garante que cada funcionario tenha um id único


def funcionarios_cadastro(id):   # Função para cadastrar funcionário
    nome = input("Escreva o nome de usuário: ")
    setor = input("Digite o setor: ")
    salario = float(input("Informe o salário: "))
    funcionario = {"id": id,"nome": nome ,"setor": setor ,"salario R$": salario}
    funcionarios_lista.append(funcionario)
    print("Funcionário cadastrado com sucesso !!!")

def consultar_funcionarios():  # Função de consulta
    while True:
        opcao = input("\n1 - Geral | 2 -Pelo ID | 3 - Por Setor | 4 - Voltar: ")
        if opcao == "1":
            for f in funcionarios_lista:
                print(f)
        elif opcao == "2":
            id_buscado = int(input("Digite o ID: "))
            encontrado = False
            for f in funcionarios_lista:
                if f["id"] == id_buscado:
                    print(f)
                    encontrado = True
                    break
            if not encontrado:
                print("Funcionário não encontrado.")
        elif opcao == "3":
            setor_encontrado = input("Digite o setor: ")
            encontrado = False
            for f in funcionarios_lista:
                if f["setor"].lower() == setor_encontrado.lower():
                    print(f)
                    encontrado = True
            if not encontrado:
                print("Nenhum funcionário encontrado neste setor.")
        elif opcao == "4":
            break
        else:
            print("Opção incorreta...")
def remover_funcionario():  # Função para remover funcionário
    while True:
        id_remover = int(input("ID para remover: "))
        for f in funcionarios_lista:
            if f["id"] == id_remover:
                funcionarios_lista.remove(f)
                print("Removido com sucesso!")
                return
        print("ID inválido. Tente novamente.")
# Menu principal
while True:
    print("\n--- MENU PRINCIPAL ---")
    opcao = input("1 -Fazer Cadastro para funcionário | 2 -  Consultar | 3 - Remover | 4 - Sair: ")
    if opcao == "1":
        funcionarios_cadastro(global_id)
        global_id += 1
    elif opcao == "2":
        consultar_funcionarios()
    elif opcao == "3":
        remover_funcionario()
    elif opcao == "4":
        print("Encerrando...")
        break
    else:
        print("Opção inválida.")
