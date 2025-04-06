import pygame as pg, random
def find(v, a):
    for i in range(len(v)):
        for j in range(len(v[i])):
            if(v[i][j]==a):
                return (i,j)
def findRect(v, a):
    for i in range(len(v)):
        for j in range(len(v[i])):
            if(v[i][j].colliderect(a)):
                return (i,j)
def sufle(v, a):
    global hodi

    for i in range(a):
        napr=random.randint(1,4)
        if (napr == 1):#DOWN
            n = find(v, 0)
            if (n[1] > 0):
                v[n[0]][n[1]], v[n[0]][n[1] - 1] = v[n[0]][n[1] - 1], v[n[0]][n[1]]
                hodi.append("DOWN")
                if (prin):
                    print()
                    print(*v, sep="\n")

        elif (napr == 2):#UP
            n = find(v, 0)
            if (n[1] < (siz - 1)):
                v[n[0]][n[1]], v[n[0]][n[1] + 1] = v[n[0]][n[1] + 1], v[n[0]][n[1]]
                hodi.append("UP")
                if (prin):
                    print()
                    print(*v, sep="\n")
        elif (napr == 3):#RIGHT
            n = find(v, 0)
            if (n[0] > 0):
                v[n[0]][n[1]], v[n[0] - 1][n[1]] = v[n[0] - 1][n[1]], v[n[0]][n[1]]
                hodi.append("RIGHT")
                if (prin):
                    print()
        elif (napr == 4):#LEFT
            n = find(v, 0)
            if (n[0] < (siz - 1)):
                v[n[0]][n[1]], v[n[0] + 1][n[1]] = v[n[0] + 1][n[1]], v[n[0]][n[1]]
                hodi.append("LEFT")
                if (prin):
                    print()
                    print(*v, sep="\n")
    return v
global hodi
hodi=[]
win=pg.display.set_mode((600,600))
siz=int(input("ВВедите размер поля"))
pg.font.init()
var=True
prin=False
raz=600//siz
lastlen=999999
v=[]
v1=[]
MouseMove=True
r=[]
au=False
f1 = pg.font.Font(None, 75*4//siz)
napr=""
if(False):
    for i in range(siz):
        v1=[]
        r1=[]
        for j in range(siz):
            r1.append(pg.Rect(raz*i, raz*j, raz, raz))
            k=random.randint(0,len(num)-1)
            v1.append(num[k])
            num.pop(k)
        r.append(r1)
        v.append(v1)
else:
    v111=[]
    for i in range(siz):
        v1=[]
        v11=[]
        r1=[]
        for j in range(siz):
            r1.append(pg.Rect(raz*i, raz*j, raz, raz))
            v1.append((j*siz+i+1)%(siz*siz))
            v11.append((j * siz + i + 1) % (siz * siz))
        r.append(r1)
        v111.append(v11)
        v.append(v1)
v=sufle(v, 250//16*siz*siz)
hod=0
#print(*v, sep="\n")
obr=False
lastpos=(-100,-100)
while True:
    if(obr):
        if(au==False):
            if(len(hodi)==0):
                obr=False
            else:
                napr=hodi[-1]
                if (napr == "UP"):  # DOWN
                    n = find(v, 0)
                    if (n[1] > 0):
                        v[n[0]][n[1]], v[n[0]][n[1] - 1] = v[n[0]][n[1] - 1], v[n[0]][n[1]]
                        if (prin):
                            print()
                            print(*v, sep="\n")
                elif (napr == "DOWN"):  # UP
                    n = find(v, 0)
                    if (n[1] < (siz - 1)):
                        v[n[0]][n[1]], v[n[0]][n[1] + 1] = v[n[0]][n[1] + 1], v[n[0]][n[1]]
                        if (prin):
                            print()
                            print(*v, sep="\n")
                elif (napr == "LEFT"):  # RIGHT
                    n = find(v, 0)
                    if (n[0] > 0):
                        v[n[0]][n[1]], v[n[0] - 1][n[1]] = v[n[0] - 1][n[1]], v[n[0]][n[1]]
                        if (prin):
                            print()
                elif (napr == "RIGHT"):  # LEFT
                    n = find(v, 0)
                    if (n[0] < (siz - 1)):
                        v[n[0]][n[1]], v[n[0] + 1][n[1]] = v[n[0] + 1][n[1]], v[n[0]][n[1]]
                        if (prin):
                            print()
                            print(*v, sep="\n")
                hodi.pop(-1)
                #pg.time.delay(100)
        elif(len(hodi)>0):
            for i in pg.event.get():
                if(pg.mouse.get_pos!=lastpos or lastlen==len(hodi)):
                    napr = hodi[-1]
                    if (napr == "UP"):  # DOWN
                        n = find(v, 0)
                        if (n[1] > 0):
                            pg.mouse.set_pos((n[0])*raz+raz//2, (n[1]-1)*raz+raz//2)
                            lastpos=((n[0])*raz+raz//2, (n[1]-1)*raz+raz//2)
                    elif (napr == "DOWN"):  # UP
                        n = find(v, 0)
                        if (n[1] < (siz - 1)):
                            pg.mouse.set_pos((n[0]) * raz + raz // 2, (n[1] + 1) * raz + raz // 2)
                            lastpos=((n[0]) * raz + raz // 2, (n[1] + 1) * raz + raz // 2)
                    elif (napr == "LEFT"):  # RIGHT
                        n = find(v, 0)
                        if (n[0] > 0):
                            pg.mouse.set_pos((n[0]-1) * raz + raz // 2, (n[1]) * raz + raz // 2)
                            lastpos=((n[0]-1) * raz + raz // 2, (n[1]) * raz + raz // 2)
                    elif (napr == "RIGHT"):  # LEFT
                        n = find(v, 0)
                        if (n[0] < (siz - 1)):
                            pg.mouse.set_pos((n[0]+1) * raz + raz // 2, (n[1]) * raz + raz // 2)
                            lastpos=((n[0]+1) * raz + raz // 2, (n[1]) * raz + raz // 2)
                if (i.type == pg.MOUSEBUTTONDOWN):
                    napr = hodi[-1]
                    if (napr == "UP"):  # DOWN
                        n = find(v, 0)
                        if (n[1] > 0):
                            v[n[0]][n[1]], v[n[0]][n[1] - 1] = v[n[0]][n[1] - 1], v[n[0]][n[1]]
                            if (prin):
                                print()
                                print(*v, sep="\n")
                    elif (napr == "DOWN"):  # UP
                        n = find(v, 0)
                        if (n[1] < (siz - 1)):
                            v[n[0]][n[1]], v[n[0]][n[1] + 1] = v[n[0]][n[1] + 1], v[n[0]][n[1]]
                            if (prin):
                                print()
                                print(*v, sep="\n")
                    elif (napr == "LEFT"):  # RIGHT
                        n = find(v, 0)
                        if (n[0] > 0):
                            v[n[0]][n[1]], v[n[0] - 1][n[1]] = v[n[0] - 1][n[1]], v[n[0]][n[1]]
                            if (prin):
                                print()
                    elif (napr == "RIGHT"):  # LEFT
                        n = find(v, 0)
                        if (n[0] < (siz - 1)):
                            v[n[0]][n[1]], v[n[0] + 1][n[1]] = v[n[0] + 1][n[1]], v[n[0]][n[1]]
                            if (prin):
                                print()
                                print(*v, sep="\n")
                    lastlen=len(hodi)-1
                    hodi.pop(-1)
                #pg.time.delay(100)
    for i in range(siz):
        for j in range(siz):
            if(v[i][j]!=0):
                text1 = f1.render(str(v[i][j]), True,(255, 0, 0))
                pg.draw.rect(win,(255,255,255), r[i][j])
                win.blit(text1, r[i][j].move(raz//4, raz//4))
            else:
                if(prin):
                    print(v, i, j)
                pg.draw.rect(win, (0, 0, 0), r[i][j])

    for i in pg.event.get():
        if i.type == pg.QUIT:
            pg.quit()
            exit()
        if (MouseMove and obr==False):#1=DOWN  2=UP  3=RIGHT 4=LEFT
            if(i.type==pg.MOUSEBUTTONDOWN):
                mouse=pg.mouse.get_pos()
                #print(hodi)
                mrect=pg.Rect(mouse[0], mouse[1], 1,1)
                re=findRect(r, mrect)
                if(v[re[0]][re[1]]!=0):
                    pyst=find(v,0)
                    if(abs(re[0]-pyst[0])+ abs(re[1]-pyst[1])==1):
                        v[pyst[0]][pyst[1]],v[re[0]][re[1]]=v[re[0]][re[1]],v[pyst[0]][pyst[1]]
                        if(pyst[0]>re[0]):
                            hodi.append("RIGHT")
                            hod += 1
                        elif(pyst[0]<re[0]):
                            hodi.append("LEFT")
                            hod += 1
                        elif(pyst[1]>re[1]):
                            hodi.append("DOWN")
                            hod += 1
                        elif (pyst[1] < re[1]):
                            hodi.append("UP")
                            hod += 1
                        print(hod)
                if (v == v111):
                    print("YOU WIN!!!")
                    text1 = f1.render("YOU WIN!!!", True, (255, 0, 0))
                    win.fill((255,255,255))
                    win.blit(text1,(100,250,600,600))
                    pg.display.flip()
                    pg.time.delay(3000)
                    exit()

        if(i.type==pg.KEYDOWN):
            if(i.key==pg.K_SPACE):
                obr=True
                print(len(hodi))
                hodi1=[]
                for i in hodi:
                    try:
                        if(hodi1[-1]=="UP" and i=="DOWN" or hodi1[-1]=="DOWN" and i=="UP" or hodi1[-1]=="RIGHT" and i=="LEFT" or hodi1[-1]=="LEFT" and i=="RIGHT"):
                            hodi1.pop(-1)
                        else:
                            hodi1.append(i)
                    except:
                        hodi1.append(i)
                hodi=hodi1
                print(len(hodi))


        if(var and MouseMove==False):
            if i.type == pg.KEYDOWN:
                if pg.key.get_pressed()[pg.K_w]:
                    napr = "up"

                if pg.key.get_pressed()[pg.K_s]:
                    napr = "down"

                if pg.key.get_pressed()[pg.K_d]:
                    napr = "right"

                if pg.key.get_pressed()[pg.K_a]:
                    napr = "left"
    if(not(var) and MouseMove==False):
        keys = pg.key.get_pressed()
        if (keys[pg.K_w]):
            napr="up"
        elif (keys[pg.K_s]):
            napr="down"
        elif (keys[pg.K_d]):
            napr="right"
        elif (keys[pg.K_a]):
            napr="left"

    if(napr=="down"):
        napr = ""
        n = find(v, 0)
        if (n[1] > 0):
            v[n[0]][n[1]], v[n[0]][n[1] - 1] = v[n[0]][n[1] - 1], v[n[0]][n[1]]
            if (prin):
                print()
                print(*v, sep="\n")

    elif (napr == "up"):
        napr = ""
        n = find(v, 0)
        if (n[1] < (siz - 1)):
            v[n[0]][n[1]], v[n[0]][n[1] + 1] = v[n[0]][n[1] + 1], v[n[0]][n[1]]
            if (prin):
                print()
                print(*v, sep="\n")
    elif (napr == "right"):
        napr = ""
        n = find(v, 0)
        if (n[0] > 0):
            v[n[0]][n[1]], v[n[0] - 1][n[1]] = v[n[0] - 1][n[1]], v[n[0]][n[1]]
            if (prin):
                print()
    elif (napr == "left"):
        napr = ""
        n = find(v, 0)
        if (n[0] < (siz - 1)):
            v[n[0]][n[1]], v[n[0] + 1][n[1]] = v[n[0] + 1][n[1]], v[n[0]][n[1]]
            if (prin):
                print()
                print(*v, sep="\n")
    pg.display.flip()