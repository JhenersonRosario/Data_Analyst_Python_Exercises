def str_para_bool(valor):
    if valor == 'True':
        return True
    else:
        return False
def load_data(nome_arquivo, separador):
    alunos = []
    arquivo = open(nome_arquivo, 'r')
    linhas = arquivo.readlines()

    for linha in linhas [1:]:
        linha = linha.replace('\n', '')
        registro = linha.split(separador)
        aluno = {
            'nome' : registro[0],
            'ano'  : int(registro[1]),
            'escola' : registro[2],
            'nota_semestre_1' : float(registro[3]),
            'nota_semestre_2' : float(registro[4]),
            'faltas' : int(registro[5]),
            'nota_exame' : float(registro[6]),
            'monitoria' : str_para_bool(registro[7])
        }
        alunos.append(aluno)
    return alunos

