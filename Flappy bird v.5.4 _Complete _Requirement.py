import pygame
import random
import time

#สี RGB
black = (0,0,0)
white = (255,255,255)
bluu = (0,80,255)
navy = (61,79,206)
navy_bright = (61,79,255)
green = (0,255,100)
green_bright = (0,200,0)
w_grey = (240,240,240)
grey = (128,128,128)
grey_bright = (179,179,179)
fade = (84,98,48)
fate = (95,66,84)
pygame.init()


#ขนาดหน้าต่างเกม
display_x = 1000
display_y = 800
screen = pygame.display.set_mode((display_x,display_y))
pygame.display.set_caption("Flappy bird")#ตั้้งชื่อตรงหัวหน้าต่างเกม

#เพิ่มเสียง
hit_sound = pygame.mixer.Sound("sfx_hit.wav")
score_sound = pygame.mixer.Sound("sfx_point.wav")
wing_sound = pygame.mixer.Sound("sfx_wing.wav")
#music_1 = pygame.mixer.music.load("FreeBird.mp3")
#music_2 = pygame.mixer.music.load("Underclocked.mp3")

#หน้าต่างเมนูก่อนเข้าเกม
def start_menu():
    pygame.mixer.music.load("Underclocked.mp3") #เพิ่มเพลงเข้ามาในเกม แต่ยังไม่เล่น
    pygame.mixer.music.play(-1) #เล่นเพลง :argument(-1 คือเล่นวนไป,0 เและ 1 คือ 1ครั้ง แต่ 2 จะเล่น 3 ครั้ง เป็นอย่างงี้เรื่อยๆไป)
    volume = pygame.mixer.music.get_volume() #call method ให้บอกระดับเสียงค่าจะออกมาตั้ง 0 ถึง 1.0 เป็นทศนิยม
    volume_status = True #~ヾ(・ω・)
    #print(volume)
    pygame.mixer.music.set_volume(0.3) #call method for set volume DO YOU UNDERSTAND? ☉_☉!? (ค่าที่ set ได้ตั้งแต่ 0.0 ถึง 1.0 นะจ๊ะ)
    b_move = 0 #สำหรับภาพพื้นหลัง
    menu = True 
    while menu: #ถ้าเป็นจริงให้ทำไปเรื่อยๆนะจ๊ะ
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            
            if event.type == pygame.KEYDOWN and event.key == pygame.K_m and volume_status is False:#กดลงที่ตัว m ไม่ใหญ่นะครับ ಠ◡ಠ (กรณีกดเพื่อเปิดเสียง)
                pygame.mixer.music.set_volume(0.3) #call method for set volume DO YOU UNDERSTAND? ☉_☉!?
                volume_status = True#~ヾ(・ω・)
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_m: #กรณีกดปิดเสียง
                pygame.mixer.music.set_volume(0) #call method for set volume DO YOU UNDERSTAND? ☉_☉!?
                volume_status = False#~ヾ(・ω・)

        mouse = pygame.mouse.get_pos() #จับตำแหน่งเมาส์
        #print(mouse)
        screen.fill(white) #เติมสีทั้งหมด แบบถังสีในโปรแกรม Painting อะ DO YOU UNDERSTAND? ☉_☉!?
        ### ทำให้พื้นหลังขยับอย่างช้ากับเพลงอันสุดจะไพเราะ (`•ω•´๑)
        rel_x = b_move % background.get_rect().width #mod เพื่ออะไร คนทำยังงงเลยฮะ Study yourself mamannnnn
        screen.blit(background,(rel_x - background.get_rect().width,0))
        if rel_x < display_x: #ถ้าภาพพื้นหลังจะใกล้หลุดเฟรมให้เรียกภาพขึ้นมาต่อท้าย (ﾟдﾟ；)!! NANI  (・｀ω´・)OMAE WA MOU SHINDEIRU 
            screen.blit(background,(rel_x,0))
        b_move -= 0.1 #8;k,gi๕ซษฒฌณ(กว่าจะเปลี่ยนได้)ความเร็วภาพพื้นหลัง
        #print(rel_x)
        ###
        screen.blit(Title,(display_x*0.17,display_y/4)) #อันนี้โลโก้ชื่อเกม เอ้อลืมให้เครดิตเลย เดี๋ยวไปเพิ่มแปป
        
        message_out(24,"Press m to on/off music.",black,0,0) #call function message_out ทำไมต้องมีตัว c ด้วยวะ ชั่งมันเถอะครับ
                   #(ขนาดฟอนท์,"ข้อความ",สี,ตำแหน่ง X,ตำแหน่ง Y)
        
        ######call function button ขอขอบคุณแแชแนล sentdex ภิมถูคปร่าวว่ะ สอนทำฟังก์ชั่น button ข้าน้อยขอคารวะ#########
        #button("ข้อความ",ตำแหน่ง x,ตำแหน่ง y,width,height,สี,สีสว่าง,"อันท้ายไม่ใช่ข้อความนะครับเป็นประมาณว่าเป็นตัวรับว่าจะactionอะไร")
        button("",278,395,100,80,w_grey,w_grey,"play")
        button("",678,395,100,80,w_grey,w_grey,"quit")
        button("Start",282,400,90,70,grey,grey_bright,"play")
        button("Quit",682,400,90,70,grey,grey_bright,"quit")
        pygame.display.update() #อันนี้ทำงานคล้ายๆกับ pygame.display.update()

#ฟังก์ชั่นหน้าต่างสรุปคะแนน เมื่อตาย     
def screen_score(point,text,size_text):
    volume = pygame.mixer.music.get_volume() #ลืมหรือยัง กลับไปดูนะขี้เกียจพิมพ์ user:อ้าวแล้วไมไม่ก็อปวาง me:(｡☉౪ ⊙｡) ไม่รู้จักครับ Ctrl+c Ctrl+v ไม่รู้จักครับ
    pygame.mixer.music.stop() #stop music DO YOU UNDERSTAND? ☉_☉!? user:เนี่ยเรียก Ctrl+c Ctrl+v me:ม่ายอันที่ คลิ๊กขวา copy คลิ๊กขวา paste
    menu = True
    while menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_m and volume == 0:
                pygame.mixer.music.set_volume(0.3)
                volume = 1
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_m:
                pygame.mixer.music.set_volume(0)
                volume = 0

        pygame.draw.rect(screen,green,[(display_x/2)-130,180,300,400]) #วาด(ที่ไหน\\มันก็ต้องหน้าจอป่าววะ,สี,x,y,wid,height)
        pygame.draw.rect(screen,white,[(display_x/2)-125,185,290,390]) #วาดซ้อนเพื่อความหล่อครับ user: สวย!!! me:พ่ามพ้าม
        ###
        message_out(42,"Score : %d" % point,black,(display_x/2-20)-70,210)#เข้าใจยัง?
        ###
        message_out(size_text,text,black,(display_x/2)-90,280)
        button("",(display_x/2)-90,350,223,50,green_bright,green,"again")
        ###
        message_out(25,"Try again?",black,(display_x/2-160)+(223/2),(350-42)+(200/4))
        button("",(display_x/2)-90,425,223,50,green_bright,green,"menu")
        ###
        message_out(25,"Main menu",black,(display_x/2-160)+(223/2),(350-15)+(200/2))
        pygame.display.update()

#ฟังก์ชั้นหน้าต่างเลือกระดับความยาก
def screen_difficult():
    mouse = pygame.mouse.get_pos() 
    volume = pygame.mixer.music.get_volume()
    pygame.mixer.music.set_volume(0.3)
    b_move = 0
    menu = True
    while menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_m and volume == 0:
                pygame.mixer.music.set_volume(0.3)
                volume = 1
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_m:
                pygame.mixer.music.set_volume(0)
                volume = 0

            mouse = pygame.mouse.get_pos()
            #print(mouse)
        ###
        screen.fill(white)
        ###
        rel_x = b_move % background.get_rect().width
        screen.blit(background,(rel_x - background.get_rect().width,0))
        if rel_x < display_x:
            screen.blit(background,(rel_x,0))
        b_move -= 0.1
        screen.blit(Title,(display_x*0.17,display_y/4))
        ###
        message_out(24,"Press m to on/off music.",black,0,0)
        ###
        button("",228-50,505,100,80,w_grey,w_grey,"Easy")
        button("Easy",232-50,510,90,70,grey,grey_bright,"Easy")
        if 232+90 > mouse[0] > 232 and 510+70 > mouse[1] > 510: #setว่าถ้าตำแหน่งเมาส์อยู่ในบริเวณนี้จะ...........
            message_out(20,"Very Easy.",black,display_x/2-70,360)
        ###
        button("",408,505,140,80,w_grey,w_grey,"normal")
        button("",412,510,130,70,grey,grey_bright,"normal")
        message_out(28,"Normal",black,display_x/2-70,530)
        if 412+130 > mouse[0] > 412 and 510+70 > mouse[1] > 510:#setว่าถ้าตำแหน่งเมาส์อยู่ในบริเวณนี้จะ...........
            message_out(20,"Faster than easy mode a little bit.",black,300,360)
        ###
        button("",578+50,505,310,80,w_grey,w_grey,"hard")
        button("",582+50,510,300,70,grey,grey_bright,"hard")
        message_out(28,"Lynyrd Skynyrd",black,display_x/2+155,530)
        if 632+300 > mouse[0] > 632 and 510+70 > mouse[1] > 510:#setว่าถ้าตำแหน่งเมาส์อยู่ในบริเวณนี้จะ...........
            message_out(20,"All you have to do is play until music ends.(10 minutes)",black,190,360)
            message_out(20,"Lynyrd Skynyrd is an American rock band for popularizing during the 1970s.",black,70,420)
            message_out(20,"This mode will use ''Free bird(8 Bit)'' song by Lynyrd Skynyrd.",black,160,390)
        ###
        pygame.display.update()
        
#เพิ่มรูปตรงนี้ เรียกมาเฉยๆยังไม่เอาไปโชว
bird_img = pygame.image.load('bird.png') #
background = pygame.image.load("background.jpg").convert()
Title = pygame.image.load("FlappyBird_title.png")
pipe_1 = pygame.image.load("pip_1.png")
pipe_2 = pygame.image.load("pip_2.png")
#ฟังก์ชั่นปุ่ม 
def button(text,x,y,w,h,color,color_bright,dosomething=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed() #action การคลิ๊กเมาส์
    
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(screen,color_bright,(x,y,w,h)) #if mouse is stay around this position จะเกิดactionสีสว่างขึ้น
        if click[0] == 1 and dosomething != None: #if click mouse around this position and *******dosomething******** มีการรับคำสังมา != None คือถ้า dosomething ไม่ว่างเปล่า
            if dosomething == "play":#ส่งคำว่า"play"มา ลองกลับไปดูข้างบนอีกรอบ
                screen_difficult()   #จึงcall function นี้
            elif dosomething == "quit":                     #DO YOU UNDERSTAND? ☉_☉!?
                pygame.quit()                                 #DO YOU UNDERSTAND? ☉_☉!?
                quit()                                         #DO YOU UNDERSTAND? ☉_☉!?
            elif dosomething == "Easy":                         #DO YOU UNDERSTAND? ☉_☉!?
                pygame.mixer.music.stop()                        #DO YOU UNDERSTAND? ☉_☉!?
                regame(4,170)                                     #DO YOU UNDERSTAND? ☉_☉!?
            elif dosomething == "normal":                          #DO YOU UNDERSTAND? ☉_☉!?
                pygame.mixer.music.stop()                           #DO YOU UNDERSTAND? ☉_☉!?
                regame(4,135)                                     #DO YOU UNDERSTAND? ☉_☉!?
            elif dosomething == "hard":                             #DO YOU UNDERSTAND? ☉_☉!?
                pygame.mixer.music.load("FreeBird.mp3")            #DO YOU UNDERSTAND? ☉_☉!?
                pygame.mixer.music.play(1)                        #DO YOU UNDERSTAND? ☉_☉!?
                regame(5,120)                                    #DO YOU UNDERSTAND? ☉_☉!?
            elif dosomething == "again":                        #DO YOU UNDERSTAND? ☉_☉!?
                screen_difficult()                             #DO YOU UNDERSTAND? ☉_☉!?
            elif dosomething == "menu":                       #DO YOU UNDERSTAND? ☉_☉!?
                start_menu()                                 #DO YOU UNDERSTAND? ☉_☉!?
                
    else:
        pygame.draw.rect(screen,color,(x,y,w,h)) #แล้วถ้าเมาส์ไม่ได้อยู่บริเวณนี้ ก็สร้างธรรมดา ไม่มีอะไร

    Text_onBlock = pygame.font.SysFont('couriernew',28) #set (font,size_font)
    textOn,text_pos = add_text(text,Text_onBlock,black) #call function ****add_text("ข้อความ",ฟอนต์,สี)***พึ่งรู้ว่าฟอนต์พิมพ์ ต์ พึ่งgoogle เมื่อกี้เลย
    text_pos = (((x-38)+(w/2)), ((y-15)+(h/2))) #set position
    screen.blit(textOn,text_pos) #ทำการแสดง เหมือน print()แหละ

#ฟังก์ชั่นเรียกนกออกหน้าจอ
def bird(x,y):
    screen.blit(bird_img,(x,y))
#ฟังก์ชั่นสร้างอุปสรรค
def tube_1(x_outscreen_1,y_outscreen,x_wid,y_long_1,waytopass):
    pygame.draw.rect(screen,fade,[x_outscreen_1,y_outscreen,x_wid,y_long_1]) #ท่ออันบนไม่ปัญหาอะไร
    pygame.draw.rect(screen,fate,[x_outscreen_1,int(y_long_1+waytopass),x_wid,y_long_1+1000]) #ปัญหาอยู่ตรงนี้ หลักการคือต้องset ตำแหน่ง y ให้เท่ากับความยาวท่ออันบนบวกกับ waytopass เพื่อเว้นช่องว่างไว้เป็นทางผ่าน
    screen.blit(pipe_1,(x_outscreen_1,y_long_1-1201))                                                                                   #บวก1000 เพราะ y_long เป็นค่า random ตลอด ถ้ามันrandomได้ต่ำกว่า500 ท่อจะยาวไม่พอ นึกภาพไม่ออกลองไม่บวก1000ดู
    screen.blit(pipe_2,(x_outscreen_1,y_long_1+waytopass))

def tube_2(x_outscreen_2,y_outscreen,x_wid,y_long_2,waytopass):
    pygame.draw.rect(screen,fade,[x_outscreen_2,y_outscreen,x_wid,y_long_2]) #ท่ออันบนไม่ปัญหาอะไร
    pygame.draw.rect(screen,fate,[x_outscreen_2,int(y_long_2+waytopass),x_wid,y_long_2+1000]) #ปัญหาอยู่ตรงนี้ หลักการคือต้องset ตำแหน่ง y ให้เท่ากับความยาวท่ออันบนบวกกับ waytopass เพื่อเว้นช่องว่างไว้เป็นทางผ่าน
    screen.blit(pipe_1,(x_outscreen_2,y_long_2-1201))                                                                                   #บวก1000 เพราะ y_long เป็นค่า random ตลอด ถ้ามันrandomได้ต่ำกว่า500 ท่อจะยาวไม่พอ นึกภาพไม่ออกลองไม่บวก1000ดู
    screen.blit(pipe_2,(x_outscreen_2,y_long_2+waytopass))

def tube_3(x_outscreen_3,y_outscreen,x_wid,y_long_3,waytopass):
    pygame.draw.rect(screen,fade,[x_outscreen_3,y_outscreen,x_wid,y_long_3]) #ท่ออันบนไม่ปัญหาอะไร
    pygame.draw.rect(screen,fate,[x_outscreen_3,int(y_long_3+waytopass),x_wid,y_long_3+1000]) #ปัญหาอยู่ตรงนี้ หลักการคือต้องset ตำแหน่ง y ให้เท่ากับความยาวท่ออันบนบวกกับ waytopass เพื่อเว้นช่องว่างไว้เป็นทางผ่าน
    screen.blit(pipe_1,(x_outscreen_3,y_long_3-1201))                                                                                   #บวก1000 เพราะ y_long เป็นค่า random ตลอด ถ้ามันrandomได้ต่ำกว่า500 ท่อจะยาวไม่พอ นึกภาพไม่ออกลองไม่บวก1000ดู
    screen.blit(pipe_2,(x_outscreen_3,y_long_3+waytopass))
#ฟังก์ชั่นนับคะแนน
def score(text,point,x,y,font,size_font,color):
    font = pygame.font.SysFont(None,60)
    Score_onscreen = font.render(text+str(point),True,white)
    screen.blit(Score_onscreen,[x,y])
#ฟังก์ชั่นเพิ่มข้อความ
def add_text(text_add,font,color): #ต่อจากข่้างบนเมื่อกี้ เอาค่าที่ส่งมาrender
    text_added = font.render(text_add,True,color)
    return text_added, text_added.get_rect() #ส่งกลับ
#ฟังก์ชั่นแสดงข้อความ
def message_out(size_letter,text_add,color,text_posx,text_posy):#(ขนาดฟอนท์,"ข้อความ",สี,ตำแหน่ง X,ตำแหน่ง Y)
    font = pygame.font.SysFont('couriernew',size_letter)
    textOn,text_pos = add_text(text_add,font,color)
    text_pos = [text_posx,text_posy]
    screen.blit(textOn,text_pos)
#ฟังก์ชั่นสมน้ำหน้าไปเล่นใหม่
def died(point):
    pygame.mixer.Sound.play(hit_sound)
    screen_score(point,"Game over",42)
    

count = 0
#ความกว้างของอุปสรรค
x_wid = 90

#ฟงัก์ชั่นบิน
def flap():
    pygame.mixer.Sound.set_volume(wing_sound,0.1)
    pygame.mixer.Sound.play(wing_sound)
    return 7 #ส่งค่าไปว่ากระโดดสูงแค่ไหน
def reduce_life():
    life -= 1
    

#ตัวเกมหลัก รับค่า 2 ค่า คือความเร็วอุปสรรค กับ ความยาว y ช่องว่าง
def regame(speed_tube,waytopass):
    
    die = False
    clock = pygame.time.Clock()
    x = 300
    y = 400
    bird_y = 0.3
    dY = 8
    #อุปสรรคออกมาตำแหน่งไหน ไม่ใช่ประโยคคำถามนะจ๊ะ
    x_outscreen = 1200
    x_outscreen_1 = 1100
    x_outscreen_2 = 1600
    x_outscreen_3 = 2100
    
    y_outscreen = 0
    y_long_1 = random.randrange(250,550) #method randomค่า250 ถึง 550
    y_long_2 = random.randrange(250,550) #User: แล้วทำไมไม่เซตไว้ที่ 0 ถึง 800 อะ Me:งั้นลองเซตดู แล้วไปลองเล่นเอา
    y_long_3 = random.randrange(250,550)
    point = 0
    #backgound
    b_move = 0
    #พลังชีวิด
    life = 3
    life_before = 0
    life_after = 0

    while not die:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                die = True
            if event.type == pygame.KEYDOWN: #กด spacebar จะขยับขึ้น
                if event.key == pygame.K_SPACE:
                    dY = flap()

        #Algorithm Smooth Gravity and Smooth Flapping คนทำยังไม่เข้าใจเลยครับ ไปอ่านมาแล้วลองทำดู ประกอบดูของเพื่อนกลุ่มอื่น ได้เฉย ตอนนั้นยังรู้สึกงงอยู่เลย ทำได้ไงวะ แต่ก็ดีใจมากกกกนั่งคิด ค้นคว้าเป็นหลายชั่วโมงกว่าจะได้
        #dy เปรียบเสมือนค่า g แรงโน่มถ่วง เพราะงั้นความเร็วการตกของนกจะเพิ่มเร็วขึ้นตามค่า g จึงเอาไปค่า bird_y ด้วย 0.2 เรื่อย เพื่อสร้างความเร็วในการตกเร็วมากขึ้น
        #ในกรณีที่เราไม่กดflap ค่าขอ y จะลบด้วย dyที่มากขึ้นไป ตัวอย่าง สมมติ 1 วินาทีผ่าน dy = 5 , y = 400-dy = 395(ขยับขึ้น) วินาทีที่ 2 dy = 4.8 , y = 390.2 (ยังขึ้นอยู่แต่ความช้าลง) ไปเรื่อยๆจน
        #dy = 0 ตากหลักฟิสิกส์การเคลื่อนที่ในแนวดิ่งเมื่อวัตถุหยุดที่จุดสูงสุดความเร็วจะเป็น 0 dy จะเริ่มติดลบ ตัวอย่าง dy = -1 ,y = 500 - (-1) ลบลบ เป็น + y = 501 (เคลื่อนที่ลงและเร็วขึ้นเรื่อยๆ) ประมาณนี้
        #เอาเป็นว่าลอง printออกมาดูก่อนก็ได้
        #print(dY)
        #print(y)
        #ส่วนฟังก์ชั่น flap() return 6 มาให้ dy เพราะว่า dy จะโดนลบไปเรื่อยๆ เพราะงั้นเราจึงเซตมันให้เท่ากับ 6 ใหม่ เพื่อให้นกขยับขึ้น
        dY -= bird_y
        y -= dY

        screen.fill(white)

        rel_x = b_move % background.get_rect().width
        screen.blit(background,(rel_x - background.get_rect().width,0))
        if rel_x < display_x:
            screen.blit(background,(rel_x,0))
        b_move -= 1
        

        tube_1(x_outscreen_1,y_outscreen,x_wid,y_long_1,waytopass)
        tube_2(x_outscreen_2,y_outscreen,x_wid,y_long_2,waytopass)
        tube_3(x_outscreen_3,y_outscreen,x_wid,y_long_3,waytopass)
        
        bird(x,y)
        #เงื่อนไขนับคะแนน
        #ค่าที่ตั้งต้องหารด้วยค่า speed_tube ลงตัว เท่านั้น!!!!!!!! ไม่งั้นมันไม่นับคะแนน
        #speed_tube ปัจจุบัน = 4
        if x_outscreen_1 == 200: #ตำแหน่ง x ของนก ลบด้วย x_wid(ไม่เป๊ะนะจ๊ะ)
            pygame.mixer.Sound.play(score_sound)
            point +=1
        if x_outscreen_2 == 200: #ตำแหน่ง x ของนก ลบด้วย x_wid(ไม่เป๊ะนะจ๊ะ)
            pygame.mixer.Sound.play(score_sound)
            point +=1
        if x_outscreen_3 == 200: #ตำแหน่ง x ของนก ลบด้วย x_wid(ไม่เป๊ะนะจ๊ะ)
            pygame.mixer.Sound.play(score_sound)
            point +=1


        wid_bird = bird_img.get_rect().height
        height_bird = bird_img.get_rect().width
        #print(wid_bird)

        score("",point,500,200,None,60,white)
        score("LIFE : ",life,0,0,None,48,black)
        speed = speed_tube

        y += bird_y # + เพราะ +y เพิ่มขึ้นตามแนวแกน
        x_outscreen_1 -= speed # - เพราะอุปสรรคเคลื่อนที่ตามแนวแกน X
        x_outscreen_2 -= speed
        x_outscreen_3 -= speed

        #ถ้าอุปสรรคผ่านแล้วออกไปจากหน้าต่างให้สร้างอุปสรรคมาใหม่
        if x_outscreen_1 < - 400: #70 ===> x_wid
            x_outscreen_1 = 1100
            y_long_1 = random.randrange(0,600) #สุ่มตัวเลข (เริ่ม,ถึงไหนก็ว่าไป)
        if x_outscreen_2 < - 400: #70 ===> x_wid
            x_outscreen_2 = 1100
            y_long_2 = random.randrange(0,600)
        if x_outscreen_3 < - 400: #70 ===> x_wid
            x_outscreen_3 = 1100
            y_long_3 = random.randrange(0,600)

        
        #ตกพื้นตาย 
        if y > display_y-52:
            bird_y = 0
            speed_tube = 0
            died(point)
            break
    
        #ชนท่อบน
        if x+height_bird-1.5 > x_outscreen_1 and y <= y_long_1 and x < x_wid+x_outscreen_1:
            life_after -= 1 #ถ้านกชน ให้ลบไป แล้วเก็บค่าไว้ก่อน
        if x_outscreen_1 == 220 and life_after != 0:  #ถัดมาเอาค่า life_before มาเช็คว่าติดลบไหม ถ้าติดจะหักพลังชีวิตลง 1 
            life_after = 0
            life -= 1
            pygame.mixer.Sound.play(hit_sound)
            life_after = 0
    
        #ชนท่อล่าง
        if x+height_bird-1.5 > x_outscreen_1 and y >= y_long_1+waytopass-wid_bird and x < x_wid+x_outscreen_1:
            life_before -= 1
            
        if x_outscreen_1 == 220 and life_before < 0:
            life_before = 0
            life -= 1
            pygame.mixer.Sound.play(hit_sound)
############################
        #ชนท่อบน
        if x+height_bird-1.5 > x_outscreen_2 and y <= y_long_2 and x < x_wid+x_outscreen_2:
            life_after -= 1 #ถ้านกชน ให้ลบไป แล้วเก็บค่าไว้ก่อน
        if x_outscreen_2 == 220 and life_after != 0:  #ถัดมาเอาค่า life_before มาเช็คว่าติดลบไหม ถ้าติดจะหักพลังชีวิตลง 1 
            life_after = 0
            life -= 1
            pygame.mixer.Sound.play(hit_sound)
            life_after = 0
    
        #ชนท่อล่าง
        if x+height_bird-1.5 > x_outscreen_2 and y >= y_long_2+waytopass-wid_bird and x < x_wid+x_outscreen_2:
            life_before -= 1
            
        if x_outscreen_2 == 220 and life_before < 0:
            life_before = 0
            life -= 1
            pygame.mixer.Sound.play(hit_sound)
#############################
        #ชนท่อบน
        if x+height_bird-1.5 > x_outscreen_3 and y <= y_long_3 and x < x_wid+x_outscreen_3:
            life_after -= 1 #ถ้านกชน ให้ลบไป แล้วเก็บค่าไว้ก่อน
        if x_outscreen_3 == 220 and life_after != 0:  #ถัดมาเอาค่า life_before มาเช็คว่าติดลบไหม ถ้าติดจะหักพลังชีวิตลง 1 
            life_after = 0
            life -= 1
            pygame.mixer.Sound.play(hit_sound)
            life_after = 0
    
        #ชนท่อล่าง
        if x+height_bird-1.5 > x_outscreen_3 and y >= y_long_3+waytopass-wid_bird and x < x_wid+x_outscreen_3:
            life_before -= 1
            
        if x_outscreen_3 == 220 and life_before < 0:
            life_before = 0
            life -= 1
            pygame.mixer.Sound.play(hit_sound)
               
        if life < 0:#เช็คว่าพลังชีวิตเป็น -1 จะตาย
            bird_y = 0
            speed_tube = 0
            died(point)
            
        pos = pygame.mixer.music.get_pos() #method บอกว่าเพลงเล่นไปแล้วกี่***มิลลิวินาที***
        #ถ้าเล่นโหมด Lynyrd Skynyrd ผ่านจะขึ้น Congratulations แทน Game over
        if pos >= 614400: # ความยาวเพลง หน่วยมิลลิวินาที เพลง 10 นาที 21 วินาที
            screen_score(point,"Congratulations",26) 
        #print(pos)

            
        pygame.display.update()
        clock.tick(60)
    pygame.quit()
    quit()


start_menu()
regame()
pygame.quit()
quit()
        
S
