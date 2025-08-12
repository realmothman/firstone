from dataclasses import dataclass

@dataclass
class TitiaFofa:
    """Representa o estado básico da Titia Fofa na simulação."""
    peso: float = 150.0  # peso inicial em kg
    energia: float = 100.0  # energia inicial em unidades arbitrárias

    def comer(self, calorias: float) -> None:
        """Aumenta o peso e a energia de acordo com as calorias ingeridas."""
        self.peso += 0.0002 * calorias
        self.energia += calorias * 0.001

    def caminhar(self, distancia: float) -> None:
        """Reduz o peso e a energia com base na distância percorrida em km."""
        self.peso -= 0.01 * distancia
        self.energia -= 0.1 * distancia

    def __str__(self) -> str:
        return f"Titia Fofa - peso: {self.peso:.2f} kg, energia: {self.energia:.2f}"
