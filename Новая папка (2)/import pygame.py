import pygame
import sys

def space_wait():
    wait=True
    while wait:
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                wait = False 
                pygame.quit() 
                sys.exit()
        keys = pygame.key.get_pressed() 
        if keys[pygame.K_SPACE]: 
            wait = False 

pygame.init() 
screen = pygame.display.set_mode((1000, 650)) 
clock = pygame.time.Clock() 
running = True 
s_width=1000 
s_high=600 
b_main=True
b_tick=50

pygame.font.init() 
myfont = pygame.font.SysFont('Comic Sans MS', 30) 
screen.blit("background_pic.jpg",(0,0)) 
screen.blit("start_pic.jpg",(420,250))
pygame.display.flip() 
space_wait() 

while running:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            running = False 

ball = 0

screen.bgpic("уптпита.jpg")
print("Поздравляю! Вы прошли один из этапов своей жизни и перешли к следущему.Начало студенческой жизни, новые знакомства и новые приключения. Все шло отлично пока вы не поняли, что сможете поступить только в ПТПИТ.Ваша единственная цель закончить первый курс.Удачи..Всего у вас будет ... дней. По их окончаю вам вынесут вердикт, а какой вы узнаете в конце")
answer=input('Готовы начать? (Да/Нет).lower() == "да" :')
score=0
print("День 1")
print("Проснувшись с утра вы видите на часах время 8:10")
print("Что вы будете делать?")


print("1 Быстро собраться и поехать на первую пару")
print("2 С мыслью *Все равно не успею* не торопиться и ехать ко второй")
print("3 В принципе не такие и важные пары. Останусь дома")

playerChoise = input("Выбери 1, 2 or 3")
if playerChoise =="1":
  print("Вы немного опоздали, зато приехали на контрольную по математике и написали ее успешно")
  ball = ball + 3

elif playerChoise =="2":
  print("Вы немного опоздали, зато приехали на контрольную по математике и написали ее успешно")
  ball = ball + 2

elif playerChoise =="3":
  print("В принципе не такие и важные пары. Останусь дома")
  ball = ball + 0
  print("День окончен")

print("Начинается вторая пара - истории.Кажись сегодня нужно написать всего лишь конспект.Что вы предпочтете?")
print("1)Ну конспекты обычно не проверяют,посижу в телефоне")
print("2)*Всю ленту в ВК уже пролистала*,напишу хоть для приличия")
print("3)Всем кто пишет удачи, а я лучше посплю")

playerChoise = input("Выберите 1,2 или 3")
if playerChoise =="2":
  print("*Да я как знала* вы сдали тетрадь")
  ball = + 2

elif playerChoise =="3":
  print("Да твою ж...вы не стали сдавать тетрадь")
  ball = + 0
  
elif playerChoise =="1":
  print("Да твою ж...вы не стали сдавать тетрадь")
  ball = + 0

Print("День окончен")

b_tick=b_tick-1 
if b_tick==0: 
    b_tick=50 
    b_main = not b_main 

pygame.display.flip()
clock.tick(50) 
    
print("The game has closed") 
pygame.quit() 
sys.exit() 