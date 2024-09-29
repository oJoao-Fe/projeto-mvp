# Dynamic Programming

# a) [Seleção de Conteúdo] --> [Desenvolvimento de AR/VR] --> [Interação Estudante-Cenário]
#                                                               |
#                                                              V
# [Monitoramento de Desempenho] --> [Relatórios e Feedback] --> [Aprimoramento Contínuo]

# b-c) Criação de uma matriz para armazenar os dados de desempenho dos estudantes
# Cada linha representa um estudante e as colunas são métricas de desempenho
performance_matrix = [
    # [Tempo de resposta, Precisão, Interações corretas]
    [12.5, 0.95, 18],
    [10.8, 0.92, 20],
    [15.3, 0.88, 16]
]

# d) Função para calcular a média de desempenho de todos os estudantes
def calcular_media(performance_matrix):
    media = [sum(col) / len(col) for col in zip(*performance_matrix)]
    return media

def gerar_feedback(estudante):
    tempo_resposta, precisao, interacoes = estudante
    if tempo_resposta < 13 and precisao > 0.90 and interacoes > 17:
        return "Ótimo desempenho!"
    else:
        return "Precisa melhorar nos critérios."
    
performance = performance_matrix[0]  
print(gerar_feedback(performance))   
