import csv
import heapq
import numpy as np
import matplotlib.pyplot as plt

# Classe para representar um usuário
class Usuario:
    def __init__(self, cpf, nome, idade, celular, prioridade=None, tempo_espera=None):
        self.cpf = cpf
        self.nome = nome
        self.idade = idade
        self.celular = celular
        self.prioridade = prioridade
        self.tempo_espera = tempo_espera

# Lista para armazenar usuários
usuarios = []

# Função para salvar usuário no arquivo CSV
def salvar_em_csv(usuario):
    fieldnames = ['CPF', 'Nome', 'Idade', 'Celular', 'Prioridade', 'Tempo de espera']
    with open('usuarios.csv', mode='a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writerow({
            'CPF': usuario.cpf,
            'Nome': usuario.nome,
            'Idade': usuario.idade,
            'Celular': usuario.celular,
            'Prioridade': usuario.prioridade,
            'Tempo de espera': usuario.tempo_espera
        })

# Função para cadastrar um novo usuário
def cadastrar_usuario():
    cpf = input('CPF: ')
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    celular = input('Celular: ')
    usuario = Usuario(cpf, nome, idade, celular)
    usuarios.append(usuario)
    salvar_em_csv(usuario)
    print('Usuário cadastrado com sucesso!')

# Função para ler dados do arquivo CSV
def ler_e_imprimir_dados_csv():
    try:
        # Abrir o arquivo CSV para leitura
        with open('usuarios.csv', mode='r') as file:
            # Criar um objeto reader para ler o arquivo CSV
            reader = csv.DictReader(file)
            
            # Verificar se o arquivo CSV tem cabeçalhos
            if not reader.fieldnames:
                print("O arquivo CSV não tem cabeçalhos.")
                return
            
            # Imprimir cada linha do arquivo CSV
            for row in reader:
                # Formatar os dados para exibição
                print(f"CPF: {row.get('CPF', 'N/A')}, Nome: {row.get('Nome', 'N/A')}, "
                      f"Idade: {row.get('Idade', 'N/A')}, Celular: {row.get('Celular', 'N/A')}, "
                      f"Prioridade: {row.get('Prioridade', 'N/A')}, Tempo de espera: {row.get('Tempo de espera', 'N/A')}")
    
    except FileNotFoundError:
        print("O arquivo 'usuarios.csv' não foi encontrado.")
    except csv.Error as e:
        print(f"Erro ao ler o arquivo CSV: {e}")

# Função para exibir usuários do arquivo CSV
def exibir_usuarios():
    ler_e_imprimir_dados_csv()  # Carregar os usuários do arquivo CSV
    for usuario in usuarios:
        print(f'CPF: {usuario.cpf}, Nome: {usuario.nome}, Idade: {usuario.idade}, Celular: {usuario.celular}, Prioridade: {usuario.prioridade}, Tempo de espera: {usuario.tempo_espera}')

# Função para inserir tempo de espera e prioridade para um usuário
def inserir_tempo_espera_e_prioridade():
    ler_e_imprimir_dados_csv()  # Carregar os usuários do arquivo CSV
    for usuario in usuarios:
        print(f'Usuário: {usuario.nome}')
        tempo_espera = float(input('Digite o tempo de espera (minutos): ')) / 60
        prioridade = int(input('Digite a prioridade (0 a 100): '))
        usuario.tempo_espera = tempo_espera
        usuario.prioridade = prioridade
        salvar_em_csv(usuario)
        print(f'Tempo de espera de {usuario.nome} atualizado para {tempo_espera:.2f} horas')
        print(f'Prioridade de {usuario.nome} atualizada para {prioridade}')

# Função para calcular a integral exponencial com base em uma prioridade mínima
def calcular_integral_exponencial(prioridade_minima):
    ler_e_imprimir_dados_csv() # Carregar os usuários do arquivo CSV
    usuarios_selecionados = [usuario for usuario in usuarios if usuario.prioridade >= prioridade_minima and usuario.tempo_espera is not None]

    if not usuarios_selecionados:
        print('Nenhum tempo de espera na fila foi inserido para os usuários selecionados. Não é possível calcular a integral.')
        return None

    tempo_medio_espera = sum(usuario.tempo_espera for usuario in usuarios_selecionados) / len(usuarios_selecionados)
    lambda_ = 1 / tempo_medio_espera
    integral = np.exp(-lambda_)
    print(f'A integral exponencial é {integral:.2f}')
    return integral

# Função para calcular o tempo de espera por prioridade
def calcular_tempo_espera_por_prioridade():
    ler_e_imprimir_dados_csv()  # Carregar os usuários do arquivo CSV
    tempos_por_prioridade = {}

    for usuario in usuarios:
        if usuario.prioridade is not None and usuario.tempo_espera is not None:
            if usuario.prioridade in tempos_por_prioridade:
                tempos_por_prioridade[usuario.prioridade] += usuario.tempo_espera
            else:
                tempos_por_prioridade[usuario.prioridade] = usuario.tempo_espera

    return sorted(tempos_por_prioridade.items())

# Função para plotar gráfico de tempo de espera por prioridade
def plotar_grafico():
    tempos_por_prioridade = calcular_tempo_espera_por_prioridade()
    if not tempos_por_prioridade:
        print('Não há dados suficientes para plotar o gráfico.')
        return

    prioridades, tempos_espera = zip(*tempos_por_prioridade)
    plt.plot(prioridades, tempos_espera, marker='o')
    plt.xlabel('Prioridade')
    plt.ylabel('Tempo de espera (horas)')
    plt.title('Tempo de espera por prioridade')
    plt.show()

# Função principal para executar o programa
def main():
    while True:
        print('''Escolha uma opção:
1 - Cadastrar usuário
2 - Exibir usuários
3 - Inserir tempo de espera e prioridade
4 - Calcular integral exponencial
5 - Plotar gráfico de tempo de espera por prioridade
6 - Sair''')
        opcao = int(input('Opção: '))

        if opcao == 1:
            cadastrar_usuario()
        elif opcao == 2:
            ler_e_imprimir_dados_csv()
        elif opcao == 3:
            inserir_tempo_espera_e_prioridade()
        elif opcao == 4:
            prioridade_minima = int(input('Digite a prioridade mínima: '))
            calcular_integral_exponencial(prioridade_minima)
        elif opcao == 5:
            plotar_grafico()
        elif opcao == 6:
            print('Programa encerrado.')
            break
        else:
            print('Opção inválida. Por favor, tente novamente.')

if __name__ == "__main__":
    main()
