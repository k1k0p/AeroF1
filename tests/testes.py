from model.wing import WingConfig
from model.physics import calcular_tudo

def testar(nome, **kwargs):
    # Cria uma asa com os parâmetros passados e imprime os resultados
    wing = WingConfig(**kwargs)
    resultados = calcular_tudo(wing)
    print(f"\n--- {nome} ---")
    print(f"  Downforce : {resultados['downforce']} N")
    print(f"  Drag      : {resultados['drag']} N")
    print(f"  Eficiência: {resultados['eficiencia']}")

# Teste 1 — valores base (referência)
testar("Base", angle_of_attack=5, velocity=100, area=1.5, camber=0.05)

# Teste 2 — velocidade baixa vs alta
testar("Velocidade baixa", angle_of_attack=5, velocity=50, area=1.5, camber=0.05)
testar("Velocidade alta",  angle_of_attack=5, velocity=200, area=1.5, camber=0.05)

# Teste 3 — ângulo pequeno vs grande
testar("Ângulo pequeno", angle_of_attack=2,  velocity=100, area=1.5, camber=0.05)
testar("Ângulo grande",  angle_of_attack=20, velocity=100, area=1.5, camber=0.05)

# Teste 4 — área pequena vs grande
testar("Área pequena", angle_of_attack=5, velocity=100, area=0.5, camber=0.05)
testar("Área grande",  angle_of_attack=5, velocity=100, area=3.0, camber=0.05)

# Teste 5 — curvatura baixa vs alta
testar("Curvatura baixa", angle_of_attack=5, velocity=100, area=1.5, camber=0.01)
testar("Curvatura alta",  angle_of_attack=5, velocity=100, area=1.5, camber=0.2)