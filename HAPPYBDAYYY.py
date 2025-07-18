import pygame,time
pygame.init()

screen=pygame.display.set_mode((600,600))
pygame.display.set_caption("HAPPY BDAYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY")
font=pygame.font.SysFont("Rockwell",50)

while True:
    for i in pygame.event.get():
        if i.type==pygame.QUIT:
            exit()

    titlepage=pygame.image.load("balloon.jpg")
    screen.blit(titlepage,(0,0))
    texttitle=font.render("Happy birthdayy",True,(87,11,87))
    screen.blit(texttitle,(140,110))
    
    pygame.display.update()
    time.sleep(4)

    giftpage=pygame.image.load("gift.jpg")
    screen.blit(giftpage,(0,0))
    textgift=font.render("Ur so old hahaaa",True,(87,11,87))
    screen.blit(textgift,(150,60))
    
    pygame.display.update()
    time.sleep(4)

    finalpage=pygame.image.load("cake.jpg")
    screen.blit(finalpage,(0,0))
    textfinal=font.render("have a wonderful dayy",True,(87,11,87))
    screen.blit(textfinal,(150,70))
    
    pygame.display.update()
    time.sleep(4)


