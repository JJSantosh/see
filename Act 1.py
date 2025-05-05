import pygame

def main():
    pygame.init()
    scw,sch=500,500
    screen=pygame.display.set_mode((500,500))
    pygame.display.set_caption("moving cube")

    c={"blue": pygame.Color("blue"),
       "pink": pygame.Color("pink"),
       "green": pygame.Color("green")
       }
    col=c["green"]
    x,y=30,30
    sw,sh=60,60
    clock=pygame.time.Clock()
    done=False

    while not done:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                done=True
        pressed=pygame.key.get_pressed()
        if pressed[pygame.K_LEFT]: x=x-5
        if pressed[pygame.K_RIGHT]: x=x+5
        if pressed[pygame.K_UP]: y=y-5
        if pressed[pygame.K_DOWN]: y=y+5

        x=min(max(0,x),scw-sw)
        y=min(max(0,y),sch-sh)
        if x==0: col=c["blue"]
        elif x==scw-sw: col=c["pink"]
        elif y==0: col=c["green"]

        screen.fill((0,0,0))
        pygame.draw.rect(screen,col,(x,y,sw,sh))
        pygame.display.flip()
        clock.tick(90)
    pygame.quit()

if __name__=="__main__":
    main()