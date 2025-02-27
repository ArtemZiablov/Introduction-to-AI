import pygame
import numpy as np

# Кольори
COLOR_DEAD = (47, 79, 79)    # Темно-сірий (фон)
COLOR_ALIVE = (0, 255, 0)    # Зелений (живі клітини)
COLOR_GRID = (70, 130, 180)  # Синюватий колір сітки (для фону)
COLOR_DIE = (255, 0, 0)      # Червоний (для тих, що «вимирають» – опційно)

# Функція підрахунку сусідів з урахуванням «замкнених» меж
def count_neighbors_toroidal(matrix, x, y):
    """
    Повертає кількість живих сусідів клітини (x, y).
    'Замкнені' межі реалізовано через (x ± 1) % height та (y ± 1) % width.
    """
    height, width = matrix.shape
    total = 0
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if dx == 0 and dy == 0:
                continue  # не враховувати саму клітину
            nx = (x + dx) % height
            ny = (y + dy) % width
            total += matrix[nx, ny]
    return total

# Функція, що обраховує новий стан гри (наступне покоління)
def update_state_toroidal(surface, current_matrix, scale):
    height, width = current_matrix.shape
    new_matrix = np.zeros((height, width))

    for x in range(height):
        for y in range(width):
            neighbors = count_neighbors_toroidal(current_matrix, x, y)
            cell = current_matrix[x, y]

            # Правила гри «Життя» Конвея
            if cell == 1:
                # 1) Якщо живих сусідів < 2 або > 3 => клітина вимирає
                if neighbors < 2 or neighbors > 3:
                    color = COLOR_DEAD
                else:
                    # 2) Якщо 2 чи 3 сусіда => клітина виживає
                    new_matrix[x, y] = 1
                    color = COLOR_ALIVE
            else:
                # 3) Якщо клітина була мертва, але має рівно 3 сусіди => «народжується»
                if neighbors == 3:
                    new_matrix[x, y] = 1
                    color = COLOR_ALIVE
                else:
                    color = COLOR_DEAD

            # Малюємо клітинку
            rect = (y * scale, x * scale, scale - 1, scale - 1)
            pygame.draw.rect(surface, color, rect)

    return new_matrix

def initial_pattern(pattern_name, width, height):
    """
    Повертає матрицю з початковим розташуванням (pattern_name).
    """
    matrix = np.zeros((height, width))

    if pattern_name == "random":
        # Випадкове заповнення
        matrix = np.random.randint(2, size=(height, width))

    elif pattern_name == "block":
        # Статичний блок 2x2 у центрі
        cx, cy = height // 2, width // 2
        matrix[cx][cy] = 1
        matrix[cx][cy+1] = 1
        matrix[cx+1][cy] = 1
        matrix[cx+1][cy+1] = 1

    elif pattern_name == "blinker":
        # «Мигалка» з періодом 2
        cx, cy = height // 2, width // 2
        matrix[cx, cy-1] = 1
        matrix[cx, cy]   = 1
        matrix[cx, cy+1] = 1

    elif pattern_name == "toad":
        # «Жаба» (Toad) з періодом 2
        # Розмістимо десь у центрі
        cx, cy = height // 2, width // 2
        matrix[cx,   cy] = 1
        matrix[cx,   cy+1] = 1
        matrix[cx,   cy+2] = 1
        matrix[cx+1, cy-1] = 1
        matrix[cx+1, cy]   = 1
        matrix[cx+1, cy+1] = 1

    elif pattern_name == "glider":
        # Планер (Glider), який рухатиметься по діагоналі
        matrix[1, 0] = 1
        matrix[2, 1] = 1
        matrix[0, 2] = 1
        matrix[1, 2] = 1
        matrix[2, 2] = 1

    elif pattern_name == "beacon":
        # «Маяк» (Beacon), період 2
        cx, cy = height // 2, width // 2
        # квадрат 2x2
        matrix[cx,   cy] = 1
        matrix[cx,   cy-1] = 1
        matrix[cx-1, cy] = 1
        matrix[cx-1, cy-1] = 1
        # сусідній квадрат 2x2
        matrix[cx+1, cy+1] = 1
        matrix[cx+1, cy+2] = 1
        matrix[cx+2, cy+1] = 1
        matrix[cx+2, cy+2] = 1


    elif pattern_name == "pulsar":
        # Пульсар - це фігура розміром 15x15, яка повторюється кожні 3 кроки
        cx, cy = height // 2, width // 2  # Визначаємо центр поля
        # Масив зсувів (координат), які формують пульсар
        pulsar_offsets = [
            (-6, -4), (-6, -3), (-6, -2), (-6, 2), (-6, 3), (-6, 4),
            (-4, -6), (-3, -6), (-2, -6), (2, -6), (3, -6), (4, -6),
            (-4, -1), (-3, -1), (-2, -1), (2, -1), (3, -1), (4, -1),
            (-1, -4), (-1, -3), (-1, -2), (-1, 2), (-1, 3), (-1, 4),
            (-4, 1), (-3, 1), (-2, 1), (2, 1), (3, 1), (4, 1),
            (1, -4), (1, -3), (1, -2), (1, 2), (1, 3), (1, 4),
            (-6, -4), (-6, -3), (-6, -2), (-6, 2), (-6, 3), (-6, 4),
            (-4, 6), (-3, 6), (-2, 6), (2, 6), (3, 6), (4, 6),
            (6, -4), (6, -3), (6, -2), (6, 2), (6, 3), (6, 4),
            (-4, 6), (-3, 6), (-2, 6), (2, 6), (3, 6), (4, 6),
            (6, -4), (6, -3), (6, -2), (6, 2), (6, 3), (6, 4)
        ]

        for dx, dy in pulsar_offsets:
            matrix[(cx + dx) % height, (cy + dy) % width] = 1


    else:
        # За замовчуванням: нехай буде випадкове
        matrix = np.random.randint(2, size=(height, width))

    return matrix


def main():
    pygame.init()
    pygame.display.set_caption("Game of Life (замкнене поле)")

    # Розміри поля у клітинах
    width = 50
    height = 30

    # Розмір клітинки в пікселях
    scale = 15

    # Створюємо вікно
    screen = pygame.display.set_mode((width * scale, height * scale))

    # початковий патерн ("toad", "block", "blinker", "glider", "beacon", "random", "pulsar" )
    pattern_name = "pulsar"
    cells = initial_pattern(pattern_name, width, height)

    clock = pygame.time.Clock()

    running = True
    while running:
        clock.tick(5)  # FPS (кількість оновлень за секунду)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Заливаємо фон сітки
        screen.fill(COLOR_GRID)

        # Генеруємо наступне покоління з урахуванням тороїдальних меж
        cells = update_state_toroidal(screen, cells, scale)

        # Оновлюємо зображення на екрані
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
