"""
UNIVERSIDAD DEL VALLE DE GUATEMALA
Gráficas por computadoras

Walter Saldaña #19897
"""

__author__ = "Walter Saldaña"
__version__ = "0.1.0"


from game.render import Render


def main():
    patterns = []

    star = [
        [0, 0, 1],
        [1, 0, 1],
        [0, 1, 1],
        [1, 0, 1],
        [0, 0, 1]
    ]
    patterns.append((star, 5, 5))
    patterns.append((star, 90, 5))
    patterns.append((star, 5, 90))
    patterns.append((star, 90, 90))

    pulsar = [
        [0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0],
        [0],
        [1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1],
        [0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0],
        [0],
        [0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0],
        [1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1],
        [0],
        [0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0]
    ]
    patterns.append((pulsar, 45, 40))

    light_space_ship = [
        [0, 1, 1, 1, 1],
        [1, 0, 0, 0, 1],
        [0, 0, 0, 0, 1],
        [1, 0, 0, 1, 0]
    ]
    patterns.append((light_space_ship, 2, 25))
    patterns.append((light_space_ship, 10, 25))
    patterns.append((light_space_ship, 80, 25))
    patterns.append((light_space_ship, 88, 25))
    patterns.append((light_space_ship, 47, 25))

    heavy_space_ship = [
        [1, 1, 1, 1, 1, 1, 0],
        [1, 0, 0, 0, 0, 0, 1],
        [1],
        [0, 1, 0, 0, 0, 0, 1],
        [0, 0, 0, 1, 1, 0, 0]
    ]
    patterns.append((heavy_space_ship, 2, 65))
    patterns.append((heavy_space_ship, 14, 65))
    patterns.append((heavy_space_ship, 80, 65))
    patterns.append((heavy_space_ship, 92, 65))
    patterns.append((heavy_space_ship, 47, 65))

    rocket = [
        [0, 0, 1, 1, 0, 0],
        [0, 1, 0, 0, 1, 0],
        [0, 1, 0, 0, 1, 0],
        [1, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 1],
        [0, 1, 1, 1, 1, 0],
        [1, 1, 0, 0, 1, 1],
        [1, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 1],
        [0],
        [0],
        [0, 1, 1, 1, 1, 0],
        [0, 0, 1, 1, 0, 0]
    ]
    patterns.append((rocket, 20, 45))
    patterns.append((rocket[::-1], 75, 35))

    eyes = [
        [0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
        [1, 1, 0, 1, 1, 1, 1, 0, 1, 1],
        [0, 0, 1, 0, 0, 0, 0, 1, 0, 0]
    ]
    patterns.append((eyes, 46, 6))
    patterns.append((eyes, 46, 90))

    r = Render(100, 100, patterns)
    r.run()


if __name__ == "__main__":
    main()
