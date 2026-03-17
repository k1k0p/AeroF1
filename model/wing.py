# Classe que representa a configuração de uma asa aerodinâmica
class WingConfig:

    # Construtor — corre automaticamente quando fazes WingConfig()
    # Cada parâmetro tem um valor por omissão caso não passes nenhum
    def __init__(
        self,
        angle_of_attack: float = 5.0,   # Ângulo de ataque em graus
        velocity: float = 100.0,         # Velocidade em km/h
        area: float = 1.5,               # Área da asa em m²
        camber: float = 0.05,            # Curvatura da asa (0 = plana, 0.2 = muito curva)
        air_density: float = 1.225       # Densidade do ar em kg/m³ (valor padrão ao nível do mar)
    ):
        # Guarda cada parâmetro dentro do objeto para poder usar depois com self.
        self.angle_of_attack = angle_of_attack
        self.velocity = velocity
        self.area = area
        self.camber = camber
        self.air_density = air_density

    # Função que valida se os valores fazem sentido fisicamente
    def validate(self):
        # assert verifica se a condição é verdadeira
        # se não for, lança um erro com a mensagem escrita
        assert 0 <= self.angle_of_attack <= 25, "Ângulo de ataque deve estar entre 0 e 25 graus"
        assert 0 < self.velocity <= 400, "Velocidade deve estar entre 0 e 400 km/h"
        assert 0 < self.area <= 10, "Área deve estar entre 0 e 10 m²"
        assert 0 <= self.camber <= 0.2, "Curvatura deve estar entre 0 e 0.2"
        assert 0 < self.air_density <= 2, "Densidade do ar inválida"

    # Define o que aparece quando fazes print(w)
    # Sem isto o Python mostraria algo como <object at 0x10f3a2d30>
    def __repr__(self):
        return (
            f"WingConfig("
            f"angle={self.angle_of_attack}°, "       # f"..." permite meter variáveis com {}
            f"velocity={self.velocity}km/h, "
            f"area={self.area}m², "
            f"camber={self.camber}, "
            f"air_density={self.air_density}kg/m³)"
        )