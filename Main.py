import csv
import sympy as sp
from usuario import Usuario
from Fila_prioridade import FilaPrioridade
from Grafico import plotar_grafico
import matplotlib.pyplot as plt
import heapq

class Usuario:
    def __init__(self, cpf, celular, idade, nome):
        self.cpf = cpf
        self.celular = celular
        self.idade = idade
        self.nome = nome

class FilaPrioridade:
    def __init__(self):
        self.fila = []

    def adicionar_usuario(self, usuario):
        heapq.heappush(self.fila, (usuario.idade, usuario.nome))

    def proximo_usuario(self):
        if self.fila:
            idade, nome = heapq.heappop(self.fila)
            return nome, idade
        else:
            return None


def ler_usuarios_do_csv():
    usuarios = []
    with open('usuarios.csv', mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            usuario = Usuario(row['CPF'], row['Celular'], int(row['Idade']), row['Nome'])
            usuarios.append(usuario)
    return usuarios

def cadastrar_usuario():
    cpf = input("Digite o CPF: ")
    celular = input("Digite o celular: ")
    idade = int(input("Digite a idade: "))
    nome = input("Digite o nome: ")
    
    usuario = Usuario(cpf, celular, idade, nome)
    salvar_em_csv(usuario)
    return usuario

def salvar_em_csv(usuario):
    with open('usuarios.csv', mode='a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['CPF', 'Celular', 'Idade', 'Nome'])
        if file.tell() == 0:
            writer.writeheader()
        writer.writerow({'CPF': usuario.cpf, 'Celular': usuario.celular, 'Idade': usuario.idade, 'Nome': usuario.nome})

def calcular_tempo_medio_espera(usuarios):
    tempo_espera_total = sum(usuario.idade for usuario in usuarios)
    tempo_medio_espera = tempo_espera_total / len(usuarios)
    return tempo_medio_espera

def calcular_integral_exponencial():
    # Definindo a variável simbólica
    x = sp.Symbol('x')

    # Definindo a função de densidade de probabilidade da distribuição exponencial
    lambda_ = sp.Symbol('lambda', positive=True)  # Parâmetro de taxa da distribuição exponencial
    funcao = lambda_ * sp.exp(-lambda_ * x)

    # Calculando a integral da função de 0 a infinito
    integral, _ = sp.integrate(funcao, (x, 0, sp.oo))

    return integral

def plotar_grafico(integral_exponencial):
    # Dados do gráfico
    dados = {'Integral Exponencial': integral_exponencial}

    # Criar o gráfico
    plt.figure(figsize=(8, 6))
    plt.bar(dados.keys(), dados.values(), color=['blue'])

    # Adicionar título e rótulos
    plt.title('Integral da Distribuição Exponencial')
    plt.xlabel('Integral')
    plt.ylabel('Valor')

    # Exibir o gráfico
    plt.show()

def main():
    while True:
        opcao = input("Escolha uma opção:\n1. Cadastrar usuário\n2. Ler usuários do CSV\n3. Calcular tempo médio de espera dos clientes\n4. Calcular a integral da distribuição exponencial\n5. Plotar o gráfico estatístico\n6. Sair\nOpção: ")

        if opcao == "1":
            usuario = cadastrar_usuario()
            print("Usuário cadastrado com sucesso!")
        elif opcao == "2":
            usuarios = ler_usuarios_do_csv()
            print("Usuários lidos do CSV com sucesso!")
        elif opcao == "3":
            if 'usuarios' not in locals():
                print("Erro: Nenhum usuário foi lido do CSV ainda. Por favor, escolha a opção 2 para ler os usuários do CSV.")
                continue
            tempo_medio_espera = calcular_tempo_medio_espera(usuarios)
            print("Tempo médio de espera dos clientes:", tempo_medio_espera)
        elif opcao == "4":
            integral_exponencial = calcular_integral_exponencial()
            print("Integral da distribuição exponencial:", integral_exponencial)
        elif opcao == "5":
            if 'integral_exponencial' not in locals():
                print("Erro: A integral da distribuição exponencial não foi calculada ainda. Por favor, escolha a opção 4 para calcular a integral.")
                continue
            plotar_grafico(integral_exponencial)
        elif opcao == "6":
            print("Encerrando o programa.")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    main()