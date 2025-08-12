from titia_fofa import TitiaFofa


def progress_bar(value: float, max_value: float, length: int = 20) -> str:
    filled = int(length * value / max_value)
    return "[" + "#" * filled + " " * (length - filled) + "]"


def mostrar_estado(fofa: TitiaFofa) -> None:
    print(f"Peso:    {progress_bar(fofa.peso, 200)} {fofa.peso:.2f} kg")
    print(f"Energia: {progress_bar(fofa.energia, 200)} {fofa.energia:.2f}\n")


def simular_dia() -> None:
    """Executa um dia simples na vida da Titia Fofa."""
    fofa = TitiaFofa()
    mostrar_estado(fofa)
    acoes = [
        ("comer", 500),
        ("caminhar", 2),
        ("comer", 800),
        ("caminhar", 1),
        ("comer", 700),
    ]
    for acao, valor in acoes:
        getattr(fofa, acao)(valor)
        mostrar_estado(fofa)
    print(fofa)


if __name__ == "__main__":
    simular_dia()
