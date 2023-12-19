import pygame as pg
import random
import sys

pg.init()

WIDTH, HEIGHT = 400, 600  #ゲームウィンドウの幅
screen = pg.display.set_mode((WIDTH, HEIGHT))  #ゲームウィンドウの高さ
pg.display.set_caption("車ゲーム")

WHITE = (255, 255, 255) #白
RED = (255, 0, 0)  #赤

player_width, player_height = 50, 50
player_x = WIDTH // 2 - player_width // 2
player_y = HEIGHT - player_height -20
player_speed = 10

obstacle_width, obstacle_height = 40, 40
obstacle_speed = 5

def draw_player(x, y):
    pg.draw.rect(screen, WHITE, [x, y, player_width, player_height])  #プレイヤーの車
def draw_obstacle(x, y):
    pg.draw.rect(screen, RED, [x, y, obstacle_width, obstacle_height])  #障害物
def game():
    clock = pg.time.Clock()

    obstacles = []
    score = 0  #スコア
    lives = 3  #プレイヤーのライフを設定
    gasoline = 100  #ガソリン
    global player_x
    font = pg.font.Font(None,36)  # フォントオブジェクトを作成

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
        keys = pg.key.get_pressed()
        player_x += (keys[pg.K_RIGHT] - keys[pg.K_LEFT]) * player_speed

        player_x = max(0, min(WIDTH - player_width, player_x))

        if keys[pg.K_RETURN]:
            gasoline -= 1
            if gasoline == 0:  #ガソリンが0になったら
                    print(f"Game Over! Score: {score}")
                    pg.quit()
                    sys.exit()

        if random.randint(1, 20) == 1:
            obstacle_x = random.randint(0, WIDTH - obstacle_width)
            obstacle_y = -obstacle_height
            obstacles.append([obstacle_x, obstacle_y])

        for obstacle in obstacles:
            obstacle[1] += obstacle_speed
            if(
                player_x < obstacle[0] + obstacle_width
                and player_x + player_width > obstacle[0]
                and player_y < obstacle[1] + obstacle_height
                and player_y + player_height > obstacle[1]
            ):
                if not keys[pg.K_RETURN]:
                    lives -= 1   #障害物に当たったらライフ -1
                    score -= 1  #障害物に当たったらスコア　-1
                if lives == 0 or score < 0:  #ライフが0になったらorスコアが0より小さくなったら
                    print(f"Game Over! Score: {score}")
                    pg.quit()
                    sys.exit()

        screen.fill((0, 0, 0))
        
        gasoline_text = font.render(f"gasoline{gasoline}",True,(255,255,255))
        lives_text = font.render(f"Lives: {lives}", True, (255, 255, 255))  # ライフの数を描画するテキストを作成
        screen.blit(gasoline_text, (30, 30))  # テキストを画面上に描画
        screen.blit(lives_text, (10, 10))  # テキストを画面上に描画

        draw_player(player_x, player_y)

        for obstacle in obstacles:
            draw_obstacle(obstacle[0], obstacle[1])

        score += 1

        pg.display.flip()
        clock.tick(30)

if __name__ == "__main__":
    game()
        
