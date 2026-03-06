import pygame
import sys
import random

#ביקשתי מהצאט לשלוח לי תבנית מוכנה לpygame
# ויכתוב לי איפה לרשום את הפונקציות של הלוגיקה של המשחק בעצמי

# --- הגדרות בסיסיות (כבר מוכן) ---
pygame.init()
WIDTH, HEIGHT = 600, 800
BOARD_OFFSET_Y = 100
BOARD_SIZE = 600
LINE_WIDTH = 15
BG_COLOR = (28, 170, 156)
LINE_COLOR = (23, 145, 135)
WHITE = (239, 231, 200)
DARK_GREY = (66, 66, 66)
RED = (200, 0, 0)
BUTTON_COLOR = (20, 120, 110)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe - Challenge Mode")

# פונטים
font_btn = pygame.font.SysFont("Arial", 30, bold=True)
font_turn = pygame.font.SysFont("Arial", 40, bold=True)
font_menu = pygame.font.SysFont("Arial", 50, bold=True)

# --- נתוני המשחק ---
board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
current_player = "X"
game_over = False
game_mode = None  # 'pvp' או 'pvc'

# כפתורים לתפריט
pvp_button_rect = pygame.Rect(150, 300, 300, 80)
pvc_button_rect = pygame.Rect(150, 450, 300, 80)


# כאן צריך להגדיר את המלבן של כפתור הריסטארט (restart_button_rect)

# --- פונקציות עזר גרפיות (כבר מוכן) ---
def draw_lines():
    screen.fill(BG_COLOR)
    pygame.draw.line(screen, LINE_COLOR, (0, BOARD_OFFSET_Y + 200), (600, BOARD_OFFSET_Y + 200), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (0, BOARD_OFFSET_Y + 400), (600, BOARD_OFFSET_Y + 400), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (200, BOARD_OFFSET_Y), (200, BOARD_OFFSET_Y + 600), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (400, BOARD_OFFSET_Y), (400, BOARD_OFFSET_Y + 600), LINE_WIDTH)


def draw_figures():
    for row in range(3):
        for col in range(3):
            idx = row * 3 + col
            center_x, center_y = col * 200 + 100, row * 200 + 100 + BOARD_OFFSET_Y
            if board[idx] == "O":
                pygame.draw.circle(screen, WHITE, (center_x, center_y), 60, 15)
            elif board[idx] == "X":
                pygame.draw.line(screen, DARK_GREY, (center_x - 55, center_y - 55), (center_x + 55, center_y + 55), 25)
                pygame.draw.line(screen, DARK_GREY, (center_x + 55, center_y - 55), (center_x - 55, center_y + 55), 25)


def draw_menu():
    screen.fill(BG_COLOR)
    title = font_menu.render("TIC TAC TOE", True, WHITE)
    screen.blit(title, (WIDTH // 2 - title.get_width() // 2, 150))
    pygame.draw.rect(screen, BUTTON_COLOR, pvp_button_rect, border_radius=15)
    pygame.draw.rect(screen, BUTTON_COLOR, pvc_button_rect, border_radius=15)
    # כאן צריך לצייר את הטקסט על הכפתורים


# --- פונקציות לוגיות להשלמה ---

def check_winner():
    # כאן צריך להוסיף את הלוגיקה שבודקת ניצחון לפי השילובים (win_combos)
    # הפונקציה צריכה להחזיר True אם מישהו ניצח ולעדכן מי המנצח
    return False


def restart_game():
    # כאן צריך לאפס את כל המשתנים (הלוח, השחקן הנוכחי, המנצח וכו')
    pass


def computer_move():
    # כאן צריך להוסיף לוגיקה שהמחשב בוחר משבצת פנויה מהרשימה board
    # טיפ: השתמש ב-random.choice
    pass


# --- לולאה ראשית ---
clock = pygame.time.Clock()

while True:
    if game_mode is None:
        draw_menu()
    else:
        draw_lines()
        draw_figures()

        # כאן צריך לצייר את לוח התוצאות ואת כפתור הריסטארט

        # הצגת מצב (תור של מי עכשיו)
        status = f"Turn: {current_player}" if not game_over else "Game Over!"
        txt = font_turn.render(status, True, WHITE)
        screen.blit(txt, (WIDTH // 2 - txt.get_width() // 2, 25))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = event.pos

            # לחיצה בתפריט
            if game_mode is None:
                if pvp_button_rect.collidepoint(pos):
                    game_mode = 'pvp'
                elif pvc_button_rect.collidepoint(pos):
                    game_mode = 'pvc'

            # לחיצה בזמן משחק
            else:
                # כאן צריך לבדוק אם לחצו על כפתור הריסטארט

                # לחיצה על משבצת בלוח
                if not game_over and BOARD_OFFSET_Y <= pos[1] < BOARD_OFFSET_Y + BOARD_SIZE:
                    row = (pos[1] - BOARD_OFFSET_Y) // 200
                    col = pos[0] // 200
                    idx = row * 3 + col

                    if board[idx] not in ["X", "O"]:
                        board[idx] = current_player
                        # כאן צריך לבדוק אם המהלך הזה הוביל לניצחון או תיקו
                        # ואז להחליף שחקן
                        current_player = "O" if current_player == "X" else "X"

    # כאן צריך להוסיף את התור של המחשב (אם game_mode הוא 'pvc')

    pygame.display.update()
    clock.tick(60)