import math
from model.wing import WingConfig

def calcular_pressao_dinamica(wing: WingConfig) -> float:
    # Converte velocidade de km/h para m/s (necessário para as fórmulas físicas)
    velocidade_ms = wing.velocity / 3.6

    # Pressão dinâmica — quanta "força" o ar tem quando bate na asa
    # Cresce com o quadrado da velocidade, por isso duplicar a velocidade quadruplica a pressão
    q = 0.5 * wing.air_density * velocidade_ms ** 2

    return q


def calcular_CL(wing: WingConfig) -> float:
    # Converte o ângulo de ataque de graus para radianos (necessário para math.sin)
    angulo_rad = math.radians(wing.angle_of_attack)

    # Coeficiente de sustentação — combina o efeito do ângulo de ataque e da curvatura
    # Quanto maior o ângulo e maior a curvatura, maior o CL
    CL = 2 * math.pi * math.sin(angulo_rad) + 2 * wing.camber

    # Limita o CL a 1.5 para simular o stall — a partir de certo ângulo a asa "perde"
    CL = min(CL, 1.5)

    return CL


def calcular_CD(CL: float) -> float:
    # Coeficiente de arrasto base — drag mínimo mesmo sem gerar downforce
    CD_base = 0.02

    # Fator de eficiência de Oswald — representa as imperfeições da asa real
    k = 0.05

    # O drag cresce com o quadrado do CL — quanto mais downforce geras, mais drag pagas
    CD = CD_base + k * CL ** 2

    return CD


def calcular_downforce(wing: WingConfig) -> float:
    q = calcular_pressao_dinamica(wing)
    CL = calcular_CL(wing)

    # Downforce — força que empurra o carro para o chão
    downforce = CL * q * wing.area

    return round(downforce, 2)


def calcular_drag(wing: WingConfig) -> float:
    q = calcular_pressao_dinamica(wing)
    CL = calcular_CL(wing)
    CD = calcular_CD(CL)

    # Drag — resistência ao avanço, o ar a "travar" o carro
    drag = CD * q * wing.area

    return round(drag, 2)


def calcular_eficiencia(wing: WingConfig) -> float:
    downforce = calcular_downforce(wing)
    drag = calcular_drag(wing)

    # Evita divisão por zero caso o drag seja 0
    if drag == 0:
        return 0.0

    # Eficiência — downforce gerada por cada unidade de drag
    # Valor alto significa boa asa, valor baixo significa que estás a pagar muito drag
    eficiencia = downforce / drag

    return round(eficiencia, 2)


def calcular_tudo(wing: WingConfig) -> dict:
    # Função principal — recebe uma asa e devolve todas as métricas de uma vez
    return {
        "downforce": calcular_downforce(wing),
        "drag": calcular_drag(wing),
        "eficiencia": calcular_eficiencia(wing)
    }