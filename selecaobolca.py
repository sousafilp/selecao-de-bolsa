#  programa seleção de bolsa

import os
import PyPDF2

banco_matriculas = []
banco_matriculas_professores = []
banco_nomes = []
banco_nomes_professores = []
banco_notas_alunos = []
banco_status_aluno = []
menu = 1


#  Funções

def cadastrar_professor(nome, matricula):
    banco_nomes_professores.append(nome)
    banco_matriculas_professores.append(matricula)


def cadastrar_aluno(nome, matricula, nota, status='Aguardando'):
    banco_nomes.append(nome)
    banco_matriculas.append(matricula)
    banco_notas_alunos.append(nota)
    banco_status_aluno.append(status)


def comparar_notas(lst_nota, lst_matricula_aluno, lst_nome_aluno, lst_status_aluno):
    ok = False
    while not ok:
        ok = True
        for i in range(len(lst_nota) - 1):
            if lst_nota[i] < lst_nota[i + 1]:
                lst_nota[i], lst_nota[i + 1] = lst_nota[i + 1], lst_nota[i]
                lst_matricula_aluno[i], lst_matricula_aluno[i + 1] = lst_matricula_aluno[i + 1], lst_matricula_aluno[i]
                lst_nome_aluno[i], lst_nome_aluno[i + 1] = lst_nome_aluno[i + 1], lst_nome_aluno[i]
                lst_status_aluno[i], lst_status_aluno[i + 1] = lst_status_aluno[i + 1], lst_status_aluno[i]
                ok = False


def encontrar_login_professor(nome, matricula):
    for n in banco_nomes_professores:
        if n == nome:
            if banco_matriculas_professores.index(matricula) == banco_nomes_professores.index(nome):
                print('Login efetuado com sucesso')
                return 1
            else:
                return 2


def encontrar_login_aluno(nome, matricula):
    for n in banco_nomes:
        if n == nome:
            if banco_matriculas.index(matricula) == banco_nomes.index(nome):
                print('Login efetuado com sucesso')
                return 1
            else:
                return 2


def menu_professor():
    print(
        '\tMenu do Professor\n1 - Anexar edital\n2 - adicionar descrição ao anexo\n3 - Definir Status do Aluno\n '
        'Entre com sua resposta: ')


def menu_aluno():
    print(
        '\tMenu do Aluno\n1 - visualizar editais\n2 - Escolher bolsas\n3 - Adicionar notas\n4 - Status\n Entre com '
        'sua resposta: ')
    #  Adicionar nota ao criar a conta - check
    #  o programa vai rankear os selecionaveis - check

def status_aluno(lst_status_aluno):
    #  diz se ele foi reprovado ou classificavel
    #  nota menor que a exigida no edital
    print(lst_status_aluno[])


def anexar_historico(historico):
    #  para alunos classificaveis
    #  um arquivo historico.txt para ser criado
    pass


def mostar_arquivos_alunos():
    #  Professor ter acesso aos documentos anexado pelos alunos
    # vai mostrar o historico para o professor
    pass


def classificado():
    #  Professor consegue alterar o status do aluno de classificavel para classificado
    #  Vai aparecer um menu com os alunos aí o professor vai escolher um aluno
    #  vai aparecer outro menu com três opções: 1 - aprovado, 2 - classificavel, 3 - reprovado
    pass


#  Funções aluno

def vizualizar_editais():
    #  vizualiza editais postados pelos professores
    #  o aluno vai ler o arquivo criado pelo professor(menu: o indice vai ser a opcao do menu)
    #  pypdf2
    pass


def escolher_bolsas():
    #  para poder escolher uma bolsa eu devo ter informado as notas
    #  menu com opcoes de bolsa e que o indice da lista corresponde a leitura do edital
    pass

def status():
    #  mostrar o estado de como o aluno está na seleção
    #  para o aluno vai aparecer aguardando enquanto o professor não settar o status dele
    pass


while menu:

    os.system('cls')
    menu = int(input('\tMenu\n1 - Cadastrar\n2 - Login\n3 - print lista\n0 - sair\nResposta: '))
    if menu == 1:
        tipo_conta = int(input('Informe o tipo de conta que você deseja criar: 1 -  Professor / 2 - aluno: '))
        os.system('cls')

        if tipo_conta == 1:
            nome = input('Informe seu nome: ')
            matricula = input('informe sua matricula: ')
            cadastrar_professor(nome, matricula)
            os.system('pause')
            os.system('cls')

        if tipo_conta == 2:
            nome = input('Informe seu nome: ')
            matricula = input('informe sua matricula: ')
            cadastrar_aluno(nome, matricula)
            os.system('pause')
            os.system('cls')
            os.system('cls')

    if menu == 2:
        tipo_conta = int(input('Informe o tipo da sua conta 1 - Professor / 2 - Aluno: '))
        if tipo_conta == 1:
            nome = input('Informe seu nome: ')
            matricula = input('informe sua matricula: ')
            encontrar_login_professor(nome, matricula)
            os.system('pause')
            os.system('cls')
            menu_professor()
            os.system('pause')
            os.system('cls')
            #  acesso a area do Professor
            #  anexa arquivos(editais)
            #  descrição dos anexos
            os.system('cls')
            pass
        if tipo_conta == 2:
            nome = input('Informe seu nome: ')
            matricula = input('informe sua matricula: ')
            encontrar_login_aluno(nome, matricula)
            os.system('pause')
            os.system('cls')
            menu_aluno()

            # encontrar_login_professor(nome, matricula)
            os.system('pause')
            os.system('cls')

            #  acesso a area do Aluno
            #  vizualiza arquivos postados pelo professor
            #  escolhe as bolsas em que quer se candidatar
            #  o aluno add suas notas ao sistema
            os.system('cls')
    if menu == 3:
        print(banco_nomes)
        os.system('pause')
