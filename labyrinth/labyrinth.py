import pygame
import random
import sys

# -------------------------
# Налаштування
# -------------------------
# Розміри лабіринту (N x N)
N = 20

# Розмір клітинки (в пікселях)
CELL_SIZE = 30

# Час затримки (мс) між кроками пошуку - щоб бачити анімацію повільніше
SEARCH_DELAY = 30

# Кольори (R,G,B)
WHITE  = (255, 255, 255)
BLACK  = (0, 0, 0)
GRAY   = (100, 100, 100)
BLUE   = (0, 0, 255)
GREEN  = (0, 255, 0)
RED    = (255, 0, 0)
YELLOW = (255, 255, 0)


# -------------------------
# Клас клітинки
# -------------------------
class Cell:
    """
    Зберігає інформацію про стіни і чи відвідана клітинка.
    """
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.visited = False  # для генерації (DFS)
        # Стіни: True = є стіна, False = немає стіни
        # Спочатку всі стіни зачинені.
        self.walls = {
            'up': True,
            'down': True,
            'left': True,
            'right': True
        }

    def draw(self, screen):
        """
        Малює клітинку (її стіни).
        Сама клітинка заливається білим, стіни - чорні.
        """
        x = self.col * CELL_SIZE
        y = self.row * CELL_SIZE

        # Заливаємо тлом (білим)
        rect = pygame.Rect(x, y, CELL_SIZE, CELL_SIZE)
        pygame.draw.rect(screen, WHITE, rect)

        # Малюємо стіни
        # Верхня
        if self.walls['up']:
            pygame.draw.line(screen, BLACK, (x, y), (x + CELL_SIZE, y), 2)
        # Нижня
        if self.walls['down']:
            pygame.draw.line(screen, BLACK, (x, y + CELL_SIZE), (x + CELL_SIZE, y + CELL_SIZE), 2)
        # Ліва
        if self.walls['left']:
            pygame.draw.line(screen, BLACK, (x, y), (x, y + CELL_SIZE), 2)
        # Права
        if self.walls['right']:
            pygame.draw.line(screen, BLACK, (x + CELL_SIZE, y), (x + CELL_SIZE, y + CELL_SIZE), 2)


# -------------------------
# Ініціалізація Pygame
# -------------------------
pygame.init()
WIDTH = N * CELL_SIZE
HEIGHT = N * CELL_SIZE
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Генерація та пошук шляху в лабіринті")
clock = pygame.time.Clock()


# -------------------------
# Створення сітки клітин
# -------------------------
grid = []
for r in range(N):
    row_cells = []
    for c in range(N):
        row_cells.append(Cell(r, c))
    grid.append(row_cells)


# -------------------------
# Допоміжні функції
# -------------------------
def get_neighbors(r, c):
    """
    Повертає сусідні клітинки всередині границь лабіринту
    """
    neighbors = []
    if r > 0:      neighbors.append((r - 1, c))  # up
    if r < N - 1:  neighbors.append((r + 1, c))  # down
    if c > 0:      neighbors.append((r, c - 1))  # left
    if c < N - 1:  neighbors.append((r, c + 1))  # right
    return neighbors


def remove_walls(cell1, cell2):
    """
    Прибирає стіни між двома сусідніми клітинками.
    """
    r1, c1 = cell1.row, cell1.col
    r2, c2 = cell2.row, cell2.col

    if r1 == r2:  # однаковий ряд
        if c1 == c2 + 1:
            # cell1 правіше cell2 => прибираємо ліву стіну в cell1 і праву в cell2
            cell1.walls['left'] = False
            cell2.walls['right'] = False
        elif c1 + 1 == c2:
            # cell1 лівіше cell2
            cell1.walls['right'] = False
            cell2.walls['left'] = False

    elif c1 == c2:  # однаковий стовпець
        if r1 == r2 + 1:
            # cell1 нижче
            cell1.walls['up'] = False
            cell2.walls['down'] = False
        elif r1 + 1 == r2:
            # cell1 вище
            cell1.walls['down'] = False
            cell2.walls['up'] = False


def draw_grid():
    """
    Перемальовує весь лабіринт (усі клітинки).
    """
    screen.fill(GRAY)
    for r in range(N):
        for c in range(N):
            grid[r][c].draw(screen)


def highlight_cell(r, c, color):
    """
    Підсвічує одну клітинку заданим кольором.
    """
    x = c * CELL_SIZE
    y = r * CELL_SIZE
    rect = pygame.Rect(x+2, y+2, CELL_SIZE-4, CELL_SIZE-4)
    pygame.draw.rect(screen, color, rect)


# -------------------------
# 1. Генерація лабіринту (DFS)
# -------------------------
def generate_maze_dfs(r, c):
    stack = []
    current_cell = grid[r][c]
    current_cell.visited = True
    stack.append(current_cell)

    while stack:
        # 1) Беремо поточну клітинку (верхівка стека)
        current = stack[-1]
        r_cur, c_cur = current.row, current.col

        # 2) Визначимо всіх сусідів, які не відвідані
        unvisited_neighbors = []
        for (nr, nc) in get_neighbors(r_cur, c_cur):
            if not grid[nr][nc].visited:
                unvisited_neighbors.append(grid[nr][nc])

        if unvisited_neighbors:
            # Випадково обираємо одного невідвіданого сусіда
            chosen = random.choice(unvisited_neighbors)
            chosen.visited = True

            # Прибираємо стіни
            remove_walls(current, chosen)

            # Стаємо на цього сусіда і заносимо в стек
            stack.append(chosen)
        else:
            # Якщо всі сусіди відвідані, повертаємось назад
            stack.pop()

        # Відмалюємо поточний стан
        draw_grid()
        # Підсвітимо клітинку, де зараз "копаємо"
        highlight_cell(r_cur, c_cur, BLUE)
        pygame.display.update()
        clock.tick(60)  # регулюємо FPS


# -------------------------
# 2. Пошук шляху (BFS)
# -------------------------
def find_path_bfs(start_r, start_c, end_r, end_c):
    """
    Шукає шлях від (start_r, start_c) до (end_r, end_c) за допомогою BFS.
    Повертає список клітинок-шляху від старту до фінішу.
    Якщо шляху немає (теоретично не має статись у згенерованому лабіринті),
    повертає порожній список.
    """
    visited = [[False]*N for _ in range(N)]
    parent = dict()  # (r,c) -> (pr, pc)
    queue = []

    queue.append((start_r, start_c))
    visited[start_r][start_c] = True

    found = False

    while queue and not found:
        # Дістаємо з черги
        (cr, cc) = queue.pop(0)

        # Якщо це кінцева клітинка - виходимо
        if (cr, cc) == (end_r, end_c):
            found = True
            break

        # Додаємо в чергу сусідів, до яких можна перейти
        current_cell = grid[cr][cc]
        # Перевіримо сусідів, але з урахуванням стін
        # Вгору
        if not current_cell.walls['up'] and not visited[cr-1][cc]:
            visited[cr-1][cc] = True
            parent[(cr-1, cc)] = (cr, cc)
            queue.append((cr-1, cc))

        # Вниз
        if not current_cell.walls['down'] and not visited[cr+1][cc]:
            visited[cr+1][cc] = True
            parent[(cr+1, cc)] = (cr, cc)
            queue.append((cr+1, cc))

        # Вліво
        if not current_cell.walls['left'] and not visited[cr][cc-1]:
            visited[cr][cc-1] = True
            parent[(cr, cc-1)] = (cr, cc)
            queue.append((cr, cc-1))

        # Вправо
        if not current_cell.walls['right'] and not visited[cr][cc+1]:
            visited[cr][cc+1] = True
            parent[(cr, cc+1)] = (cr, cc)
            queue.append((cr, cc+1))

        # Відмалюємо поточний етап пошуку
        draw_grid()

        # Підсвітимо вже відвідані/оброблені (наприклад, червоним)
        for r_ in range(N):
            for c_ in range(N):
                if visited[r_][c_]:
                    highlight_cell(r_, c_, (255, 200, 200))  # світло-червоний

        # Підсвічуємо поточний вузол
        highlight_cell(cr, cc, RED)

        pygame.display.update()
        pygame.time.delay(SEARCH_DELAY)

    # Якщо знайшли шлях - відновимо його
    path = []
    if found:
        # "Підіймаємось" від кінця до початку за parent
        cur = (end_r, end_c)
        path.append(cur)
        while cur != (start_r, start_c):
            cur = parent[cur]
            path.append(cur)
        path.reverse()

    return path


def main():
    # 1) Згенерувати лабіринт (гарантує один шлях між будь-якими двома клітинками)
    generate_maze_dfs(0, 0)

    # Після генерації приберемо позначку visited для пошуку шляху (не обов'язково, але охайно)
    for r in range(N):
        for c in range(N):
            grid[r][c].visited = False

    # 2) Виконати пошук шляху та візуалізувати його
    start_r, start_c = 0, 0
    end_r, end_c = N-1, N-1
    path = find_path_bfs(start_r, start_c, end_r, end_c)

    # 3) Якщо шлях знайдений, підсвітити його іншим кольором
    if path:
        draw_grid()
        for (r, c) in path:
            highlight_cell(r, c, YELLOW)
            pygame.display.update()
            pygame.time.delay(10)

    # Залишимо вікно відкритим, поки користувач не закриє
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        pygame.display.update()
        clock.tick(30)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
