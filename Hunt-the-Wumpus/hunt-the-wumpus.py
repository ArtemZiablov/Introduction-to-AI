import pygame
import math
import random
import sys

# Ініціалізація бібліотеки Pygame для використання в проекті
pygame.init()

# Налаштування розмірів і створення вікна гри
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Світ Вампусу")

# Налаштування шрифтів для відображення тексту (звичайного та великого)
font = pygame.font.SysFont("Arial", 20)
big_font = pygame.font.SysFont("Arial", 36)

# Визначення кольорів, які використовуватимуться у грі
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GRAY = (200, 200, 200)

# Кількість кімнат в "печері", положення центру печери та радіус розташування кімнат
NUM_ROOMS = 20
CENTER = (WIDTH // 2, HEIGHT // 2)
RADIUS = 220

# Розрахунок координат для кожної кімнати, розташованих рівномірно по колу
rooms_positions = {}
for i in range(NUM_ROOMS):
    angle = 2 * math.pi * i / NUM_ROOMS - math.pi / 2  # Початковий кут -90 градусів для вирівнювання
    x = CENTER[0] + int(RADIUS * math.cos(angle))
    y = CENTER[1] + int(RADIUS * math.sin(angle))
    rooms_positions[i] = (x, y)

# Задання з'єднань (сусідніх кімнат) для кожної кімнати у печері
neighbors = {
    0: [1, 4, 7],
    1: [0, 2, 9],
    2: [1, 3, 11],
    3: [2, 4, 13],
    4: [0, 3, 5],
    5: [4, 6, 14],
    6: [5, 7, 16],
    7: [0, 6, 8],
    8: [7, 9, 17],
    9: [1, 8, 10],
    10: [9, 11, 18],
    11: [2, 10, 12],
    12: [11, 13, 19],
    13: [3, 12, 14],
    14: [5, 13, 15],
    15: [14, 16, 19],
    16: [6, 15, 17],
    17: [8, 16, 18],
    18: [10, 17, 19],
    19: [12, 15, 18]
}

# Функція для ініціалізації небезпек (встановлення положення Вампуса, провалів та кажанів)
def init_hazards():
    available_rooms = list(range(NUM_ROOMS))
    # Випадковий вибір стартової кімнати для гравця; ця кімната гарантовано без небезпек
    start_room = random.choice(available_rooms)
    available_rooms.remove(start_room)

    # Випадковий вибір кімнати для Вампуса та виключення її зі списку доступних
    wumpus_room = random.choice(available_rooms)
    available_rooms.remove(wumpus_room)

    # Випадковий вибір 2 кімнат для провалів та їх виключення
    pits = random.sample(available_rooms, 2)
    for p in pits:
        available_rooms.remove(p)

    # Випадковий вибір 2 кімнат для кажанів
    bats = random.sample(available_rooms, 2)

    return start_room, wumpus_room, pits, bats

# Виклик функції ініціалізації небезпек
player_room, wumpus_room, pits, bats = init_hazards()

# Лічильник стрільб: встановлено максимальну кількість стрільб (в даному прикладі 1 для тестування)
max_arrows = 1
arrows = max_arrows

# Ініціалізація змінних для стану гри
game_over = False
won = False
message = "Гра почалась! Обирайте сусідню кімнату (ЛКМ - рух, ПКМ - стрільба)"

# Функція для відображення тексту на заданій поверхні (screen)
def draw_text(surface, text, pos, color=WHITE, font=font):
    text_surface = font.render(text, True, color)
    surface.blit(text_surface, pos)

# Функція перевірки, чи знаходиться Вампус у сусідніх кімнатах від гравця, і повертає повідомлення
def check_wumpus_nearby():
    for n in neighbors[player_room]:
        if n == wumpus_room:
            return "Відчувається неприємний запах Вампуса!"
    return ""

# Основний ігровий цикл: обробляє події, оновлює екран, перевіряє стан гри
def game_loop():
    global player_room, game_over, won, message, wumpus_room, arrows

    clock = pygame.time.Clock()

    while True:
        clock.tick(30)  # Обмеження частоти кадрів до 30 FPS
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Обробка подій, якщо гра не завершена
            if not game_over and event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                # Якщо натиснуто ЛКМ або ПКМ
                if event.button in [1, 3]:
                    valid = False
                    # Перевірка, чи вибір потрапляє у одну із сусідніх кімнат
                    for n in neighbors[player_room]:
                        pos = rooms_positions[n]
                        # Перевірка за допомогою відстані (радіус 20 пікселів)
                        if math.hypot(mouse_pos[0] - pos[0], mouse_pos[1] - pos[1]) <= 20:
                            valid = True
                            chosen_room = n
                            # Якщо натиснуто ЛКМ – пересування до сусідньої кімнати
                            if event.button == 1:
                                message = f"Перемістились у кімнату {chosen_room}."
                                player_room = chosen_room
                                check_hazards()  # Перевірка, чи не потрапив гравець у небезпечну кімнату
                            # Якщо натиснуто ПКМ – спроба вистрілу в сусідню кімнату (за умови наявності стріл)
                            elif event.button == 3:
                                if arrows > 0:
                                    arrows -= 1
                                    message = (f"Вистрілили у кімнату {chosen_room}. "
                                               f"Залишилось стрільб: {arrows}.")
                                    # Перевірка попадання: якщо клік був спрямований на кімнату Вампуса
                                    if chosen_room == wumpus_room:
                                        won = True
                                        game_over = True
                                        message = "Ви влучили! Вампус переможений. Ви виграли!"
                                    else:
                                        message += " Промах! Вампус прокинувся..."
                                        # Місце для додаткової логіки пересування Вампуса
                                else:
                                    message = "Стріли закінчилися!"
                            break
                    if not valid:
                        message = "Обирайте лише сусідню кімнату!"

        # Якщо стріли закінчилися, а гра ще не завершена, оголосити програш
        if arrows <= 0 and not won and not game_over:
            message = "Стріли закінчилися! Ви програли."
            game_over = True

        # Оновлення екрану: заповнення чорним кольором
        screen.fill(BLACK)

        # Малювання ліній, що з'єднують кімнати (відображення графу печери)
        for room, nbrs in neighbors.items():
            for n in nbrs:
                pygame.draw.line(screen, GRAY, rooms_positions[room], rooms_positions[n], 2)

        # Малювання кімнат як кіл
        for i, pos in rooms_positions.items():
            color = WHITE
            if i == player_room:
                color = GREEN  # Виділення кімнати, де знаходиться гравець
            # Для відладки можна розкоментувати наступні рядки, щоб бачити розташування небезпек
            # elif i == wumpus_room:
            #     color = RED
            # elif i in pits:
            #     color = BLUE
            # elif i in bats:
            #     color = YELLOW
            pygame.draw.circle(screen, color, pos, 20)
            draw_text(screen, str(i), (pos[0] - 10, pos[1] - 10), BLACK)

        # Відображення основного повідомлення у верхньому лівому куті
        draw_text(screen, message, (20, 20), YELLOW, font)

        # Якщо поруч із гравцем є кімната, де знаходиться Вампус, виводимо попередження
        warning = check_wumpus_nearby()
        if warning:
            draw_text(screen, warning, (20, 50), RED, font)

        # Відображення лічильника стріл у нижньому лівому кутку
        arrow_text = f"Стріли: {arrows}/{max_arrows}"
        draw_text(screen, arrow_text, (20, HEIGHT - 40), WHITE, font)

        # Якщо гра завершена - виводимо повідомлення про завершення гри та очікуємо натискання клавіші
        if game_over:
            text = "Натисніть будь-яку клавішу для виходу."
            text_surface = big_font.render(text, True, WHITE)
            screen.blit(text_surface, (WIDTH // 2 - text_surface.get_width() // 2, HEIGHT // 2))
            pygame.display.flip()
            wait_for_key()
            pygame.quit()
            sys.exit()

        pygame.display.flip()


# Функція перевірки потрапляння гравця у кімнату з небезпекою
def check_hazards():
    global player_room, game_over, message
    # Якщо гравець заходить у кімнату, де знаходиться Вампус
    if player_room == wumpus_room:
        message = "Ви потрапили до кімнати Вампуса. Вас з’їв Вампус!"
        game_over = True
    # Якщо гравець заходить у кімнату з провалом
    elif player_room in pits:
        message = "Ви впали в провал!"
        game_over = True
    # Якщо гравець потрапляє у кімнату з кажанами – транспортування у випадкову кімнату
    elif player_room in bats:
        message = "Кажани підібрали вас і перенесли в іншу кімнату..."
        safe_rooms = [i for i in range(NUM_ROOMS) if i not in pits and i != wumpus_room]
        player_room = random.choice(safe_rooms)
        message += f" Тепер ви в кімнаті {player_room}."
        if player_room in bats:
            message += " Але кажани знову не турбують вас."


# Функція, яка очікує натискання клавіші після завершення гри
def wait_for_key():
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN or event.type == pygame.QUIT:
                waiting = False


if __name__ == "__main__":
    game_loop()
