import math
import pygame
import sys
import tkinter as tk
from math import *
from tkinter import Button, Entry, IntVar, Label, Tk, mainloop, messagebox,ttk
import os

screen = pygame.display.set_mode((800, 800))
#cài đặt thư viện trước khi chạy: mở terminal và gõ: pip install pygame
class spot:
    def __init__(self, x, y):
        self.i = x
        self.j = y
        self.f = 0
        self.g = 0
        self.h = 0
        self.neighbors = []
        self.previous = None
        self.obs = False
        self.closed = False
        self.value = 1

    def show(self, color, st):
        if self.closed == False :
            pygame.draw.rect(screen, color, (self.i * w, self.j * h, w, h), st)
            pygame.display.update()

    def path(self, color, st):
        pygame.draw.rect(screen, color, (self.i * w, self.j * h, w, h), st)
        pygame.display.update()

    def addNeighbors(self, grid):
        i = self.i
        j = self.j
        if i < cols-1 and grid[self.i + 1][j].obs == False:
            self.neighbors.append(grid[self.i + 1][j])
        if i > 0 and grid[self.i - 1][j].obs == False:
            self.neighbors.append(grid[self.i - 1][j])
        if j < row-1 and grid[self.i][j + 1].obs == False:
            self.neighbors.append(grid[self.i][j + 1])
        if j > 0 and grid[self.i][j - 1].obs == False:
            self.neighbors.append(grid[self.i][j - 1])


cols = 50 #số lượng cột
grid = [0 for i in range(cols)] #lưới, giá trị ban đầu là 0
row = 50 #số lượng dòng
openSet = [] #tập Open 
closedSet = [] # tập Closed
red = (255, 0, 0) #màu đỏ
green = (0, 255, 0) # xanh lá
blue = (0, 0, 255) #xanh dương
grey = (220, 220, 220) #xám
yellow = 	(255,255,0) #vàng
w = 800 / cols #=16: bề rộng của một ô trên màn hình
h = 800 / row #=16: chiều cao của một ô trên màn hình



for i in range(cols):
    grid[i] = [0 for i in range(row)]

for i in range(cols):
    for j in range(row):
        grid[i][j] = spot(i, j)


# tạo giá trị mặc định ban đầu
start = grid[10][15]
end = grid[15][35]

for i in range(cols):
    for j in range(row):
        grid[i][j].show((255, 255, 255), 1)

for i in range(0,row):
    grid[0][i].show(grey, 0)
    grid[0][i].obs = True
    grid[cols-1][i].obs = True
    grid[cols-1][i].show(grey, 0)
    grid[i][row-1].show(grey, 0)
    grid[i][0].show(grey, 0)
    grid[i][0].obs = True
    grid[i][row-1].obs = True

def onsubmit():
    global start
    global end
    st = startBox.get().split(',')
    ed = endBox.get().split(',')
    start = grid[int(st[0])][int(st[1])]
    end = grid[int(ed[0])][int(ed[1])]
    window.quit()
    window.destroy()

window = Tk()
label = Label(window, text='Điểm bắt đầu(x,y): ')
startBox = Entry(window)
label1 = Label(window, text='Điểm đích(x,y): ')
endBox = Entry(window)
var = IntVar()
showPath = ttk.Checkbutton(window, text='Hiển thị chi tiết đường đi:', onvalue=1, offvalue=0, variable=var)

submit = Button(window, text='Bắt đầu', command=onsubmit)

showPath.grid(columnspan=2, row=2)
submit.grid(columnspan=2, row=3)
label1.grid(row=1, pady=3)
endBox.grid(row=1, column=1, pady=3)
startBox.grid(row=0, column=1, pady=3)
label.grid(row=0, pady=3)

window.update()
mainloop()

pygame.init()
openSet.append(start)

def mousePress(x):
    xValue = x[0] 
    yValue = x[1]
    c = xValue // (800 // cols)
    r = yValue // (800 // row)
    acess = grid[c][r]
    if acess != start and acess != end:
        if acess.obs == False:
            acess.obs = True
            acess.show((255, 255, 255), 0)

end.show(yellow, 0)
start.show(yellow, 0)

loop = True
while loop:
    ev = pygame.event.get()

    for event in ev:
        if event.type == pygame.QUIT:
            pygame.quit()
        if pygame.mouse.get_pressed()[0]:
            try:
                pos = pygame.mouse.get_pos()
                mousePress(pos)
            except AttributeError:
                pass
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                loop = False
                break

for i in range(cols):
    for j in range(row):
        grid[i][j].addNeighbors(grid)

def heurisitic(n, e):
    d = math.sqrt((n.i - e.i)**2 + (n.j - e.j)**2)
    return d

def main():
    end.show(yellow, 0)
    start.show(yellow, 0)
    if len(openSet) > 0:
        current = None
        #duyệt danh sách trong open list để tìm ra node có đường đi tới đích ngắn nhất: 
        for v in openSet:
            if current == None or v.f <current.f:
                current = v;

        
        if current == end:
            start.show(yellow,0)
            temp = current.f
            for i in range(round(current.f)):
                current.closed = False
                current.show(blue, 0)
                current = current.previous
            end.show(yellow, 0)

            Tk().wm_withdraw()
            result = messagebox.askokcancel('Kết thúc', ('Chi phí của đường đi là: ' + str(temp) + ' ô. \n Bạn có muốn thoát không?'))
            if result == True:
                os.execl(sys.executable,sys.executable, *sys.argv)
            else:
                ag = True
                while ag:
                    ev = pygame.event.get()
                    for event in ev:
                        if event.type == pygame.KEYDOWN:
                            ag = False
                            break
            pygame.quit()

        openSet.remove(current)
        closedSet.append(current)

        neighbors = current.neighbors
        for neighbor in neighbors:
            tempG = current.g + current.value
            
            if neighbor not in openSet and neighbor not in closedSet:
                openSet.append(neighbor)
                neighbor.g = tempG
            else:
                if neighbor.g >tempG: 
                    neighbor.g = tempG
                    if neighbor in closedSet:
                        closedSet.remove(neighbor)
                        openSet.append(neighbor)


               

            neighbor.h = heurisitic(neighbor, end)
            neighbor.f = neighbor.g + neighbor.h

            if neighbor.previous == None:
                neighbor.previous = current
    if var.get():
        for i in range(len(openSet)):
            openSet[i].show(green, 0)

        for i in range(len(closedSet)):
            if closedSet[i] != start:
                closedSet[i].show(red, 0)
    current.closed = True


while True:
    ev = pygame.event.poll()
    if ev.type == pygame.QUIT:
        pygame.quit()
    pygame.display.update()
    main()