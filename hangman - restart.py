import pygame
import random
import sys
from pygame.locals import *

pygame.init()

#var definitions
game = True
screen = pygame.display.set_mode((725,600))
lives = 10
word_list2 = ['elbow','jazz','abruptly','bayou','dwarves','gossip','awkward','jockey','jigsaw','zigzagging','wizard','transcript','quiz','pneumonia','oxygen','pixel,','transplant','rhubarb','queue','rhythm','topaz','swivel','unworthy','witchcraft','wavy','whiskey','yoke','zigzag','microwave','sphinx','scratch','thrift','xylophone','zombie','vodka','syndrome','neighbour','neighborhood','occasional','independent','egypt','grandmother','official,','monkey,','explanation','arrangement','mysterious']
word_list = ['goat']
word = random.choice(word_list)
correct_guess = 0
alphabet = ['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m']
heading = pygame.image.load("hangman_heading.png")
click = False
guess = ''
mouse_pos = pygame.mouse.get_pos()
lives_txt = 10
head = pygame.image.load("head.png")


#colours
white = (255,255,255)
black = (0,0,0)
blue = (152,211,255)
yellow = (0,124,255)

#text...
font = pygame.font.SysFont('arial', 50)
font2 = pygame.font.SysFont('arial', 40)
font3 = pygame.font.SysFont('arial', 20)
font4 = pygame.font.SysFont('arial', 30)
letter_4 = font2.render("There are 4 letters", True, black)
letter_5 = font2.render("There are 5 letters", True, black)
letter_6 = font2.render("There are 6 letters", True, black)
letter_7 = font2.render("There are 7 letters", True, black)
letter_8 = font2.render("There are 8 letters", True, black)
letter_9 = font2.render("There are 9 letters", True, black)
letter_10 = font2.render("There are 10 letters", True, black)
letter_11 = font2.render("There are 11 letters", True, black)
letter_12 = font2.render("There are 12 letters", True, black)

lives_txt_render = font3.render("You have " + str(lives_txt) + " lives", True, black)

#DEFINE .Rect OF THE LETTER BLOCKS
a_block = pygame.Rect(5,480,50,50)
b_block = pygame.Rect(60,480,50,50)
c_block = pygame.Rect(115,480,50,50)
d_block = pygame.Rect(170,480,50,50)
e_block = pygame.Rect(225,480,50,50)
f_block = pygame.Rect(280,480,50,50)
g_block = pygame.Rect(335,480,50,50)
h_block = pygame.Rect(390,480,50,50)
i_block = pygame.Rect(445,480,50,50)
j_block = pygame.Rect(500,480,50,50)
k_block = pygame.Rect(555,480,50,50)
l_block = pygame.Rect(610,480,50,50)
m_block = pygame.Rect(665,480,50,50)
n_block = pygame.Rect(5,535,50,50)
o_block = pygame.Rect(60,535,50,50)
p_block = pygame.Rect(115,535,50,50)
q_block = pygame.Rect(170,535,50,50)
r_block = pygame.Rect(225,535,50,50)
s_block = pygame.Rect(280,535,50,50)
t_block = pygame.Rect(335,535,50,50)
u_block = pygame.Rect(390,535,50,50)
v_block = pygame.Rect(445,535,50,50)
w_block = pygame.Rect(500,535,50,50)
x_block = pygame.Rect(555,535,50,50)
y_block = pygame.Rect(610,535,50,50)
z_block = pygame.Rect(665,535,50,50)

lives_block = pygame.Rect(5,155,200,20)



def draw_screen():
	screen.fill(white)
	screen.blit(heading, (5,5))

	if len(word) == 12:
	    pygame.draw.rect(screen, yellow, (245,350,300,50))
	    pygame.draw.rect(screen, black, (245, 350, 300, 50), 1)
	    screen.blit(letter_12, (250, 350))
	    pygame.draw.line(screen, black, (250, 300), (280, 300), 4)
	    pygame.draw.line(screen, black, (285, 300), (315, 300), 4)
	    pygame.draw.line(screen, black, (320, 300), (350, 300), 4)
	    pygame.draw.line(screen, black, (355, 300), (385, 300), 4)
	    pygame.draw.line(screen, black, (390, 300), (420, 300), 4)
	    pygame.draw.line(screen, black, (425, 300), (455, 300), 4)
	    pygame.draw.line(screen, black, (460, 300), (490, 300), 4)
	    pygame.draw.line(screen, black, (495, 300), (525, 300), 4)
	    pygame.draw.line(screen, black, (530, 300), (560, 300), 4)
	    pygame.draw.line(screen, black, (565, 300), (595, 300), 4)
	    pygame.draw.line(screen, black, (600, 300), (630, 300), 4)
	    pygame.draw.line(screen, black, (635, 300), (665, 300), 4)

	if len(word) == 11:
	    pygame.draw.rect(screen, yellow, (245,350,300,50))
	    pygame.draw.rect(screen, black, (245, 350, 300, 50), 1)
	    screen.blit(letter_11, (250, 350))
	    pygame.draw.line(screen, black, (250, 300), (280, 300), 4)
	    pygame.draw.line(screen, black, (285, 300), (315, 300), 4)
	    pygame.draw.line(screen, black, (320, 300), (350, 300), 4)
	    pygame.draw.line(screen, black, (355, 300), (385, 300), 4)
	    pygame.draw.line(screen, black, (390, 300), (420, 300), 4)
	    pygame.draw.line(screen, black, (425, 300), (455, 300), 4)
	    pygame.draw.line(screen, black, (460, 300), (490, 300), 4)
	    pygame.draw.line(screen, black, (495, 300), (525, 300), 4)
	    pygame.draw.line(screen, black, (530, 300), (560, 300), 4)
	    pygame.draw.line(screen, black, (565, 300), (595, 300), 4)
	    pygame.draw.line(screen, black, (600, 300), (630, 300), 4)

	if len(word) == 10:
	    pygame.draw.rect(screen, yellow, (280,350,300,50))
	    pygame.draw.rect(screen, black, (280, 350, 300, 50), 1)
	    screen.blit(letter_10, (285, 350))
	    pygame.draw.line(screen, black, (285, 300), (315, 300), 4)
	    pygame.draw.line(screen, black, (320, 300), (350, 300), 4)
	    pygame.draw.line(screen, black, (355, 300), (385, 300), 4)
	    pygame.draw.line(screen, black, (390, 300), (420, 300), 4)
	    pygame.draw.line(screen, black, (425, 300), (455, 300), 4)
	    pygame.draw.line(screen, black, (460, 300), (490, 300), 4)
	    pygame.draw.line(screen, black, (495, 300), (525, 300), 4)
	    pygame.draw.line(screen, black, (530, 300), (560, 300), 4)
	    pygame.draw.line(screen, black, (565, 300), (595, 300), 4)
	    pygame.draw.line(screen, black, (600, 300), (630, 300), 4)

	if len(word) == 9:
	    pygame.draw.rect(screen, yellow, (280,350,300,50))
	    pygame.draw.rect(screen, black, (280, 350, 300, 50), 1)
	    screen.blit(letter_9, (285, 350))
	    pygame.draw.line(screen, black, (285, 300), (315, 300), 4)
	    pygame.draw.line(screen, black, (320, 300), (350, 300), 4)
	    pygame.draw.line(screen, black, (355, 300), (385, 300), 4)
	    pygame.draw.line(screen, black, (390, 300), (420, 300), 4)
	    pygame.draw.line(screen, black, (425, 300), (455, 300), 4)
	    pygame.draw.line(screen, black, (460, 300), (490, 300), 4)
	    pygame.draw.line(screen, black, (495, 300), (525, 300), 4)
	    pygame.draw.line(screen, black, (530, 300), (560, 300), 4)
	    pygame.draw.line(screen, black, (565, 300), (595, 300), 4)

	if len(word) == 8:
	    pygame.draw.rect(screen, yellow, (315,350,300,50))
	    pygame.draw.rect(screen, black, (315, 350, 300, 50), 1)
	    screen.blit(letter_8, (320, 350))
	    pygame.draw.line(screen, black, (320, 300), (350, 300), 4)
	    pygame.draw.line(screen, black, (355, 300), (385, 300), 4)
	    pygame.draw.line(screen, black, (390, 300), (420, 300), 4)
	    pygame.draw.line(screen, black, (425, 300), (455, 300), 4)
	    pygame.draw.line(screen, black, (460, 300), (490, 300), 4)
	    pygame.draw.line(screen, black, (495, 300), (525, 300), 4)
	    pygame.draw.line(screen, black, (530, 300), (560, 300), 4)
	    pygame.draw.line(screen, black, (565, 300), (595, 300), 4)

	if len(word) == 7:
	    pygame.draw.rect(screen, yellow, (315,350,300,50))
	    pygame.draw.rect(screen, black, (315, 350, 300, 50), 1)
	    screen.blit(letter_7, (320, 350))
	    pygame.draw.line(screen, black, (320, 300), (350, 300), 4)
	    pygame.draw.line(screen, black, (355, 300), (385, 300), 4)
	    pygame.draw.line(screen, black, (390, 300), (420, 300), 4)
	    pygame.draw.line(screen, black, (425, 300), (455, 300), 4)
	    pygame.draw.line(screen, black, (460, 300), (490, 300), 4)
	    pygame.draw.line(screen, black, (495, 300), (525, 300), 4)
	    pygame.draw.line(screen, black, (530, 300), (560, 300), 4)

	if len(word) == 6:
	    pygame.draw.rect(screen, yellow, (350,350,300,50))
	    pygame.draw.rect(screen, black, (350, 350, 300, 50), 1)
	    screen.blit(letter_6, (355, 350))
	    pygame.draw.line(screen, black, (355, 300), (385, 300), 4)
	    pygame.draw.line(screen, black, (390, 300), (420, 300), 4)
	    pygame.draw.line(screen, black, (425, 300), (455, 300), 4)
	    pygame.draw.line(screen, black, (460, 300), (490, 300), 4)
	    pygame.draw.line(screen, black, (495, 300), (525, 300), 4)
	    pygame.draw.line(screen, black, (530, 300), (560, 300), 4)

	if len(word) == 5:
	    pygame.draw.rect(screen, yellow, (350,350,300,50))
	    pygame.draw.rect(screen, black, (350, 350, 300, 50), 1)
	    screen.blit(letter_5, (355, 350))
	    pygame.draw.line(screen, black, (355, 300), (385, 300), 4)
	    pygame.draw.line(screen, black, (390, 300), (420, 300), 4)
	    pygame.draw.line(screen, black, (425, 300), (455, 300), 4)
	    pygame.draw.line(screen, black, (460, 300), (490, 300), 4)
	    pygame.draw.line(screen, black, (495, 300), (525, 300), 4)

	if len(word) == 4:
	    pygame.draw.rect(screen, yellow, (385,350,300,50))
	    screen.blit(letter_4, (390, 350))
	    pygame.draw.line(screen, black, (390, 300), (420, 300), 4)
	    pygame.draw.line(screen, black, (425, 300), (455, 300), 4)
	    pygame.draw.line(screen, black, (460, 300), (490, 300), 4)
	    pygame.draw.line(screen, black, (495, 300), (525, 300), 4)

	#DEFINE LETTERS
	aa = font.render('A', True, black)
	bb = font.render('B', True, black)
	cc = font.render('C', True, black)
	dd = font.render('D', True, black)
	ee = font.render('E', True, black)
	ff = font.render('F', True, black)
	gg = font.render('G', True, black)
	hh = font.render('H', True, black)
	ii = font.render('I', True, black)
	jj = font.render('J', True, black)
	kk = font.render('K', True, black)
	ll = font.render('L', True, black)
	mm = font.render('M', True, black)
	nn = font.render('N', True, black)
	oo = font.render('O', True, black)
	pp = font.render('P', True, black)
	qq = font.render('Q', True, black)
	rr = font.render('R', True, black)
	ss = font.render('S', True, black)
	tt = font.render('T', True, black)
	uu = font.render('U', True, black)
	vv = font.render('V', True, black)
	ww = font.render('W', True, black)
	xx = font.render('X', True, black)
	yy = font.render('Y', True, black)
	zz = font.render('Z', True, black)
	# DRAW LETTER BLOCKS
	pygame.draw.rect(screen, blue, (q_block))
	pygame.draw.rect(screen, blue, (w_block))
	pygame.draw.rect(screen, blue, (e_block))
	pygame.draw.rect(screen, blue, (r_block))
	pygame.draw.rect(screen, blue, (t_block))
	pygame.draw.rect(screen, blue, (y_block))
	pygame.draw.rect(screen, blue, (u_block))
	pygame.draw.rect(screen, blue, (i_block))
	pygame.draw.rect(screen, blue, (o_block))
	pygame.draw.rect(screen, blue, (p_block))
	pygame.draw.rect(screen, blue, (a_block))
	pygame.draw.rect(screen, blue, (s_block))
	pygame.draw.rect(screen, blue, (d_block))
	pygame.draw.rect(screen, blue, (f_block))
	pygame.draw.rect(screen, blue, (g_block))
	pygame.draw.rect(screen, blue, (h_block))
	pygame.draw.rect(screen, blue, (j_block))
	pygame.draw.rect(screen, blue, (k_block))
	pygame.draw.rect(screen, blue, (l_block))
	pygame.draw.rect(screen, blue, (z_block))
	pygame.draw.rect(screen, blue, (x_block))
	pygame.draw.rect(screen, blue, (c_block))
	pygame.draw.rect(screen, blue, (v_block))
	pygame.draw.rect(screen, blue, (b_block))
	pygame.draw.rect(screen, blue, (n_block))
	pygame.draw.rect(screen, blue, (m_block))
	#LETTER BLOCK BORDERS
	pygame.draw.rect(screen, black, (q_block),1)
	pygame.draw.rect(screen, black, (w_block),1)
	pygame.draw.rect(screen, black, (e_block),1)
	pygame.draw.rect(screen, black, (r_block),1)
	pygame.draw.rect(screen, black, (t_block),1)
	pygame.draw.rect(screen, black, (y_block),1)
	pygame.draw.rect(screen, black, (u_block),1)
	pygame.draw.rect(screen, black, (i_block),1)
	pygame.draw.rect(screen, black, (o_block),1)
	pygame.draw.rect(screen, black, (p_block),1)
	pygame.draw.rect(screen, black, (a_block),1)
	pygame.draw.rect(screen, black, (s_block),1)
	pygame.draw.rect(screen, black, (d_block),1)
	pygame.draw.rect(screen, black, (f_block),1)
	pygame.draw.rect(screen, black, (g_block),1)
	pygame.draw.rect(screen, black, (h_block),1)
	pygame.draw.rect(screen, black, (j_block),1)
	pygame.draw.rect(screen, black, (k_block),1)
	pygame.draw.rect(screen, black, (l_block),1)
	pygame.draw.rect(screen, black, (z_block),1)
	pygame.draw.rect(screen, black, (x_block),1)
	pygame.draw.rect(screen, black, (c_block),1)
	pygame.draw.rect(screen, black, (v_block),1)
	pygame.draw.rect(screen, black, (b_block),1)
	pygame.draw.rect(screen, black, (n_block),1)
	pygame.draw.rect(screen, black, (m_block),1)
	#BLIT LETTERS
	screen.blit(aa, (15,475))
	screen.blit(bb, (70,475))
	screen.blit(cc, (125,475))
	screen.blit(dd, (180,475))
	screen.blit(ee, (235,475))
	screen.blit(ff, (290,475))
	screen.blit(gg, (345,475))
	screen.blit(hh, (400,475))
	screen.blit(ii, (455,475))
	screen.blit(jj, (510,475))
	screen.blit(kk, (565,475))
	screen.blit(ll, (620,475))
	screen.blit(mm, (675,475))
	screen.blit(nn, (15,535))
	screen.blit(oo, (70,535))
	screen.blit(pp, (125,535))
	screen.blit(qq, (180,535))
	screen.blit(rr, (235,535))
	screen.blit(ss, (290,535))
	screen.blit(tt, (345,535))
	screen.blit(uu, (400,535))
	screen.blit(vv, (455,535))
	screen.blit(ww, (510,535))
	screen.blit(xx, (565,535))
	screen.blit(yy, (620,535))
	screen.blit(zz, (675,535))

	#screen.blit(a, (350,250))

	screen.blit(lives_txt_render, (5, 150))

	pygame.display.update()

game = True
lives = 10
click = False
guess = ''


def guesses():
    global guess, click, mouse_pos, a_, l3, l_num
    guess = ''
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN :
            click = True
        if event.type == pygame.MOUSEBUTTONUP :
            click = False
    while game:
	    if a_block.collidepoint(mouse_pos)and click:
	        guess = 'a'
	        pygame.draw.rect(screen, white, (a_block))

	        if guess in word:

	        	a_ = word.index(guess)
	        	print(a_)
	        	a = font4.render(word[a_], True, black)
	        	letterDrawer()
	        	if a_ == 0:
	        		l_num = l1
	        	if a_ == 1:
	        		l_num = l2
	        	if a_ == 2:
	        		l_num = l3
	        	if a_ == 3:
	        		l_num = l4
	        	if a_ == 4:
	        		l_num = l5
	        	if a_ == 5:
	        		l_num = l6
	        	if a_ == 6:
	        		l_num = l7
	        	if a_ == 7:
	        		l_num = l8
	        	if a_ == 8:
	        		l_num = l9
	        	if a_ == 9:
	        		l_num = l10
	        	if a_ == 10:
	        		l_num = l11
	        	if a_ == 11:
	        		l_num = l12
	        	if a_ == 12:
	        		l_num = l13
	        	screen.blit(a, l_num)

	    if b_block.collidepoint(mouse_pos)and click:
	        guess = 'b'
	        pygame.draw.rect(screen, white, (b_block))
	        if guess in word:

	        	b_ = word.index(guess)
	        	b = font4.render(word[b_], True, black)
	        	letterDrawer()
	        	if b_ == 0:
	        		l_num = l1
	        	if b_ == 1:
	        		l_num = l2
	        	if b_ == 2:
	        		l_num = l3
	        	if b_ == 3:
	        		l_num = l4
	        	if b_ == 4:
	        		l_num = l5
	        	if b_ == 5:
	        		l_num = l6
	        	if b_ == 6:
	        		l_num = l7
	        	if b_ == 7:
	        		l_num = l8
	        	if b_ == 8:
	        		l_num = l9
	        	if b_ == 9:
	        		l_num = l10
	        	if b_ == 10:
	        		l_num = l11
	        	if b_ == 11:
	        		l_num = l12
	        	if b_ == 12:
	        		l_num = l13
	        	screen.blit(b, l_num)
	    if c_block.collidepoint(mouse_pos)and click:
	        guess = 'c'
	        pygame.draw.rect(screen, white, (c_block))
	        if guess in word:

	        	c_ = word.index(guess)
	        	c = font4.render(word[c_], True, black)
	        	letterDrawer()
	        	if c_ == 0:
	        		l_num = l1
	        	if c_ == 1:
	        		l_num = l2
	        	if c_ == 2:
	        		l_num = l3
	        	if c_ == 3:
	        		l_num = l4
	        	if c_ == 4:
	        		l_num = l5
	        	if c_ == 5:
	        		l_num = l6
	        	if c_ == 6:
	        		l_num = l7
	        	if c_ == 7:
	        		l_num = l8
	        	if c_ == 8:
	        		l_num = l9
	        	if c_ == 9:
	        		l_num = l10
	        	if c_ == 10:
	        		l_num = l11
	        	if c_ == 11:
	        		l_num = l12
	        	if c_ == 12:
	        		l_num = l13
	        	screen.blit(c, l_num)
	    if d_block.collidepoint(mouse_pos)and click:
	        guess = 'd'
	        pygame.draw.rect(screen, white, (d_block))
	        if guess in word:

	        	d_ = word.index(guess)
	        	d = font4.render(word[d_], True, black)
	        	letterDrawer()
	        	if d_ == 0:
	        		l_num = l1
	        	if d_ == 1:
	        		l_num = l2
	        	if d_ == 2:
	        		l_num = l3
	        	if d_ == 3:
	        		l_num = l4
	        	if d_ == 4:
	        		l_num = l5
	        	if d_ == 5:
	        		l_num = l6
	        	if d_ == 6:
	        		l_num = l7
	        	if d_ == 7:
	        		l_num = l8
	        	if d_ == 8:
	        		l_num = l9
	        	if d_ == 9:
	        		l_num = l10
	        	if d_ == 10:
	        		l_num = l11
	        	if d_ == 11:
	        		l_num = l12
	        	if d_ == 12:
	        		l_num = l13
	        	screen.blit(d, l_num)
	    if e_block.collidepoint(mouse_pos)and click:
	        guess = 'e'
	        pygame.draw.rect(screen, white, (e_block))
	        if guess in word:

	        	e_ = word.index(guess)
	        	e = font4.render(word[e_], True, black)
	        	letterDrawer()
	        	if e_ == 0:
	        		l_num = l1
	        	if e_ == 1:
	        		l_num = l2
	        	if e_ == 2:
	        		l_num = l3
	        	if e_ == 3:
	        		l_num = l4
	        	if e_ == 4:
	        		l_num = l5
	        	if e_ == 5:
	        		l_num = l6
	        	if e_ == 6:
	        		l_num = l7
	        	if e_ == 7:
	        		l_num = l8
	        	if e_ == 8:
	        		l_num = l9
	        	if e_ == 9:
	        		l_num = l10
	        	if e_ == 10:
	        		l_num = l11
	        	if e_ == 11:
	        		l_num = l12
	        	if e_ == 12:
	        		l_num = l13
	        	screen.blit(e, l_num)
	    if f_block.collidepoint(mouse_pos)and click:
	        guess = 'f'
	        pygame.draw.rect(screen, white, (f_block))
	        if guess in word:

	        	f_ = word.index(guess)
	        	f = font4.render(word[f_], True, black)
	        	letterDrawer()
	        	if f_ == 0:
	        		l_num = l1
	        	if f_ == 1:
	        		l_num = l2
	        	if f_ == 2:
	        		l_num = l3
	        	if f_ == 3:
	        		l_num = l4
	        	if f_ == 4:
	        		l_num = l5
	        	if f_ == 5:
	        		l_num = l6
	        	if f_ == 6:
	        		l_num = l7
	        	if f_ == 7:
	        		l_num = l8
	        	if f_ == 8:
	        		l_num = l9
	        	if f_ == 9:
	        		l_num = l10
	        	if f_ == 10:
	        		l_num = l11
	        	if f_ == 11:
	        		l_num = l12
	        	if f_ == 12:
	        		l_num = l13
	        	screen.blit(f, l_num)
	    if g_block.collidepoint(mouse_pos)and click:
	        guess = 'g'
	        pygame.draw.rect(screen, white, (g_block))
	        if guess in word:

	        	g_ = word.index(guess)
	        	g = font4.render(word[g_], True, black)
	        	letterDrawer()
	        	if g_ == 0:
	        		l_num = l1
	        	if g_ == 1:
	        		l_num = l2
	        	if g_ == 2:
	        		l_num = l3
	        	if g_ == 3:
	        		l_num = l4
	        	if g_ == 4:
	        		l_num = l5
	        	if g_ == 5:
	        		l_num = l6
	        	if g_ == 6:
	        		l_num = l7
	        	if g_ == 7:
	        		l_num = l8
	        	if g_ == 8:
	        		l_num = l9
	        	if g_ == 9:
	        		l_num = l10
	        	if g_ == 10:
	        		l_num = l11
	        	if g_ == 11:
	        		l_num = l12
	        	if g_ == 12:
	        		l_num = l13
	        	screen.blit(g, l_num)
	    if h_block.collidepoint(mouse_pos)and click:
	        guess = 'h'
	        pygame.draw.rect(screen, white, (h_block))
	        if guess in word:

	        	h_ = word.index(guess)
	        	h = font4.render(word[h_], True, black)
	        	letterDrawer()
	        	if h_ == 0:
	        		l_num = l1
	        	if h_ == 1:
	        		l_num = l2
	        	if h_ == 2:
	        		l_num = l3
	        	if h_ == 3:
	        		l_num = l4
	        	if h_ == 4:
	        		l_num = l5
	        	if h_ == 5:
	        		l_num = l6
	        	if h_ == 6:
	        		l_num = l7
	        	if h_ == 7:
	        		l_num = l8
	        	if h_ == 8:
	        		l_num = l9
	        	if h_ == 9:
	        		l_num = l10
	        	if h_ == 10:
	        		l_num = l11
	        	if h_ == 11:
	        		l_num = l12
	        	if h_ == 12:
	        		l_num = l13
	        	screen.blit(h, l_num)
	    if i_block.collidepoint(mouse_pos)and click:
	        guess = 'i'
	        pygame.draw.rect(screen, white, (i_block))
	        if guess in word:

	        	i_ = word.index(guess)
	        	i = font4.render(word[i_], True, black)
	        	letterDrawer()
	        	if i_ == 0:
	        		l_num = l1
	        	if i_ == 1:
	        		l_num = l2
	        	if i_ == 2:
	        		l_num = l3
	        	if i_ == 3:
	        		l_num = l4
	        	if i_ == 4:
	        		l_num = l5
	        	if i_ == 5:
	        		l_num = l6
	        	if i_ == 6:
	        		l_num = l7
	        	if i_ == 7:
	        		l_num = l8
	        	if i_ == 8:
	        		l_num = l9
	        	if i_ == 9:
	        		l_num = l10
	        	if i_ == 10:
	        		l_num = l11
	        	if i_ == 11:
	        		l_num = l12
	        	if i_ == 12:
	        		l_num = l13
	        	screen.blit(i, l_num)
	    if j_block.collidepoint(mouse_pos)and click:
	        guess = 'j'
	        pygame.draw.rect(screen, white, (j_block))
	        if guess in word:

	        	j_ = word.index(guess)
	        	j = font4.render(word[j_], True, black)
	        	letterDrawer()
	        	if j_ == 0:
	        		l_num = l1
	        	if j_ == 1:
	        		l_num = l2
	        	if j_ == 2:
	        		l_num = l3
	        	if j_ == 3:
	        		l_num = l4
	        	if j_ == 4:
	        		l_num = l5
	        	if j_ == 5:
	        		l_num = l6
	        	if j_ == 6:
	        		l_num = l7
	        	if j_ == 7:
	        		l_num = l8
	        	if j_ == 8:
	        		l_num = l9
	        	if j_ == 9:
	        		l_num = l10
	        	if j_ == 10:
	        		l_num = l11
	        	if j_ == 11:
	        		l_num = l12
	        	if j_ == 12:
	        		l_num = l13
	        	screen.blit(j, l_num)
	    if k_block.collidepoint(mouse_pos)and click:
	        guess = 'k'
	        pygame.draw.rect(screen, white, (k_block))
	        if guess in word:

	        	k_ = word.index(guess)
	        	k = font4.render(word[k_], True, black)
	        	letterDrawer()
	        	if k_ == 0:
	        		l_num = l1
	        	if k_ == 1:
	        		l_num = l2
	        	if k_ == 2:
	        		l_num = l3
	        	if k_ == 3:
	        		l_num = l4
	        	if k_ == 4:
	        		l_num = l5
	        	if k_ == 5:
	        		l_num = l6
	        	if k_ == 6:
	        		l_num = l7
	        	if k_ == 7:
	        		l_num = l8
	        	if k_ == 8:
	        		l_num = l9
	        	if k_ == 9:
	        		l_num = l10
	        	if k_ == 10:
	        		l_num = l11
	        	if k_ == 11:
	        		l_num = l12
	        	if k_ == 12:
	        		l_num = l13
	        	screen.blit(k, l_num)
	    if l_block.collidepoint(mouse_pos)and click:
	        guess = 'l'
	        pygame.draw.rect(screen, white, (l_block))
	        if guess in word:

	        	l_ = word.index(guess)
	        	l = font4.render(word[l_], True, black)
	        	letterDrawer()
	        	if l_ == 0:
	        		l_num = l1
	        	if l_ == 1:
	        		l_num = l2
	        	if l_ == 2:
	        		l_num = l3
	        	if l_ == 3:
	        		l_num = l4
	        	if l_ == 4:
	        		l_num = l5
	        	if l_ == 5:        
	        		l_num = l6
	        	if l_ == 6:
	        		l_num = l7
	        	if l_ == 7:
	        		l_num = l8
	        	if l_ == 8:
	        		l_num = l9
	        	if l_ == 9:
	        		l_num = l10
	        	if l_ == 10:
	        		l_num = l11
	        	if l_ == 11:
	        		l_num = l12
	        	if l_ == 12:
	        		l_num = l13
	        	screen.blit(l, l_num)
	    if m_block.collidepoint(mouse_pos)and click:
	        guess = 'm'
	        pygame.draw.rect(screen, white, (m_block))
	        if guess in word:

	        	m_ = word.index(guess)
	        	m = font4.render(word[m_], True, black)
	        	letterDrawer()
	        	if m_ == 0:
	        		l_num = l1
	        	if m_ == 1:
	        		l_num = l2
	        	if m_ == 2:
	        		l_num = l3
	        	if m_ == 3:
	        		l_num = l4
	        	if m_ == 4:
	        		l_num = l5
	        	if m_ == 5:
	        		l_num = l6
	        	if m_ == 6:
	        		l_num = l7
	        	if m_ == 7:
	        		l_num = l8
	        	if m_ == 8:
	        		l_num = l9
	        	if m_ == 9:
	        		l_num = l10
	        	if m_ == 10:
	        		l_num = l11
	        	if m_ == 11:
	        		l_num = l12
	        	if m_ == 12:
	        		l_num = l13
	        	screen.blit(m, l_num)
	    if n_block.collidepoint(mouse_pos)and click:
	        guess = 'n'
	        pygame.draw.rect(screen, white, (n_block))
	        if guess in word:

	        	n_ = word.index(guess)
	        	n = font4.render(word[n_], True, black)
	        	letterDrawer()
	        	if n_ == 0:
	        		l_num = l1
	        	if n_ == 1:
	        		l_num = l2
	        	if n_ == 2:
	        		l_num = l3
	        	if n_ == 3:
	        		l_num = l4
	        	if n_ == 4:
	        		l_num = l5
	        	if n_ == 5:
	        		l_num = l6
	        	if n_ == 6:
	        		l_num = l7
	        	if n_ == 7:
	        		l_num = l8
	        	if n_ == 8:
	        		l_num = l9
	        	if n_ == 9:
	        		l_num = l10
	        	if n_ == 10:
	        		l_num = l11
	        	if n_ == 11:
	        		l_num = l12
	        	if n_ == 12:
	        		l_num = l13
	        	screen.blit(n, l_num)
	    if o_block.collidepoint(mouse_pos)and click:
	        guess = 'o'
	        pygame.draw.rect(screen, white, (o_block))
	        if guess in word:

	        	o_ = word.index(guess)
	        	o = font4.render(word[o_], True, black)
	        	letterDrawer()
	        	if o_ == 0:
	        		l_num = l1
	        	if o_ == 1:
	        		l_num = l2
	        	if o_ == 2:
	        		l_num = l3
	        	if o_ == 3:
	        		l_num = l4
	        	if o_ == 4:
	        		l_num = l5
	        	if o_ == 5:
	        		l_num = l6
	        	if o_ == 6:
	        		l_num = l7
	        	if o_ == 7:
	        		l_num = l8
	        	if o_ == 8:
	        		l_num = l9
	        	if o_ == 9:
	        		l_num = l10
	        	if o_ == 10:
	        		l_num = l11
	        	if o_ == 11:
	        		l_num = l12
	        	if o_ == 12:
	        		l_num = l13
	        	screen.blit(o, l_num)
	    if p_block.collidepoint(mouse_pos)and click:
	        guess = 'p'
	        pygame.draw.rect(screen, white, (p_block))
	        if guess in word:

	        	p_ = word.index(guess)
	        	p = font4.render(word[p_], True, black)
	        	letterDrawer()
	        	if p_ == 0:
	        		l_num = l1
	        	if p_ == 1:
	        		l_num = l2
	        	if p_ == 2:
	        		l_num = l3
	        	if p_ == 3:
	        		l_num = l4
	        	if p_ == 4:
	        		l_num = l5
	        	if p_ == 5:
	        		l_num = l6
	        	if p_ == 6:
	        		l_num = l7
	        	if p_ == 7:
	        		l_num = l8
	        	if p_ == 8:
	        		l_num = l9
	        	if p_ == 9:
	        		l_num = l10
	        	if p_ == 10:
	        		l_num = l11
	        	if p_ == 11:
	        		l_num = l12
	        	if p_ == 12:
	        		l_num = l13
	        	screen.blit(p, l_num)
	    if q_block.collidepoint(mouse_pos)and click:
	        guess = 'q'
	        pygame.draw.rect(screen, white, (q_block))
	        if guess in word:

	        	q_ = word.index(guess)
	        	q = font4.render(word[q_], True, black)
	        	letterDrawer()
	        	if q_ == 0:
	        		l_num = l1
	        	if q_ == 1:
	        		l_num = l2
	        	if q_ == 2:
	        		l_num = l3
	        	if q_ == 3:
	        		l_num = l4
	        	if q_ == 4:
	        		l_num = l5
	        	if q_ == 5:
	        		l_num = l6
	        	if q_ == 6:
	        		l_num = l7
	        	if q_ == 7:
	        		l_num = l8
	        	if q_ == 8:
	        		l_num = l9
	        	if q_ == 9:
	        		l_num = l10
	        	if q_ == 10:
	        		l_num = l11
	        	if q_ == 11:
	        		l_num = l12
	        	if q_ == 12:
	        		l_num = l13
	        	screen.blit(q, l_num)
	    if r_block.collidepoint(mouse_pos)and click:
	        guess = 'r'
	        pygame.draw.rect(screen, white, (r_block))
	        if guess in word:

	        	r_ = word.index(guess)
	        	r = font4.render(word[r_], True, black)
	        	letterDrawer()
	        	if r_ == 0:
	        		l_num = l1
	        	if r_ == 1:
	        		l_num = l2
	        	if r_ == 2:
	        		l_num = l3
	        	if r_ == 3:
	        		l_num = l4
	        	if r_ == 4:
	        		l_num = l5
	        	if r_ == 5:
	        		l_num = l6
	        	if r_ == 6:
	        		l_num = l7
	        	if r_ == 7:
	        		l_num = l8
	        	if r_ == 8:
	        		l_num = l9
	        	if r_ == 9:
	        		l_num = l10
	        	if r_ == 10:
	        		l_num = l11
	        	if r_ == 11:
	        		l_num = l12
	        	if r_ == 12:
	        		l_num = l13
	        	screen.blit(r, l_num)
	    if s_block.collidepoint(mouse_pos)and click:
	        guess = 's'
	        pygame.draw.rect(screen, white, (s_block))
	        if guess in word:

	        	s_ = word.index(guess)
	        	s = font4.render(word[s_], True, black)
	        	letterDrawer()
	        	if s_ == 0:
	        		l_num = l1
	        	if s_ == 1:
	        		l_num = l2
	        	if s_ == 2:
	        		l_num = l3
	        	if s_ == 3:
	        		l_num = l4
	        	if s_ == 4:
	        		l_num = l5
	        	if s_ == 5:
	        		l_num = l6
	        	if s_ == 6:
	        		l_num = l7
	        	if s_ == 7:
	        		l_num = l8
	        	if s_ == 8:
	        		l_num = l9
	        	if s_ == 9:
	        		l_num = l10
	        	if s_ == 10:
	        		l_num = l11
	        	if s_ == 11:
	        		l_num = l12
	        	if s_ == 12:
	        		l_num = l13
	        	screen.blit(s, l_num)
	    if t_block.collidepoint(mouse_pos)and click:
	        guess = 't'
	        pygame.draw.rect(screen, white, (t_block))
	        if guess in word:

	        	t_ = word.index(guess)
	        	t = font4.render(word[t_], True, black)
	        	letterDrawer()
	        	if t_ == 0:
	        		l_num = l1
	        	if t_ == 1:
	        		l_num = l2
	        	if t_ == 2:
	        		l_num = l3
	        	if t_ == 3:
	        		l_num = l4
	        	if t_ == 4:
	        		l_num = l5
	        	if t_ == 5:
	        		l_num = l6
	        	if t_ == 6:
	        		l_num = l7
	        	if t_ == 7:
	        		l_num = l8
	        	if t_ == 8:
	        		l_num = l9
	        	if t_ == 9:
	        		l_num = l10
	        	if t_ == 10:
	        		l_num = l11
	        	if t_ == 11:
	        		l_num = l12
	        	if t_ == 12:
	        		l_num = l13
	        	screen.blit(t, l_num)
	    if u_block.collidepoint(mouse_pos)and click:
	        guess = 'u'
	        pygame.draw.rect(screen, white, (u_block))
	        if guess in word:

	        	u_ = word.index(guess)
	        	u = font4.render(word[u_], True, black)
	        	letterDrawer()
	        	if u_ == 0:
	        		l_num = l1
	        	if u_ == 1:
	        		l_num = l2
	        	if u_ == 2:
	        		l_num = l3
	        	if u_ == 3:
	        		l_num = l4
	        	if u_ == 4:
	        		l_num = l5
	        	if u_ == 5:
	        		l_num = l6
	        	if u_ == 6:
	        		l_num = l7
	        	if u_ == 7:
	        		l_num = l8
	        	if u_ == 8:
	        		l_num = l9
	        	if u_ == 9:
	        		l_num = l10
	        	if u_ == 10:
	        		l_num = l11
	        	if u_ == 11:
	        		l_num = l12
	        	if u_ == 12:
	        		l_num = l13
	        	screen.blit(u, l_num)
	    if v_block.collidepoint(mouse_pos)and click:
	        guess = 'v'
	        pygame.draw.rect(screen, white, (v_block))
	        if guess in word:

	        	v_ = word.index(guess)
	        	v = font4.render(word[v_], True, black)
	        	letterDrawer()
	        	if v_ == 0:
	        		l_num = l1
	        	if v_ == 1:
	        		l_num = l2
	        	if v_ == 2:
	        		l_num = l3
	        	if v_ == 3:
	        		l_num = l4
	        	if v_ == 4:
	        		l_num = l5
	        	if v_ == 5:
	        		l_num = l6
	        	if v_ == 6:
	        		l_num = l7
	        	if v_ == 7:
	        		l_num = l8
	        	if v_ == 8:
	        		l_num = l9
	        	if v_ == 9:
	        		l_num = l10
	        	if v_ == 10:
	        		l_num = l11
	        	if v_ == 11:
	        		l_num = l12
	        	if v_ == 12:
	        		l_num = l13
	        	screen.blit(v, l_num)
	    if w_block.collidepoint(mouse_pos)and click:
	        guess = 'w'
	        pygame.draw.rect(screen, white, (w_block))
	        if guess in word:

	        	w_ = word.index(guess)
	        	w = font4.render(word[w_], True, black)
	        	letterDrawer()
	        	if w_ == 0:
	        		l_num = l1
	        	if w_ == 1:
	        		l_num = l2
	        	if w_ == 2:
	        		l_num = l3
	        	if w_ == 3:
	        		l_num = l4
	        	if w_ == 4:
	        		l_num = l5
	        	if w_ == 5:
	        		l_num = l6
	        	if w_ == 6:
	        		l_num = l7
	        	if w_ == 7:
	        		l_num = l8
	        	if w_ == 8:
	        		l_num = l9
	        	if w_ == 9:
	        		l_num = l10
	        	if w_ == 10:
	        		l_num = l11
	        	if w_ == 11:
	        		l_num = l12
	        	if w_ == 12:
	        		l_num = l13
	        	screen.blit(w, l_num)
	    if x_block.collidepoint(mouse_pos)and click:
	        guess = 'x'
	        pygame.draw.rect(screen, white, (x_block))
	        if guess in word:

	        	x_ = word.index(guess)
	        	x = font4.render(word[x_], True, black)
	        	letterDrawer()
	        	if x_ == 0:
	        		l_num = l1
	        	if x_ == 1:
	        		l_num = l2
	        	if x_ == 2:
	        		l_num = l3
	        	if x_ == 3:
	        		l_num = l4
	        	if x_ == 4:
	        		l_num = l5
	        	if x_ == 5:
	        		l_num = l6
	        	if x_ == 6:
	        		l_num = l7
	        	if x_ == 7:
	        		l_num = l8
	        	if x_ == 8:
	        		l_num = l9
	        	if x_ == 9:
	        		l_num = l10
	        	if x_ == 10:
	        		l_num = l11
	        	if x_ == 11:
	        		l_num = l12
	        	if x_ == 12:
	        		l_num = l13
	        	screen.blit(x, l_num)
	    if y_block.collidepoint(mouse_pos) and click:
	        guess = 'y'
	        pygame.draw.rect(screen, white, (y_block))
	        if guess in word:

	        	y_ = word.index(guess)
	        	y = font4.render(word[y_], True, black)
	        	letterDrawer()
	        	if y_ == 0:
	        		l_num = l1
	        	if y_ == 1:
	        		l_num = l2
	        	if y_ == 2:
	        		l_num = l3
	        	if y_ == 3:
	        		l_num = l4
	        	if y_ == 4:
	        		l_num = l5
	        	if y_ == 5:
	        		l_num = l6
	        	if y_ == 6:
	        		l_num = l7
	        	if y_ == 7:
	        		l_num = l8
	        	if y_ == 8:
	        		l_num = l9
	        	if y_ == 9:
	        		l_num = l10
	        	if y_ == 10:
	        		l_num = l11
	        	if y_ == 11:
	        		l_num = l12
	        	if y_ == 12:
	        		l_num = l13
	        	screen.blit(y, l_num)
	    if z_block.collidepoint(mouse_pos) and click:
	        guess = 'z'
	        pygame.draw.rect(screen, white, (z_block))
	        if guess in word:

	        	z_ = word.index(guess)
	        	z = font4.render(word[z_], True, black)
	        	letterDrawer()
	        	if z_ == 0:
	        		l_num = l1
	        	if z_ == 1:
	        		l_num = l2
	        	if z_ == 2:
	        		l_num = l3
	        	if z_ == 3:
	        		l_num = l4
	        	if z_ == 4:
	        		l_num = l5
	        	if z_ == 5:
	        		l_num = l6
	        	if z_ == 6:
	        		l_num = l7
	        	if z_ == 7:
	        		l_num = l8
	        	if z_ == 8:
	        		l_num = l9
	        	if z_ == 9:
	        		l_num = l10
	        	if z_ == 10:
	        		l_num = l11
	        	if z_ == 11:
	        		l_num = l12
	        	if z_ == 12:
	        		l_num = l13
	        	screen.blit(z, l_num)

	    return guess

def letterDrawer():
	global a_
	if len(word) == 12:
	    l1 = (255,260)
	    l2 = (290,260)
	    l3 = (325,260)
	    l4 = (360,260)
	    l5 = (395,260)
	    l6 = (430,260)
	    l7 = (465,260)
	    l8 = (500,260)
	    l9 = (535,260)
	    l10 = (570,260)
	    l11 = (605,260)
	    l12 = (640,260)

	    a = font4.render(word[0], True, black)
	    b = font4.render(word[1], True, black)
	    c = font4.render(word[2], True, black)
	    d = font4.render(word[3], True, black)
	    e = font4.render(word[4], True, black)
	    f = font4.render(word[5], True, black)
	    g = font4.render(word[6], True, black)
	    h = font4.render(word[7], True, black)
	    i = font4.render(word[8], True, black)
	    j = font4.render(word[9], True, black)
	    k = font4.render(word[10], True, black)
	    l = font4.render(word[11], True, black)

	    '''screen.blit(a, l1)
	    screen.blit(b, l2)
	    screen.blit(c, l3)
	    screen.blit(d, l4)
	    screen.blit(e, l5)
	    screen.blit(f, l6)
	    screen.blit(g, l7)
	    screen.blit(h, l8)
	    screen.blit(i, l9)
	    screen.blit(j, l11)
	    screen.blit(k, l12)
	    screen.blit(l, l13)'''

	elif len(word) == 11:
	    l1 = (255,260)
	    l2 = (290,260)
	    l3 = (325,260)
	    l4 = (360,260)
	    l5 = (395,260)
	    l6 = (430,260)
	    l7 = (465,260)
	    l8 = (500,260)
	    l9 = (535,260)
	    l10 = (570,260)
	    l11 = (605,260)

	    a = font4.render(word[0], True, black)
	    b = font4.render(word[1], True, black)
	    c = font4.render(word[2], True, black)
	    d = font4.render(word[3], True, black)
	    e = font4.render(word[4], True, black)
	    f = font4.render(word[5], True, black)
	    g = font4.render(word[6], True, black)
	    h = font4.render(word[7], True, black)
	    i = font4.render(word[8], True, black)
	    j = font4.render(word[9], True, black)
	    k = font4.render(word[10], True, black)

	    '''screen.blit(a, l1)
	    screen.blit(b, l2)
	    screen.blit(c, l3)
	    screen.blit(d, l4)
	    screen.blit(e, l5)
	    screen.blit(f, l6)
	    screen.blit(g, l7)
	    screen.blit(h, l8)
	    screen.blit(i, l9)
	    screen.blit(j, l11)
	    screen.blit(k, l12)'''
	elif len(word) == 10:
	    l1 = (290,260)
	    l2 = (325,260)
	    l3 = (360,260)
	    l4 = (395,260)
	    l5 = (430,260)
	    l6 = (465,260)
	    l7 = (500,260)
	    l8 = (535,260)
	    l9 = (570,260)
	    l10 = (605,260)

	    a = font4.render(word[0], True, black)
	    b = font4.render(word[1], True, black)
	    c = font4.render(word[2], True, black)
	    d = font4.render(word[3], True, black)
	    e = font4.render(word[4], True, black)
	    f = font4.render(word[5], True, black)
	    g = font4.render(word[6], True, black)
	    h = font4.render(word[7], True, black)
	    i = font4.render(word[8], True, black)
	    j = font4.render(word[9], True, black)

	    '''screen.blit(a, l1)
	    screen.blit(b, l2)
	    screen.blit(c, l3)
	    screen.blit(d, l4)
	    screen.blit(e, l5)
	    screen.blit(f, l6)
	    screen.blit(g, l7)
	    screen.blit(h, l8)
	    screen.blit(i, l9)
	    screen.blit(j, l10)'''
	elif len(word) == 9:
	    l1 = (290,260)
	    l2 = (325,260)
	    l3 = (360,260)
	    l4 = (395,260)
	    l5 = (430,260)
	    l6 = (465,260)
	    l7 = (500,260)
	    l8 = (535,260)
	    l9 = (570,260)

	    a = font4.render(word[0], True, black)
	    b = font4.render(word[1], True, black)
	    c = font4.render(word[2], True, black)
	    d = font4.render(word[3], True, black)
	    e = font4.render(word[4], True, black)
	    f = font4.render(word[5], True, black)
	    g = font4.render(word[6], True, black)
	    h = font4.render(word[7], True, black)
	    i = font4.render(word[8], True, black)

	    '''screen.blit(a, l1)
	    screen.blit(b, l2)
	    screen.blit(c, l3)
	    screen.blit(d, l4)
	    screen.blit(e, l5)
	    screen.blit(f, l6)
	    screen.blit(g, l7)
	    screen.blit(h, l8)
	    screen.blit(i, l9)'''
	elif len(word) == 8:
	    l1 = (325,260)
	    l2 = (360,260)
	    l3 = (395,260)
	    l4 = (430,260)
	    l5 = (465,260)
	    l6 = (500,260)
	    l7 = (535,260)
	    l8 = (570,260)

	    a = font4.render(word[0], True, black)
	    b = font4.render(word[1], True, black)
	    c = font4.render(word[2], True, black)
	    d = font4.render(word[3], True, black)
	    e = font4.render(word[4], True, black)
	    f = font4.render(word[5], True, black)
	    g = font4.render(word[6], True, black)
	    h = font4.render(word[7], True, black)

	    '''screen.blit(a, l1)
	    screen.blit(b, l2)
	    screen.blit(c, l3)
	    screen.blit(d, l4)
	    screen.blit(e, l5)
	    screen.blit(f, l6)
	    screen.blit(g, l7)
	    screen.blit(h, l8)'''

	elif len(word) == 7:
	    l1 = (325,260)
	    l2 = (360,260)
	    l3 = (395,260)
	    l4 = (430,260)
	    l5 = (465,260)
	    l6 = (500,260)
	    l7 = (535,260)

	    a = font4.render(word[0], True, black)
	    b = font4.render(word[1], True, black)
	    c = font4.render(word[2], True, black)
	    d = font4.render(word[3], True, black)
	    e = font4.render(word[4], True, black)
	    f = font4.render(word[5], True, black)
	    g = font4.render(word[6], True, black)

	    '''screen.blit(a, l1)
	    screen.blit(b, l2)
	    screen.blit(c, l3)
	    screen.blit(d, l4)
	    screen.blit(e, l5)
	    screen.blit(f, l6)
	    screen.blit(g, l7)'''
	elif len(word) == 6:
	    l1 = (360,260)
	    l2 = (395,260)
	    l3 = (430,260)
	    l4 = (465,260)
	    l5 = (500,260)
	    l6 = (535,260)

	    a = font4.render(word[0], True, black)
	    b = font4.render(word[1], True, black)
	    c = font4.render(word[2], True, black)
	    d = font4.render(word[3], True, black)
	    e = font4.render(word[4], True, black)
	    f = font4.render(word[5], True, black)

	    '''screen.blit(a, l1)
	    screen.blit(b, l2)
	    screen.blit(c, l3)
	    screen.blit(d, l4)
	    screen.blit(e, l5)
	    screen.blit(f, l6)'''

	elif len(word) == 5:
	    l1 = (360,260)
	    l2 = (395,260)
	    l3 = (430,260)
	    l4 = (465,260)
	    l5 = (500,260)

	    a = font4.render(word[0], True, black)
	    b = font4.render(word[1], True, black)
	    c = font4.render(word[2], True, black)
	    d = font4.render(word[3], True, black)
	    e = font4.render(word[4], True, black)

	    '''screen.blit(a, l1)
	    screen.blit(b, l2)
	    screen.blit(c, l3)
	    screen.blit(d, l4)
	    screen.blit(e, l5)'''

	elif len(word) == 4:
	    l1 = (395,260)
	    l2 = (430,260)
	    l3 = (465,260)
	    l4 = (500,260)

	    a = font4.render(word[a_], True, black)
	    b = font4.render(word[a_], True, black)
	    c = font4.render(word[a_], True, black)
	    d = font4.render(word[a_], True, black)

	    '''screen.blit(a, l1)
	    screen.blit(b, l2)
	    screen.blit(c, l3)
	    screen.blit(d, l4)'''





game = True
lives = 10
click = False
correct_guess = 0
lives_txt = 10
draw_screen()
#main loop
while True:
	if click:
		guesses()
		click = False

	if guess in alphabet:
		if guess != '':
			alphabet.remove(guess)
			if guess in word:
				correct_guess += 1
				letterDrawer()
			if guess not in word:
				lives -= 1
				lives_txt -= 1
				lives_txt_render = font3.render("You have " + str(lives_txt) + " lives", True, black)
				pygame.draw.rect(screen, white, (lives_block))
				screen.blit(lives_txt_render, (5, 150))
				pygame.display.update()
				pass
			word2 = set(word)
			if correct_guess == len(word2):
				print('you won!')
				pygame.quit()
				sys.exit()

	if lives == 9:
		one = pygame.draw.line(screen, black, (20, 450), (200, 450), 4)
		pygame.display.update()
	elif lives == 8:
		two = pygame.draw.line(screen, black, (90, 450), (90, 220), 4)
		pygame.display.update()
	elif lives == 7:
		three = pygame.draw.line(screen, black, (90, 220), (200, 220), 4)
		pygame.display.update()
	elif lives == 6:
		four = pygame.draw.line(screen, black, (200, 220), (200, 250), 4)
		pygame.display.update()
	elif lives == 5:
		five = screen.blit(head,(150,250))
		pygame.display.update()
	elif lives == 4:
		six = pygame.draw.line(screen, black, (200, 335), (200, 375), 3)
		pygame.display.update()
	elif lives == 3:
		seven = pygame.draw.line(screen, black, (200, 375), (190, 420), 3)
		pygame.display.update()
	elif lives == 2:
		eight = pygame.draw.line(screen, black, (200, 375), (210, 420), 3)
		pygame.display.update()
	elif lives == 1:
		nine = pygame.draw.line(screen, black, (200, 340), (180, 380), 3)
		pygame.display.update()
	elif lives == 0:
		ten = pygame.draw.line(screen, black, (200, 340), (250, 330), 3)
		pygame.display.update()
		game = False


	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
		if event.type == pygame.MOUSEBUTTONDOWN :
			click = True
		if event.type == pygame.MOUSEBUTTONUP :
			click = False
         
	mouse_pos = pygame.mouse.get_pos()

	pygame.display.update()