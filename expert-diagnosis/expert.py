import pygame
import sys

# Ініціалізація Pygame
pygame.init()

# Налаштування екрану
WIDTH, HEIGHT = 640, 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Експертна система: Медична діагностика")

# Основні кольори та шрифти
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
FONT = pygame.font.SysFont("Arial", 24)


def draw_multiline_text(text, font, color, surface, rect, align_center=True):
    """
    Малює багаторядковий текст (із '\n') всередині заданого прямокутника rect.
    За замовчуванням вирівнює текст по центру по горизонталі.
    """
    # Розбиваємо текст на рядки за символом нової лінії
    lines = text.split('\n')
    line_height = font.get_linesize()
    total_text_height = line_height * len(lines)

    # Початкова координата Y (щоб відцентрувати весь блок)
    y = rect.centery - total_text_height // 2

    for line in lines:
        # Малюємо кожен рядок
        text_surface = font.render(line, True, color)
        text_rect = text_surface.get_rect()

        if align_center:
            # Вирівнювання по центру горизонталі
            text_rect.centerx = rect.centerx
        else:
            # Якщо потрібне інше вирівнювання, можна використати rect.x чи rect.left
            text_rect.x = rect.x

        # Встановлюємо координату Y для поточного рядка і відображаємо
        text_rect.y = y
        surface.blit(text_surface, text_rect)

        # Зсув Y на висоту рядка
        y += line_height


#  розширений словник для демонстрації багаторядкового результату
transition_table = {
    "start": {
        "question": "Чи відчуваєте загальну слабкість\nабо недомагання?",
        "yes": "fever_check",
        "no": "healthy"
    },
    "healthy": {
        "result": "Ваш стан хороший.\nПродовжуйте слідкувати за здоров'ям!"
    },
    "fever_check": {
        "question": "Чи є підвищена температура?",
        "yes": "temp_high",
        "no": "temp_normal"
    },
    "temp_high": {
        "question": "Чи є сухий кашель?",
        "yes": "covid_check",
        "no": "flu_check"
    },
    "covid_check": {
        "question": "Чи є проблеми з диханням?",
        "yes": "covid_warning",
        "no": "covid_possible"
    },
    "covid_warning": {
        "result": "Схоже на важкий перебіг COVID-19.\nНегайно зверніться до лікаря!"
    },
    "covid_possible": {
        "result": "Можливо, у вас легка форма COVID-19.\nРекомендується тестування та самоізоляція."
    },
    "flu_check": {
        "question": "Чи супроводжується температура болями в тілі?",
        "yes": "flu",
        "no": "other_infection_high_temp"
    },
    "flu": {
        "result": "Можливо, у вас грип.\nЗверніться до лікаря та відпочиньте."
    },
    "other_infection_high_temp": {
        "result": "Симптоми не типові для грипу.\nЗверніться до лікаря для уточнення діагнозу."
    },
    "temp_normal": {
        "question": "Чи є нежить або біль у горлі?",
        "yes": "cold",
        "no": "mild_infection"
    },
    "cold": {
        "result": "Можливо, у вас звичайна простуда.\nРекомендується відпочинок і вживання рідини."
    },
    "mild_infection": {
        "result": "Симптоми слабкі.\nСпостерігайте за станом або зверніться до лікаря, якщо погіршиться."
    }
}

# Кнопки "Так" та "Ні"
button_width, button_height = 150, 50
button_yes_rect = pygame.Rect((WIDTH // 4 - button_width // 2, HEIGHT - 100), (button_width, button_height))
button_no_rect = pygame.Rect(((WIDTH * 3) // 4 - button_width // 2, HEIGHT - 100), (button_width, button_height))

# Поточний вузол
current_node = "start"

running = True
while running:
    screen.fill(WHITE)

    node_data = transition_table[current_node]

    # Якщо є ключ "result", це фінальний результат
    if "result" in node_data:
        result_text = node_data["result"]
        # Відображаємо багаторядковий текст у середині екрана
        result_rect = pygame.Rect(0, 0, WIDTH, HEIGHT // 2)
        result_rect.center = (WIDTH // 2, HEIGHT // 2)
        draw_multiline_text(result_text, FONT, BLACK, screen, result_rect, align_center=True)

        # Інструкція для виходу
        exit_rect = pygame.Rect(0, HEIGHT - 70, WIDTH, 50)
        draw_multiline_text(
            "Натисніть [ESC] або закрийте вікно для виходу",
            pygame.font.SysFont("Arial", 20),
            GRAY,
            screen,
            exit_rect
        )
    else:
        question_text = node_data["question"]

        # Відображаємо багаторядковий текст питання
        question_rect = pygame.Rect(0, 0, WIDTH, HEIGHT // 2)
        question_rect.center = (WIDTH // 2, HEIGHT // 2 - 50)
        draw_multiline_text(question_text, FONT, BLACK, screen, question_rect, align_center=True)

        # Кнопка "Так"
        pygame.draw.rect(screen, GRAY, button_yes_rect)
        draw_multiline_text("Так", FONT, BLACK, screen, button_yes_rect)

        # Кнопка "Ні"
        pygame.draw.rect(screen, GRAY, button_no_rect)
        draw_multiline_text("Ні", FONT, BLACK, screen, button_no_rect)

    # Обробка подій
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
                pygame.quit()
                sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_pos = pygame.mouse.get_pos()
            # Якщо це не фінальний вузол
            if "result" not in node_data:
                if button_yes_rect.collidepoint(mouse_pos):
                    # Переходимо за "yes"
                    if "yes" in node_data:
                        current_node = node_data["yes"]
                elif button_no_rect.collidepoint(mouse_pos):
                    # Переходимо за "no"
                    if "no" in node_data:
                        current_node = node_data["no"]

    pygame.display.flip()
