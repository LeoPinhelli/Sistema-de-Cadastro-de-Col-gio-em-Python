import json

# Definição dos menus
def menu1():
    print("--- MENU PRINCIPAL ---")
    print("1-Estudantes")
    print("2-Disciplinas")
    print("3-Professores")
    print("4-Turmas")
    print("5-Matrículas")
    print("6-Sair")

def menu2(opcao):
    print(f"--- MENU DE OPERAÇÕES PARA {opcoes[opcao]} ---")
    print("1-Incluir.")
    print("2-Listar.")
    print("3-Atualizar.")
    print("4-Excluir.")
    print("5-Voltar ao menu principal.")

def inserir():
    global codigo
    try:
        # Tentar abrir o arquivo existente
        with open("listas.json", "r") as arquivo:
            data = json.load(arquivo)
            estudantes = data.get('estudantes', [])
            disciplinas = data.get('disciplinas', [])
            professores = data.get('professores', [])
            turmas = data.get('turmas', [])
            matriculas = data.get('matriculas', [])
    except FileNotFoundError:
        # Se o arquivo não existir, criar um novo arquivo vazio
        estudantes = []
        disciplinas = []
        professores = []
        turmas = []
        matriculas = []

    if opcao == 1:
        print("---INCLUSÃO DE ESTUDANTE---")
        nome = input("Digite o nome: ")
        cpf = input("Digite o CPF: ")
        # Verifica se o CPF já existe
        while True:
            if any(estudante['cpf'] == cpf for estudante in estudantes):
                print("CPF já existe. Por favor, insira um CPF diferente.")
                cpf = input("Digite o CPF: ")
            else:
                break
        estudante = {"codigo": codigo, "nome": nome, "cpf": cpf}
        estudantes.append(estudante)
    elif opcao == 2:
        print("---INCLUSÃO DE DISCIPLINA---")
        nome = input("Digite o nome da disciplina: ")
        # Verifica se o nome da disciplina já existe
        while True:
            if any(disciplina['nome'] == nome for disciplina in disciplinas):
                print("Disciplina já existe. Por favor, insira um nome de disciplina diferente.")
                nome = input("Digite o nome da disciplina: ")
            else:
                break
        disciplina = {"codigo": codigo, "nome": nome}
        disciplinas.append(disciplina)
    elif opcao == 3:
        print("---INCLUSÃO DE PROFESSOR---")
        nome = input("Digite o nome: ")
        cpf = input("Digite o CPF: ")
        # Verifica se o CPF já existe
        while True:
            if any(professor['cpf'] == cpf for professor in professores):
                print("CPF já existe. Por favor, insira um CPF diferente.")
                cpf = input("Digite o CPF: ")
            else:
                break
        professor = {"codigo": codigo, "nome": nome, "cpf": cpf}
        professores.append(professor)
    elif opcao == 4:
        print("---INCLUSÃO DE TURMA---")
        codigo_prof = int(input("Digite o código do professor: "))
        codigo_disc = int(input("Digite o código da disciplina: "))
        # Verifica se os códigos de professor e disciplina existem
        if any(professor['codigo'] == codigo_prof for professor in professores) and any(disciplina['codigo'] == codigo_disc for disciplina in disciplinas):
            turma = {"codigo": codigo, "codigo_prof": codigo_prof, "codigo_disc": codigo_disc}
            turmas.append(turma)
        else:
            print("Professor ou disciplina não encontrados.")
    elif opcao == 5:
        print("---INCLUSÃO DE MATRÍCULA---")
        codigo_estudante = int(input("Digite o código do estudante: "))
        codigo_turma = int(input("Digite o código da turma: "))
        # Verifica se os códigos de estudante e turma existem
        if any(estudante['codigo'] == codigo_estudante for estudante in estudantes) and any(turma['codigo'] == codigo_turma for turma in turmas):
            matricula = {"codigo_estudante": codigo_estudante, "codigo_turma": codigo_turma}
            matriculas.append(matricula)
            codigo += 1
        else:
            print("Estudante ou turma não encontrados.")

    # Atualiza os dados no arquivo JSON
    data = {
        'estudantes': estudantes,
        'disciplinas': disciplinas,
        'professores': professores,
        'turmas': turmas,
        'matriculas': matriculas
    }

    with open("listas.json", "w") as arquivo:
        json.dump(data, arquivo)

    input("Aperte ENTER para continuar")



def listar():
    print("---LISTAGEM---")
    try:
        with open("listas.json", "r") as arquivo:
            data = json.load(arquivo)
            estudantes = data['estudantes']
            disciplinas = data['disciplinas']
            professores = data['professores']
            turmas = data['turmas']
            matriculas = data['matriculas']

        if opcao == 1:
            print("Estudantes:")
            for estudante in estudantes:
                print(estudante)
        elif opcao == 2:
            print("Disciplinas:")
            for disciplina in disciplinas:
                print(disciplina)
        elif opcao == 3:
            print("Professores:")
            for professor in professores:
                print(professor)
        elif opcao == 4:
            print("Turmas:")
            for turma in turmas:
                print(turma)
        elif opcao == 5:
            print("Matrículas:")
            for matricula in matriculas:
                print(matricula)

    except Exception as e:
        print("Erro ao listar:", e)

    input("Aperte ENTER para continuar")

def atualizacao():
    try:
        with open("listas.json", "r") as arquivo:
            data = json.load(arquivo)
            estudantes = data['estudantes']
            disciplinas = data['disciplinas']
            professores = data['professores']
            turmas = data['turmas']
            matriculas = data['matriculas']

        print("---ATUALIZAÇÃO---")
        codigo_atualizacao = int(input("Digite o código do item que deseja atualizar: "))
        encontrado = False

        if opcao == 1:
            lista = estudantes
        elif opcao == 2:
            lista = disciplinas
        elif opcao == 3:
            lista = professores
        elif opcao == 4:
            lista = turmas
        elif opcao == 5:
            lista = matriculas

        for item in lista:
            if item['codigo'] == codigo_atualizacao:
                if opcao == 1:
                    novo_nome = input("Digite o novo nome: ")
                    novo_cpf = input("Digite o novo CPF: ")
                    # Verifica se o novo CPF já existe
                    while True:
                        if any(estudante['cpf'] == novo_cpf for estudante in estudantes if estudante['codigo'] != codigo_atualizacao):
                            print("CPF já existe. Por favor, insira um CPF diferente.")
                            novo_cpf = input("Digite o novo CPF: ")
                        else:
                            break
                    item['nome'] = novo_nome
                    item['cpf'] = novo_cpf
                elif opcao == 2:
                    novo_nome = input("Digite o novo nome: ")
                    # Verifica se o novo nome já existe
                    while True:
                        if any(disciplina['nome'] == novo_nome for disciplina in disciplinas if disciplina['codigo'] != codigo_atualizacao):
                            print("Disciplina já existe. Por favor, insira um nome de disciplina diferente.")
                            novo_nome = input("Digite o novo nome: ")
                        else:
                            break
                    item['nome'] = novo_nome
                elif opcao == 3:
                    novo_nome = input("Digite o novo nome: ")
                    novo_cpf = input("Digite o novo CPF: ")
                    # Verifica se o novo CPF já existe
                    while True:
                        if any(professor['cpf'] == novo_cpf for professor in professores if professor['codigo'] != codigo_atualizacao):
                            print("CPF já existe. Por favor, insira um CPF diferente.")
                            novo_cpf = input("Digite o novo CPF: ")
                        else:
                            break
                    item['nome'] = novo_nome
                    item['cpf'] = novo_cpf
                elif opcao == 4:
                    novo_codigo_prof = int(input("Digite o novo código do professor: "))
                    novo_codigo_disc = int(input("Digite o novo código da disciplina: "))
                    # Verifica se os novos códigos de professor e disciplina existem
                    if any(professor['codigo'] == novo_codigo_prof for professor in professores) and any(disciplina['codigo'] == novo_codigo_disc for disciplina in disciplinas):
                        item['codigo_prof'] = novo_codigo_prof
                        item['codigo_disc'] = novo_codigo_disc
                    else:
                        print("Professor ou disciplina não encontrados.")
                elif opcao == 5:
                    novo_codigo_estudante = int(input("Digite o novo código do estudante: "))
                    novo_codigo_turma = int(input("Digite o novo código da turma: "))
                    # Verifica se os novos códigos de estudante e turma existem
                    if any(estudante['codigo'] == novo_codigo_estudante for estudante in estudantes) and any(turma['codigo'] == novo_codigo_turma for turma in turmas):
                        item['codigo_estudante'] = novo_codigo_estudante
                        item['codigo_turma'] = novo_codigo_turma
                    else:
                        print("Estudante ou turma não encontrados.")

                encontrado = True
                print("Dados atualizados com sucesso!")
                break

        if encontrado:
            with open("listas.json", "w") as arquivo:
                json.dump(data, arquivo)
        else:
            print("Item não encontrado.")
        input("Aperte ENTER para continuar")
    except Exception as e:
        print("Erro ao atualizar:", e)

def excluir():
    try:
        with open("listas.json", "r") as arquivo:
            data = json.load(arquivo)
            estudantes = data['estudantes']
            disciplinas = data['disciplinas']
            professores = data['professores']
            turmas = data['turmas']
            matriculas = data['matriculas']

        print("---EXCLUSÃO---")
        codigo_exclusao = int(input("Digite o código do item que deseja excluir: "))
        encontrado = False

        if opcao == 1:
            lista = estudantes
        elif opcao == 2:
            lista = disciplinas
        elif opcao == 3:
            lista = professores
        elif opcao == 4:
            lista = turmas
        elif opcao == 5:
            lista = matriculas

        for item in lista:
            if item['codigo'] == codigo_exclusao:
                confirmacao = input(f"Tem certeza de que deseja excluir o item {item}? (S/N): ")
                if confirmacao.lower() == 's':
                    lista.remove(item)
                    encontrado = True
                    print("Item excluído com sucesso!")
                else:
                    print("Exclusão cancelada.")
                break

        if encontrado:
            with open("listas.json", "w") as arquivo:
                json.dump(data, arquivo)
        else:
            print("Item não encontrado.")
        input("Aperte ENTER para continuar")
    except Exception as e:
        print("Erro ao excluir:", e)

def recuperar_arquivo(arquivo):
    try:
        if arquivo == 1:
            with open("listas.json", "r" , enconding="utf-8" ) as arquivo:
                dados = json.load(arquivo)
        elif arquivo == 2:
            with open("listas.json", "r" , enconding="utf-8" ) as arquivo:
                dados = json.load(arquivo)
        elif arquivo == 4:
            with open("listas.json", "r" , enconding="utf-8" ) as arquivo:
                dados = json.load(arquivo)
        elif arquivo == 4:
            with open("listas.json", "r" , enconding="utf-8" ) as arquivo:
                dados = json.load(arquivo)
        elif arquivo == 5:
            with open("listas.json", "r" , enconding="utf-8" ) as arquivo:
                dados = json.load(arquivo)
        return dados
        
    except:
        dados = []
        return dados
    
# Dicionário para mapear opções numéricas para nomes
opcoes = {1: "ESTUDANTES", 2: "DISCIPLINAS", 3: "PROFESSORES", 4: "TURMAS", 5: "MATRICULAS"}
dados = recuperar_arquivo(1,2,3,4,5)
codigo = 1  # Inicializa o contador de códigos

# Loop principal do programa
while True:
    # Exibe o menu principal
    menu1()

    try:
        # Solicita ao usuário uma opção do menu principal
        opcao = int(input("Digite uma opção: "))

        # Valida a opção selecionada
        if opcao < 1 or opcao > 6:
            print("Opção Inválida")

        elif opcao == 6:
            # Opção para sair do programa
            print("Até mais")
            break

        elif opcao in [1, 2, 3, 4, 5]:
            # Menu de operações para a opção selecionada
            
            while True:
                # Exibe o menu de operações para a opção selecionada
                menu2(opcao)

                try:
                    # Solicita ao usuário uma opção do menu de operações
                    opcao2 = int(input("Digite uma opção: "))

                    # Valida a opção selecionada
                    if opcao2 < 1 or opcao2 > 5:
                        print("Opção Inválida")

                    elif opcao2 == 5:
                        # Opção para voltar ao menu principal
                        break

                    elif opcao2 == 1:
                        # Função de inserir item
                        inserir()

                    elif opcao2 == 2:
                        # Função de listar itens
                        listar()

                    elif opcao2 == 3:
                        # Funcionalidade de atualizar
                        atualizacao()

                    elif opcao2 == 4:
                        # Funcionalidade de exclusão
                        excluir()

                except Exception as e:
                    print("Opção Inválida:", e)

    except Exception as e:
        print("Opção Inválida:", e)
