"""Перевод единиц длины."""

# Сколько метров в одной единице
FACTORS = {"mm": 0.001, "cm": 0.01, "m": 1, "km": 1000}


def convert_length(value, src, dst):
    """Переводит value из единицы src в единицу dst."""
    if src not in FACTORS or dst not in FACTORS:
        raise ValueError(f"Неизвестная единица: {src} или {dst}")
    return value * FACTORS[src] / FACTORS[dst]
