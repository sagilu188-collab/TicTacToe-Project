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
player = ["X", "O"]
game_over = False
current_player = random.choice(player)
game_mode = None  # 'pvp' או 'pvc'
winning_combo = None
score_x = 0
score_o = 0
ties = 0

# כפתורים לתפריט
pvp_button_rect = pygame.Rect(150, 300, 300, 80)
pvc_button_rect = pygame.Rect(150, 450, 300, 80)


restart_button_rect = pygame.Rect(200, 730, 200, 50)

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

    pvp_text = font_btn.render("2 Players", True, WHITE)
    pvp_text_rect = pvp_text.get_rect(center=pvp_button_rect.center)
    screen.blit(pvp_text, pvp_text_rect)


    pvc_text = font_btn.render("Play vs Computer", True, WHITE)
    pvc_text_rect = pvc_text.get_rect(center=pvc_button_rect.center)
    screen.blit(pvc_text, pvc_text_rect)


def draw_winning_line():
    if winning_combo:
        # לוקחים את האינדקס הראשון (למשל 0) והאחרון (למשל 2) בשלישייה
        start_idx = winning_combo[0]
        end_idx = winning_combo[2]

        # חישוב מרכז המשבצת הראשונה
        start_pos = (start_idx % 3 * 200 + 100, start_idx // 3 * 200 + 100 + BOARD_OFFSET_Y)
        # חישוב מרכז המשבצת האחרונה
        end_pos = (end_idx % 3 * 200 + 100, end_idx // 3 * 200 + 100 + BOARD_OFFSET_Y)

        # ציור הקו האדום
        pygame.draw.line(screen, RED, start_pos, end_pos, 15)

# --- פונקציות לוגיות להשלמה ---

def check_winner():
    # כאן צריך להוסיף את הלוגיקה שבודקת ניצחון לפי השילובים (win_combos)
    # הפונקציה צריכה להחזיר True אם מישהו ניצח ולעדכן מי המנצח
    global game_over, winning_combo, score_x, score_o

    win_combos = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                  (0, 3, 6), (1, 4, 7), (2, 5, 8),
                  (0, 4, 8), (2, 4, 6)]

    for combo in win_combos:
        if board[combo[0]] == board[combo[1]] == board[combo[2]]:
            winning_combo = combo


            if board[combo[0]] == "X":
                score_x += 1
            else:
                score_o += 1

            return True

    return False



def restart_game():
    # כאן צריך לאפס את כל המשתנים (הלוח, השחקן הנוכחי, המנצח וכו')
    global board, game_over, current_player
    board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    current_player = random.choice(["X", "O"])
    game_over = False
    pass


def computer_move():
    # כאן צריך להוסיף לוגיקה שהמחשב בוחר משבצת פנויה מהרשימה board
    # טיפ: השתמש ב-random.choice
    available_moves = []
    for i in range(9):
        if board[i] not in ["X" , "O"]:
            available_moves.append(i)
    if available_moves:
        return random.choice(available_moves)

    return None


# --- לולאה ראשית ---
clock = pygame.time.Clock()

while True:
    if game_mode is None:
        draw_menu()
    else:
        draw_lines()
        draw_figures()
        if game_over and winning_combo:
            draw_winning_line()

        # כאן צריך לצייר את לוח התוצאות ואת כפתור הריסטארט
        score_text = font_btn.render(f"X: {score_x}  |  O: {score_o}  |  Ties: {ties}", True, DARK_GREY)
        screen.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, 685))
        pygame.draw.rect(screen, BUTTON_COLOR, restart_button_rect, border_radius=10)
        restart_text = font_btn.render("RESTART", True, WHITE)
        text_rect = restart_text.get_rect(center=restart_button_rect.center)
        screen.blit(restart_text, text_rect)

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
                if restart_button_rect.collidepoint(event.pos):
                    restart_game()

                # לחיצה על משבצת בלוח
                if not game_over and BOARD_OFFSET_Y <= pos[1] < BOARD_OFFSET_Y + BOARD_SIZE:
                    row = (pos[1] - BOARD_OFFSET_Y) // 200
                    col = pos[0] // 200
                    idx = row * 3 + col

                    if board[idx] not in ["X", "O"]:
                        board[idx] = current_player
                        # כאן צריך לבדוק אם המהלך הזה הוביל לניצחון או תיקו
                        if check_winner():
                            game_over = True
                            print(f"player {current_player} wins!")
                        elif all(cell in ["X", "O"] for cell in board):
                            game_over = True
                            print("It's a tie!")
                        # ואז להחליף שחקן
                        if not game_over:
                          current_player = "O" if current_player == "X" else "X"
        # כאן צריך להוסיף את התור של המחשב (אם game_mode הוא 'pvc')
        if game_mode == "pvc" and current_player == "O" and not game_over:

            draw_lines()
            draw_figures()
            score_txt = font_btn.render(f"X: {score_x}  |  O: {score_o}  |  Ties: {ties}", True, DARK_GREY)
            screen.blit(score_txt, (WIDTH // 2 - score_txt.get_width() // 2, 685))
            pygame.display.update()
            pygame.time.delay(500)

            move = computer_move()
            if move is not None:
                board[move] = "O"
                if check_winner():
                    game_over = True
                elif all(cell in ["X", "O"] for cell in board):
                    game_over = True

                if not game_over:
                    current_player = "X"





    pygame.display.update()
    clock.tick(60)