"""Примеры использования модулей конвертера."""
from length import convert_length
from temperature import c_to_f, f_to_c


def main():
    """Печатает примеры перевода единиц."""
    print(convert_length(2.5, "km", "m"))   # 2.5 км в метрах
    print(c_to_f(36.6))                     # нормальная температура тела
    print(f_to_c(-40))                      # точка совпадения шкал


if __name__ == "__main__":
    main()
