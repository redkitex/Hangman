import pygame
import random
import sys
from pygame.locals import *
import pywhatkit

pygame.init()

# var definitions
game = True
screen = pygame.display.set_mode((725, 600))
lives = 10
pygame.display.set_caption('Hangman!')

with open("words.txt","r") as f:
	word_list = f.readlines()
word_list = [x.strip() for x in word_list]
word = random.choice(word_list)
actual_word = word
correct_guess = 0
alphabet = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x',
			'c', 'v', 'b', 'n', 'm']
heading = pygame.image.load("hangman_heading.png")
click = False
guess = ''
idk_var = True
mouse_pos = pygame.mouse.get_pos()
lives_txt = 10
head = pygame.image.load("head.png")
head2 = pygame.image.load("head2.png")
hints = 25

# colours
white = (255, 255, 255)
black = (0, 0, 0)
blue = (152, 211, 255)
yellow = (0, 124, 255)
grey = (202, 207, 210)
actual_yellow = (249, 230, 0)

# text...
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
restart = font3.render("RESTART", True, black) #text for restart button
hint_txt = font3.render("HINTS: " + str(hints), True, black) #text for hint button
lives_txt_render = font3.render("You have " + str(lives_txt) + " lives", True, black) #text for lives left
hint_block = pygame.Rect(475,135,90,30) #.Rect of hint button
restart_block = pygame.Rect(578,135,100,30) #.Rect of restart button
idk_txt = font3.render("That can't be a word!", True, black) #text for definition button
idk_block = pygame.Rect(475,178,203,30)

# DEFINE .Rect OF THE LETTER BLOCKS
a_block = pygame.Rect(5, 480, 50, 50)
b_block = pygame.Rect(60, 480, 50, 50)
c_block = pygame.Rect(115, 480, 50, 50)
d_block = pygame.Rect(170, 480, 50, 50)
e_block = pygame.Rect(225, 480, 50, 50)
f_block = pygame.Rect(280, 480, 50, 50)
g_block = pygame.Rect(335, 480, 50, 50)
h_block = pygame.Rect(390, 480, 50, 50)
i_block = pygame.Rect(445, 480, 50, 50)
j_block = pygame.Rect(500, 480, 50, 50)
k_block = pygame.Rect(555, 480, 50, 50)
l_block = pygame.Rect(610, 480, 50, 50)
m_block = pygame.Rect(665, 480, 50, 50)
n_block = pygame.Rect(5, 535, 50, 50)
o_block = pygame.Rect(60, 535, 50, 50)
p_block = pygame.Rect(115, 535, 50, 50)
q_block = pygame.Rect(170, 535, 50, 50)
r_block = pygame.Rect(225, 535, 50, 50)
s_block = pygame.Rect(280, 535, 50, 50)
t_block = pygame.Rect(335, 535, 50, 50)
u_block = pygame.Rect(390, 535, 50, 50)
v_block = pygame.Rect(445, 535, 50, 50)
w_block = pygame.Rect(500, 535, 50, 50)
x_block = pygame.Rect(555, 535, 50, 50)
y_block = pygame.Rect(610, 535, 50, 50)
z_block = pygame.Rect(665, 535, 50, 50)

lives_block = pygame.Rect(5, 155, 200, 20)

letter1 = True
letter2 = True
letter3 = True
letter4 = True
letter5 = True
letter6 = True
letter7 = True
letter8 = True
letter9 = True
letter10 = True
letter11 = True
letter12 = True

def draw_screen():

	letter1 = True
	letter2 = True
	letter3 = True
	letter4 = True
	letter5 = True
	letter6 = True
	letter7 = True
	letter8 = True
	letter9 = True
	letter10 = True
	letter11 = True
	letter12 = True

	screen.fill(white)
	screen.blit(heading, (5, 5))

	if len(word) == 12:
		pygame.draw.rect(screen, yellow, (245, 350, 300, 50))
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
		pygame.draw.rect(screen, yellow, (245, 350, 300, 50))
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
		pygame.draw.rect(screen, yellow, (280, 350, 300, 50))
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
		pygame.draw.rect(screen, yellow, (280, 350, 300, 50))
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
		pygame.draw.rect(screen, yellow, (315, 350, 300, 50))
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
		pygame.draw.rect(screen, yellow, (315, 350, 300, 50))
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
		pygame.draw.rect(screen, yellow, (350, 350, 300, 50))
		pygame.draw.rect(screen, black, (350, 350, 300, 50), 1)
		screen.blit(letter_6, (355, 350))
		pygame.draw.line(screen, black, (355, 300), (385, 300), 4)
		pygame.draw.line(screen, black, (390, 300), (420, 300), 4)
		pygame.draw.line(screen, black, (425, 300), (455, 300), 4)
		pygame.draw.line(screen, black, (460, 300), (490, 300), 4)
		pygame.draw.line(screen, black, (495, 300), (525, 300), 4)
		pygame.draw.line(screen, black, (530, 300), (560, 300), 4)

	if len(word) == 5:
		pygame.draw.rect(screen, yellow, (350, 350, 300, 50))
		pygame.draw.rect(screen, black, (350, 350, 300, 50), 1)
		screen.blit(letter_5, (355, 350))
		pygame.draw.line(screen, black, (355, 300), (385, 300), 4)
		pygame.draw.line(screen, black, (390, 300), (420, 300), 4)
		pygame.draw.line(screen, black, (425, 300), (455, 300), 4)
		pygame.draw.line(screen, black, (460, 300), (490, 300), 4)
		pygame.draw.line(screen, black, (495, 300), (525, 300), 4)

	if len(word) == 4:
		pygame.draw.rect(screen, yellow, (385, 350, 300, 50))
		pygame.draw.rect(screen, black, (385, 350, 300, 50), 1)
		screen.blit(letter_4, (390, 350))
		pygame.draw.line(screen, black, (390, 300), (420, 300), 4)
		pygame.draw.line(screen, black, (425, 300), (455, 300), 4)
		pygame.draw.line(screen, black, (460, 300), (490, 300), 4)
		pygame.draw.line(screen, black, (495, 300), (525, 300), 4)

	# DEFINE LETTERS
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
	pygame.draw.rect(screen, blue, q_block)
	pygame.draw.rect(screen, blue, w_block)
	pygame.draw.rect(screen, blue, e_block)
	pygame.draw.rect(screen, blue, r_block)
	pygame.draw.rect(screen, blue, t_block)
	pygame.draw.rect(screen, blue, y_block)
	pygame.draw.rect(screen, blue, u_block)
	pygame.draw.rect(screen, blue, i_block)
	pygame.draw.rect(screen, blue, o_block)
	pygame.draw.rect(screen, blue, p_block)
	pygame.draw.rect(screen, blue, a_block)
	pygame.draw.rect(screen, blue, s_block)
	pygame.draw.rect(screen, blue, d_block)
	pygame.draw.rect(screen, blue, f_block)
	pygame.draw.rect(screen, blue, g_block)
	pygame.draw.rect(screen, blue, h_block)
	pygame.draw.rect(screen, blue, j_block)
	pygame.draw.rect(screen, blue, k_block)
	pygame.draw.rect(screen, blue, l_block)
	pygame.draw.rect(screen, blue, z_block)
	pygame.draw.rect(screen, blue, x_block)
	pygame.draw.rect(screen, blue, c_block)
	pygame.draw.rect(screen, blue, v_block)
	pygame.draw.rect(screen, blue, b_block)
	pygame.draw.rect(screen, blue, n_block)
	pygame.draw.rect(screen, blue, m_block)
	# LETTER BLOCK BORDERS
	pygame.draw.rect(screen, black, q_block, 1)
	pygame.draw.rect(screen, black, (w_block), 1)
	pygame.draw.rect(screen, black, (e_block), 1)
	pygame.draw.rect(screen, black, r_block, 1)
	pygame.draw.rect(screen, black, (t_block), 1)
	pygame.draw.rect(screen, black, (y_block), 1)
	pygame.draw.rect(screen, black, (u_block), 1)
	pygame.draw.rect(screen, black, (i_block), 1)
	pygame.draw.rect(screen, black, (o_block), 1)
	pygame.draw.rect(screen, black, (p_block), 1)
	pygame.draw.rect(screen, black, (a_block), 1)
	pygame.draw.rect(screen, black, (s_block), 1)
	pygame.draw.rect(screen, black, (d_block), 1)
	pygame.draw.rect(screen, black, (f_block), 1)
	pygame.draw.rect(screen, black, (g_block), 1)
	pygame.draw.rect(screen, black, (h_block), 1)
	pygame.draw.rect(screen, black, (j_block), 1)
	pygame.draw.rect(screen, black, (k_block), 1)
	pygame.draw.rect(screen, black, (l_block), 1)
	pygame.draw.rect(screen, black, (z_block), 1)
	pygame.draw.rect(screen, black, (x_block), 1)
	pygame.draw.rect(screen, black, (c_block), 1)
	pygame.draw.rect(screen, black, (v_block), 1)
	pygame.draw.rect(screen, black, (b_block), 1)
	pygame.draw.rect(screen, black, (n_block), 1)
	pygame.draw.rect(screen, black, (m_block), 1)

	# restart block

	pygame.draw.rect(screen, grey, (restart_block))
	pygame.draw.rect(screen, black, (restart_block), 1)
	screen.blit(restart, (590,138))

	# hints block

	pygame.draw.rect(screen, actual_yellow, hint_block)
	pygame.draw.rect(screen, black, hint_block, 1)
	screen.blit(hint_txt, (480,138))

	# idk block

	pygame.draw.rect(screen, blue, idk_block)
	pygame.draw.rect(screen, black, idk_block, 1)
	screen.blit(idk_txt, (500, 180))


	# BLIT LETTERS
	screen.blit(aa, (15, 475))
	screen.blit(bb, (70, 475))
	screen.blit(cc, (125, 475))
	screen.blit(dd, (180, 475))
	screen.blit(ee, (235, 475))
	screen.blit(ff, (290, 475))
	screen.blit(gg, (345, 475))
	screen.blit(hh, (400, 475))
	screen.blit(ii, (455, 475))
	screen.blit(jj, (510, 475))
	screen.blit(kk, (565, 475))
	screen.blit(ll, (620, 475))
	screen.blit(mm, (675, 475))
	screen.blit(nn, (15, 535))
	screen.blit(oo, (70, 535))
	screen.blit(pp, (125, 535))
	screen.blit(qq, (180, 535))
	screen.blit(rr, (235, 535))
	screen.blit(ss, (290, 535))
	screen.blit(tt, (345, 535))
	screen.blit(uu, (400, 535))
	screen.blit(vv, (455, 535))
	screen.blit(ww, (510, 535))
	screen.blit(xx, (565, 535))
	screen.blit(yy, (620, 535))
	screen.blit(zz, (675, 535))

	

	lives_txt_render = font3.render("You have " + str(lives_txt) + " lives", True, black)
	pygame.draw.rect(screen, white, lives_block)
	screen.blit(lives_txt_render, (5, 150))
	

	

	pygame.display.update()


game = True
lives = 10
click = False
guess = ''



def guesses():
	global guess, click, mouse_pos, a_, l3, l_num, word, actual_word
	guess = ''
	for event in pygame.event.get():
		if event.type == pygame.MOUSEBUTTONDOWN:
			click = True
		if event.type == pygame.MOUSEBUTTONUP:
			click = False
	if game:
		if a_block.collidepoint(mouse_pos) and click:
			pygame.draw.rect(screen, white, (a_block))
			guess = 'a'
			if guess in actual_word:
				a_ = actual_word.index(guess)
				a = font4.render(actual_word[a_], True, black)
				if len(word) == 4:
					if a_ == 0:
						l_num = (395, 260)
					if a_ == 1:
						l_num = (430, 260)
					if a_ == 2:
						l_num = (465, 260)
					if a_ == 3:
						l_num = (500, 260)
				if len(word) == 5:
					if a_ == 0:
						l_num = (360, 260)
					if a_ == 1:
						l_num = (395, 260)
					if a_ == 2:
						l_num = (430, 260)
					if a_ == 3:
						l_num = (465, 260)
					if a_ == 4:
						l_num = (500, 260)
				if len(word) == 6:
					if a_ == 0:
						l_num = (360, 260)
					if a_ == 1:
						l_num = (395, 260)
					if a_ == 2:
						l_num = (430, 260)
					if a_ == 3:
						l_num = (465, 260)
					if a_ == 4:
						l_num = (500, 260)
					if a_ == 5:
						l_num = (535, 260)
				if len(word) == 7:
					if a_ == 0:
						l_num = (325, 260)
					if a_ == 1:
						l_num = (360, 260)
					if a_ == 2:
						l_num = (395, 260)
					if a_ == 3:
						l_num = (430, 260)
					if a_ == 4:
						l_num = (465, 260)
					if a_ == 5:
						l_num = (500, 260)
					if a_ == 6:
						l_num = (535, 260)
				if len(word) == 8:
					if a_ == 0:
						l_num = (325, 260)
					if a_ == 1:
						l_num = (360, 260)
					if a_ == 2:
						l_num = (395, 260)
					if a_ == 3:
						l_num = (430, 260)
					if a_ == 4:
						l_num = (465, 260)
					if a_ == 5:
						l_num = (500, 260)
					if a_ == 6:
						l_num = (535, 260)
					if a_ == 7:
						l_num = (570, 260)
				if len(word) == 9:
					if a_ == 0:
						l_num = (290, 260)
					if a_ == 1:
						l_num = (325, 260)
					if a_ == 2:
						l_num = (360, 260)
					if a_ == 3:
						l_num = (395, 260)
					if a_ == 4:
						l_num = (430, 260)
					if a_ == 5:
						l_num = (465, 260)
					if a_ == 6:
						l_num = (500, 260)
					if a_ == 7:
						l_num = (535, 260)
					if a_ == 8:
						l_num = (570, 260)
				if len(word) == 10:
					if a_ == 0:
						l_num = (290, 260)
					if a_ == 1:
						l_num = (325, 260)
					if a_ == 2:
						l_num = (360, 260)
					if a_ == 3:
						l_num = (395, 260)
					if a_ == 4:
						l_num = (430, 260)
					if a_ == 5:
						l_num = (465, 260)
					if a_ == 6:
						l_num = (500, 260)
					if a_ == 7:
						l_num = (535, 260)
					if a_ == 8:
						l_num = (570, 260)
					if a_ == 9:
						l_num = (605, 260)
				if len(word) == 11:
					if a_ == 0:
						l_num = (255, 260)
					if a_ == 1:
						l_num = (290, 260)
					if a_ == 2:
						l_num = (325, 260)
					if a_ == 3:
						l_num = (360, 260)
					if a_ == 4:
						l_num = (395, 260)
					if a_ == 5:
						l_num = (430, 260)
					if a_ == 6:
						l_num = (465, 260)
					if a_ == 7:
						l_num = (500, 260)
					if a_ == 8:
						l_num = (535, 260)
					if a_ == 9:
						l_num = (570, 260)
					if a_ == 10:
						l_num = (605, 260)
				if len(word) == 12:
					if a_ == 0:
						l_num = (255, 260)
					if a_ == 1:
						l_num = (290, 260)
					if a_ == 2:
						l_num = (325, 260)
					if a_ == 3:
						l_num = (360, 260)
					if a_ == 4:
						l_num = (395, 260)
					if a_ == 5:
						l_num = (430, 260)
					if a_ == 6:
						l_num = (465, 260)
					if a_ == 7:
						l_num = (500, 260)
					if a_ == 8:
						l_num = (535, 260)
					if a_ == 9:
						l_num = (570, 260)
					if a_ == 10:
						l_num = (605, 260)
					if a_ == 11:
						l_num = (640, 260)

				screen.blit(a, l_num)
				word100()

		if b_block.collidepoint(mouse_pos) and click:
			guess = 'b'
			pygame.draw.rect(screen, white, (b_block))
			if guess in actual_word:
				a_ = actual_word.index(guess)
				a = font4.render(actual_word[a_], True, black)
				if len(word) == 4:
					if a_ == 0:
						l_num = (395, 260)
					if a_ == 1:
						l_num = (430, 260)
					if a_ == 2:
						l_num = (465, 260)
					if a_ == 3:
						l_num = (500, 260)
				if len(word) == 5:
					if a_ == 0:
						l_num = (360, 260)
					if a_ == 1:
						l_num = (395, 260)
					if a_ == 2:
						l_num = (430, 260)
					if a_ == 3:
						l_num = (465, 260)
					if a_ == 4:
						l_num = (500, 260)
				if len(word) == 6:
					if a_ == 0:
						l_num = (360, 260)
					if a_ == 1:
						l_num = (395, 260)
					if a_ == 2:
						l_num = (430, 260)
					if a_ == 3:
						l_num = (465, 260)
					if a_ == 4:
						l_num = (500, 260)
					if a_ == 5:
						l_num = (535, 260)
				if len(word) == 7:
					if a_ == 0:
						l_num = (325, 260)
					if a_ == 1:
						l_num = (360, 260)
					if a_ == 2:
						l_num = (395, 260)
					if a_ == 3:
						l_num = (430, 260)
					if a_ == 4:
						l_num = (465, 260)
					if a_ == 5:
						l_num = (500, 260)
					if a_ == 6:
						l_num = (535, 260)
				if len(word) == 8:
					if a_ == 0:
						l_num = (325, 260)
					if a_ == 1:
						l_num = (360, 260)
					if a_ == 2:
						l_num = (395, 260)
					if a_ == 3:
						l_num = (430, 260)
					if a_ == 4:
						l_num = (465, 260)
					if a_ == 5:
						l_num = (500, 260)
					if a_ == 6:
						l_num = (535, 260)
					if a_ == 7:
						l_num = (570, 260)
				if len(word) == 9:
					if a_ == 0:
						l_num = (290, 260)
					if a_ == 1:
						l_num = (325, 260)
					if a_ == 2:
						l_num = (360, 260)
					if a_ == 3:
						l_num = (395, 260)
					if a_ == 4:
						l_num = (430, 260)
					if a_ == 5:
						l_num = (465, 260)
					if a_ == 6:
						l_num = (500, 260)
					if a_ == 7:
						l_num = (535, 260)
					if a_ == 8:
						l_num = (570, 260)
				if len(word) == 10:
					if a_ == 0:
						l_num = (290, 260)
					if a_ == 1:
						l_num = (325, 260)
					if a_ == 2:
						l_num = (360, 260)
					if a_ == 3:
						l_num = (395, 260)
					if a_ == 4:
						l_num = (430, 260)
					if a_ == 5:
						l_num = (465, 260)
					if a_ == 6:
						l_num = (500, 260)
					if a_ == 7:
						l_num = (535, 260)
					if a_ == 8:
						l_num = (370, 260)
					if a_ == 9:
						l_num = (605, 260)
				if len(word) == 11:
					if a_ == 0:
						l_num = (255, 260)
					if a_ == 1:
						l_num = (290, 260)
					if a_ == 2:
						l_num = (325, 260)
					if a_ == 3:
						l_num = (360, 260)
					if a_ == 4:
						l_num = (395, 260)
					if a_ == 5:
						l_num = (430, 260)
					if a_ == 6:
						l_num = (465, 260)
					if a_ == 7:
						l_num = (500, 260)
					if a_ == 8:
						l_num = (535, 260)
					if a_ == 9:
						l_num = (570, 260)
					if a_ == 10:
						l_num = (605, 260)
				if len(word) == 12:
					if a_ == 0:
						l_num = (255, 260)
					if a_ == 1:
						l_num = (290, 260)
					if a_ == 2:
						l_num = (325, 260)
					if a_ == 3:
						l_num = (360, 260)
					if a_ == 4:
						l_num = (395, 260)
					if a_ == 5:
						l_num = (430, 260)
					if a_ == 6:
						l_num = (465, 260)
					if a_ == 7:
						l_num = (500, 260)
					if a_ == 8:
						l_num = (535, 260)
					if a_ == 9:
						l_num = (570, 260)
					if a_ == 10:
						l_num = (605, 260)
					if a_ == 11:
						l_num = (640, 260)

				screen.blit(a, l_num)
				word100()

		if c_block.collidepoint(mouse_pos) and click:
			guess = 'c'
			pygame.draw.rect(screen, white, (c_block))
			if guess in actual_word:
				a_ = actual_word.index(guess)
				a = font4.render(actual_word[a_], True, black)
				if len(word) == 4:
					if a_ == 0:
						l_num = (395, 260)
					if a_ == 1:
						l_num = (430, 260)
					if a_ == 2:
						l_num = (465, 260)
					if a_ == 3:
						l_num = (500, 260)
				if len(word) == 5:
					if a_ == 0:
						l_num = (360, 260)
					if a_ == 1:
						l_num = (395, 260)
					if a_ == 2:
						l_num = (430, 260)
					if a_ == 3:
						l_num = (465, 260)
					if a_ == 4:
						l_num = (500, 260)
				if len(word) == 6:
					if a_ == 0:
						l_num = (360, 260)
					if a_ == 1:
						l_num = (395, 260)
					if a_ == 2:
						l_num = (430, 260)
					if a_ == 3:
						l_num = (465, 260)
					if a_ == 4:
						l_num = (500, 260)
					if a_ == 5:
						l_num = (535, 260)
				if len(word) == 7:
					if a_ == 0:
						l_num = (325, 260)
					if a_ == 1:
						l_num = (360, 260)
					if a_ == 2:
						l_num = (395, 260)
					if a_ == 3:
						l_num = (430, 260)
					if a_ == 4:
						l_num = (465, 260)
					if a_ == 5:
						l_num = (500, 260)
					if a_ == 6:
						l_num = (535, 260)
				if len(word) == 8:
					if a_ == 0:
						l_num = (325, 260)
					if a_ == 1:
						l_num = (360, 260)
					if a_ == 2:
						l_num = (395, 260)
					if a_ == 3:
						l_num = (430, 260)
					if a_ == 4:
						l_num = (465, 260)
					if a_ == 5:
						l_num = (500, 260)
					if a_ == 6:
						l_num = (535, 260)
					if a_ == 7:
						l_num = (570, 260)
				if len(word) == 9:
					if a_ == 0:
						l_num = (290, 260)
					if a_ == 1:
						l_num = (325, 260)
					if a_ == 2:
						l_num = (360, 260)
					if a_ == 3:
						l_num = (395, 260)
					if a_ == 4:
						l_num = (430, 260)
					if a_ == 5:
						l_num = (465, 260)
					if a_ == 6:
						l_num = (500, 260)
					if a_ == 7:
						l_num = (535, 260)
					if a_ == 8:
						l_num = (570, 260)
				if len(word) == 10:
					if a_ == 0:
						l_num = (290, 260)
					if a_ == 1:
						l_num = (325, 260)
					if a_ == 2:
						l_num = (360, 260)
					if a_ == 3:
						l_num = (395, 260)
					if a_ == 4:
						l_num = (430, 260)
					if a_ == 5:
						l_num = (465, 260)
					if a_ == 6:
						l_num = (500, 260)
					if a_ == 7:
						l_num = (535, 260)
					if a_ == 8:
						l_num = (370, 260)
					if a_ == 9:
						l_num = (605, 260)
				if len(word) == 11:
					if a_ == 0:
						l_num = (255, 260)
					if a_ == 1:
						l_num = (290, 260)
					if a_ == 2:
						l_num = (325, 260)
					if a_ == 3:
						l_num = (360, 260)
					if a_ == 4:
						l_num = (395, 260)
					if a_ == 5:
						l_num = (430, 260)
					if a_ == 6:
						l_num = (465, 260)
					if a_ == 7:
						l_num = (500, 260)
					if a_ == 8:
						l_num = (535, 260)
					if a_ == 9:
						l_num = (570, 260)
					if a_ == 10:
						l_num = (605, 260)
				if len(word) == 12:
					if a_ == 0:
						l_num = (255, 260)
					if a_ == 1:
						l_num = (290, 260)
					if a_ == 2:
						l_num = (325, 260)
					if a_ == 3:
						l_num = (360, 260)
					if a_ == 4:
						l_num = (395, 260)
					if a_ == 5:
						l_num = (430, 260)
					if a_ == 6:
						l_num = (465, 260)
					if a_ == 7:
						l_num = (500, 260)
					if a_ == 8:
						l_num = (535, 260)
					if a_ == 9:
						l_num = (570, 260)
					if a_ == 10:
						l_num = (605, 260)
					if a_ == 11:
						l_num = (640, 260)

				screen.blit(a, l_num)
				word100()

		if d_block.collidepoint(mouse_pos) and click:
			guess = 'd'
			pygame.draw.rect(screen, white, d_block)
			if guess in actual_word:
				a_ = actual_word.index(guess)
				a = font4.render(actual_word[a_], True, black)
				if len(word) == 4:
					if a_ == 0:
						l_num = (395, 260)
					if a_ == 1:
						l_num = (430, 260)
					if a_ == 2:
						l_num = (465, 260)
					if a_ == 3:
						l_num = (500, 260)
				if len(word) == 5:
					if a_ == 0:
						l_num = (360, 260)
					if a_ == 1:
						l_num = (395, 260)
					if a_ == 2:
						l_num = (430, 260)
					if a_ == 3:
						l_num = (465, 260)
					if a_ == 4:
						l_num = (500, 260)
				if len(word) == 6:
					if a_ == 0:
						l_num = (360, 260)
					if a_ == 1:
						l_num = (395, 260)
					if a_ == 2:
						l_num = (430, 260)
					if a_ == 3:
						l_num = (465, 260)
					if a_ == 4:
						l_num = (500, 260)
					if a_ == 5:
						l_num = (535, 260)
				if len(word) == 7:
					if a_ == 0:
						l_num = (325, 260)
					if a_ == 1:
						l_num = (360, 260)
					if a_ == 2:
						l_num = (395, 260)
					if a_ == 3:
						l_num = (430, 260)
					if a_ == 4:
						l_num = (465, 260)
					if a_ == 5:
						l_num = (500, 260)
					if a_ == 6:
						l_num = (535, 260)
				if len(word) == 8:
					if a_ == 0:
						l_num = (325, 260)
					if a_ == 1:
						l_num = (360, 260)
					if a_ == 2:
						l_num = (395, 260)
					if a_ == 3:
						l_num = (430, 260)
					if a_ == 4:
						l_num = (465, 260)
					if a_ == 5:
						l_num = (500, 260)
					if a_ == 6:
						l_num = (535, 260)
					if a_ == 7:
						l_num = (570, 260)
				if len(word) == 9:
					if a_ == 0:
						l_num = (290, 260)
					if a_ == 1:
						l_num = (325, 260)
					if a_ == 2:
						l_num = (360, 260)
					if a_ == 3:
						l_num = (395, 260)
					if a_ == 4:
						l_num = (430, 260)
					if a_ == 5:
						l_num = (465, 260)
					if a_ == 6:
						l_num = (500, 260)
					if a_ == 7:
						l_num = (535, 260)
					if a_ == 8:
						l_num = (570, 260)
				if len(word) == 10:
					if a_ == 0:
						l_num = (290, 260)
					if a_ == 1:
						l_num = (325, 260)
					if a_ == 2:
						l_num = (360, 260)
					if a_ == 3:
						l_num = (395, 260)
					if a_ == 4:
						l_num = (430, 260)
					if a_ == 5:
						l_num = (465, 260)
					if a_ == 6:
						l_num = (500, 260)
					if a_ == 7:
						l_num = (535, 260)
					if a_ == 8:
						l_num = (370, 260)
					if a_ == 9:
						l_num = (605, 260)
				if len(word) == 11:
					if a_ == 0:
						l_num = (255, 260)
					if a_ == 1:
						l_num = (290, 260)
					if a_ == 2:
						l_num = (325, 260)
					if a_ == 3:
						l_num = (360, 260)
					if a_ == 4:
						l_num = (395, 260)
					if a_ == 5:
						l_num = (430, 260)
					if a_ == 6:
						l_num = (465, 260)
					if a_ == 7:
						l_num = (500, 260)
					if a_ == 8:
						l_num = (535, 260)
					if a_ == 9:
						l_num = (570, 260)
					if a_ == 10:
						l_num = (605, 260)
				if len(word) == 12:
					if a_ == 0:
						l_num = (255, 260)
					if a_ == 1:
						l_num = (290, 260)
					if a_ == 2:
						l_num = (325, 260)
					if a_ == 3:
						l_num = (360, 260)
					if a_ == 4:
						l_num = (395, 260)
					if a_ == 5:
						l_num = (430, 260)
					if a_ == 6:
						l_num = (465, 260)
					if a_ == 7:
						l_num = (500, 260)
					if a_ == 8:
						l_num = (535, 260)
					if a_ == 9:
						l_num = (570, 260)
					if a_ == 10:
						l_num = (605, 260)
					if a_ == 11:
						l_num = (640, 260)

				screen.blit(a, l_num)
				word100()

		if e_block.collidepoint(mouse_pos) and click:
			guess = 'e'
			pygame.draw.rect(screen, white, (e_block))
			if guess in actual_word:
				a_ = actual_word.index(guess)
				a = font4.render(actual_word[a_], True, black)
				if len(word) == 4:
					if a_ == 0:
						l_num = (395, 260)
					if a_ == 1:
						l_num = (430, 260)
					if a_ == 2:
						l_num = (465, 260)
					if a_ == 3:
						l_num = (500, 260)
				if len(word) == 5:
					if a_ == 0:
						l_num = (360, 260)
					if a_ == 1:
						l_num = (395, 260)
					if a_ == 2:
						l_num = (430, 260)
					if a_ == 3:
						l_num = (465, 260)
					if a_ == 4:
						l_num = (500, 260)
				if len(word) == 6:
					if a_ == 0:
						l_num = (360, 260)
					if a_ == 1:
						l_num = (395, 260)
					if a_ == 2:
						l_num = (430, 260)
					if a_ == 3:
						l_num = (465, 260)
					if a_ == 4:
						l_num = (500, 260)
					if a_ == 5:
						l_num = (535, 260)
				if len(word) == 7:
					if a_ == 0:
						l_num = (325, 260)
					if a_ == 1:
						l_num = (360, 260)
					if a_ == 2:
						l_num = (395, 260)
					if a_ == 3:
						l_num = (430, 260)
					if a_ == 4:
						l_num = (465, 260)
					if a_ == 5:
						l_num = (500, 260)
					if a_ == 6:
						l_num = (535, 260)
				if len(word) == 8:
					if a_ == 0:
						l_num = (325, 260)
					if a_ == 1:
						l_num = (360, 260)
					if a_ == 2:
						l_num = (395, 260)
					if a_ == 3:
						l_num = (430, 260)
					if a_ == 4:
						l_num = (465, 260)
					if a_ == 5:
						l_num = (500, 260)
					if a_ == 6:
						l_num = (535, 260)
					if a_ == 7:
						l_num = (570, 260)
				if len(word) == 9:
					if a_ == 0:
						l_num = (290, 260)
					if a_ == 1:
						l_num = (325, 260)
					if a_ == 2:
						l_num = (360, 260)
					if a_ == 3:
						l_num = (395, 260)
					if a_ == 4:
						l_num = (430, 260)
					if a_ == 5:
						l_num = (465, 260)
					if a_ == 6:
						l_num = (500, 260)
					if a_ == 7:
						l_num = (535, 260)
					if a_ == 8:
						l_num = (570, 260)
				if len(word) == 10:
					if a_ == 0:
						l_num = (290, 260)
					if a_ == 1:
						l_num = (325, 260)
					if a_ == 2:
						l_num = (360, 260)
					if a_ == 3:
						l_num = (395, 260)
					if a_ == 4:
						l_num = (430, 260)
					if a_ == 5:
						l_num = (465, 260)
					if a_ == 6:
						l_num = (500, 260)
					if a_ == 7:
						l_num = (535, 260)
					if a_ == 8:
						l_num = (370, 260)
					if a_ == 9:
						l_num = (605, 260)
				if len(word) == 11:
					if a_ == 0:
						l_num = (255, 260)
					if a_ == 1:
						l_num = (290, 260)
					if a_ == 2:
						l_num = (325, 260)
					if a_ == 3:
						l_num = (360, 260)
					if a_ == 4:
						l_num = (395, 260)
					if a_ == 5:
						l_num = (430, 260)
					if a_ == 6:
						l_num = (465, 260)
					if a_ == 7:
						l_num = (500, 260)
					if a_ == 8:
						l_num = (535, 260)
					if a_ == 9:
						l_num = (570, 260)
					if a_ == 10:
						l_num = (605, 260)
				if len(word) == 12:
					if a_ == 0:
						l_num = (255, 260)
					if a_ == 1:
						l_num = (290, 260)
					if a_ == 2:
						l_num = (325, 260)
					if a_ == 3:
						l_num = (360, 260)
					if a_ == 4:
						l_num = (395, 260)
					if a_ == 5:
						l_num = (430, 260)
					if a_ == 6:
						l_num = (465, 260)
					if a_ == 7:
						l_num = (500, 260)
					if a_ == 8:
						l_num = (535, 260)
					if a_ == 9:
						l_num = (570, 260)
					if a_ == 10:
						l_num = (605, 260)
					if a_ == 11:
						l_num = (640, 260)

				screen.blit(a, l_num)
				word100()

		if f_block.collidepoint(mouse_pos) and click:
			guess = 'f'
			pygame.draw.rect(screen, white, (f_block))
			if guess in actual_word:
				a_ = actual_word.index(guess)
				a = font4.render(actual_word[a_], True, black)
				if len(word) == 4:
					if a_ == 0:
						l_num = (395, 260)
					if a_ == 1:
						l_num = (430, 260)
					if a_ == 2:
						l_num = (465, 260)
					if a_ == 3:
						l_num = (500, 260)
				if len(word) == 5:
					if a_ == 0:
						l_num = (360, 260)
					if a_ == 1:
						l_num = (395, 260)
					if a_ == 2:
						l_num = (430, 260)
					if a_ == 3:
						l_num = (465, 260)
					if a_ == 4:
						l_num = (500, 260)
				if len(word) == 6:
					if a_ == 0:
						l_num = (360, 260)
					if a_ == 1:
						l_num = (395, 260)
					if a_ == 2:
						l_num = (430, 260)
					if a_ == 3:
						l_num = (465, 260)
					if a_ == 4:
						l_num = (500, 260)
					if a_ == 5:
						l_num = (535, 260)
				if len(word) == 7:
					if a_ == 0:
						l_num = (325, 260)
					if a_ == 1:
						l_num = (360, 260)
					if a_ == 2:
						l_num = (395, 260)
					if a_ == 3:
						l_num = (430, 260)
					if a_ == 4:
						l_num = (465, 260)
					if a_ == 5:
						l_num = (500, 260)
					if a_ == 6:
						l_num = (535, 260)
				if len(word) == 8:
					if a_ == 0:
						l_num = (325, 260)
					if a_ == 1:
						l_num = (360, 260)
					if a_ == 2:
						l_num = (395, 260)
					if a_ == 3:
						l_num = (430, 260)
					if a_ == 4:
						l_num = (465, 260)
					if a_ == 5:
						l_num = (500, 260)
					if a_ == 6:
						l_num = (535, 260)
					if a_ == 7:
						l_num = (570, 260)
				if len(word) == 9:
					if a_ == 0:
						l_num = (290, 260)
					if a_ == 1:
						l_num = (325, 260)
					if a_ == 2:
						l_num = (360, 260)
					if a_ == 3:
						l_num = (395, 260)
					if a_ == 4:
						l_num = (430, 260)
					if a_ == 5:
						l_num = (465, 260)
					if a_ == 6:
						l_num = (500, 260)
					if a_ == 7:
						l_num = (535, 260)
					if a_ == 8:
						l_num = (570, 260)
				if len(word) == 10:
					if a_ == 0:
						l_num = (290, 260)
					if a_ == 1:
						l_num = (325, 260)
					if a_ == 2:
						l_num = (360, 260)
					if a_ == 3:
						l_num = (395, 260)
					if a_ == 4:
						l_num = (430, 260)
					if a_ == 5:
						l_num = (465, 260)
					if a_ == 6:
						l_num = (500, 260)
					if a_ == 7:
						l_num = (535, 260)
					if a_ == 8:
						l_num = (370, 260)
					if a_ == 9:
						l_num = (605, 260)
				if len(word) == 11:
					if a_ == 0:
						l_num = (255, 260)
					if a_ == 1:
						l_num = (290, 260)
					if a_ == 2:
						l_num = (325, 260)
					if a_ == 3:
						l_num = (360, 260)
					if a_ == 4:
						l_num = (395, 260)
					if a_ == 5:
						l_num = (430, 260)
					if a_ == 6:
						l_num = (465, 260)
					if a_ == 7:
						l_num = (500, 260)
					if a_ == 8:
						l_num = (535, 260)
					if a_ == 9:
						l_num = (570, 260)
					if a_ == 10:
						l_num = (605, 260)
				if len(word) == 12:
					if a_ == 0:
						l_num = (255, 260)
					if a_ == 1:
						l_num = (290, 260)
					if a_ == 2:
						l_num = (325, 260)
					if a_ == 3:
						l_num = (360, 260)
					if a_ == 4:
						l_num = (395, 260)
					if a_ == 5:
						l_num = (430, 260)
					if a_ == 6:
						l_num = (465, 260)
					if a_ == 7:
						l_num = (500, 260)
					if a_ == 8:
						l_num = (535, 260)
					if a_ == 9:
						l_num = (570, 260)
					if a_ == 10:
						l_num = (605, 260)
					if a_ == 11:
						l_num = (640, 260)

				screen.blit(a, l_num)
				word100()


		if g_block.collidepoint(mouse_pos) and click:
			guess = 'g'
			pygame.draw.rect(screen, white, (g_block))
			if guess in actual_word:
				a_ = actual_word.index(guess)
				a = font4.render(actual_word[a_], True, black)
				if len(word) == 4:
					if a_ == 0:
						l_num = (395, 260)
					if a_ == 1:
						l_num = (430, 260)
					if a_ == 2:
						l_num = (465, 260)
					if a_ == 3:
						l_num = (500, 260)
				if len(word) == 5:
					if a_ == 0:
						l_num = (360, 260)
					if a_ == 1:
						l_num = (395, 260)
					if a_ == 2:
						l_num = (430, 260)
					if a_ == 3:
						l_num = (465, 260)
					if a_ == 4:
						l_num = (500, 260)
				if len(word) == 6:
					if a_ == 0:
						l_num = (360, 260)
					if a_ == 1:
						l_num = (395, 260)
					if a_ == 2:
						l_num = (430, 260)
					if a_ == 3:
						l_num = (465, 260)
					if a_ == 4:
						l_num = (500, 260)
					if a_ == 5:
						l_num = (535, 260)
				if len(word) == 7:
					if a_ == 0:
						l_num = (325, 260)
					if a_ == 1:
						l_num = (360, 260)
					if a_ == 2:
						l_num = (395, 260)
					if a_ == 3:
						l_num = (430, 260)
					if a_ == 4:
						l_num = (465, 260)
					if a_ == 5:
						l_num = (500, 260)
					if a_ == 6:
						l_num = (535, 260)
				if len(word) == 8:
					if a_ == 0:
						l_num = (325, 260)
					if a_ == 1:
						l_num = (360, 260)
					if a_ == 2:
						l_num = (395, 260)
					if a_ == 3:
						l_num = (430, 260)
					if a_ == 4:
						l_num = (465, 260)
					if a_ == 5:
						l_num = (500, 260)
					if a_ == 6:
						l_num = (535, 260)
					if a_ == 7:
						l_num = (570, 260)
				if len(word) == 9:
					if a_ == 0:
						l_num = (290, 260)
					if a_ == 1:
						l_num = (325, 260)
					if a_ == 2:
						l_num = (360, 260)
					if a_ == 3:
						l_num = (395, 260)
					if a_ == 4:
						l_num = (430, 260)
					if a_ == 5:
						l_num = (465, 260)
					if a_ == 6:
						l_num = (500, 260)
					if a_ == 7:
						l_num = (535, 260)
					if a_ == 8:
						l_num = (570, 260)
				if len(word) == 10:
					if a_ == 0:
						l_num = (290, 260)
					if a_ == 1:
						l_num = (325, 260)
					if a_ == 2:
						l_num = (360, 260)
					if a_ == 3:
						l_num = (395, 260)
					if a_ == 4:
						l_num = (430, 260)
					if a_ == 5:
						l_num = (465, 260)
					if a_ == 6:
						l_num = (500, 260)
					if a_ == 7:
						l_num = (535, 260)
					if a_ == 8:
						l_num = (370, 260)
					if a_ == 9:
						l_num = (605, 260)
				if len(word) == 11:
					if a_ == 0:
						l_num = (255, 260)
					if a_ == 1:
						l_num = (290, 260)
					if a_ == 2:
						l_num = (325, 260)
					if a_ == 3:
						l_num = (360, 260)
					if a_ == 4:
						l_num = (395, 260)
					if a_ == 5:
						l_num = (430, 260)
					if a_ == 6:
						l_num = (465, 260)
					if a_ == 7:
						l_num = (500, 260)
					if a_ == 8:
						l_num = (535, 260)
					if a_ == 9:
						l_num = (570, 260)
					if a_ == 10:
						l_num = (605, 260)
				if len(word) == 12:
					if a_ == 0:
						l_num = (255, 260)
					if a_ == 1:
						l_num = (290, 260)
					if a_ == 2:
						l_num = (325, 260)
					if a_ == 3:
						l_num = (360, 260)
					if a_ == 4:
						l_num = (395, 260)
					if a_ == 5:
						l_num = (430, 260)
					if a_ == 6:
						l_num = (465, 260)
					if a_ == 7:
						l_num = (500, 260)
					if a_ == 8:
						l_num = (535, 260)
					if a_ == 9:
						l_num = (570, 260)
					if a_ == 10:
						l_num = (605, 260)
					if a_ == 11:
						l_num = (640, 260)

				screen.blit(a, l_num)
				word100()

		if h_block.collidepoint(mouse_pos) and click:
			guess = 'h'
			pygame.draw.rect(screen, white, (h_block))
			if guess in actual_word:
				a_ = actual_word.index(guess)
				a = font4.render(actual_word[a_], True, black)
				if len(word) == 4:
					if a_ == 0:
						l_num = (395, 260)
					if a_ == 1:
						l_num = (430, 260)
					if a_ == 2:
						l_num = (465, 260)
					if a_ == 3:
						l_num = (500, 260)
				if len(word) == 5:
					if a_ == 0:
						l_num = (360, 260)
					if a_ == 1:
						l_num = (395, 260)
					if a_ == 2:
						l_num = (430, 260)
					if a_ == 3:
						l_num = (465, 260)
					if a_ == 4:
						l_num = (500, 260)
				if len(word) == 6:
					if a_ == 0:
						l_num = (360, 260)
					if a_ == 1:
						l_num = (395, 260)
					if a_ == 2:
						l_num = (430, 260)
					if a_ == 3:
						l_num = (465, 260)
					if a_ == 4:
						l_num = (500, 260)
					if a_ == 5:
						l_num = (535, 260)
				if len(word) == 7:
					if a_ == 0:
						l_num = (325, 260)
					if a_ == 1:
						l_num = (360, 260)
					if a_ == 2:
						l_num = (395, 260)
					if a_ == 3:
						l_num = (430, 260)
					if a_ == 4:
						l_num = (465, 260)
					if a_ == 5:
						l_num = (500, 260)
					if a_ == 6:
						l_num = (535, 260)
				if len(word) == 8:
					if a_ == 0:
						l_num = (325, 260)
					if a_ == 1:
						l_num = (360, 260)
					if a_ == 2:
						l_num = (395, 260)
					if a_ == 3:
						l_num = (430, 260)
					if a_ == 4:
						l_num = (465, 260)
					if a_ == 5:
						l_num = (500, 260)
					if a_ == 6:
						l_num = (535, 260)
					if a_ == 7:
						l_num = (570, 260)
				if len(word) == 9:
					if a_ == 0:
						l_num = (290, 260)
					if a_ == 1:
						l_num = (325, 260)
					if a_ == 2:
						l_num = (360, 260)
					if a_ == 3:
						l_num = (395, 260)
					if a_ == 4:
						l_num = (430, 260)
					if a_ == 5:
						l_num = (465, 260)
					if a_ == 6:
						l_num = (500, 260)
					if a_ == 7:
						l_num = (535, 260)
					if a_ == 8:
						l_num = (570, 260)
				if len(word) == 10:
					if a_ == 0:
						l_num = (290, 260)
					if a_ == 1:
						l_num = (325, 260)
					if a_ == 2:
						l_num = (360, 260)
					if a_ == 3:
						l_num = (395, 260)
					if a_ == 4:
						l_num = (430, 260)
					if a_ == 5:
						l_num = (465, 260)
					if a_ == 6:
						l_num = (500, 260)
					if a_ == 7:
						l_num = (535, 260)
					if a_ == 8:
						l_num = (370, 260)
					if a_ == 9:
						l_num = (605, 260)
				if len(word) == 11:
					if a_ == 0:
						l_num = (255, 260)
					if a_ == 1:
						l_num = (290, 260)
					if a_ == 2:
						l_num = (325, 260)
					if a_ == 3:
						l_num = (360, 260)
					if a_ == 4:
						l_num = (395, 260)
					if a_ == 5:
						l_num = (430, 260)
					if a_ == 6:
						l_num = (465, 260)
					if a_ == 7:
						l_num = (500, 260)
					if a_ == 8:
						l_num = (535, 260)
					if a_ == 9:
						l_num = (570, 260)
					if a_ == 10:
						l_num = (605, 260)
				if len(word) == 12:
					if a_ == 0:
						l_num = (255, 260)
					if a_ == 1:
						l_num = (290, 260)
					if a_ == 2:
						l_num = (325, 260)
					if a_ == 3:
						l_num = (360, 260)
					if a_ == 4:
						l_num = (395, 260)
					if a_ == 5:
						l_num = (430, 260)
					if a_ == 6:
						l_num = (465, 260)
					if a_ == 7:
						l_num = (500, 260)
					if a_ == 8:
						l_num = (535, 260)
					if a_ == 9:
						l_num = (570, 260)
					if a_ == 10:
						l_num = (605, 260)
					if a_ == 11:
						l_num = (640, 260)

				screen.blit(a, l_num)
				word100()

		if i_block.collidepoint(mouse_pos) and click:
			guess = 'i'
			pygame.draw.rect(screen, white, (i_block))
			if guess in actual_word:
				a_ = actual_word.index(guess)
				a = font4.render(actual_word[a_], True, black)
				if len(word) == 4:
					if a_ == 0:
						l_num = (395, 260)
					if a_ == 1:
						l_num = (430, 260)
					if a_ == 2:
						l_num = (465, 260)
					if a_ == 3:
						l_num = (500, 260)
				if len(word) == 5:
					if a_ == 0:
						l_num = (360, 260)
					if a_ == 1:
						l_num = (395, 260)
					if a_ == 2:
						l_num = (430, 260)
					if a_ == 3:
						l_num = (465, 260)
					if a_ == 4:
						l_num = (500, 260)
				if len(word) == 6:
					if a_ == 0:
						l_num = (360, 260)
					if a_ == 1:
						l_num = (395, 260)
					if a_ == 2:
						l_num = (430, 260)
					if a_ == 3:
						l_num = (465, 260)
					if a_ == 4:
						l_num = (500, 260)
					if a_ == 5:
						l_num = (535, 260)
				if len(word) == 7:
					if a_ == 0:
						l_num = (325, 260)
					if a_ == 1:
						l_num = (360, 260)
					if a_ == 2:
						l_num = (395, 260)
					if a_ == 3:
						l_num = (430, 260)
					if a_ == 4:
						l_num = (465, 260)
					if a_ == 5:
						l_num = (500, 260)
					if a_ == 6:
						l_num = (535, 260)
				if len(word) == 8:
					if a_ == 0:
						l_num = (325, 260)
					if a_ == 1:
						l_num = (360, 260)
					if a_ == 2:
						l_num = (395, 260)
					if a_ == 3:
						l_num = (430, 260)
					if a_ == 4:
						l_num = (465, 260)
					if a_ == 5:
						l_num = (500, 260)
					if a_ == 6:
						l_num = (535, 260)
					if a_ == 7:
						l_num = (570, 260)
				if len(word) == 9:
					if a_ == 0:
						l_num = (290, 260)
					if a_ == 1:
						l_num = (325, 260)
					if a_ == 2:
						l_num = (360, 260)
					if a_ == 3:
						l_num = (395, 260)
					if a_ == 4:
						l_num = (430, 260)
					if a_ == 5:
						l_num = (465, 260)
					if a_ == 6:
						l_num = (500, 260)
					if a_ == 7:
						l_num = (535, 260)
					if a_ == 8:
						l_num = (570, 260)
				if len(word) == 10:
					if a_ == 0:
						l_num = (290, 260)
					if a_ == 1:
						l_num = (325, 260)
					if a_ == 2:
						l_num = (360, 260)
					if a_ == 3:
						l_num = (395, 260)
					if a_ == 4:
						l_num = (430, 260)
					if a_ == 5:
						l_num = (465, 260)
					if a_ == 6:
						l_num = (500, 260)
					if a_ == 7:
						l_num = (535, 260)
					if a_ == 8:
						l_num = (370, 260)
					if a_ == 9:
						l_num = (605, 260)
				if len(word) == 11:
					if a_ == 0:
						l_num = (255, 260)
					if a_ == 1:
						l_num = (290, 260)
					if a_ == 2:
						l_num = (325, 260)
					if a_ == 3:
						l_num = (360, 260)
					if a_ == 4:
						l_num = (395, 260)
					if a_ == 5:
						l_num = (430, 260)
					if a_ == 6:
						l_num = (465, 260)
					if a_ == 7:
						l_num = (500, 260)
					if a_ == 8:
						l_num = (535, 260)
					if a_ == 9:
						l_num = (570, 260)
					if a_ == 10:
						l_num = (605, 260)
				if len(word) == 12:
					if a_ == 0:
						l_num = (255, 260)
					if a_ == 1:
						l_num = (290, 260)
					if a_ == 2:
						l_num = (325, 260)
					if a_ == 3:
						l_num = (360, 260)
					if a_ == 4:
						l_num = (395, 260)
					if a_ == 5:
						l_num = (430, 260)
					if a_ == 6:
						l_num = (465, 260)
					if a_ == 7:
						l_num = (500, 260)
					if a_ == 8:
						l_num = (535, 260)
					if a_ == 9:
						l_num = (570, 260)
					if a_ == 10:
						l_num = (605, 260)
					if a_ == 11:
						l_num = (640, 260)

				screen.blit(a, l_num)
				word100()

		if j_block.collidepoint(mouse_pos) and click:
			guess = 'j'
			pygame.draw.rect(screen, white, (j_block))
			if guess in actual_word:
				a_ = actual_word.index(guess)
				a = font4.render(actual_word[a_], True, black)
				if len(word) == 4:
					if a_ == 0:
						l_num = (395, 260)
					if a_ == 1:
						l_num = (430, 260)
					if a_ == 2:
						l_num = (465, 260)
					if a_ == 3:
						l_num = (500, 260)
				if len(word) == 5:
					if a_ == 0:
						l_num = (360, 260)
					if a_ == 1:
						l_num = (395, 260)
					if a_ == 2:
						l_num = (430, 260)
					if a_ == 3:
						l_num = (465, 260)
					if a_ == 4:
						l_num = (500, 260)
				if len(word) == 6:
					if a_ == 0:
						l_num = (360, 260)
					if a_ == 1:
						l_num = (395, 260)
					if a_ == 2:
						l_num = (430, 260)
					if a_ == 3:
						l_num = (465, 260)
					if a_ == 4:
						l_num = (500, 260)
					if a_ == 5:
						l_num = (535, 260)
				if len(word) == 7:
					if a_ == 0:
						l_num = (325, 260)
					if a_ == 1:
						l_num = (360, 260)
					if a_ == 2:
						l_num = (395, 260)
					if a_ == 3:
						l_num = (430, 260)
					if a_ == 4:
						l_num = (465, 260)
					if a_ == 5:
						l_num = (500, 260)
					if a_ == 6:
						l_num = (535, 260)
				if len(word) == 8:
					if a_ == 0:
						l_num = (325, 260)
					if a_ == 1:
						l_num = (360, 260)
					if a_ == 2:
						l_num = (395, 260)
					if a_ == 3:
						l_num = (430, 260)
					if a_ == 4:
						l_num = (465, 260)
					if a_ == 5:
						l_num = (500, 260)
					if a_ == 6:
						l_num = (535, 260)
					if a_ == 7:
						l_num = (570, 260)
				if len(word) == 9:
					if a_ == 0:
						l_num = (290, 260)
					if a_ == 1:
						l_num = (325, 260)
					if a_ == 2:
						l_num = (360, 260)
					if a_ == 3:
						l_num = (395, 260)
					if a_ == 4:
						l_num = (430, 260)
					if a_ == 5:
						l_num = (465, 260)
					if a_ == 6:
						l_num = (500, 260)
					if a_ == 7:
						l_num = (535, 260)
					if a_ == 8:
						l_num = (570, 260)
				if len(word) == 10:
					if a_ == 0:
						l_num = (290, 260)
					if a_ == 1:
						l_num = (325, 260)
					if a_ == 2:
						l_num = (360, 260)
					if a_ == 3:
						l_num = (395, 260)
					if a_ == 4:
						l_num = (430, 260)
					if a_ == 5:
						l_num = (465, 260)
					if a_ == 6:
						l_num = (500, 260)
					if a_ == 7:
						l_num = (535, 260)
					if a_ == 8:
						l_num = (370, 260)
					if a_ == 9:
						l_num = (605, 260)
				if len(word) == 11:
					if a_ == 0:
						l_num = (255, 260)
					if a_ == 1:
						l_num = (290, 260)
					if a_ == 2:
						l_num = (325, 260)
					if a_ == 3:
						l_num = (360, 260)
					if a_ == 4:
						l_num = (395, 260)
					if a_ == 5:
						l_num = (430, 260)
					if a_ == 6:
						l_num = (465, 260)
					if a_ == 7:
						l_num = (500, 260)
					if a_ == 8:
						l_num = (535, 260)
					if a_ == 9:
						l_num = (570, 260)
					if a_ == 10:
						l_num = (605, 260)
				if len(word) == 12:
					if a_ == 0:
						l_num = (255, 260)
					if a_ == 1:
						l_num = (290, 260)
					if a_ == 2:
						l_num = (325, 260)
					if a_ == 3:
						l_num = (360, 260)
					if a_ == 4:
						l_num = (395, 260)
					if a_ == 5:
						l_num = (430, 260)
					if a_ == 6:
						l_num = (465, 260)
					if a_ == 7:
						l_num = (500, 260)
					if a_ == 8:
						l_num = (535, 260)
					if a_ == 9:
						l_num = (570, 260)
					if a_ == 10:
						l_num = (605, 260)
					if a_ == 11:
						l_num = (640, 260)

				screen.blit(a, l_num)
				word100()

		if k_block.collidepoint(mouse_pos) and click:
			guess = 'k'
			pygame.draw.rect(screen, white, (k_block))
			if guess in actual_word:
				a_ = actual_word.index(guess)
				a = font4.render(actual_word[a_], True, black)
				if len(word) == 4:
					if a_ == 0:
						l_num = (395, 260)
					if a_ == 1:
						l_num = (430, 260)
					if a_ == 2:
						l_num = (465, 260)
					if a_ == 3:
						l_num = (500, 260)
				if len(word) == 5:
					if a_ == 0:
						l_num = (360, 260)
					if a_ == 1:
						l_num = (395, 260)
					if a_ == 2:
						l_num = (430, 260)
					if a_ == 3:
						l_num = (465, 260)
					if a_ == 4:
						l_num = (500, 260)
				if len(word) == 6:
					if a_ == 0:
						l_num = (360, 260)
					if a_ == 1:
						l_num = (395, 260)
					if a_ == 2:
						l_num = (430, 260)
					if a_ == 3:
						l_num = (465, 260)
					if a_ == 4:
						l_num = (500, 260)
					if a_ == 5:
						l_num = (535, 260)
				if len(word) == 7:
					if a_ == 0:
						l_num = (325, 260)
					if a_ == 1:
						l_num = (360, 260)
					if a_ == 2:
						l_num = (395, 260)
					if a_ == 3:
						l_num = (430, 260)
					if a_ == 4:
						l_num = (465, 260)
					if a_ == 5:
						l_num = (500, 260)
					if a_ == 6:
						l_num = (535, 260)
				if len(word) == 8:
					if a_ == 0:
						l_num = (325, 260)
					if a_ == 1:
						l_num = (360, 260)
					if a_ == 2:
						l_num = (395, 260)
					if a_ == 3:
						l_num = (430, 260)
					if a_ == 4:
						l_num = (465, 260)
					if a_ == 5:
						l_num = (500, 260)
					if a_ == 6:
						l_num = (535, 260)
					if a_ == 7:
						l_num = (570, 260)
				if len(word) == 9:
					if a_ == 0:
						l_num = (290, 260)
					if a_ == 1:
						l_num = (325, 260)
					if a_ == 2:
						l_num = (360, 260)
					if a_ == 3:
						l_num = (395, 260)
					if a_ == 4:
						l_num = (430, 260)
					if a_ == 5:
						l_num = (465, 260)
					if a_ == 6:
						l_num = (500, 260)
					if a_ == 7:
						l_num = (535, 260)
					if a_ == 8:
						l_num = (570, 260)
				if len(word) == 10:
					if a_ == 0:
						l_num = (290, 260)
					if a_ == 1:
						l_num = (325, 260)
					if a_ == 2:
						l_num = (360, 260)
					if a_ == 3:
						l_num = (395, 260)
					if a_ == 4:
						l_num = (430, 260)
					if a_ == 5:
						l_num = (465, 260)
					if a_ == 6:
						l_num = (500, 260)
					if a_ == 7:
						l_num = (535, 260)
					if a_ == 8:
						l_num = (370, 260)
					if a_ == 9:
						l_num = (605, 260)
				if len(word) == 11:
					if a_ == 0:
						l_num = (255, 260)
					if a_ == 1:
						l_num = (290, 260)
					if a_ == 2:
						l_num = (325, 260)
					if a_ == 3:
						l_num = (360, 260)
					if a_ == 4:
						l_num = (395, 260)
					if a_ == 5:
						l_num = (430, 260)
					if a_ == 6:
						l_num = (465, 260)
					if a_ == 7:
						l_num = (500, 260)
					if a_ == 8:
						l_num = (535, 260)
					if a_ == 9:
						l_num = (570, 260)
					if a_ == 10:
						l_num = (605, 260)
				if len(word) == 12:
					if a_ == 0:
						l_num = (255, 260)
					if a_ == 1:
						l_num = (290, 260)
					if a_ == 2:
						l_num = (325, 260)
					if a_ == 3:
						l_num = (360, 260)
					if a_ == 4:
						l_num = (395, 260)
					if a_ == 5:
						l_num = (430, 260)
					if a_ == 6:
						l_num = (465, 260)
					if a_ == 7:
						l_num = (500, 260)
					if a_ == 8:
						l_num = (535, 260)
					if a_ == 9:
						l_num = (570, 260)
					if a_ == 10:
						l_num = (605, 260)
					if a_ == 11:
						l_num = (640, 260)

				screen.blit(a, l_num)
				word100()

		if l_block.collidepoint(mouse_pos) and click:
			guess = 'l'
			pygame.draw.rect(screen, white, (l_block))
			if guess in actual_word:
				a_ = actual_word.index(guess)
				a = font4.render(actual_word[a_], True, black)
				if len(word) == 4:
					if a_ == 0:
						l_num = (395, 260)
					if a_ == 1:
						l_num = (430, 260)
					if a_ == 2:
						l_num = (465, 260)
					if a_ == 3:
						l_num = (500, 260)
				if len(word) == 5:
					if a_ == 0:
						l_num = (360, 260)
					if a_ == 1:
						l_num = (395, 260)
					if a_ == 2:
						l_num = (430, 260)
					if a_ == 3:
						l_num = (465, 260)
					if a_ == 4:
						l_num = (500, 260)
				if len(word) == 6:
					if a_ == 0:
						l_num = (360, 260)
					if a_ == 1:
						l_num = (395, 260)
					if a_ == 2:
						l_num = (430, 260)
					if a_ == 3:
						l_num = (465, 260)
					if a_ == 4:
						l_num = (500, 260)
					if a_ == 5:
						l_num = (535, 260)
				if len(word) == 7:
					if a_ == 0:
						l_num = (325, 260)
					if a_ == 1:
						l_num = (360, 260)
					if a_ == 2:
						l_num = (395, 260)
					if a_ == 3:
						l_num = (430, 260)
					if a_ == 4:
						l_num = (465, 260)
					if a_ == 5:
						l_num = (500, 260)
					if a_ == 6:
						l_num = (535, 260)
				if len(word) == 8:
					if a_ == 0:
						l_num = (325, 260)
					if a_ == 1:
						l_num = (360, 260)
					if a_ == 2:
						l_num = (395, 260)
					if a_ == 3:
						l_num = (430, 260)
					if a_ == 4:
						l_num = (465, 260)
					if a_ == 5:
						l_num = (500, 260)
					if a_ == 6:
						l_num = (535, 260)
					if a_ == 7:
						l_num = (570, 260)
				if len(word) == 9:
					if a_ == 0:
						l_num = (290, 260)
					if a_ == 1:
						l_num = (325, 260)
					if a_ == 2:
						l_num = (360, 260)
					if a_ == 3:
						l_num = (395, 260)
					if a_ == 4:
						l_num = (430, 260)
					if a_ == 5:
						l_num = (465, 260)
					if a_ == 6:
						l_num = (500, 260)
					if a_ == 7:
						l_num = (535, 260)
					if a_ == 8:
						l_num = (570, 260)
				if len(word) == 10:
					if a_ == 0:
						l_num = (290, 260)
					if a_ == 1:
						l_num = (325, 260)
					if a_ == 2:
						l_num = (360, 260)
					if a_ == 3:
						l_num = (395, 260)
					if a_ == 4:
						l_num = (430, 260)
					if a_ == 5:
						l_num = (465, 260)
					if a_ == 6:
						l_num = (500, 260)
					if a_ == 7:
						l_num = (535, 260)
					if a_ == 8:
						l_num = (370, 260)
					if a_ == 9:
						l_num = (605, 260)
				if len(word) == 11:
					if a_ == 0:
						l_num = (255, 260)
					if a_ == 1:
						l_num = (290, 260)
					if a_ == 2:
						l_num = (325, 260)
					if a_ == 3:
						l_num = (360, 260)
					if a_ == 4:
						l_num = (395, 260)
					if a_ == 5:
						l_num = (430, 260)
					if a_ == 6:
						l_num = (465, 260)
					if a_ == 7:
						l_num = (500, 260)
					if a_ == 8:
						l_num = (535, 260)
					if a_ == 9:
						l_num = (570, 260)
					if a_ == 10:
						l_num = (605, 260)
				if len(word) == 12:
					if a_ == 0:
						l_num = (255, 260)
					if a_ == 1:
						l_num = (290, 260)
					if a_ == 2:
						l_num = (325, 260)
					if a_ == 3:
						l_num = (360, 260)
					if a_ == 4:
						l_num = (395, 260)
					if a_ == 5:
						l_num = (430, 260)
					if a_ == 6:
						l_num = (465, 260)
					if a_ == 7:
						l_num = (500, 260)
					if a_ == 8:
						l_num = (535, 260)
					if a_ == 9:
						l_num = (570, 260)
					if a_ == 10:
						l_num = (605, 260)
					if a_ == 11:
						l_num = (640, 260)

				screen.blit(a, l_num)
				word100()

		if m_block.collidepoint(mouse_pos) and click:
			guess = 'm'
			pygame.draw.rect(screen, white, (m_block))
			if guess in actual_word:
				a_ = actual_word.index(guess)
				a = font4.render(actual_word[a_], True, black)
				if len(word) == 4:
					if a_ == 0:
						l_num = (395, 260)
					if a_ == 1:
						l_num = (430, 260)
					if a_ == 2:
						l_num = (465, 260)
					if a_ == 3:
						l_num = (500, 260)
				if len(word) == 5:
					if a_ == 0:
						l_num = (360, 260)
					if a_ == 1:
						l_num = (395, 260)
					if a_ == 2:
						l_num = (430, 260)
					if a_ == 3:
						l_num = (465, 260)
					if a_ == 4:
						l_num = (500, 260)
				if len(word) == 6:
					if a_ == 0:
						l_num = (360, 260)
					if a_ == 1:
						l_num = (395, 260)
					if a_ == 2:
						l_num = (430, 260)
					if a_ == 3:
						l_num = (465, 260)
					if a_ == 4:
						l_num = (500, 260)
					if a_ == 5:
						l_num = (535, 260)
				if len(word) == 7:
					if a_ == 0:
						l_num = (325, 260)
					if a_ == 1:
						l_num = (360, 260)
					if a_ == 2:
						l_num = (395, 260)
					if a_ == 3:
						l_num = (430, 260)
					if a_ == 4:
						l_num = (465, 260)
					if a_ == 5:
						l_num = (500, 260)
					if a_ == 6:
						l_num = (535, 260)
				if len(word) == 8:
					if a_ == 0:
						l_num = (325, 260)
					if a_ == 1:
						l_num = (360, 260)
					if a_ == 2:
						l_num = (395, 260)
					if a_ == 3:
						l_num = (430, 260)
					if a_ == 4:
						l_num = (465, 260)
					if a_ == 5:
						l_num = (500, 260)
					if a_ == 6:
						l_num = (535, 260)
					if a_ == 7:
						l_num = (570, 260)
				if len(word) == 9:
					if a_ == 0:
						l_num = (290, 260)
					if a_ == 1:
						l_num = (325, 260)
					if a_ == 2:
						l_num = (360, 260)
					if a_ == 3:
						l_num = (395, 260)
					if a_ == 4:
						l_num = (430, 260)
					if a_ == 5:
						l_num = (465, 260)
					if a_ == 6:
						l_num = (500, 260)
					if a_ == 7:
						l_num = (535, 260)
					if a_ == 8:
						l_num = (570, 260)
				if len(word) == 10:
					if a_ == 0:
						l_num = (290, 260)
					if a_ == 1:
						l_num = (325, 260)
					if a_ == 2:
						l_num = (360, 260)
					if a_ == 3:
						l_num = (395, 260)
					if a_ == 4:
						l_num = (430, 260)
					if a_ == 5:
						l_num = (465, 260)
					if a_ == 6:
						l_num = (500, 260)
					if a_ == 7:
						l_num = (535, 260)
					if a_ == 8:
						l_num = (370, 260)
					if a_ == 9:
						l_num = (605, 260)
				if len(word) == 11:
					if a_ == 0:
						l_num = (255, 260)
					if a_ == 1:
						l_num = (290, 260)
					if a_ == 2:
						l_num = (325, 260)
					if a_ == 3:
						l_num = (360, 260)
					if a_ == 4:
						l_num = (395, 260)
					if a_ == 5:
						l_num = (430, 260)
					if a_ == 6:
						l_num = (465, 260)
					if a_ == 7:
						l_num = (500, 260)
					if a_ == 8:
						l_num = (535, 260)
					if a_ == 9:
						l_num = (570, 260)
					if a_ == 10:
						l_num = (605, 260)
				if len(word) == 12:
					if a_ == 0:
						l_num = (255, 260)
					if a_ == 1:
						l_num = (290, 260)
					if a_ == 2:
						l_num = (325, 260)
					if a_ == 3:
						l_num = (360, 260)
					if a_ == 4:
						l_num = (395, 260)
					if a_ == 5:
						l_num = (430, 260)
					if a_ == 6:
						l_num = (465, 260)
					if a_ == 7:
						l_num = (500, 260)
					if a_ == 8:
						l_num = (535, 260)
					if a_ == 9:
						l_num = (570, 260)
					if a_ == 10:
						l_num = (605, 260)
					if a_ == 11:
						l_num = (640, 260)

				screen.blit(a, l_num)
				word100()

		if n_block.collidepoint(mouse_pos) and click:
			guess = 'n'
			pygame.draw.rect(screen, white, (n_block))
			if guess in actual_word:
				a_ = actual_word.index(guess)
				a = font4.render(actual_word[a_], True, black)
				if len(word) == 4:
					if a_ == 0:
						l_num = (395, 260)
					if a_ == 1:
						l_num = (430, 260)
					if a_ == 2:
						l_num = (465, 260)
					if a_ == 3:
						l_num = (500, 260)
				if len(word) == 5:
					if a_ == 0:
						l_num = (360, 260)
					if a_ == 1:
						l_num = (395, 260)
					if a_ == 2:
						l_num = (430, 260)
					if a_ == 3:
						l_num = (465, 260)
					if a_ == 4:
						l_num = (500, 260)
				if len(word) == 6:
					if a_ == 0:
						l_num = (360, 260)
					if a_ == 1:
						l_num = (395, 260)
					if a_ == 2:
						l_num = (430, 260)
					if a_ == 3:
						l_num = (465, 260)
					if a_ == 4:
						l_num = (500, 260)
					if a_ == 5:
						l_num = (535, 260)
				if len(word) == 7:
					if a_ == 0:
						l_num = (325, 260)
					if a_ == 1:
						l_num = (360, 260)
					if a_ == 2:
						l_num = (395, 260)
					if a_ == 3:
						l_num = (430, 260)
					if a_ == 4:
						l_num = (465, 260)
					if a_ == 5:
						l_num = (500, 260)
					if a_ == 6:
						l_num = (535, 260)
				if len(word) == 8:
					if a_ == 0:
						l_num = (325, 260)
					if a_ == 1:
						l_num = (360, 260)
					if a_ == 2:
						l_num = (395, 260)
					if a_ == 3:
						l_num = (430, 260)
					if a_ == 4:
						l_num = (465, 260)
					if a_ == 5:
						l_num = (500, 260)
					if a_ == 6:
						l_num = (535, 260)
					if a_ == 7:
						l_num = (570, 260)
				if len(word) == 9:
					if a_ == 0:
						l_num = (290, 260)
					if a_ == 1:
						l_num = (325, 260)
					if a_ == 2:
						l_num = (360, 260)
					if a_ == 3:
						l_num = (395, 260)
					if a_ == 4:
						l_num = (430, 260)
					if a_ == 5:
						l_num = (465, 260)
					if a_ == 6:
						l_num = (500, 260)
					if a_ == 7:
						l_num = (535, 260)
					if a_ == 8:
						l_num = (570, 260)
				if len(word) == 10:
					if a_ == 0:
						l_num = (290, 260)
					if a_ == 1:
						l_num = (325, 260)
					if a_ == 2:
						l_num = (360, 260)
					if a_ == 3:
						l_num = (395, 260)
					if a_ == 4:
						l_num = (430, 260)
					if a_ == 5:
						l_num = (465, 260)
					if a_ == 6:
						l_num = (500, 260)
					if a_ == 7:
						l_num = (535, 260)
					if a_ == 8:
						l_num = (370, 260)
					if a_ == 9:
						l_num = (605, 260)
				if len(word) == 11:
					if a_ == 0:
						l_num = (255, 260)
					if a_ == 1:
						l_num = (290, 260)
					if a_ == 2:
						l_num = (325, 260)
					if a_ == 3:
						l_num = (360, 260)
					if a_ == 4:
						l_num = (395, 260)
					if a_ == 5:
						l_num = (430, 260)
					if a_ == 6:
						l_num = (465, 260)
					if a_ == 7:
						l_num = (500, 260)
					if a_ == 8:
						l_num = (535, 260)
					if a_ == 9:
						l_num = (570, 260)
					if a_ == 10:
						l_num = (605, 260)
				if len(word) == 12:
					if a_ == 0:
						l_num = (255, 260)
					if a_ == 1:
						l_num = (290, 260)
					if a_ == 2:
						l_num = (325, 260)
					if a_ == 3:
						l_num = (360, 260)
					if a_ == 4:
						l_num = (395, 260)
					if a_ == 5:
						l_num = (430, 260)
					if a_ == 6:
						l_num = (465, 260)
					if a_ == 7:
						l_num = (500, 260)
					if a_ == 8:
						l_num = (535, 260)
					if a_ == 9:
						l_num = (570, 260)
					if a_ == 10:
						l_num = (605, 260)
					if a_ == 11:
						l_num = (640, 260)

				screen.blit(a, l_num)
				word100()

		if o_block.collidepoint(mouse_pos) and click:
			guess = 'o'
			pygame.draw.rect(screen, white, (o_block))
			if guess in actual_word:
				a_ = actual_word.index(guess)
				a = font4.render(actual_word[a_], True, black)
				if len(word) == 4:
					if a_ == 0:
						l_num = (395, 260)
					if a_ == 1:
						l_num = (430, 260)
					if a_ == 2:
						l_num = (465, 260)
					if a_ == 3:
						l_num = (500, 260)
				if len(word) == 5:
					if a_ == 0:
						l_num = (360, 260)
					if a_ == 1:
						l_num = (395, 260)
					if a_ == 2:
						l_num = (430, 260)
					if a_ == 3:
						l_num = (465, 260)
					if a_ == 4:
						l_num = (500, 260)
				if len(word) == 6:
					if a_ == 0:
						l_num = (360, 260)
					if a_ == 1:
						l_num = (395, 260)
					if a_ == 2:
						l_num = (430, 260)
					if a_ == 3:
						l_num = (465, 260)
					if a_ == 4:
						l_num = (500, 260)
					if a_ == 5:
						l_num = (535, 260)
				if len(word) == 7:
					if a_ == 0:
						l_num = (325, 260)
					if a_ == 1:
						l_num = (360, 260)
					if a_ == 2:
						l_num = (395, 260)
					if a_ == 3:
						l_num = (430, 260)
					if a_ == 4:
						l_num = (465, 260)
					if a_ == 5:
						l_num = (500, 260)
					if a_ == 6:
						l_num = (535, 260)
				if len(word) == 8:
					if a_ == 0:
						l_num = (325, 260)
					if a_ == 1:
						l_num = (360, 260)
					if a_ == 2:
						l_num = (395, 260)
					if a_ == 3:
						l_num = (430, 260)
					if a_ == 4:
						l_num = (465, 260)
					if a_ == 5:
						l_num = (500, 260)
					if a_ == 6:
						l_num = (535, 260)
					if a_ == 7:
						l_num = (570, 260)
				if len(word) == 9:
					if a_ == 0:
						l_num = (290, 260)
					if a_ == 1:
						l_num = (325, 260)
					if a_ == 2:
						l_num = (360, 260)
					if a_ == 3:
						l_num = (395, 260)
					if a_ == 4:
						l_num = (430, 260)
					if a_ == 5:
						l_num = (465, 260)
					if a_ == 6:
						l_num = (500, 260)
					if a_ == 7:
						l_num = (535, 260)
					if a_ == 8:
						l_num = (570, 260)
				if len(word) == 10:
					if a_ == 0:
						l_num = (290, 260)
					if a_ == 1:
						l_num = (325, 260)
					if a_ == 2:
						l_num = (360, 260)
					if a_ == 3:
						l_num = (395, 260)
					if a_ == 4:
						l_num = (430, 260)
					if a_ == 5:
						l_num = (465, 260)
					if a_ == 6:
						l_num = (500, 260)
					if a_ == 7:
						l_num = (535, 260)
					if a_ == 8:
						l_num = (370, 260)
					if a_ == 9:
						l_num = (605, 260)
				if len(word) == 11:
					if a_ == 0:
						l_num = (255, 260)
					if a_ == 1:
						l_num = (290, 260)
					if a_ == 2:
						l_num = (325, 260)
					if a_ == 3:
						l_num = (360, 260)
					if a_ == 4:
						l_num = (395, 260)
					if a_ == 5:
						l_num = (430, 260)
					if a_ == 6:
						l_num = (465, 260)
					if a_ == 7:
						l_num = (500, 260)
					if a_ == 8:
						l_num = (535, 260)
					if a_ == 9:
						l_num = (570, 260)
					if a_ == 10:
						l_num = (605, 260)
				if len(word) == 12:
					if a_ == 0:
						l_num = (255, 260)
					if a_ == 1:
						l_num = (290, 260)
					if a_ == 2:
						l_num = (325, 260)
					if a_ == 3:
						l_num = (360, 260)
					if a_ == 4:
						l_num = (395, 260)
					if a_ == 5:
						l_num = (430, 260)
					if a_ == 6:
						l_num = (465, 260)
					if a_ == 7:
						l_num = (500, 260)
					if a_ == 8:
						l_num = (535, 260)
					if a_ == 9:
						l_num = (570, 260)
					if a_ == 10:
						l_num = (605, 260)
					if a_ == 11:
						l_num = (640, 260)

				screen.blit(a, l_num)
				word100()

		if p_block.collidepoint(mouse_pos) and click:
			guess = 'p'
			pygame.draw.rect(screen, white, (p_block))
			if guess in actual_word:
				a_ = actual_word.index(guess)
				a = font4.render(actual_word[a_], True, black)
				if len(word) == 4:
					if a_ == 0:
						l_num = (395, 260)
					if a_ == 1:
						l_num = (430, 260)
					if a_ == 2:
						l_num = (465, 260)
					if a_ == 3:
						l_num = (500, 260)
				if len(word) == 5:
					if a_ == 0:
						l_num = (360, 260)
					if a_ == 1:
						l_num = (395, 260)
					if a_ == 2:
						l_num = (430, 260)
					if a_ == 3:
						l_num = (465, 260)
					if a_ == 4:
						l_num = (500, 260)
				if len(word) == 6:
					if a_ == 0:
						l_num = (360, 260)
					if a_ == 1:
						l_num = (395, 260)
					if a_ == 2:
						l_num = (430, 260)
					if a_ == 3:
						l_num = (465, 260)
					if a_ == 4:
						l_num = (500, 260)
					if a_ == 5:
						l_num = (535, 260)
				if len(word) == 7:
					if a_ == 0:
						l_num = (325, 260)
					if a_ == 1:
						l_num = (360, 260)
					if a_ == 2:
						l_num = (395, 260)
					if a_ == 3:
						l_num = (430, 260)
					if a_ == 4:
						l_num = (465, 260)
					if a_ == 5:
						l_num = (500, 260)
					if a_ == 6:
						l_num = (535, 260)
				if len(word) == 8:
					if a_ == 0:
						l_num = (325, 260)
					if a_ == 1:
						l_num = (360, 260)
					if a_ == 2:
						l_num = (395, 260)
					if a_ == 3:
						l_num = (430, 260)
					if a_ == 4:
						l_num = (465, 260)
					if a_ == 5:
						l_num = (500, 260)
					if a_ == 6:
						l_num = (535, 260)
					if a_ == 7:
						l_num = (570, 260)
				if len(word) == 9:
					if a_ == 0:
						l_num = (290, 260)
					if a_ == 1:
						l_num = (325, 260)
					if a_ == 2:
						l_num = (360, 260)
					if a_ == 3:
						l_num = (395, 260)
					if a_ == 4:
						l_num = (430, 260)
					if a_ == 5:
						l_num = (465, 260)
					if a_ == 6:
						l_num = (500, 260)
					if a_ == 7:
						l_num = (535, 260)
					if a_ == 8:
						l_num = (570, 260)
				if len(word) == 10:
					if a_ == 0:
						l_num = (290, 260)
					if a_ == 1:
						l_num = (325, 260)
					if a_ == 2:
						l_num = (360, 260)
					if a_ == 3:
						l_num = (395, 260)
					if a_ == 4:
						l_num = (430, 260)
					if a_ == 5:
						l_num = (465, 260)
					if a_ == 6:
						l_num = (500, 260)
					if a_ == 7:
						l_num = (535, 260)
					if a_ == 8:
						l_num = (370, 260)
					if a_ == 9:
						l_num = (605, 260)
				if len(word) == 11:
					if a_ == 0:
						l_num = (255, 260)
					if a_ == 1:
						l_num = (290, 260)
					if a_ == 2:
						l_num = (325, 260)
					if a_ == 3:
						l_num = (360, 260)
					if a_ == 4:
						l_num = (395, 260)
					if a_ == 5:
						l_num = (430, 260)
					if a_ == 6:
						l_num = (465, 260)
					if a_ == 7:
						l_num = (500, 260)
					if a_ == 8:
						l_num = (535, 260)
					if a_ == 9:
						l_num = (570, 260)
					if a_ == 10:
						l_num = (605, 260)
				if len(word) == 12:
					if a_ == 0:
						l_num = (255, 260)
					if a_ == 1:
						l_num = (290, 260)
					if a_ == 2:
						l_num = (325, 260)
					if a_ == 3:
						l_num = (360, 260)
					if a_ == 4:
						l_num = (395, 260)
					if a_ == 5:
						l_num = (430, 260)
					if a_ == 6:
						l_num = (465, 260)
					if a_ == 7:
						l_num = (500, 260)
					if a_ == 8:
						l_num = (535, 260)
					if a_ == 9:
						l_num = (570, 260)
					if a_ == 10:
						l_num = (605, 260)
					if a_ == 11:
						l_num = (640, 260)

				screen.blit(a, l_num)
				word100()
		if q_block.collidepoint(mouse_pos) and click:
			guess = 'q'
			pygame.draw.rect(screen, white, q_block)
			if guess in actual_word:
				a_ = actual_word.index(guess)
				a = font4.render(actual_word[a_], True, black)
				if len(word) == 4:
					if a_ == 0:
						l_num = (395, 260)
					if a_ == 1:
						l_num = (430, 260)
					if a_ == 2:
						l_num = (465, 260)
					if a_ == 3:
						l_num = (500, 260)
				if len(word) == 5:
					if a_ == 0:
						l_num = (360, 260)
					if a_ == 1:
						l_num = (395, 260)
					if a_ == 2:
						l_num = (430, 260)
					if a_ == 3:
						l_num = (465, 260)
					if a_ == 4:
						l_num = (500, 260)
				if len(word) == 6:
					if a_ == 0:
						l_num = (360, 260)
					if a_ == 1:
						l_num = (395, 260)
					if a_ == 2:
						l_num = (430, 260)
					if a_ == 3:
						l_num = (465, 260)
					if a_ == 4:
						l_num = (500, 260)
					if a_ == 5:
						l_num = (535, 260)
				if len(word) == 7:
					if a_ == 0:
						l_num = (325, 260)
					if a_ == 1:
						l_num = (360, 260)
					if a_ == 2:
						l_num = (395, 260)
					if a_ == 3:
						l_num = (430, 260)
					if a_ == 4:
						l_num = (465, 260)
					if a_ == 5:
						l_num = (500, 260)
					if a_ == 6:
						l_num = (535, 260)
				if len(word) == 8:
					if a_ == 0:
						l_num = (325, 260)
					if a_ == 1:
						l_num = (360, 260)
					if a_ == 2:
						l_num = (395, 260)
					if a_ == 3:
						l_num = (430, 260)
					if a_ == 4:
						l_num = (465, 260)
					if a_ == 5:
						l_num = (500, 260)
					if a_ == 6:
						l_num = (535, 260)
					if a_ == 7:
						l_num = (570, 260)
				if len(word) == 9:
					if a_ == 0:
						l_num = (290, 260)
					if a_ == 1:
						l_num = (325, 260)
					if a_ == 2:
						l_num = (360, 260)
					if a_ == 3:
						l_num = (395, 260)
					if a_ == 4:
						l_num = (430, 260)
					if a_ == 5:
						l_num = (465, 260)
					if a_ == 6:
						l_num = (500, 260)
					if a_ == 7:
						l_num = (535, 260)
					if a_ == 8:
						l_num = (570, 260)
				if len(word) == 10:
					if a_ == 0:
						l_num = (290, 260)
					if a_ == 1:
						l_num = (325, 260)
					if a_ == 2:
						l_num = (360, 260)
					if a_ == 3:
						l_num = (395, 260)
					if a_ == 4:
						l_num = (430, 260)
					if a_ == 5:
						l_num = (465, 260)
					if a_ == 6:
						l_num = (500, 260)
					if a_ == 7:
						l_num = (535, 260)
					if a_ == 8:
						l_num = (370, 260)
					if a_ == 9:
						l_num = (605, 260)
				if len(word) == 11:
					if a_ == 0:
						l_num = (255, 260)
					if a_ == 1:
						l_num = (290, 260)
					if a_ == 2:
						l_num = (325, 260)
					if a_ == 3:
						l_num = (360, 260)
					if a_ == 4:
						l_num = (395, 260)
					if a_ == 5:
						l_num = (430, 260)
					if a_ == 6:
						l_num = (465, 260)
					if a_ == 7:
						l_num = (500, 260)
					if a_ == 8:
						l_num = (535, 260)
					if a_ == 9:
						l_num = (570, 260)
					if a_ == 10:
						l_num = (605, 260)
				if len(word) == 12:
					if a_ == 0:
						l_num = (255, 260)
					if a_ == 1:
						l_num = (290, 260)
					if a_ == 2:
						l_num = (325, 260)
					if a_ == 3:
						l_num = (360, 260)
					if a_ == 4:
						l_num = (395, 260)
					if a_ == 5:
						l_num = (430, 260)
					if a_ == 6:
						l_num = (465, 260)
					if a_ == 7:
						l_num = (500, 260)
					if a_ == 8:
						l_num = (535, 260)
					if a_ == 9:
						l_num = (570, 260)
					if a_ == 10:
						l_num = (605, 260)
					if a_ == 11:
						l_num = (640, 260)

				screen.blit(a, l_num)
				word100()
		if r_block.collidepoint(mouse_pos) and click:
			guess = 'r'
			pygame.draw.rect(screen, white, (r_block))
			if guess in actual_word:
				a_ = actual_word.index(guess)
				a = font4.render(actual_word[a_], True, black)
				if len(word) == 4:
					if a_ == 0:
						l_num = (395, 260)
					if a_ == 1:
						l_num = (430, 260)
					if a_ == 2:
						l_num = (465, 260)
					if a_ == 3:
						l_num = (500, 260)
				if len(word) == 5:
					if a_ == 0:
						l_num = (360, 260)
					if a_ == 1:
						l_num = (395, 260)
					if a_ == 2:
						l_num = (430, 260)
					if a_ == 3:
						l_num = (465, 260)
					if a_ == 4:
						l_num = (500, 260)
				if len(word) == 6:
					if a_ == 0:
						l_num = (360, 260)
					if a_ == 1:
						l_num = (395, 260)
					if a_ == 2:
						l_num = (430, 260)
					if a_ == 3:
						l_num = (465, 260)
					if a_ == 4:
						l_num = (500, 260)
					if a_ == 5:
						l_num = (535, 260)
				if len(word) == 7:
					if a_ == 0:
						l_num = (325, 260)
					if a_ == 1:
						l_num = (360, 260)
					if a_ == 2:
						l_num = (395, 260)
					if a_ == 3:
						l_num = (430, 260)
					if a_ == 4:
						l_num = (465, 260)
					if a_ == 5:
						l_num = (500, 260)
					if a_ == 6:
						l_num = (535, 260)
				if len(word) == 8:
					if a_ == 0:
						l_num = (325, 260)
					if a_ == 1:
						l_num = (360, 260)
					if a_ == 2:
						l_num = (395, 260)
					if a_ == 3:
						l_num = (430, 260)
					if a_ == 4:
						l_num = (465, 260)
					if a_ == 5:
						l_num = (500, 260)
					if a_ == 6:
						l_num = (535, 260)
					if a_ == 7:
						l_num = (570, 260)
				if len(word) == 9:
					if a_ == 0:
						l_num = (290, 260)
					if a_ == 1:
						l_num = (325, 260)
					if a_ == 2:
						l_num = (360, 260)
					if a_ == 3:
						l_num = (395, 260)
					if a_ == 4:
						l_num = (430, 260)
					if a_ == 5:
						l_num = (465, 260)
					if a_ == 6:
						l_num = (500, 260)
					if a_ == 7:
						l_num = (535, 260)
					if a_ == 8:
						l_num = (570, 260)
				if len(word) == 10:
					if a_ == 0:
						l_num = (290, 260)
					if a_ == 1:
						l_num = (325, 260)
					if a_ == 2:
						l_num = (360, 260)
					if a_ == 3:
						l_num = (395, 260)
					if a_ == 4:
						l_num = (430, 260)
					if a_ == 5:
						l_num = (465, 260)
					if a_ == 6:
						l_num = (500, 260)
					if a_ == 7:
						l_num = (535, 260)
					if a_ == 8:
						l_num = (370, 260)
					if a_ == 9:
						l_num = (605, 260)
				if len(word) == 11:
					if a_ == 0:
						l_num = (255, 260)
					if a_ == 1:
						l_num = (290, 260)
					if a_ == 2:
						l_num = (325, 260)
					if a_ == 3:
						l_num = (360, 260)
					if a_ == 4:
						l_num = (395, 260)
					if a_ == 5:
						l_num = (430, 260)
					if a_ == 6:
						l_num = (465, 260)
					if a_ == 7:
						l_num = (500, 260)
					if a_ == 8:
						l_num = (535, 260)
					if a_ == 9:
						l_num = (570, 260)
					if a_ == 10:
						l_num = (605, 260)
				if len(word) == 12:
					if a_ == 0:
						l_num = (255, 260)
					if a_ == 1:
						l_num = (290, 260)
					if a_ == 2:
						l_num = (325, 260)
					if a_ == 3:
						l_num = (360, 260)
					if a_ == 4:
						l_num = (395, 260)
					if a_ == 5:
						l_num = (430, 260)
					if a_ == 6:
						l_num = (465, 260)
					if a_ == 7:
						l_num = (500, 260)
					if a_ == 8:
						l_num = (535, 260)
					if a_ == 9:
						l_num = (570, 260)
					if a_ == 10:
						l_num = (605, 260)
					if a_ == 11:
						l_num = (640, 260)

				screen.blit(a, l_num)
				word100()
		if s_block.collidepoint(mouse_pos) and click:
			guess = 's'
			pygame.draw.rect(screen, white, (s_block))

			if guess in actual_word:
				a_ = actual_word.index(guess)
				a = font4.render(actual_word[a_], True, black)
				if len(word) == 4:
					if a_ == 0:
						l_num = (395, 260)
					if a_ == 1:
						l_num = (430, 260)
					if a_ == 2:
						l_num = (465, 260)
					if a_ == 3:
						l_num = (500, 260)
				if len(word) == 5:
					if a_ == 0:
						l_num = (360, 260)
					if a_ == 1:
						l_num = (395, 260)
					if a_ == 2:
						l_num = (430, 260)
					if a_ == 3:
						l_num = (465, 260)
					if a_ == 4:
						l_num = (500, 260)
				if len(word) == 6:
					if a_ == 0:
						l_num = (360, 260)
					if a_ == 1:
						l_num = (395, 260)
					if a_ == 2:
						l_num = (430, 260)
					if a_ == 3:
						l_num = (465, 260)
					if a_ == 4:
						l_num = (500, 260)
					if a_ == 5:
						l_num = (535, 260)
				if len(word) == 7:
					if a_ == 0:
						l_num = (325, 260)
					if a_ == 1:
						l_num = (360, 260)
					if a_ == 2:
						l_num = (395, 260)
					if a_ == 3:
						l_num = (430, 260)
					if a_ == 4:
						l_num = (465, 260)
					if a_ == 5:
						l_num = (500, 260)
					if a_ == 6:
						l_num = (535, 260)
				if len(word) == 8:
					if a_ == 0:
						l_num = (325, 260)
					if a_ == 1:
						l_num = (360, 260)
					if a_ == 2:
						l_num = (395, 260)
					if a_ == 3:
						l_num = (430, 260)
					if a_ == 4:
						l_num = (465, 260)
					if a_ == 5:
						l_num = (500, 260)
					if a_ == 6:
						l_num = (535, 260)
					if a_ == 7:
						l_num = (570, 260)
				if len(word) == 9:
					if a_ == 0:
						l_num = (290, 260)
					if a_ == 1:
						l_num = (325, 260)
					if a_ == 2:
						l_num = (360, 260)
					if a_ == 3:
						l_num = (395, 260)
					if a_ == 4:
						l_num = (430, 260)
					if a_ == 5:
						l_num = (465, 260)
					if a_ == 6:
						l_num = (500, 260)
					if a_ == 7:
						l_num = (535, 260)
					if a_ == 8:
						l_num = (570, 260)
				if len(word) == 10:
					if a_ == 0:
						l_num = (290, 260)
					if a_ == 1:
						l_num = (325, 260)
					if a_ == 2:
						l_num = (360, 260)
					if a_ == 3:
						l_num = (395, 260)
					if a_ == 4:
						l_num = (430, 260)
					if a_ == 5:
						l_num = (465, 260)
					if a_ == 6:
						l_num = (500, 260)
					if a_ == 7:
						l_num = (535, 260)
					if a_ == 8:
						l_num = (370, 260)
					if a_ == 9:
						l_num = (605, 260)
				if len(word) == 11:
					if a_ == 0:
						l_num = (255, 260)
					if a_ == 1:
						l_num = (290, 260)
					if a_ == 2:
						l_num = (325, 260)
					if a_ == 3:
						l_num = (360, 260)
					if a_ == 4:
						l_num = (395, 260)
					if a_ == 5:
						l_num = (430, 260)
					if a_ == 6:
						l_num = (465, 260)
					if a_ == 7:
						l_num = (500, 260)
					if a_ == 8:
						l_num = (535, 260)
					if a_ == 9:
						l_num = (570, 260)
					if a_ == 10:
						l_num = (605, 260)
				if len(word) == 12:
					if a_ == 0:
						l_num = (255, 260)
					if a_ == 1:
						l_num = (290, 260)
					if a_ == 2:
						l_num = (325, 260)
					if a_ == 3:
						l_num = (360, 260)
					if a_ == 4:
						l_num = (395, 260)
					if a_ == 5:
						l_num = (430, 260)
					if a_ == 6:
						l_num = (465, 260)
					if a_ == 7:
						l_num = (500, 260)
					if a_ == 8:
						l_num = (535, 260)
					if a_ == 9:
						l_num = (570, 260)
					if a_ == 10:
						l_num = (605, 260)
					if a_ == 11:
						l_num = (640, 260)

				screen.blit(a, l_num)
				word100()
		if t_block.collidepoint(mouse_pos) and click:
			guess = 't'
			pygame.draw.rect(screen, white, (t_block))
			if guess in actual_word:
				a_ = actual_word.index(guess)
				a = font4.render(actual_word[a_], True, black)
				if len(word) == 4:
					if a_ == 0:
						l_num = (395, 260)
					if a_ == 1:
						l_num = (430, 260)
					if a_ == 2:
						l_num = (465, 260)
					if a_ == 3:
						l_num = (500, 260)
				if len(word) == 5:
					if a_ == 0:
						l_num = (360, 260)
					if a_ == 1:
						l_num = (395, 260)
					if a_ == 2:
						l_num = (430, 260)
					if a_ == 3:
						l_num = (465, 260)
					if a_ == 4:
						l_num = (500, 260)
				if len(word) == 6:
					if a_ == 0:
						l_num = (360, 260)
					if a_ == 1:
						l_num = (395, 260)
					if a_ == 2:
						l_num = (430, 260)
					if a_ == 3:
						l_num = (465, 260)
					if a_ == 4:
						l_num = (500, 260)
					if a_ == 5:
						l_num = (535, 260)
				if len(word) == 7:
					if a_ == 0:
						l_num = (325, 260)
					if a_ == 1:
						l_num = (360, 260)
					if a_ == 2:
						l_num = (395, 260)
					if a_ == 3:
						l_num = (430, 260)
					if a_ == 4:
						l_num = (465, 260)
					if a_ == 5:
						l_num = (500, 260)
					if a_ == 6:
						l_num = (535, 260)
				if len(word) == 8:
					if a_ == 0:
						l_num = (325, 260)
					if a_ == 1:
						l_num = (360, 260)
					if a_ == 2:
						l_num = (395, 260)
					if a_ == 3:
						l_num = (430, 260)
					if a_ == 4:
						l_num = (465, 260)
					if a_ == 5:
						l_num = (500, 260)
					if a_ == 6:
						l_num = (535, 260)
					if a_ == 7:
						l_num = (570, 260)
				if len(word) == 9:
					if a_ == 0:
						l_num = (290, 260)
					if a_ == 1:
						l_num = (325, 260)
					if a_ == 2:
						l_num = (360, 260)
					if a_ == 3:
						l_num = (395, 260)
					if a_ == 4:
						l_num = (430, 260)
					if a_ == 5:
						l_num = (465, 260)
					if a_ == 6:
						l_num = (500, 260)
					if a_ == 7:
						l_num = (535, 260)
					if a_ == 8:
						l_num = (570, 260)
				if len(word) == 10:
					if a_ == 0:
						l_num = (290, 260)
					if a_ == 1:
						l_num = (325, 260)
					if a_ == 2:
						l_num = (360, 260)
					if a_ == 3:
						l_num = (395, 260)
					if a_ == 4:
						l_num = (430, 260)
					if a_ == 5:
						l_num = (465, 260)
					if a_ == 6:
						l_num = (500, 260)
					if a_ == 7:
						l_num = (535, 260)
					if a_ == 8:
						l_num = (370, 260)
					if a_ == 9:
						l_num = (605, 260)
				if len(word) == 11:
					if a_ == 0:
						l_num = (255, 260)
					if a_ == 1:
						l_num = (290, 260)
					if a_ == 2:
						l_num = (325, 260)
					if a_ == 3:
						l_num = (360, 260)
					if a_ == 4:
						l_num = (395, 260)
					if a_ == 5:
						l_num = (430, 260)
					if a_ == 6:
						l_num = (465, 260)
					if a_ == 7:
						l_num = (500, 260)
					if a_ == 8:
						l_num = (535, 260)
					if a_ == 9:
						l_num = (570, 260)
					if a_ == 10:
						l_num = (605, 260)
				if len(word) == 12:
					if a_ == 0:
						l_num = (255, 260)
					if a_ == 1:
						l_num = (290, 260)
					if a_ == 2:
						l_num = (325, 260)
					if a_ == 3:
						l_num = (360, 260)
					if a_ == 4:
						l_num = (395, 260)
					if a_ == 5:
						l_num = (430, 260)
					if a_ == 6:
						l_num = (465, 260)
					if a_ == 7:
						l_num = (500, 260)
					if a_ == 8:
						l_num = (535, 260)
					if a_ == 9:
						l_num = (570, 260)
					if a_ == 10:
						l_num = (605, 260)
					if a_ == 11:
						l_num = (640, 260)

				screen.blit(a, l_num)
				word100()

		if u_block.collidepoint(mouse_pos) and click:
			guess = 'u'
			pygame.draw.rect(screen, white, (u_block))
			if guess in actual_word:
				a_ = actual_word.index(guess)
				a = font4.render(actual_word[a_], True, black)
				if len(word) == 4:
					if a_ == 0:
						l_num = (395, 260)
					if a_ == 1:
						l_num = (430, 260)
					if a_ == 2:
						l_num = (465, 260)
					if a_ == 3:
						l_num = (500, 260)
				if len(word) == 5:
					if a_ == 0:
						l_num = (360, 260)
					if a_ == 1:
						l_num = (395, 260)
					if a_ == 2:
						l_num = (430, 260)
					if a_ == 3:
						l_num = (465, 260)
					if a_ == 4:
						l_num = (500, 260)
				if len(word) == 6:
					if a_ == 0:
						l_num = (360, 260)
					if a_ == 1:
						l_num = (395, 260)
					if a_ == 2:
						l_num = (430, 260)
					if a_ == 3:
						l_num = (465, 260)
					if a_ == 4:
						l_num = (500, 260)
					if a_ == 5:
						l_num = (535, 260)
				if len(word) == 7:
					if a_ == 0:
						l_num = (325, 260)
					if a_ == 1:
						l_num = (360, 260)
					if a_ == 2:
						l_num = (395, 260)
					if a_ == 3:
						l_num = (430, 260)
					if a_ == 4:
						l_num = (465, 260)
					if a_ == 5:
						l_num = (500, 260)
					if a_ == 6:
						l_num = (535, 260)
				if len(word) == 8:
					if a_ == 0:
						l_num = (325, 260)
					if a_ == 1:
						l_num = (360, 260)
					if a_ == 2:
						l_num = (395, 260)
					if a_ == 3:
						l_num = (430, 260)
					if a_ == 4:
						l_num = (465, 260)
					if a_ == 5:
						l_num = (500, 260)
					if a_ == 6:
						l_num = (535, 260)
					if a_ == 7:
						l_num = (570, 260)
				if len(word) == 9:
					if a_ == 0:
						l_num = (290, 260)
					if a_ == 1:
						l_num = (325, 260)
					if a_ == 2:
						l_num = (360, 260)
					if a_ == 3:
						l_num = (395, 260)
					if a_ == 4:
						l_num = (430, 260)
					if a_ == 5:
						l_num = (465, 260)
					if a_ == 6:
						l_num = (500, 260)
					if a_ == 7:
						l_num = (535, 260)
					if a_ == 8:
						l_num = (570, 260)
				if len(word) == 10:
					if a_ == 0:
						l_num = (290, 260)
					if a_ == 1:
						l_num = (325, 260)
					if a_ == 2:
						l_num = (360, 260)
					if a_ == 3:
						l_num = (395, 260)
					if a_ == 4:
						l_num = (430, 260)
					if a_ == 5:
						l_num = (465, 260)
					if a_ == 6:
						l_num = (500, 260)
					if a_ == 7:
						l_num = (535, 260)
					if a_ == 8:
						l_num = (370, 260)
					if a_ == 9:
						l_num = (605, 260)
				if len(word) == 11:
					if a_ == 0:
						l_num = (255, 260)
					if a_ == 1:
						l_num = (290, 260)
					if a_ == 2:
						l_num = (325, 260)
					if a_ == 3:
						l_num = (360, 260)
					if a_ == 4:
						l_num = (395, 260)
					if a_ == 5:
						l_num = (430, 260)
					if a_ == 6:
						l_num = (465, 260)
					if a_ == 7:
						l_num = (500, 260)
					if a_ == 8:
						l_num = (535, 260)
					if a_ == 9:
						l_num = (570, 260)
					if a_ == 10:
						l_num = (605, 260)
				if len(word) == 12:
					if a_ == 0:
						l_num = (255, 260)
					if a_ == 1:
						l_num = (290, 260)
					if a_ == 2:
						l_num = (325, 260)
					if a_ == 3:
						l_num = (360, 260)
					if a_ == 4:
						l_num = (395, 260)
					if a_ == 5:
						l_num = (430, 260)
					if a_ == 6:
						l_num = (465, 260)
					if a_ == 7:
						l_num = (500, 260)
					if a_ == 8:
						l_num = (535, 260)
					if a_ == 9:
						l_num = (570, 260)
					if a_ == 10:
						l_num = (605, 260)
					if a_ == 11:
						l_num = (640, 260)

				screen.blit(a, l_num)
				word100()
		if v_block.collidepoint(mouse_pos) and click:
			guess = 'v'
			pygame.draw.rect(screen, white, (v_block))
			if guess in actual_word:
				a_ = actual_word.index(guess)
				a = font4.render(actual_word[a_], True, black)
				if len(word) == 4:
					if a_ == 0:
						l_num = (395, 260)
					if a_ == 1:
						l_num = (430, 260)
					if a_ == 2:
						l_num = (465, 260)
					if a_ == 3:
						l_num = (500, 260)
				if len(word) == 5:
					if a_ == 0:
						l_num = (360, 260)
					if a_ == 1:
						l_num = (395, 260)
					if a_ == 2:
						l_num = (430, 260)
					if a_ == 3:
						l_num = (465, 260)
					if a_ == 4:
						l_num = (500, 260)
				if len(word) == 6:
					if a_ == 0:
						l_num = (360, 260)
					if a_ == 1:
						l_num = (395, 260)
					if a_ == 2:
						l_num = (430, 260)
					if a_ == 3:
						l_num = (465, 260)
					if a_ == 4:
						l_num = (500, 260)
					if a_ == 5:
						l_num = (535, 260)
				if len(word) == 7:
					if a_ == 0:
						l_num = (325, 260)
					if a_ == 1:
						l_num = (360, 260)
					if a_ == 2:
						l_num = (395, 260)
					if a_ == 3:
						l_num = (430, 260)
					if a_ == 4:
						l_num = (465, 260)
					if a_ == 5:
						l_num = (500, 260)
					if a_ == 6:
						l_num = (535, 260)
				if len(word) == 8:
					if a_ == 0:
						l_num = (325, 260)
					if a_ == 1:
						l_num = (360, 260)
					if a_ == 2:
						l_num = (395, 260)
					if a_ == 3:
						l_num = (430, 260)
					if a_ == 4:
						l_num = (465, 260)
					if a_ == 5:
						l_num = (500, 260)
					if a_ == 6:
						l_num = (535, 260)
					if a_ == 7:
						l_num = (570, 260)
				if len(word) == 9:
					if a_ == 0:
						l_num = (290, 260)
					if a_ == 1:
						l_num = (325, 260)
					if a_ == 2:
						l_num = (360, 260)
					if a_ == 3:
						l_num = (395, 260)
					if a_ == 4:
						l_num = (430, 260)
					if a_ == 5:
						l_num = (465, 260)
					if a_ == 6:
						l_num = (500, 260)
					if a_ == 7:
						l_num = (535, 260)
					if a_ == 8:
						l_num = (570, 260)
				if len(word) == 10:
					if a_ == 0:
						l_num = (290, 260)
					if a_ == 1:
						l_num = (325, 260)
					if a_ == 2:
						l_num = (360, 260)
					if a_ == 3:
						l_num = (395, 260)
					if a_ == 4:
						l_num = (430, 260)
					if a_ == 5:
						l_num = (465, 260)
					if a_ == 6:
						l_num = (500, 260)
					if a_ == 7:
						l_num = (535, 260)
					if a_ == 8:
						l_num = (370, 260)
					if a_ == 9:
						l_num = (605, 260)
				if len(word) == 11:
					if a_ == 0:
						l_num = (255, 260)
					if a_ == 1:
						l_num = (290, 260)
					if a_ == 2:
						l_num = (325, 260)
					if a_ == 3:
						l_num = (360, 260)
					if a_ == 4:
						l_num = (395, 260)
					if a_ == 5:
						l_num = (430, 260)
					if a_ == 6:
						l_num = (465, 260)
					if a_ == 7:
						l_num = (500, 260)
					if a_ == 8:
						l_num = (535, 260)
					if a_ == 9:
						l_num = (570, 260)
					if a_ == 10:
						l_num = (605, 260)
				if len(word) == 12:
					if a_ == 0:
						l_num = (255, 260)
					if a_ == 1:
						l_num = (290, 260)
					if a_ == 2:
						l_num = (325, 260)
					if a_ == 3:
						l_num = (360, 260)
					if a_ == 4:
						l_num = (395, 260)
					if a_ == 5:
						l_num = (430, 260)
					if a_ == 6:
						l_num = (465, 260)
					if a_ == 7:
						l_num = (500, 260)
					if a_ == 8:
						l_num = (535, 260)
					if a_ == 9:
						l_num = (570, 260)
					if a_ == 10:
						l_num = (605, 260)
					if a_ == 11:
						l_num = (640, 260)

				screen.blit(a, l_num)
				word100()
		if w_block.collidepoint(mouse_pos) and click:
			guess = 'w'
			pygame.draw.rect(screen, white, (w_block))
			if guess in actual_word:
				a_ = actual_word.index(guess)
				a = font4.render(actual_word[a_], True, black)
				if len(word) == 4:
					if a_ == 0:
						l_num = (395, 260)
					if a_ == 1:
						l_num = (430, 260)
					if a_ == 2:
						l_num = (465, 260)
					if a_ == 3:
						l_num = (500, 260)
				if len(word) == 5:
					if a_ == 0:
						l_num = (360, 260)
					if a_ == 1:
						l_num = (395, 260)
					if a_ == 2:
						l_num = (430, 260)
					if a_ == 3:
						l_num = (465, 260)
					if a_ == 4:
						l_num = (500, 260)
				if len(word) == 6:
					if a_ == 0:
						l_num = (360, 260)
					if a_ == 1:
						l_num = (395, 260)
					if a_ == 2:
						l_num = (430, 260)
					if a_ == 3:
						l_num = (465, 260)
					if a_ == 4:
						l_num = (500, 260)
					if a_ == 5:
						l_num = (535, 260)
				if len(word) == 7:
					if a_ == 0:
						l_num = (325, 260)
					if a_ == 1:
						l_num = (360, 260)
					if a_ == 2:
						l_num = (395, 260)
					if a_ == 3:
						l_num = (430, 260)
					if a_ == 4:
						l_num = (465, 260)
					if a_ == 5:
						l_num = (500, 260)
					if a_ == 6:
						l_num = (535, 260)
				if len(word) == 8:
					if a_ == 0:
						l_num = (325, 260)
					if a_ == 1:
						l_num = (360, 260)
					if a_ == 2:
						l_num = (395, 260)
					if a_ == 3:
						l_num = (430, 260)
					if a_ == 4:
						l_num = (465, 260)
					if a_ == 5:
						l_num = (500, 260)
					if a_ == 6:
						l_num = (535, 260)
					if a_ == 7:
						l_num = (570, 260)
				if len(word) == 9:
					if a_ == 0:
						l_num = (290, 260)
					if a_ == 1:
						l_num = (325, 260)
					if a_ == 2:
						l_num = (360, 260)
					if a_ == 3:
						l_num = (395, 260)
					if a_ == 4:
						l_num = (430, 260)
					if a_ == 5:
						l_num = (465, 260)
					if a_ == 6:
						l_num = (500, 260)
					if a_ == 7:
						l_num = (535, 260)
					if a_ == 8:
						l_num = (570, 260)
				if len(word) == 10:
					if a_ == 0:
						l_num = (290, 260)
					if a_ == 1:
						l_num = (325, 260)
					if a_ == 2:
						l_num = (360, 260)
					if a_ == 3:
						l_num = (395, 260)
					if a_ == 4:
						l_num = (430, 260)
					if a_ == 5:
						l_num = (465, 260)
					if a_ == 6:
						l_num = (500, 260)
					if a_ == 7:
						l_num = (535, 260)
					if a_ == 8:
						l_num = (370, 260)
					if a_ == 9:
						l_num = (605, 260)
				if len(word) == 11:
					if a_ == 0:
						l_num = (255, 260)
					if a_ == 1:
						l_num = (290, 260)
					if a_ == 2:
						l_num = (325, 260)
					if a_ == 3:
						l_num = (360, 260)
					if a_ == 4:
						l_num = (395, 260)
					if a_ == 5:
						l_num = (430, 260)
					if a_ == 6:
						l_num = (465, 260)
					if a_ == 7:
						l_num = (500, 260)
					if a_ == 8:
						l_num = (535, 260)
					if a_ == 9:
						l_num = (570, 260)
					if a_ == 10:
						l_num = (605, 260)
				if len(word) == 12:
					if a_ == 0:
						l_num = (255, 260)
					if a_ == 1:
						l_num = (290, 260)
					if a_ == 2:
						l_num = (325, 260)
					if a_ == 3:
						l_num = (360, 260)
					if a_ == 4:
						l_num = (395, 260)
					if a_ == 5:
						l_num = (430, 260)
					if a_ == 6:
						l_num = (465, 260)
					if a_ == 7:
						l_num = (500, 260)
					if a_ == 8:
						l_num = (535, 260)
					if a_ == 9:
						l_num = (570, 260)
					if a_ == 10:
						l_num = (605, 260)
					if a_ == 11:
						l_num = (640, 260)

				screen.blit(a, l_num)
				word100()
		if x_block.collidepoint(mouse_pos) and click:
			guess = 'x'
			pygame.draw.rect(screen, white, (x_block))
			if guess in actual_word:
				a_ = actual_word.index(guess)
				a = font4.render(actual_word[a_], True, black)
				if len(word) == 4:
					if a_ == 0:
						l_num = (395, 260)
					if a_ == 1:
						l_num = (430, 260)
					if a_ == 2:
						l_num = (465, 260)
					if a_ == 3:
						l_num = (500, 260)
				if len(word) == 5:
					if a_ == 0:
						l_num = (360, 260)
					if a_ == 1:
						l_num = (395, 260)
					if a_ == 2:
						l_num = (430, 260)
					if a_ == 3:
						l_num = (465, 260)
					if a_ == 4:
						l_num = (500, 260)
				if len(word) == 6:
					if a_ == 0:
						l_num = (360, 260)
					if a_ == 1:
						l_num = (395, 260)
					if a_ == 2:
						l_num = (430, 260)
					if a_ == 3:
						l_num = (465, 260)
					if a_ == 4:
						l_num = (500, 260)
					if a_ == 5:
						l_num = (535, 260)
				if len(word) == 7:
					if a_ == 0:
						l_num = (325, 260)
					if a_ == 1:
						l_num = (360, 260)
					if a_ == 2:
						l_num = (395, 260)
					if a_ == 3:
						l_num = (430, 260)
					if a_ == 4:
						l_num = (465, 260)
					if a_ == 5:
						l_num = (500, 260)
					if a_ == 6:
						l_num = (535, 260)
				if len(word) == 8:
					if a_ == 0:
						l_num = (325, 260)
					if a_ == 1:
						l_num = (360, 260)
					if a_ == 2:
						l_num = (395, 260)
					if a_ == 3:
						l_num = (430, 260)
					if a_ == 4:
						l_num = (465, 260)
					if a_ == 5:
						l_num = (500, 260)
					if a_ == 6:
						l_num = (535, 260)
					if a_ == 7:
						l_num = (570, 260)
				if len(word) == 9:
					if a_ == 0:
						l_num = (290, 260)
					if a_ == 1:
						l_num = (325, 260)
					if a_ == 2:
						l_num = (360, 260)
					if a_ == 3:
						l_num = (395, 260)
					if a_ == 4:
						l_num = (430, 260)
					if a_ == 5:
						l_num = (465, 260)
					if a_ == 6:
						l_num = (500, 260)
					if a_ == 7:
						l_num = (535, 260)
					if a_ == 8:
						l_num = (570, 260)
				if len(word) == 10:
					if a_ == 0:
						l_num = (290, 260)
					if a_ == 1:
						l_num = (325, 260)
					if a_ == 2:
						l_num = (360, 260)
					if a_ == 3:
						l_num = (395, 260)
					if a_ == 4:
						l_num = (430, 260)
					if a_ == 5:
						l_num = (465, 260)
					if a_ == 6:
						l_num = (500, 260)
					if a_ == 7:
						l_num = (535, 260)
					if a_ == 8:
						l_num = (370, 260)
					if a_ == 9:
						l_num = (605, 260)
				if len(word) == 11:
					if a_ == 0:
						l_num = (255, 260)
					if a_ == 1:
						l_num = (290, 260)
					if a_ == 2:
						l_num = (325, 260)
					if a_ == 3:
						l_num = (360, 260)
					if a_ == 4:
						l_num = (395, 260)
					if a_ == 5:
						l_num = (430, 260)
					if a_ == 6:
						l_num = (465, 260)
					if a_ == 7:
						l_num = (500, 260)
					if a_ == 8:
						l_num = (535, 260)
					if a_ == 9:
						l_num = (570, 260)
					if a_ == 10:
						l_num = (605, 260)
				if len(word) == 12:
					if a_ == 0:
						l_num = (255, 260)
					if a_ == 1:
						l_num = (290, 260)
					if a_ == 2:
						l_num = (325, 260)
					if a_ == 3:
						l_num = (360, 260)
					if a_ == 4:
						l_num = (395, 260)
					if a_ == 5:
						l_num = (430, 260)
					if a_ == 6:
						l_num = (465, 260)
					if a_ == 7:
						l_num = (500, 260)
					if a_ == 8:
						l_num = (535, 260)
					if a_ == 9:
						l_num = (570, 260)
					if a_ == 10:
						l_num = (605, 260)
					if a_ == 11:
						l_num = (640, 260)

				screen.blit(a, l_num)
				word100()
		if y_block.collidepoint(mouse_pos) and click:
			guess = 'y'
			pygame.draw.rect(screen, white, (y_block))
			if guess in actual_word:
				a_ = actual_word.index(guess)
				a = font4.render(actual_word[a_], True, black)
				if len(word) == 4:
					if a_ == 0:
						l_num = (395, 260)
					if a_ == 1:
						l_num = (430, 260)
					if a_ == 2:
						l_num = (465, 260)
					if a_ == 3:
						l_num = (500, 260)
				if len(word) == 5:
					if a_ == 0:
						l_num = (360, 260)
					if a_ == 1:
						l_num = (395, 260)
					if a_ == 2:
						l_num = (430, 260)
					if a_ == 3:
						l_num = (465, 260)
					if a_ == 4:
						l_num = (500, 260)
				if len(word) == 6:
					if a_ == 0:
						l_num = (360, 260)
					if a_ == 1:
						l_num = (395, 260)
					if a_ == 2:
						l_num = (430, 260)
					if a_ == 3:
						l_num = (465, 260)
					if a_ == 4:
						l_num = (500, 260)
					if a_ == 5:
						l_num = (535, 260)
				if len(word) == 7:
					if a_ == 0:
						l_num = (325, 260)
					if a_ == 1:
						l_num = (360, 260)
					if a_ == 2:
						l_num = (395, 260)
					if a_ == 3:
						l_num = (430, 260)
					if a_ == 4:
						l_num = (465, 260)
					if a_ == 5:
						l_num = (500, 260)
					if a_ == 6:
						l_num = (535, 260)
				if len(word) == 8:
					if a_ == 0:
						l_num = (325, 260)
					if a_ == 1:
						l_num = (360, 260)
					if a_ == 2:
						l_num = (395, 260)
					if a_ == 3:
						l_num = (430, 260)
					if a_ == 4:
						l_num = (465, 260)
					if a_ == 5:
						l_num = (500, 260)
					if a_ == 6:
						l_num = (535, 260)
					if a_ == 7:
						l_num = (570, 260)
				if len(word) == 9:
					if a_ == 0:
						l_num = (290, 260)
					if a_ == 1:
						l_num = (325, 260)
					if a_ == 2:
						l_num = (360, 260)
					if a_ == 3:
						l_num = (395, 260)
					if a_ == 4:
						l_num = (430, 260)
					if a_ == 5:
						l_num = (465, 260)
					if a_ == 6:
						l_num = (500, 260)
					if a_ == 7:
						l_num = (535, 260)
					if a_ == 8:
						l_num = (570, 260)
				if len(word) == 10:
					if a_ == 0:
						l_num = (290, 260)
					if a_ == 1:
						l_num = (325, 260)
					if a_ == 2:
						l_num = (360, 260)
					if a_ == 3:
						l_num = (395, 260)
					if a_ == 4:
						l_num = (430, 260)
					if a_ == 5:
						l_num = (465, 260)
					if a_ == 6:
						l_num = (500, 260)
					if a_ == 7:
						l_num = (535, 260)
					if a_ == 8:
						l_num = (370, 260)
					if a_ == 9:
						l_num = (605, 260)
				if len(word) == 11:
					if a_ == 0:
						l_num = (255, 260)
					if a_ == 1:
						l_num = (290, 260)
					if a_ == 2:
						l_num = (325, 260)
					if a_ == 3:
						l_num = (360, 260)
					if a_ == 4:
						l_num = (395, 260)
					if a_ == 5:
						l_num = (430, 260)
					if a_ == 6:
						l_num = (465, 260)
					if a_ == 7:
						l_num = (500, 260)
					if a_ == 8:
						l_num = (535, 260)
					if a_ == 9:
						l_num = (570, 260)
					if a_ == 10:
						l_num = (605, 260)
				if len(word) == 12:
					if a_ == 0:
						l_num = (255, 260)
					if a_ == 1:
						l_num = (290, 260)
					if a_ == 2:
						l_num = (325, 260)
					if a_ == 3:
						l_num = (360, 260)
					if a_ == 4:
						l_num = (395, 260)
					if a_ == 5:
						l_num = (430, 260)
					if a_ == 6:
						l_num = (465, 260)
					if a_ == 7:
						l_num = (500, 260)
					if a_ == 8:
						l_num = (535, 260)
					if a_ == 9:
						l_num = (570, 260)
					if a_ == 10:
						l_num = (605, 260)
					if a_ == 11:
						l_num = (640, 260)

				screen.blit(a, l_num)
				word100()
		if z_block.collidepoint(mouse_pos) and click:
			guess = 'z'
			pygame.draw.rect(screen, white, (z_block))
			if guess in actual_word:
				a_ = actual_word.index(guess)
				a = font4.render(actual_word[a_], True, black)
				if len(word) == 4:
					if a_ == 0:
						l_num = (395, 260)
					if a_ == 1:
						l_num = (430, 260)
					if a_ == 2:
						l_num = (465, 260)
					if a_ == 3:
						l_num = (500, 260)
				if len(word) == 5:
					if a_ == 0:
						l_num = (360, 260)
					if a_ == 1:
						l_num = (395, 260)
					if a_ == 2:
						l_num = (430, 260)
					if a_ == 3:
						l_num = (465, 260)
					if a_ == 4:
						l_num = (500, 260)
				if len(word) == 6:
					if a_ == 0:
						l_num = (360, 260)
					if a_ == 1:
						l_num = (395, 260)
					if a_ == 2:
						l_num = (430, 260)
					if a_ == 3:
						l_num = (465, 260)
					if a_ == 4:
						l_num = (500, 260)
					if a_ == 5:
						l_num = (535, 260)
				if len(word) == 7:
					if a_ == 0:
						l_num = (325, 260)
					if a_ == 1:
						l_num = (360, 260)
					if a_ == 2:
						l_num = (395, 260)
					if a_ == 3:
						l_num = (430, 260)
					if a_ == 4:
						l_num = (465, 260)
					if a_ == 5:
						l_num = (500, 260)
					if a_ == 6:
						l_num = (535, 260)
				if len(word) == 8:
					if a_ == 0:
						l_num = (325, 260)
					if a_ == 1:
						l_num = (360, 260)
					if a_ == 2:
						l_num = (395, 260)
					if a_ == 3:
						l_num = (430, 260)
					if a_ == 4:
						l_num = (465, 260)
					if a_ == 5:
						l_num = (500, 260)
					if a_ == 6:
						l_num = (535, 260)
					if a_ == 7:
						l_num = (570, 260)
				if len(word) == 9:
					if a_ == 0:
						l_num = (290, 260)
					if a_ == 1:
						l_num = (325, 260)
					if a_ == 2:
						l_num = (360, 260)
					if a_ == 3:
						l_num = (395, 260)
					if a_ == 4:
						l_num = (430, 260)
					if a_ == 5:
						l_num = (465, 260)
					if a_ == 6:
						l_num = (500, 260)
					if a_ == 7:
						l_num = (535, 260)
					if a_ == 8:
						l_num = (570, 260)
				if len(word) == 10:
					if a_ == 0:
						l_num = (290, 260)
					if a_ == 1:
						l_num = (325, 260)
					if a_ == 2:
						l_num = (360, 260)
					if a_ == 3:
						l_num = (395, 260)
					if a_ == 4:
						l_num = (430, 260)
					if a_ == 5:
						l_num = (465, 260)
					if a_ == 6:
						l_num = (500, 260)
					if a_ == 7:
						l_num = (535, 260)
					if a_ == 8:
						l_num = (370, 260)
					if a_ == 9:
						l_num = (605, 260)
				if len(word) == 11:
					if a_ == 0:
						l_num = (255, 260)
					if a_ == 1:
						l_num = (290, 260)
					if a_ == 2:
						l_num = (325, 260)
					if a_ == 3:
						l_num = (360, 260)
					if a_ == 4:
						l_num = (395, 260)
					if a_ == 5:
						l_num = (430, 260)
					if a_ == 6:
						l_num = (465, 260)
					if a_ == 7:
						l_num = (500, 260)
					if a_ == 8:
						l_num = (535, 260)
					if a_ == 9:
						l_num = (570, 260)
					if a_ == 10:
						l_num = (605, 260)
				if len(word) == 12:
					if a_ == 0:
						l_num = (255, 260)
					if a_ == 1:
						l_num = (290, 260)
					if a_ == 2:
						l_num = (325, 260)
					if a_ == 3:
						l_num = (360, 260)
					if a_ == 4:
						l_num = (395, 260)
					if a_ == 5:
						l_num = (430, 260)
					if a_ == 6:
						l_num = (465, 260)
					if a_ == 7:
						l_num = (500, 260)
					if a_ == 8:
						l_num = (535, 260)
					if a_ == 9:
						l_num = (570, 260)
					if a_ == 10:
						l_num = (605, 260)
					if a_ == 11:
						l_num = (640, 260)

				screen.blit(a, l_num)
				word100()


def word100():
	global a_, actual_word
	actual_word = actual_word[:a_]+ "-" + actual_word[a_+1:]
	return actual_word

def answer():
	global word, actual_word
	if len(word) == 4:
		if actual_word[0] != '-':
			a = font4.render(actual_word[0], True, yellow)
			screen.blit(a, (395, 260))
		if actual_word[1] != '-':
			a = font4.render(actual_word[1], True, yellow)
			screen.blit(a, (430, 260))
		if actual_word[2] != '-':
			a = font4.render(actual_word[2], True, yellow)
			screen.blit(a, (465, 260))
		if actual_word[3] != '-':
			a = font4.render(actual_word[3], True, yellow)
			screen.blit(a, (500, 260))

	if len(word) == 5:
		if actual_word[0] != '-':
			a = font4.render(actual_word[0], True, yellow)
			screen.blit(a, (360, 260))
		if actual_word[1] != '-':
			a = font4.render(actual_word[1], True, yellow)
			screen.blit(a, (395, 260))
		if actual_word[2] != '-':
			a = font4.render(actual_word[2], True, yellow)
			screen.blit(a, (430, 260))
		if actual_word[3] != '-':
			a = font4.render(actual_word[3], True, yellow)
			screen.blit(a, (465, 260))
		if actual_word[4] != '-':
			a = font4.render(actual_word[4], True, yellow)
			screen.blit(a, (500, 260))
		
	if len(word) == 6:
		if actual_word[0] != '-':
			a = font4.render(actual_word[0], True, yellow)
			screen.blit(a, (360, 260))
		if actual_word[1] != '-':
			a = font4.render(actual_word[1], True, yellow)
			screen.blit(a, (395, 260))
		if actual_word[2] != '-':
			a = font4.render(actual_word[2], True, yellow)
			screen.blit(a, (430, 260))
		if actual_word[3] != '-':
			a = font4.render(actual_word[3], True, yellow)
			screen.blit(a, (465, 260))
		if actual_word[4] != '-':
			a = font4.render(actual_word[4], True, yellow)
			screen.blit(a, (500, 260))
		if actual_word[5] != '-':
			a = font4.render(actual_word[5], True, yellow)
			screen.blit(a, (535, 260))
	if len(word) == 7:
		if actual_word[0] != '-':
			a = font4.render(actual_word[0], True, yellow)
			screen.blit(a, (325, 260))
		if actual_word[1] != '-':
			a = font4.render(actual_word[1], True, yellow)
			screen.blit(a, (360, 260))
		if actual_word[2] != '-':
			a = font4.render(actual_word[2], True, yellow)
			screen.blit(a, (395, 260))
		if actual_word[3] != '-':
			a = font4.render(actual_word[3], True, yellow)
			screen.blit(a, (430, 260))
		if actual_word[4] != '-':
			a = font4.render(actual_word[4], True, yellow)
			screen.blit(a, (465, 260))
		if actual_word[5] != '-':
			a = font4.render(actual_word[5], True, yellow)
			screen.blit(a, (500, 260))
		if actual_word[6] != '-':
			a = font4.render(actual_word[6], True, yellow)
			screen.blit(a, (535, 260))
	if len(word) == 8:
		if actual_word[0] != '-':
			a = font4.render(actual_word[0], True, yellow)
			screen.blit(a, (325, 260))
		if actual_word[1] != '-':
			a = font4.render(actual_word[1], True, yellow)
			screen.blit(a, (360, 260))
		if actual_word[2] != '-':
			a = font4.render(actual_word[2], True, yellow)
			screen.blit(a, (395, 260))
		if actual_word[3] != '-':
			a = font4.render(actual_word[3], True, yellow)
			screen.blit(a, (430, 260))
		if actual_word[4] != '-':
			a = font4.render(actual_word[4], True, yellow)
			screen.blit(a, (465, 260))
		if actual_word[5] != '-':
			a = font4.render(actual_word[5], True, yellow)
			screen.blit(a, (500, 260))
		if actual_word[6] != '-':
			a = font4.render(actual_word[6], True, yellow)
			screen.blit(a, (535, 260))
		if actual_word[7] != '-':
			a = font4.render(actual_word[7], True, yellow)
			screen.blit(a, (570, 260))
	if len(word) == 9:
		if actual_word[0] != '-':
			a = font4.render(actual_word[0], True, yellow)
			screen.blit(a, (290, 260))
		if actual_word[1] != '-':
			a = font4.render(actual_word[1], True, yellow)
			screen.blit(a, (325, 260))
		if actual_word[2] != '-':
			a = font4.render(actual_word[2], True, yellow)
			screen.blit(a, (360, 260))
		if actual_word[3] != '-':
			a = font4.render(actual_word[3], True, yellow)
			screen.blit(a, (395, 260))
		if actual_word[4] != '-':
			a = font4.render(actual_word[4], True, yellow)
			screen.blit(a, (430, 260))
		if actual_word[5] != '-':
			a = font4.render(actual_word[5], True, yellow)
			screen.blit(a, (465, 260))
		if actual_word[6] != '-':
			a = font4.render(actual_word[6], True, yellow)
			screen.blit(a, (500, 260))
		if actual_word[7] != '-':
			a = font4.render(actual_word[7], True, yellow)
			screen.blit(a, (535, 260))
		if actual_word[8] != '-':
			a = font4.render(actual_word[8], True, yellow)
			screen.blit(a, (570, 260))
	if len(word) == 10:
		if actual_word[0] != '-':
			a = font4.render(actual_word[0], True, yellow)
			screen.blit(a, (290, 260))
		if actual_word[1] != '-':
			a = font4.render(actual_word[1], True, yellow)
			screen.blit(a, (325, 260))
		if actual_word[2] != '-':
			a = font4.render(actual_word[2], True, yellow)
			screen.blit(a, (360, 260))
		if actual_word[3] != '-':
			a = font4.render(actual_word[3], True, yellow)
			screen.blit(a, (395, 260))
		if actual_word[4] != '-':
			a = font4.render(actual_word[4], True, yellow)
			screen.blit(a, (430, 260))
		if actual_word[5] != '-':
			a = font4.render(actual_word[5], True, yellow)
			screen.blit(a, (465, 260))
		if actual_word[6] != '-':
			a = font4.render(actual_word[6], True, yellow)
			screen.blit(a, (500, 260))
		if actual_word[7] != '-':
			a = font4.render(actual_word[7], True, yellow)
			screen.blit(a, (535, 260))
		if actual_word[8] != '-':
			a = font4.render(actual_word[8], True, yellow)
			screen.blit(a, (570, 260))
		if actual_word[9] != '-':
			a = font4.render(actual_word[9], True, yellow)
			screen.blit(a, (605, 260))
	if len(word) == 11:
		if actual_word[0] != '-':
			a = font4.render(actual_word[0], True, yellow)
			screen.blit(a, (255, 260))
		if actual_word[1] != '-':
			a = font4.render(actual_word[1], True, yellow)
			screen.blit(a, (290, 260))
		if actual_word[2] != '-':
			a = font4.render(actual_word[2], True, yellow)
			screen.blit(a, (325, 260))
		if actual_word[3] != '-':
			a = font4.render(actual_word[3], True, yellow)
			screen.blit(a, (360, 260))
		if actual_word[4] != '-':
			a = font4.render(actual_word[4], True, yellow)
			screen.blit(a, (395, 260))
		if actual_word[5] != '-':
			a = font4.render(actual_word[5], True, yellow)
			screen.blit(a, (430, 260))
		if actual_word[6] != '-':
			a = font4.render(actual_word[6], True, yellow)
			screen.blit(a, (465, 260))
		if actual_word[7] != '-':
			a = font4.render(actual_word[7], True, yellow)
			screen.blit(a, (500, 260))
		if actual_word[8] != '-':
			a = font4.render(actual_word[8], True, yellow)
			screen.blit(a, (535, 260))
		if actual_word[9] != '-':
			a = font4.render(actual_word[9], True, yellow)
			screen.blit(a, (570, 260))
		if actual_word[10] != '-':
			a = font4.render(actual_word[10], True, yellow)
			screen.blit(a, (605, 260))
	if len(word) == 12:
		if actual_word[0] != '-':
			a = font4.render(actual_word[0], True, yellow)
			screen.blit(a, (255, 260))
		if actual_word[1] != '-':
			a = font4.render(actual_word[1], True, yellow)
			screen.blit(a, (290, 260))
		if actual_word[2] != '-':
			a = font4.render(actual_word[2], True, yellow)
			screen.blit(a, (325, 260))
		if actual_word[3] != '-':
			a = font4.render(actual_word[3], True, yellow)
			screen.blit(a, (360, 260))
		if actual_word[4] != '-':
			a = font4.render(actual_word[4], True, yellow)
			screen.blit(a, (395, 260))
		if actual_word[5] != '-':
			a = font4.render(actual_word[5], True, yellow)
			screen.blit(a, (430, 260))
		if actual_word[6] != '-':
			a = font4.render(actual_word[6], True, yellow)
			screen.blit(a, (465, 260))
		if actual_word[7] != '-':
			a = font4.render(actual_word[7], True, yellow)
			screen.blit(a, (500, 260))
		if actual_word[8] != '-':
			a = font4.render(actual_word[8], True, yellow)
			screen.blit(a, (535, 260))
		if actual_word[9] != '-':
			a = font4.render(actual_word[9], True, yellow)
			screen.blit(a, (570, 260))
		if actual_word[8] != '-':
			a = font4.render(actual_word[10], True, yellow)
			screen.blit(a, (605, 260))
		if actual_word[9] != '-':
			a = font4.render(actual_word[11], True, yellow)
			screen.blit(a, (640, 260))
	pygame.display.update()
		

def hintFinder():
	global hint_len, word, actual_word, answer_var, letter1, letter2, letter3, letter4, letter5, letter6, letter7, letter8, letter9, letter10, letter11, letter12, q_block, a_block, b_block, c_block, d_block, e_block, f_block, g_block, h_block, i_block, j_block, k_block, l_block, m_block, n_block, o_block, p_block, r_block, s_block, t_block, u_block, v_block, w_block, x_block, y_block, z_block
	if len(word) == 4:
		if actual_word[0] != '-' and answer_var and letter1:
			a = font4.render(actual_word[0], True, yellow)
			screen.blit(a, (395, 260))
			answer_var = False
			letter1 = False
			hint_len += 1
			if actual_word[0] == 'a':
				pygame.draw.rect(screen, white, (a_block))
			if actual_word[0] == 'b':
				pygame.draw.rect(screen, white, (b_block))
			if actual_word[0] == 'c':
				pygame.draw.rect(screen, white, (c_block))
			if actual_word[0] == 'd':
				pygame.draw.rect(screen, white, (d_block))
			if actual_word[0] == 'e':
				pygame.draw.rect(screen, white, (e_block))
			if actual_word[0] == 'f':
				pygame.draw.rect(screen, white, (f_block))
			if actual_word[0] == 'g':
				pygame.draw.rect(screen, white, (g_block))
			if actual_word[0] == 'h':
				pygame.draw.rect(screen, white, (h_block))
			if actual_word[0] == 'i':
				pygame.draw.rect(screen, white, (i_block))
			if actual_word[0] == 'j':
				pygame.draw.rect(screen, white, (j_block))
			if actual_word[0] == 'k':
				pygame.draw.rect(screen, white, (k_block))
			if actual_word[0] == 'l':
				pygame.draw.rect(screen, white, (l_block))
			if actual_word[0] == 'm':
				pygame.draw.rect(screen, white, (m_block))
			if actual_word[0] == 'n':
				pygame.draw.rect(screen, white, (n_block))
			if actual_word[0] == 'o':
				pygame.draw.rect(screen, white, (o_block))
			if actual_word[0] == 'p':
				pygame.draw.rect(screen, white, (p_block))
			if actual_word[0] == 'q':
				pygame.draw.rect(screen, white, (q_block))
			if actual_word[0] == 'r':
				pygame.draw.rect(screen, white, (r_block))
			if actual_word[0] == 's':
				pygame.draw.rect(screen, white, (s_block))
			if actual_word[0] == 't':
				pygame.draw.rect(screen, white, (t_block))
			if actual_word[0] == 'u':
				pygame.draw.rect(screen, white, (u_block))
			if actual_word[0] == 'v':
				pygame.draw.rect(screen, white, (v_block))
			if actual_word[0] == 'w':
				pygame.draw.rect(screen, white, (w_block))
			if actual_word[0] == 'x':
				pygame.draw.rect(screen, white, (x_block))
			if actual_word[0] == 'y':
				pygame.draw.rect(screen, white, (y_block))
			if actual_word[0] == 'z':
				pygame.draw.rect(screen, white, (z_block))
			pygame.display.update()
		elif actual_word[1] != '-' and answer_var and letter2:
			a = font4.render(actual_word[1], True, yellow)
			screen.blit(a, (430, 260))
			answer_var = False
			letter2 = False
			hint_len += 1
			if actual_word[1] == 'a':
				pygame.draw.rect(screen, white, (a_block))
			if actual_word[1] == 'b':
				pygame.draw.rect(screen, white, (b_block))
			if actual_word[1] == 'c':
				pygame.draw.rect(screen, white, (c_block))
			if actual_word[1] == 'd':
				pygame.draw.rect(screen, white, (d_block))
			if actual_word[1] == 'e':
				pygame.draw.rect(screen, white, (e_block))
			if actual_word[1] == 'f':
				pygame.draw.rect(screen, white, (f_block))
			if actual_word[1] == 'g':
				pygame.draw.rect(screen, white, (g_block))
			if actual_word[1] == 'h':
				pygame.draw.rect(screen, white, (h_block))
			if actual_word[1] == 'i':
				pygame.draw.rect(screen, white, (i_block))
			if actual_word[1] == 'j':
				pygame.draw.rect(screen, white, (j_block))
			if actual_word[1] == 'k':
				pygame.draw.rect(screen, white, (k_block))
			if actual_word[1] == 'l':
				pygame.draw.rect(screen, white, (l_block))
			if actual_word[1] == 'm':
				pygame.draw.rect(screen, white, (m_block))
			if actual_word[1] == 'n':
				pygame.draw.rect(screen, white, (n_block))
			if actual_word[1] == 'o':
				pygame.draw.rect(screen, white, (o_block))
			if actual_word[1] == 'p':
				pygame.draw.rect(screen, white, (p_block))
			if actual_word[1] == 'q':
				pygame.draw.rect(screen, white, (q_block))
			if actual_word[1] == 'r':
				pygame.draw.rect(screen, white, (r_block))
			if actual_word[1] == 's':
				pygame.draw.rect(screen, white, (s_block))
			if actual_word[1] == 't':
				pygame.draw.rect(screen, white, (t_block))
			if actual_word[1] == 'u':
				pygame.draw.rect(screen, white, (u_block))
			if actual_word[1] == 'v':
				pygame.draw.rect(screen, white, (v_block))
			if actual_word[1] == 'w':
				pygame.draw.rect(screen, white, (w_block))
			if actual_word[1] == 'x':
				pygame.draw.rect(screen, white, (x_block))
			if actual_word[1] == 'y':
				pygame.draw.rect(screen, white, (y_block))
			if actual_word[1] == 'z':
				pygame.draw.rect(screen, white, (z_block))
			pygame.display.update()
		elif actual_word[2] != '-' and answer_var and letter3:
			a = font4.render(actual_word[2], True, yellow)
			screen.blit(a, (465, 260))
			answer_var = False
			letter3 = False
			hint_len += 1
			if actual_word[2] == 'a':
				pygame.draw.rect(screen, white, (a_block))
			if actual_word[2] == 'b':
				pygame.draw.rect(screen, white, (b_block))
			if actual_word[2] == 'c':
				pygame.draw.rect(screen, white, (c_block))
			if actual_word[2] == 'd':
				pygame.draw.rect(screen, white, (d_block))
			if actual_word[2] == 'e':
				pygame.draw.rect(screen, white, (e_block))
			if actual_word[2] == 'f':
				pygame.draw.rect(screen, white, (f_block))
			if actual_word[2] == 'g':
				pygame.draw.rect(screen, white, (g_block))
			if actual_word[2] == 'h':
				pygame.draw.rect(screen, white, (h_block))
			if actual_word[2] == 'i':
				pygame.draw.rect(screen, white, (i_block))
			if actual_word[2] == 'j':
				pygame.draw.rect(screen, white, (j_block))
			if actual_word[2] == 'k':
				pygame.draw.rect(screen, white, (k_block))
			if actual_word[2] == 'l':
				pygame.draw.rect(screen, white, (l_block))
			if actual_word[2] == 'm':
				pygame.draw.rect(screen, white, (m_block))
			if actual_word[2] == 'n':
				pygame.draw.rect(screen, white, (n_block))
			if actual_word[2] == 'o':
				pygame.draw.rect(screen, white, (o_block))
			if actual_word[2] == 'p':
				pygame.draw.rect(screen, white, (p_block))
			if actual_word[2] == 'q':
				pygame.draw.rect(screen, white, (q_block))
			if actual_word[2] == 'r':
				pygame.draw.rect(screen, white, (r_block))
			if actual_word[2] == 's':
				pygame.draw.rect(screen, white, (s_block))
			if actual_word[2] == 't':
				pygame.draw.rect(screen, white, (t_block))
			if actual_word[2] == 'u':
				pygame.draw.rect(screen, white, (u_block))
			if actual_word[2] == 'v':
				pygame.draw.rect(screen, white, (v_block))
			if actual_word[2] == 'w':
				pygame.draw.rect(screen, white, (w_block))
			if actual_word[2] == 'x':
				pygame.draw.rect(screen, white, (x_block))
			if actual_word[2] == 'y':
				pygame.draw.rect(screen, white, (y_block))
			if actual_word[2] == 'z':
				pygame.draw.rect(screen, white, (z_block))
			pygame.display.update()
		elif actual_word[3] != '-'and answer_var and letter4:
			a = font4.render(actual_word[3], True, yellow)
			screen.blit(a, (500, 260))
			answer_var = False
			letter4 = False
			hint_len += 1
			if actual_word[3] == 'a':
				pygame.draw.rect(screen, white, (a_block))
			if actual_word[3] == 'b':
				pygame.draw.rect(screen, white, (b_block))
			if actual_word[3] == 'c':
				pygame.draw.rect(screen, white, (c_block))
			if actual_word[3] == 'd':
				pygame.draw.rect(screen, white, (d_block))
			if actual_word[3] == 'e':
				pygame.draw.rect(screen, white, (e_block))
			if actual_word[3] == 'f':
				pygame.draw.rect(screen, white, (f_block))
			if actual_word[3] == 'g':
				pygame.draw.rect(screen, white, (g_block))
			if actual_word[3] == 'h':
				pygame.draw.rect(screen, white, (h_block))
			if actual_word[3] == 'i':
				pygame.draw.rect(screen, white, (i_block))
			if actual_word[3] == 'j':
				pygame.draw.rect(screen, white, (j_block))
			if actual_word[3] == 'k':
				pygame.draw.rect(screen, white, (k_block))
			if actual_word[3] == 'l':
				pygame.draw.rect(screen, white, (l_block))
			if actual_word[3] == 'm':
				pygame.draw.rect(screen, white, (m_block))
			if actual_word[3] == 'n':
				pygame.draw.rect(screen, white, (n_block))
			if actual_word[3] == 'o':
				pygame.draw.rect(screen, white, (o_block))
			if actual_word[3] == 'p':
				pygame.draw.rect(screen, white, (p_block))
			if actual_word[3] == 'q':
				pygame.draw.rect(screen, white, (q_block))
			if actual_word[3] == 'r':
				pygame.draw.rect(screen, white, (r_block))
			if actual_word[3] == 's':
				pygame.draw.rect(screen, white, (s_block))
			if actual_word[3] == 't':
				pygame.draw.rect(screen, white, (t_block))
			if actual_word[3] == 'u':
				pygame.draw.rect(screen, white, (u_block))
			if actual_word[3] == 'v':
				pygame.draw.rect(screen, white, (v_block))
			if actual_word[3] == 'w':
				pygame.draw.rect(screen, white, (w_block))
			if actual_word[3] == 'x':
				pygame.draw.rect(screen, white, (x_block))
			if actual_word[3] == 'y':
				pygame.draw.rect(screen, white, (y_block))
			if actual_word[3] == 'z':
				pygame.draw.rect(screen, white, (z_block))
			pygame.display.update()
	if len(word) == 5:
		if actual_word[0] != '-' and answer_var and letter1:
			a = font4.render(actual_word[0], True, yellow)
			screen.blit(a, (360, 260))
			answer_var = False
			hint_len += 1
			letter1 = False
			if actual_word[0] == 'a':
				pygame.draw.rect(screen, white, (a_block))
			if actual_word[0] == 'b':
				pygame.draw.rect(screen, white, (b_block))
			if actual_word[0] == 'c':
				pygame.draw.rect(screen, white, (c_block))
			if actual_word[0] == 'd':
				pygame.draw.rect(screen, white, (d_block))
			if actual_word[0] == 'e':
				pygame.draw.rect(screen, white, (e_block))
			if actual_word[0] == 'f':
				pygame.draw.rect(screen, white, (f_block))
			if actual_word[0] == 'g':
				pygame.draw.rect(screen, white, (g_block))
			if actual_word[0] == 'h':
				pygame.draw.rect(screen, white, (h_block))
			if actual_word[0] == 'i':
				pygame.draw.rect(screen, white, (i_block))
			if actual_word[0] == 'j':
				pygame.draw.rect(screen, white, (j_block))
			if actual_word[0] == 'k':
				pygame.draw.rect(screen, white, (k_block))
			if actual_word[0] == 'l':
				pygame.draw.rect(screen, white, (l_block))
			if actual_word[0] == 'm':
				pygame.draw.rect(screen, white, (m_block))
			if actual_word[0] == 'n':
				pygame.draw.rect(screen, white, (n_block))
			if actual_word[0] == 'o':
				pygame.draw.rect(screen, white, (o_block))
			if actual_word[0] == 'p':
				pygame.draw.rect(screen, white, (p_block))
			if actual_word[0] == 'q':
				pygame.draw.rect(screen, white, (q_block))
			if actual_word[0] == 'r':
				pygame.draw.rect(screen, white, (r_block))
			if actual_word[0] == 's':
				pygame.draw.rect(screen, white, (s_block))
			if actual_word[0] == 't':
				pygame.draw.rect(screen, white, (t_block))
			if actual_word[0] == 'u':
				pygame.draw.rect(screen, white, (u_block))
			if actual_word[0] == 'v':
				pygame.draw.rect(screen, white, (v_block))
			if actual_word[0] == 'w':
				pygame.draw.rect(screen, white, (w_block))
			if actual_word[0] == 'x':
				pygame.draw.rect(screen, white, (x_block))
			if actual_word[0] == 'y':
				pygame.draw.rect(screen, white, (y_block))
			if actual_word[0] == 'z':
				pygame.draw.rect(screen, white, (z_block))
			pygame.display.update()
		if actual_word[1] != '-'and answer_var and letter2:
			a = font4.render(actual_word[1], True, yellow)
			screen.blit(a, (395, 260))
			answer_var = False
			letter2 = False
			hint_len += 1
			if actual_word[1] == 'a':
				pygame.draw.rect(screen, white, (a_block))
			if actual_word[1] == 'b':
				pygame.draw.rect(screen, white, (b_block))
			if actual_word[1] == 'c':
				pygame.draw.rect(screen, white, (c_block))
			if actual_word[1] == 'd':
				pygame.draw.rect(screen, white, (d_block))
			if actual_word[1] == 'e':
				pygame.draw.rect(screen, white, (e_block))
			if actual_word[1] == 'f':
				pygame.draw.rect(screen, white, (f_block))
			if actual_word[1] == 'g':
				pygame.draw.rect(screen, white, (g_block))
			if actual_word[1] == 'h':
				pygame.draw.rect(screen, white, (h_block))
			if actual_word[1] == 'i':
				pygame.draw.rect(screen, white, (i_block))
			if actual_word[1] == 'j':
				pygame.draw.rect(screen, white, (j_block))
			if actual_word[1] == 'k':
				pygame.draw.rect(screen, white, (k_block))
			if actual_word[1] == 'l':
				pygame.draw.rect(screen, white, (l_block))
			if actual_word[1] == 'm':
				pygame.draw.rect(screen, white, (m_block))
			if actual_word[1] == 'n':
				pygame.draw.rect(screen, white, (n_block))
			if actual_word[1] == 'o':
				pygame.draw.rect(screen, white, (o_block))
			if actual_word[1] == 'p':
				pygame.draw.rect(screen, white, (p_block))
			if actual_word[1] == 'q':
				pygame.draw.rect(screen, white, (q_block))
			if actual_word[1] == 'r':
				pygame.draw.rect(screen, white, (r_block))
			if actual_word[1] == 's':
				pygame.draw.rect(screen, white, (s_block))
			if actual_word[1] == 't':
				pygame.draw.rect(screen, white, (t_block))
			if actual_word[1] == 'u':
				pygame.draw.rect(screen, white, (u_block))
			if actual_word[1] == 'v':
				pygame.draw.rect(screen, white, (v_block))
			if actual_word[1] == 'w':
				pygame.draw.rect(screen, white, (w_block))
			if actual_word[1] == 'x':
				pygame.draw.rect(screen, white, (x_block))
			if actual_word[1] == 'y':
				pygame.draw.rect(screen, white, (y_block))
			if actual_word[1] == 'z':
				pygame.draw.rect(screen, white, (z_block))
			pygame.display.update()
		if actual_word[2] != '-'and answer_var and letter3:
			a = font4.render(actual_word[2], True, yellow)
			screen.blit(a, (430, 260))
			answer_var = False
			letter3 = False
			hint_len += 1
			if actual_word[2] == 'a':
				pygame.draw.rect(screen, white, (a_block))
			if actual_word[2] == 'b':
				pygame.draw.rect(screen, white, (b_block))
			if actual_word[2] == 'c':
				pygame.draw.rect(screen, white, (c_block))
			if actual_word[2] == 'd':
				pygame.draw.rect(screen, white, (d_block))
			if actual_word[2] == 'e':
				pygame.draw.rect(screen, white, (e_block))
			if actual_word[2] == 'f':
				pygame.draw.rect(screen, white, (f_block))
			if actual_word[2] == 'g':
				pygame.draw.rect(screen, white, (g_block))
			if actual_word[2] == 'h':
				pygame.draw.rect(screen, white, (h_block))
			if actual_word[2] == 'i':
				pygame.draw.rect(screen, white, (i_block))
			if actual_word[2] == 'j':
				pygame.draw.rect(screen, white, (j_block))
			if actual_word[2] == 'k':
				pygame.draw.rect(screen, white, (k_block))
			if actual_word[2] == 'l':
				pygame.draw.rect(screen, white, (l_block))
			if actual_word[2] == 'm':
				pygame.draw.rect(screen, white, (m_block))
			if actual_word[2] == 'n':
				pygame.draw.rect(screen, white, (n_block))
			if actual_word[2] == 'o':
				pygame.draw.rect(screen, white, (o_block))
			if actual_word[2] == 'p':
				pygame.draw.rect(screen, white, (p_block))
			if actual_word[2] == 'q':
				pygame.draw.rect(screen, white, (q_block))
			if actual_word[2] == 'r':
				pygame.draw.rect(screen, white, (r_block))
			if actual_word[2] == 's':
				pygame.draw.rect(screen, white, (s_block))
			if actual_word[2] == 't':
				pygame.draw.rect(screen, white, (t_block))
			if actual_word[2] == 'u':
				pygame.draw.rect(screen, white, (u_block))
			if actual_word[2] == 'v':
				pygame.draw.rect(screen, white, (v_block))
			if actual_word[2] == 'w':
				pygame.draw.rect(screen, white, (w_block))
			if actual_word[2] == 'x':
				pygame.draw.rect(screen, white, (x_block))
			if actual_word[2] == 'y':
				pygame.draw.rect(screen, white, (y_block))
			if actual_word[2] == 'z':
				pygame.draw.rect(screen, white, (z_block))
			pygame.display.update()
		if actual_word[3] != '-'and answer_var and letter4:
			a = font4.render(actual_word[3], True, yellow)
			screen.blit(a, (465, 260))
			answer_var = False
			letter4 = False
			hint_len += 1
			if actual_word[3] == 'a':
				pygame.draw.rect(screen, white, (a_block))
			if actual_word[3] == 'b':
				pygame.draw.rect(screen, white, (b_block))
			if actual_word[3] == 'c':
				pygame.draw.rect(screen, white, (c_block))
			if actual_word[3] == 'd':
				pygame.draw.rect(screen, white, (d_block))
			if actual_word[3] == 'e':
				pygame.draw.rect(screen, white, (e_block))
			if actual_word[3] == 'f':
				pygame.draw.rect(screen, white, (f_block))
			if actual_word[3] == 'g':
				pygame.draw.rect(screen, white, (g_block))
			if actual_word[3] == 'h':
				pygame.draw.rect(screen, white, (h_block))
			if actual_word[3] == 'i':
				pygame.draw.rect(screen, white, (i_block))
			if actual_word[3] == 'j':
				pygame.draw.rect(screen, white, (j_block))
			if actual_word[3] == 'k':
				pygame.draw.rect(screen, white, (k_block))
			if actual_word[3] == 'l':
				pygame.draw.rect(screen, white, (l_block))
			if actual_word[3] == 'm':
				pygame.draw.rect(screen, white, (m_block))
			if actual_word[3] == 'n':
				pygame.draw.rect(screen, white, (n_block))
			if actual_word[3] == 'o':
				pygame.draw.rect(screen, white, (o_block))
			if actual_word[3] == 'p':
				pygame.draw.rect(screen, white, (p_block))
			if actual_word[3] == 'q':
				pygame.draw.rect(screen, white, (q_block))
			if actual_word[3] == 'r':
				pygame.draw.rect(screen, white, (r_block))
			if actual_word[3] == 's':
				pygame.draw.rect(screen, white, (s_block))
			if actual_word[3] == 't':
				pygame.draw.rect(screen, white, (t_block))
			if actual_word[3] == 'u':
				pygame.draw.rect(screen, white, (u_block))
			if actual_word[3] == 'v':
				pygame.draw.rect(screen, white, (v_block))
			if actual_word[3] == 'w':
				pygame.draw.rect(screen, white, (w_block))
			if actual_word[3] == 'x':
				pygame.draw.rect(screen, white, (x_block))
			if actual_word[3] == 'y':
				pygame.draw.rect(screen, white, (y_block))
			if actual_word[3] == 'z':
				pygame.draw.rect(screen, white, (z_block))
			pygame.display.update()
		if actual_word[4] != '-'and answer_var and letter5:
			a = font4.render(actual_word[4], True, yellow)
			screen.blit(a, (500, 260))
			answer_var = False
			letter5 = False
			hint_len += 1
			if actual_word[4] == 'a':
				pygame.draw.rect(screen, white, (a_block))
			if actual_word[4] == 'b':
				pygame.draw.rect(screen, white, (b_block))
			if actual_word[4] == 'c':
				pygame.draw.rect(screen, white, (c_block))
			if actual_word[4] == 'd':
				pygame.draw.rect(screen, white, (d_block))
			if actual_word[4] == 'e':
				pygame.draw.rect(screen, white, (e_block))
			if actual_word[4] == 'f':
				pygame.draw.rect(screen, white, (f_block))
			if actual_word[4] == 'g':
				pygame.draw.rect(screen, white, (g_block))
			if actual_word[4] == 'h':
				pygame.draw.rect(screen, white, (h_block))
			if actual_word[4] == 'i':
				pygame.draw.rect(screen, white, (i_block))
			if actual_word[4] == 'j':
				pygame.draw.rect(screen, white, (j_block))
			if actual_word[4] == 'k':
				pygame.draw.rect(screen, white, (k_block))
			if actual_word[4] == 'l':
				pygame.draw.rect(screen, white, (l_block))
			if actual_word[4] == 'm':
				pygame.draw.rect(screen, white, (m_block))
			if actual_word[4] == 'n':
				pygame.draw.rect(screen, white, (n_block))
			if actual_word[4] == 'o':
				pygame.draw.rect(screen, white, (o_block))
			if actual_word[4] == 'p':
				pygame.draw.rect(screen, white, (p_block))
			if actual_word[4] == 'q':
				pygame.draw.rect(screen, white, (q_block))
			if actual_word[4] == 'r':
				pygame.draw.rect(screen, white, (r_block))
			if actual_word[4] == 's':
				pygame.draw.rect(screen, white, (s_block))
			if actual_word[4] == 't':
				pygame.draw.rect(screen, white, (t_block))
			if actual_word[4] == 'u':
				pygame.draw.rect(screen, white, (u_block))
			if actual_word[4] == 'v':
				pygame.draw.rect(screen, white, (v_block))
			if actual_word[4] == 'w':
				pygame.draw.rect(screen, white, (w_block))
			if actual_word[4] == 'x':
				pygame.draw.rect(screen, white, (x_block))
			if actual_word[4] == 'y':
				pygame.draw.rect(screen, white, (y_block))
			if actual_word[4] == 'z':
				pygame.draw.rect(screen, white, (z_block))
			pygame.display.update()
	if len(word) == 6:
		if actual_word[0] != '-'and answer_var and letter1:
			a = font4.render(actual_word[0], True, yellow)
			screen.blit(a, (360, 260))
			answer_var = False
			letter1 = False
			hint_len += 1
			if actual_word[0] == 'a':
				pygame.draw.rect(screen, white, (a_block))
			if actual_word[0] == 'b':
				pygame.draw.rect(screen, white, (b_block))
			if actual_word[0] == 'c':
				pygame.draw.rect(screen, white, (c_block))
			if actual_word[0] == 'd':
				pygame.draw.rect(screen, white, (d_block))
			if actual_word[0] == 'e':
				pygame.draw.rect(screen, white, (e_block))
			if actual_word[0] == 'f':
				pygame.draw.rect(screen, white, (f_block))
			if actual_word[0] == 'g':
				pygame.draw.rect(screen, white, (g_block))
			if actual_word[0] == 'h':
				pygame.draw.rect(screen, white, (h_block))
			if actual_word[0] == 'i':
				pygame.draw.rect(screen, white, (i_block))
			if actual_word[0] == 'j':
				pygame.draw.rect(screen, white, (j_block))
			if actual_word[0] == 'k':
				pygame.draw.rect(screen, white, (k_block))
			if actual_word[0] == 'l':
				pygame.draw.rect(screen, white, (l_block))
			if actual_word[0] == 'm':
				pygame.draw.rect(screen, white, (m_block))
			if actual_word[0] == 'n':
				pygame.draw.rect(screen, white, (n_block))
			if actual_word[0] == 'o':
				pygame.draw.rect(screen, white, (o_block))
			if actual_word[0] == 'p':
				pygame.draw.rect(screen, white, (p_block))
			if actual_word[0] == 'q':
				pygame.draw.rect(screen, white, (q_block))
			if actual_word[0] == 'r':
				pygame.draw.rect(screen, white, (r_block))
			if actual_word[0] == 's':
				pygame.draw.rect(screen, white, (s_block))
			if actual_word[0] == 't':
				pygame.draw.rect(screen, white, (t_block))
			if actual_word[0] == 'u':
				pygame.draw.rect(screen, white, (u_block))
			if actual_word[0] == 'v':
				pygame.draw.rect(screen, white, (v_block))
			if actual_word[0] == 'w':
				pygame.draw.rect(screen, white, (w_block))
			if actual_word[0] == 'x':
				pygame.draw.rect(screen, white, (x_block))
			if actual_word[0] == 'y':
				pygame.draw.rect(screen, white, (y_block))
			if actual_word[0] == 'z':
				pygame.draw.rect(screen, white, (z_block))
			pygame.display.update()
		if actual_word[1] != '-'and answer_var and letter2:
			a = font4.render(actual_word[1], True, yellow)
			screen.blit(a, (395, 260))
			answer_var = False
			letter2 = False
			hint_len += 1
			if actual_word[1] == 'a':
				pygame.draw.rect(screen, white, (a_block))
			if actual_word[1] == 'b':
				pygame.draw.rect(screen, white, (b_block))
			if actual_word[1] == 'c':
				pygame.draw.rect(screen, white, (c_block))
			if actual_word[1] == 'd':
				pygame.draw.rect(screen, white, (d_block))
			if actual_word[1] == 'e':
				pygame.draw.rect(screen, white, (e_block))
			if actual_word[1] == 'f':
				pygame.draw.rect(screen, white, (f_block))
			if actual_word[1] == 'g':
				pygame.draw.rect(screen, white, (g_block))
			if actual_word[1] == 'h':
				pygame.draw.rect(screen, white, (h_block))
			if actual_word[1] == 'i':
				pygame.draw.rect(screen, white, (i_block))
			if actual_word[1] == 'j':
				pygame.draw.rect(screen, white, (j_block))
			if actual_word[1] == 'k':
				pygame.draw.rect(screen, white, (k_block))
			if actual_word[1] == 'l':
				pygame.draw.rect(screen, white, (l_block))
			if actual_word[1] == 'm':
				pygame.draw.rect(screen, white, (m_block))
			if actual_word[1] == 'n':
				pygame.draw.rect(screen, white, (n_block))
			if actual_word[1] == 'o':
				pygame.draw.rect(screen, white, (o_block))
			if actual_word[1] == 'p':
				pygame.draw.rect(screen, white, (p_block))
			if actual_word[1] == 'q':
				pygame.draw.rect(screen, white, (q_block))
			if actual_word[1] == 'r':
				pygame.draw.rect(screen, white, (r_block))
			if actual_word[1] == 's':
				pygame.draw.rect(screen, white, (s_block))
			if actual_word[1] == 't':
				pygame.draw.rect(screen, white, (t_block))
			if actual_word[1] == 'u':
				pygame.draw.rect(screen, white, (u_block))
			if actual_word[1] == 'v':
				pygame.draw.rect(screen, white, (v_block))
			if actual_word[1] == 'w':
				pygame.draw.rect(screen, white, (w_block))
			if actual_word[1] == 'x':
				pygame.draw.rect(screen, white, (x_block))
			if actual_word[1] == 'y':
				pygame.draw.rect(screen, white, (y_block))
			if actual_word[1] == 'z':
				pygame.draw.rect(screen, white, (z_block))
			pygame.display.update()
		if actual_word[2] != '-'and answer_var and letter3:
			a = font4.render(actual_word[2], True, yellow)
			screen.blit(a, (430, 260))
			answer_var = False
			letter3 = False
			hint_len += 1
			if actual_word[2] == 'a':
				pygame.draw.rect(screen, white, (a_block))
			if actual_word[2] == 'b':
				pygame.draw.rect(screen, white, (b_block))
			if actual_word[2] == 'c':
				pygame.draw.rect(screen, white, (c_block))
			if actual_word[2] == 'd':
				pygame.draw.rect(screen, white, (d_block))
			if actual_word[2] == 'e':
				pygame.draw.rect(screen, white, (e_block))
			if actual_word[2] == 'f':
				pygame.draw.rect(screen, white, (f_block))
			if actual_word[2] == 'g':
				pygame.draw.rect(screen, white, (g_block))
			if actual_word[2] == 'h':
				pygame.draw.rect(screen, white, (h_block))
			if actual_word[2] == 'i':
				pygame.draw.rect(screen, white, (i_block))
			if actual_word[2] == 'j':
				pygame.draw.rect(screen, white, (j_block))
			if actual_word[2] == 'k':
				pygame.draw.rect(screen, white, (k_block))
			if actual_word[2] == 'l':
				pygame.draw.rect(screen, white, (l_block))
			if actual_word[2] == 'm':
				pygame.draw.rect(screen, white, (m_block))
			if actual_word[2] == 'n':
				pygame.draw.rect(screen, white, (n_block))
			if actual_word[2] == 'o':
				pygame.draw.rect(screen, white, (o_block))
			if actual_word[2] == 'p':
				pygame.draw.rect(screen, white, (p_block))
			if actual_word[2] == 'q':
				pygame.draw.rect(screen, white, (q_block))
			if actual_word[2] == 'r':
				pygame.draw.rect(screen, white, (r_block))
			if actual_word[2] == 's':
				pygame.draw.rect(screen, white, (s_block))
			if actual_word[2] == 't':
				pygame.draw.rect(screen, white, (t_block))
			if actual_word[2] == 'u':
				pygame.draw.rect(screen, white, (u_block))
			if actual_word[2] == 'v':
				pygame.draw.rect(screen, white, (v_block))
			if actual_word[2] == 'w':
				pygame.draw.rect(screen, white, (w_block))
			if actual_word[2] == 'x':
				pygame.draw.rect(screen, white, (x_block))
			if actual_word[2] == 'y':
				pygame.draw.rect(screen, white, (y_block))
			if actual_word[2] == 'z':
				pygame.draw.rect(screen, white, (z_block))
			pygame.display.update()
		if actual_word[3] != '-'and answer_var and letter4:
			a = font4.render(actual_word[3], True, yellow)
			screen.blit(a, (465, 260))
			answer_var = False
			letter4 = False
			hint_len += 1
			if actual_word[3] == 'a':
				pygame.draw.rect(screen, white, (a_block))
			if actual_word[3] == 'b':
				pygame.draw.rect(screen, white, (b_block))
			if actual_word[3] == 'c':
				pygame.draw.rect(screen, white, (c_block))
			if actual_word[3] == 'd':
				pygame.draw.rect(screen, white, (d_block))
			if actual_word[3] == 'e':
				pygame.draw.rect(screen, white, (e_block))
			if actual_word[3] == 'f':
				pygame.draw.rect(screen, white, (f_block))
			if actual_word[3] == 'g':
				pygame.draw.rect(screen, white, (g_block))
			if actual_word[3] == 'h':
				pygame.draw.rect(screen, white, (h_block))
			if actual_word[3] == 'i':
				pygame.draw.rect(screen, white, (i_block))
			if actual_word[3] == 'j':
				pygame.draw.rect(screen, white, (j_block))
			if actual_word[3] == 'k':
				pygame.draw.rect(screen, white, (k_block))
			if actual_word[3] == 'l':
				pygame.draw.rect(screen, white, (l_block))
			if actual_word[3] == 'm':
				pygame.draw.rect(screen, white, (m_block))
			if actual_word[3] == 'n':
				pygame.draw.rect(screen, white, (n_block))
			if actual_word[3] == 'o':
				pygame.draw.rect(screen, white, (o_block))
			if actual_word[3] == 'p':
				pygame.draw.rect(screen, white, (p_block))
			if actual_word[3] == 'q':
				pygame.draw.rect(screen, white, (q_block))
			if actual_word[3] == 'r':
				pygame.draw.rect(screen, white, (r_block))
			if actual_word[3] == 's':
				pygame.draw.rect(screen, white, (s_block))
			if actual_word[3] == 't':
				pygame.draw.rect(screen, white, (t_block))
			if actual_word[3] == 'u':
				pygame.draw.rect(screen, white, (u_block))
			if actual_word[3] == 'v':
				pygame.draw.rect(screen, white, (v_block))
			if actual_word[3] == 'w':
				pygame.draw.rect(screen, white, (w_block))
			if actual_word[3] == 'x':
				pygame.draw.rect(screen, white, (x_block))
			if actual_word[3] == 'y':
				pygame.draw.rect(screen, white, (y_block))
			if actual_word[3] == 'z':
				pygame.draw.rect(screen, white, (z_block))
			pygame.display.update()
		if actual_word[4] != '-'and answer_var and letter5:
			a = font4.render(actual_word[4], True, yellow)
			screen.blit(a, (500, 260))
			answer_var = False
			letter5 = False
			hint_len += 1
			if actual_word[4] == 'a':
				pygame.draw.rect(screen, white, (a_block))
			if actual_word[4] == 'b':
				pygame.draw.rect(screen, white, (b_block))
			if actual_word[4] == 'c':
				pygame.draw.rect(screen, white, (c_block))
			if actual_word[4] == 'd':
				pygame.draw.rect(screen, white, (d_block))
			if actual_word[4] == 'e':
				pygame.draw.rect(screen, white, (e_block))
			if actual_word[4] == 'f':
				pygame.draw.rect(screen, white, (f_block))
			if actual_word[4] == 'g':
				pygame.draw.rect(screen, white, (g_block))
			if actual_word[4] == 'h':
				pygame.draw.rect(screen, white, (h_block))
			if actual_word[4] == 'i':
				pygame.draw.rect(screen, white, (i_block))
			if actual_word[4] == 'j':
				pygame.draw.rect(screen, white, (j_block))
			if actual_word[4] == 'k':
				pygame.draw.rect(screen, white, (k_block))
			if actual_word[4] == 'l':
				pygame.draw.rect(screen, white, (l_block))
			if actual_word[4] == 'm':
				pygame.draw.rect(screen, white, (m_block))
			if actual_word[4] == 'n':
				pygame.draw.rect(screen, white, (n_block))
			if actual_word[4] == 'o':
				pygame.draw.rect(screen, white, (o_block))
			if actual_word[4] == 'p':
				pygame.draw.rect(screen, white, (p_block))
			if actual_word[4] == 'q':
				pygame.draw.rect(screen, white, (q_block))
			if actual_word[4] == 'r':
				pygame.draw.rect(screen, white, (r_block))
			if actual_word[4] == 's':
				pygame.draw.rect(screen, white, (s_block))
			if actual_word[4] == 't':
				pygame.draw.rect(screen, white, (t_block))
			if actual_word[4] == 'u':
				pygame.draw.rect(screen, white, (u_block))
			if actual_word[4] == 'v':
				pygame.draw.rect(screen, white, (v_block))
			if actual_word[4] == 'w':
				pygame.draw.rect(screen, white, (w_block))
			if actual_word[4] == 'x':
				pygame.draw.rect(screen, white, (x_block))
			if actual_word[4] == 'y':
				pygame.draw.rect(screen, white, (y_block))
			if actual_word[4] == 'z':
				pygame.draw.rect(screen, white, (z_block))
			pygame.display.update()
		if actual_word[5] != '-'and answer_var and letter6:
			a = font4.render(actual_word[5], True, yellow)
			screen.blit(a, (535, 260))
			answer_var = False
			letter6 = False
			hint_len += 1
			if actual_word[5] == 'a':
				pygame.draw.rect(screen, white, (a_block))
			if actual_word[5] == 'b':
				pygame.draw.rect(screen, white, (b_block))
			if actual_word[5] == 'c':
				pygame.draw.rect(screen, white, (c_block))
			if actual_word[5] == 'd':
				pygame.draw.rect(screen, white, (d_block))
			if actual_word[5] == 'e':
				pygame.draw.rect(screen, white, (e_block))
			if actual_word[5] == 'f':
				pygame.draw.rect(screen, white, (f_block))
			if actual_word[5] == 'g':
				pygame.draw.rect(screen, white, (g_block))
			if actual_word[5] == 'h':
				pygame.draw.rect(screen, white, (h_block))
			if actual_word[5] == 'i':
				pygame.draw.rect(screen, white, (i_block))
			if actual_word[5] == 'j':
				pygame.draw.rect(screen, white, (j_block))
			if actual_word[5] == 'k':
				pygame.draw.rect(screen, white, (k_block))
			if actual_word[5] == 'l':
				pygame.draw.rect(screen, white, (l_block))
			if actual_word[5] == 'm':
				pygame.draw.rect(screen, white, (m_block))
			if actual_word[5] == 'n':
				pygame.draw.rect(screen, white, (n_block))
			if actual_word[5] == 'o':
				pygame.draw.rect(screen, white, (o_block))
			if actual_word[5] == 'p':
				pygame.draw.rect(screen, white, (p_block))
			if actual_word[5] == 'q':
				pygame.draw.rect(screen, white, (q_block))
			if actual_word[5] == 'r':
				pygame.draw.rect(screen, white, (r_block))
			if actual_word[5] == 's':
				pygame.draw.rect(screen, white, (s_block))
			if actual_word[5] == 't':
				pygame.draw.rect(screen, white, (t_block))
			if actual_word[5] == 'u':
				pygame.draw.rect(screen, white, (u_block))
			if actual_word[5] == 'v':
				pygame.draw.rect(screen, white, (v_block))
			if actual_word[5] == 'w':
				pygame.draw.rect(screen, white, (w_block))
			if actual_word[5] == 'x':
				pygame.draw.rect(screen, white, (x_block))
			if actual_word[5] == 'y':
				pygame.draw.rect(screen, white, (y_block))
			if actual_word[5] == 'z':
				pygame.draw.rect(screen, white, (z_block))
			pygame.display.update()
	if len(word) == 7:
		if actual_word[0] != '-'and answer_var and letter1:
			a = font4.render(actual_word[0], True, yellow)
			screen.blit(a, (325, 260))
			answer_var = False
			letter1 = False
			hint_len += 1
			if actual_word[0] == 'a':
				pygame.draw.rect(screen, white, (a_block))
			if actual_word[0] == 'b':
				pygame.draw.rect(screen, white, (b_block))
			if actual_word[0] == 'c':
				pygame.draw.rect(screen, white, (c_block))
			if actual_word[0] == 'd':
				pygame.draw.rect(screen, white, (d_block))
			if actual_word[0] == 'e':
				pygame.draw.rect(screen, white, (e_block))
			if actual_word[0] == 'f':
				pygame.draw.rect(screen, white, (f_block))
			if actual_word[0] == 'g':
				pygame.draw.rect(screen, white, (g_block))
			if actual_word[0] == 'h':
				pygame.draw.rect(screen, white, (h_block))
			if actual_word[0] == 'i':
				pygame.draw.rect(screen, white, (i_block))
			if actual_word[0] == 'j':
				pygame.draw.rect(screen, white, (j_block))
			if actual_word[0] == 'k':
				pygame.draw.rect(screen, white, (k_block))
			if actual_word[0] == 'l':
				pygame.draw.rect(screen, white, (l_block))
			if actual_word[0] == 'm':
				pygame.draw.rect(screen, white, (m_block))
			if actual_word[0] == 'n':
				pygame.draw.rect(screen, white, (n_block))
			if actual_word[0] == 'o':
				pygame.draw.rect(screen, white, (o_block))
			if actual_word[0] == 'p':
				pygame.draw.rect(screen, white, (p_block))
			if actual_word[0] == 'q':
				pygame.draw.rect(screen, white, (q_block))
			if actual_word[0] == 'r':
				pygame.draw.rect(screen, white, (r_block))
			if actual_word[0] == 's':
				pygame.draw.rect(screen, white, (s_block))
			if actual_word[0] == 't':
				pygame.draw.rect(screen, white, (t_block))
			if actual_word[0] == 'u':
				pygame.draw.rect(screen, white, (u_block))
			if actual_word[0] == 'v':
				pygame.draw.rect(screen, white, (v_block))
			if actual_word[0] == 'w':
				pygame.draw.rect(screen, white, (w_block))
			if actual_word[0] == 'x':
				pygame.draw.rect(screen, white, (x_block))
			if actual_word[0] == 'y':
				pygame.draw.rect(screen, white, (y_block))
			if actual_word[0] == 'z':
				pygame.draw.rect(screen, white, (z_block))
			pygame.display.update()
		if actual_word[1] != '-'and answer_var and letter2:
			a = font4.render(actual_word[1], True, yellow)
			screen.blit(a, (360, 260))
			answer_var = False
			letter2 = False
			hint_len += 1
			if actual_word[1] == 'a':
				pygame.draw.rect(screen, white, (a_block))
			if actual_word[1] == 'b':
				pygame.draw.rect(screen, white, (b_block))
			if actual_word[1] == 'c':
				pygame.draw.rect(screen, white, (c_block))
			if actual_word[1] == 'd':
				pygame.draw.rect(screen, white, (d_block))
			if actual_word[1] == 'e':
				pygame.draw.rect(screen, white, (e_block))
			if actual_word[1] == 'f':
				pygame.draw.rect(screen, white, (f_block))
			if actual_word[1] == 'g':
				pygame.draw.rect(screen, white, (g_block))
			if actual_word[1] == 'h':
				pygame.draw.rect(screen, white, (h_block))
			if actual_word[1] == 'i':
				pygame.draw.rect(screen, white, (i_block))
			if actual_word[1] == 'j':
				pygame.draw.rect(screen, white, (j_block))
			if actual_word[1] == 'k':
				pygame.draw.rect(screen, white, (k_block))
			if actual_word[1] == 'l':
				pygame.draw.rect(screen, white, (l_block))
			if actual_word[1] == 'm':
				pygame.draw.rect(screen, white, (m_block))
			if actual_word[1] == 'n':
				pygame.draw.rect(screen, white, (n_block))
			if actual_word[1] == 'o':
				pygame.draw.rect(screen, white, (o_block))
			if actual_word[1] == 'p':
				pygame.draw.rect(screen, white, (p_block))
			if actual_word[1] == 'q':
				pygame.draw.rect(screen, white, (q_block))
			if actual_word[1] == 'r':
				pygame.draw.rect(screen, white, (r_block))
			if actual_word[1] == 's':
				pygame.draw.rect(screen, white, (s_block))
			if actual_word[1] == 't':
				pygame.draw.rect(screen, white, (t_block))
			if actual_word[1] == 'u':
				pygame.draw.rect(screen, white, (u_block))
			if actual_word[1] == 'v':
				pygame.draw.rect(screen, white, (v_block))
			if actual_word[1] == 'w':
				pygame.draw.rect(screen, white, (w_block))
			if actual_word[1] == 'x':
				pygame.draw.rect(screen, white, (x_block))
			if actual_word[1] == 'y':
				pygame.draw.rect(screen, white, (y_block))
			if actual_word[1] == 'z':
				pygame.draw.rect(screen, white, (z_block))
			pygame.display.update()
		if actual_word[2] != '-'and answer_var and letter3:
			a = font4.render(actual_word[2], True, yellow)
			screen.blit(a, (395, 260))
			answer_var = False
			letter3 = False
			hint_len += 1
			if actual_word[2] == 'a':
				pygame.draw.rect(screen, white, (a_block))
			if actual_word[2] == 'b':
				pygame.draw.rect(screen, white, (b_block))
			if actual_word[2] == 'c':
				pygame.draw.rect(screen, white, (c_block))
			if actual_word[2] == 'd':
				pygame.draw.rect(screen, white, (d_block))
			if actual_word[2] == 'e':
				pygame.draw.rect(screen, white, (e_block))
			if actual_word[2] == 'f':
				pygame.draw.rect(screen, white, (f_block))
			if actual_word[2] == 'g':
				pygame.draw.rect(screen, white, (g_block))
			if actual_word[2] == 'h':
				pygame.draw.rect(screen, white, (h_block))
			if actual_word[2] == 'i':
				pygame.draw.rect(screen, white, (i_block))
			if actual_word[2] == 'j':
				pygame.draw.rect(screen, white, (j_block))
			if actual_word[2] == 'k':
				pygame.draw.rect(screen, white, (k_block))
			if actual_word[2] == 'l':
				pygame.draw.rect(screen, white, (l_block))
			if actual_word[2] == 'm':
				pygame.draw.rect(screen, white, (m_block))
			if actual_word[2] == 'n':
				pygame.draw.rect(screen, white, (n_block))
			if actual_word[2] == 'o':
				pygame.draw.rect(screen, white, (o_block))
			if actual_word[2] == 'p':
				pygame.draw.rect(screen, white, (p_block))
			if actual_word[2] == 'q':
				pygame.draw.rect(screen, white, (q_block))
			if actual_word[2] == 'r':
				pygame.draw.rect(screen, white, (r_block))
			if actual_word[2] == 's':
				pygame.draw.rect(screen, white, (s_block))
			if actual_word[2] == 't':
				pygame.draw.rect(screen, white, (t_block))
			if actual_word[2] == 'u':
				pygame.draw.rect(screen, white, (u_block))
			if actual_word[2] == 'v':
				pygame.draw.rect(screen, white, (v_block))
			if actual_word[2] == 'w':
				pygame.draw.rect(screen, white, (w_block))
			if actual_word[2] == 'x':
				pygame.draw.rect(screen, white, (x_block))
			if actual_word[2] == 'y':
				pygame.draw.rect(screen, white, (y_block))
			if actual_word[2] == 'z':
				pygame.draw.rect(screen, white, (z_block))
			pygame.display.update()
		if actual_word[3] != '-'and answer_var and letter4:
			a = font4.render(actual_word[3], True, yellow)
			screen.blit(a, (430, 260))
			answer_var = False
			letter4 = False
			hint_len += 1
			if actual_word[3] == 'a':
				pygame.draw.rect(screen, white, (a_block))
			if actual_word[3] == 'b':
				pygame.draw.rect(screen, white, (b_block))
			if actual_word[3] == 'c':
				pygame.draw.rect(screen, white, (c_block))
			if actual_word[3] == 'd':
				pygame.draw.rect(screen, white, (d_block))
			if actual_word[3] == 'e':
				pygame.draw.rect(screen, white, (e_block))
			if actual_word[3] == 'f':
				pygame.draw.rect(screen, white, (f_block))
			if actual_word[3] == 'g':
				pygame.draw.rect(screen, white, (g_block))
			if actual_word[3] == 'h':
				pygame.draw.rect(screen, white, (h_block))
			if actual_word[3] == 'i':
				pygame.draw.rect(screen, white, (i_block))
			if actual_word[3] == 'j':
				pygame.draw.rect(screen, white, (j_block))
			if actual_word[3] == 'k':
				pygame.draw.rect(screen, white, (k_block))
			if actual_word[3] == 'l':
				pygame.draw.rect(screen, white, (l_block))
			if actual_word[3] == 'm':
				pygame.draw.rect(screen, white, (m_block))
			if actual_word[3] == 'n':
				pygame.draw.rect(screen, white, (n_block))
			if actual_word[3] == 'o':
				pygame.draw.rect(screen, white, (o_block))
			if actual_word[3] == 'p':
				pygame.draw.rect(screen, white, (p_block))
			if actual_word[3] == 'q':
				pygame.draw.rect(screen, white, (q_block))
			if actual_word[3] == 'r':
				pygame.draw.rect(screen, white, (r_block))
			if actual_word[3] == 's':
				pygame.draw.rect(screen, white, (s_block))
			if actual_word[3] == 't':
				pygame.draw.rect(screen, white, (t_block))
			if actual_word[3] == 'u':
				pygame.draw.rect(screen, white, (u_block))
			if actual_word[3] == 'v':
				pygame.draw.rect(screen, white, (v_block))
			if actual_word[3] == 'w':
				pygame.draw.rect(screen, white, (w_block))
			if actual_word[3] == 'x':
				pygame.draw.rect(screen, white, (x_block))
			if actual_word[3] == 'y':
				pygame.draw.rect(screen, white, (y_block))
			if actual_word[3] == 'z':
				pygame.draw.rect(screen, white, (z_block))
			pygame.display.update()
		if actual_word[4] != '-'and answer_var and letter5:
			a = font4.render(actual_word[4], True, yellow)
			screen.blit(a, (465, 260))
			answer_var = False
			letter5 = False
			hint_len += 1
			if actual_word[4] == 'a':
				pygame.draw.rect(screen, white, (a_block))
			if actual_word[4] == 'b':
				pygame.draw.rect(screen, white, (b_block))
			if actual_word[4] == 'c':
				pygame.draw.rect(screen, white, (c_block))
			if actual_word[4] == 'd':
				pygame.draw.rect(screen, white, (d_block))
			if actual_word[4] == 'e':
				pygame.draw.rect(screen, white, (e_block))
			if actual_word[4] == 'f':
				pygame.draw.rect(screen, white, (f_block))
			if actual_word[4] == 'g':
				pygame.draw.rect(screen, white, (g_block))
			if actual_word[4] == 'h':
				pygame.draw.rect(screen, white, (h_block))
			if actual_word[4] == 'i':
				pygame.draw.rect(screen, white, (i_block))
			if actual_word[4] == 'j':
				pygame.draw.rect(screen, white, (j_block))
			if actual_word[4] == 'k':
				pygame.draw.rect(screen, white, (k_block))
			if actual_word[4] == 'l':
				pygame.draw.rect(screen, white, (l_block))
			if actual_word[4] == 'm':
				pygame.draw.rect(screen, white, (m_block))
			if actual_word[4] == 'n':
				pygame.draw.rect(screen, white, (n_block))
			if actual_word[4] == 'o':
				pygame.draw.rect(screen, white, (o_block))
			if actual_word[4] == 'p':
				pygame.draw.rect(screen, white, (p_block))
			if actual_word[4] == 'q':
				pygame.draw.rect(screen, white, (q_block))
			if actual_word[4] == 'r':
				pygame.draw.rect(screen, white, (r_block))
			if actual_word[4] == 's':
				pygame.draw.rect(screen, white, (s_block))
			if actual_word[4] == 't':
				pygame.draw.rect(screen, white, (t_block))
			if actual_word[4] == 'u':
				pygame.draw.rect(screen, white, (u_block))
			if actual_word[4] == 'v':
				pygame.draw.rect(screen, white, (v_block))
			if actual_word[4] == 'w':
				pygame.draw.rect(screen, white, (w_block))
			if actual_word[4] == 'x':
				pygame.draw.rect(screen, white, (x_block))
			if actual_word[4] == 'y':
				pygame.draw.rect(screen, white, (y_block))
			if actual_word[4] == 'z':
				pygame.draw.rect(screen, white, (z_block))
			pygame.display.update()
		if actual_word[5] != '-'and answer_var and letter6:
			a = font4.render(actual_word[5], True, yellow)
			screen.blit(a, (500, 260))
			answer_var = False
			letter6 = False
			hint_len += 1
			if actual_word[5] == 'a':
				pygame.draw.rect(screen, white, (a_block))
			if actual_word[5] == 'b':
				pygame.draw.rect(screen, white, (b_block))
			if actual_word[5] == 'c':
				pygame.draw.rect(screen, white, (c_block))
			if actual_word[5] == 'd':
				pygame.draw.rect(screen, white, (d_block))
			if actual_word[5] == 'e':
				pygame.draw.rect(screen, white, (e_block))
			if actual_word[5] == 'f':
				pygame.draw.rect(screen, white, (f_block))
			if actual_word[5] == 'g':
				pygame.draw.rect(screen, white, (g_block))
			if actual_word[5] == 'h':
				pygame.draw.rect(screen, white, (h_block))
			if actual_word[5] == 'i':
				pygame.draw.rect(screen, white, (i_block))
			if actual_word[5] == 'j':
				pygame.draw.rect(screen, white, (j_block))
			if actual_word[5] == 'k':
				pygame.draw.rect(screen, white, (k_block))
			if actual_word[5] == 'l':
				pygame.draw.rect(screen, white, (l_block))
			if actual_word[5] == 'm':
				pygame.draw.rect(screen, white, (m_block))
			if actual_word[5] == 'n':
				pygame.draw.rect(screen, white, (n_block))
			if actual_word[5] == 'o':
				pygame.draw.rect(screen, white, (o_block))
			if actual_word[5] == 'p':
				pygame.draw.rect(screen, white, (p_block))
			if actual_word[5] == 'q':
				pygame.draw.rect(screen, white, (q_block))
			if actual_word[5] == 'r':
				pygame.draw.rect(screen, white, (r_block))
			if actual_word[5] == 's':
				pygame.draw.rect(screen, white, (s_block))
			if actual_word[5] == 't':
				pygame.draw.rect(screen, white, (t_block))
			if actual_word[5] == 'u':
				pygame.draw.rect(screen, white, (u_block))
			if actual_word[5] == 'v':
				pygame.draw.rect(screen, white, (v_block))
			if actual_word[5] == 'w':
				pygame.draw.rect(screen, white, (w_block))
			if actual_word[5] == 'x':
				pygame.draw.rect(screen, white, (x_block))
			if actual_word[5] == 'y':
				pygame.draw.rect(screen, white, (y_block))
			if actual_word[5] == 'z':
				pygame.draw.rect(screen, white, (z_block))
			pygame.display.update()
		if actual_word[6] != '-'and answer_var and letter7:
			a = font4.render(actual_word[6], True, yellow)
			screen.blit(a, (535, 260))
			answer_var = False
			letter7 = False
			hint_len += 1
			if actual_word[6] == 'a':
				pygame.draw.rect(screen, white, (a_block))
			if actual_word[6] == 'b':
				pygame.draw.rect(screen, white, (b_block))
			if actual_word[6] == 'c':
				pygame.draw.rect(screen, white, (c_block))
			if actual_word[6] == 'd':
				pygame.draw.rect(screen, white, (d_block))
			if actual_word[6] == 'e':
				pygame.draw.rect(screen, white, (e_block))
			if actual_word[6] == 'f':
				pygame.draw.rect(screen, white, (f_block))
			if actual_word[6] == 'g':
				pygame.draw.rect(screen, white, (g_block))
			if actual_word[6] == 'h':
				pygame.draw.rect(screen, white, (h_block))
			if actual_word[6] == 'i':
				pygame.draw.rect(screen, white, (i_block))
			if actual_word[6] == 'j':
				pygame.draw.rect(screen, white, (j_block))
			if actual_word[6] == 'k':
				pygame.draw.rect(screen, white, (k_block))
			if actual_word[6] == 'l':
				pygame.draw.rect(screen, white, (l_block))
			if actual_word[6] == 'm':
				pygame.draw.rect(screen, white, (m_block))
			if actual_word[6] == 'n':
				pygame.draw.rect(screen, white, (n_block))
			if actual_word[6] == 'o':
				pygame.draw.rect(screen, white, (o_block))
			if actual_word[6] == 'p':
				pygame.draw.rect(screen, white, (p_block))
			if actual_word[6] == 'q':
				pygame.draw.rect(screen, white, (q_block))
			if actual_word[6] == 'r':
				pygame.draw.rect(screen, white, (r_block))
			if actual_word[6] == 's':
				pygame.draw.rect(screen, white, (s_block))
			if actual_word[6] == 't':
				pygame.draw.rect(screen, white, (t_block))
			if actual_word[6] == 'u':
				pygame.draw.rect(screen, white, (u_block))
			if actual_word[6] == 'v':
				pygame.draw.rect(screen, white, (v_block))
			if actual_word[6] == 'w':
				pygame.draw.rect(screen, white, (w_block))
			if actual_word[6] == 'x':
				pygame.draw.rect(screen, white, (x_block))
			if actual_word[6] == 'y':
				pygame.draw.rect(screen, white, (y_block))
			if actual_word[6] == 'z':
				pygame.draw.rect(screen, white, (z_block))
			pygame.display.update()
	if len(word) == 8:
		if actual_word[0] != '-'and answer_var and letter1:
			a = font4.render(actual_word[0], True, yellow)
			screen.blit(a, (325, 260))
			answer_var = False
			letter1 = False
			hint_len += 1
			if actual_word[0] == 'a':
				pygame.draw.rect(screen, white, (a_block))
			if actual_word[0] == 'b':
				pygame.draw.rect(screen, white, (b_block))
			if actual_word[0] == 'c':
				pygame.draw.rect(screen, white, (c_block))
			if actual_word[0] == 'd':
				pygame.draw.rect(screen, white, (d_block))
			if actual_word[0] == 'e':
				pygame.draw.rect(screen, white, (e_block))
			if actual_word[0] == 'f':
				pygame.draw.rect(screen, white, (f_block))
			if actual_word[0] == 'g':
				pygame.draw.rect(screen, white, (g_block))
			if actual_word[0] == 'h':
				pygame.draw.rect(screen, white, (h_block))
			if actual_word[0] == 'i':
				pygame.draw.rect(screen, white, (i_block))
			if actual_word[0] == 'j':
				pygame.draw.rect(screen, white, (j_block))
			if actual_word[0] == 'k':
				pygame.draw.rect(screen, white, (k_block))
			if actual_word[0] == 'l':
				pygame.draw.rect(screen, white, (l_block))
			if actual_word[0] == 'm':
				pygame.draw.rect(screen, white, (m_block))
			if actual_word[0] == 'n':
				pygame.draw.rect(screen, white, (n_block))
			if actual_word[0] == 'o':
				pygame.draw.rect(screen, white, (o_block))
			if actual_word[0] == 'p':
				pygame.draw.rect(screen, white, (p_block))
			if actual_word[0] == 'q':
				pygame.draw.rect(screen, white, (q_block))
			if actual_word[0] == 'r':
				pygame.draw.rect(screen, white, (r_block))
			if actual_word[0] == 's':
				pygame.draw.rect(screen, white, (s_block))
			if actual_word[0] == 't':
				pygame.draw.rect(screen, white, (t_block))
			if actual_word[0] == 'u':
				pygame.draw.rect(screen, white, (u_block))
			if actual_word[0] == 'v':
				pygame.draw.rect(screen, white, (v_block))
			if actual_word[0] == 'w':
				pygame.draw.rect(screen, white, (w_block))
			if actual_word[0] == 'x':
				pygame.draw.rect(screen, white, (x_block))
			if actual_word[0] == 'y':
				pygame.draw.rect(screen, white, (y_block))
			if actual_word[0] == 'z':
				pygame.draw.rect(screen, white, (z_block))
			pygame.display.update()
		if actual_word[1] != '-'and answer_var and letter2:
			a = font4.render(actual_word[1], True, yellow)
			screen.blit(a, (360, 260))
			answer_var = False
			letter2 = False
			hint_len += 1
			if actual_word[1] == 'a':
				pygame.draw.rect(screen, white, (a_block))
			if actual_word[1] == 'b':
				pygame.draw.rect(screen, white, (b_block))
			if actual_word[1] == 'c':
				pygame.draw.rect(screen, white, (c_block))
			if actual_word[1] == 'd':
				pygame.draw.rect(screen, white, (d_block))
			if actual_word[1] == 'e':
				pygame.draw.rect(screen, white, (e_block))
			if actual_word[1] == 'f':
				pygame.draw.rect(screen, white, (f_block))
			if actual_word[1] == 'g':
				pygame.draw.rect(screen, white, (g_block))
			if actual_word[1] == 'h':
				pygame.draw.rect(screen, white, (h_block))
			if actual_word[1] == 'i':
				pygame.draw.rect(screen, white, (i_block))
			if actual_word[1] == 'j':
				pygame.draw.rect(screen, white, (j_block))
			if actual_word[1] == 'k':
				pygame.draw.rect(screen, white, (k_block))
			if actual_word[1] == 'l':
				pygame.draw.rect(screen, white, (l_block))
			if actual_word[1] == 'm':
				pygame.draw.rect(screen, white, (m_block))
			if actual_word[1] == 'n':
				pygame.draw.rect(screen, white, (n_block))
			if actual_word[1] == 'o':
				pygame.draw.rect(screen, white, (o_block))
			if actual_word[1] == 'p':
				pygame.draw.rect(screen, white, (p_block))
			if actual_word[1] == 'q':
				pygame.draw.rect(screen, white, (q_block))
			if actual_word[1] == 'r':
				pygame.draw.rect(screen, white, (r_block))
			if actual_word[1] == 's':
				pygame.draw.rect(screen, white, (s_block))
			if actual_word[1] == 't':
				pygame.draw.rect(screen, white, (t_block))
			if actual_word[1] == 'u':
				pygame.draw.rect(screen, white, (u_block))
			if actual_word[1] == 'v':
				pygame.draw.rect(screen, white, (v_block))
			if actual_word[1] == 'w':
				pygame.draw.rect(screen, white, (w_block))
			if actual_word[1] == 'x':
				pygame.draw.rect(screen, white, (x_block))
			if actual_word[1] == 'y':
				pygame.draw.rect(screen, white, (y_block))
			if actual_word[1] == 'z':
				pygame.draw.rect(screen, white, (z_block))
			pygame.display.update()
		if actual_word[2] != '-'and answer_var and letter3:
			a = font4.render(actual_word[2], True, yellow)
			screen.blit(a, (395, 260))
			answer_var = False
			letter3 = False
			hint_len += 1
			if actual_word[2] == 'a':
				pygame.draw.rect(screen, white, (a_block))
			if actual_word[2] == 'b':
				pygame.draw.rect(screen, white, (b_block))
			if actual_word[2] == 'c':
				pygame.draw.rect(screen, white, (c_block))
			if actual_word[2] == 'd':
				pygame.draw.rect(screen, white, (d_block))
			if actual_word[2] == 'e':
				pygame.draw.rect(screen, white, (e_block))
			if actual_word[2] == 'f':
				pygame.draw.rect(screen, white, (f_block))
			if actual_word[2] == 'g':
				pygame.draw.rect(screen, white, (g_block))
			if actual_word[2] == 'h':
				pygame.draw.rect(screen, white, (h_block))
			if actual_word[2] == 'i':
				pygame.draw.rect(screen, white, (i_block))
			if actual_word[2] == 'j':
				pygame.draw.rect(screen, white, (j_block))
			if actual_word[2] == 'k':
				pygame.draw.rect(screen, white, (k_block))
			if actual_word[2] == 'l':
				pygame.draw.rect(screen, white, (l_block))
			if actual_word[2] == 'm':
				pygame.draw.rect(screen, white, (m_block))
			if actual_word[2] == 'n':
				pygame.draw.rect(screen, white, (n_block))
			if actual_word[2] == 'o':
				pygame.draw.rect(screen, white, (o_block))
			if actual_word[2] == 'p':
				pygame.draw.rect(screen, white, (p_block))
			if actual_word[2] == 'q':
				pygame.draw.rect(screen, white, (q_block))
			if actual_word[2] == 'r':
				pygame.draw.rect(screen, white, (r_block))
			if actual_word[2] == 's':
				pygame.draw.rect(screen, white, (s_block))
			if actual_word[2] == 't':
				pygame.draw.rect(screen, white, (t_block))
			if actual_word[2] == 'u':
				pygame.draw.rect(screen, white, (u_block))
			if actual_word[2] == 'v':
				pygame.draw.rect(screen, white, (v_block))
			if actual_word[2] == 'w':
				pygame.draw.rect(screen, white, (w_block))
			if actual_word[2] == 'x':
				pygame.draw.rect(screen, white, (x_block))
			if actual_word[2] == 'y':
				pygame.draw.rect(screen, white, (y_block))
			if actual_word[2] == 'z':
				pygame.draw.rect(screen, white, (z_block))
			pygame.display.update()
		if actual_word[3] != '-'and answer_var and letter4:
			a = font4.render(actual_word[3], True, yellow)
			screen.blit(a, (430, 260))
			answer_var = False
			letter4 = False
			hint_len += 1
			if actual_word[3] == 'a':
				pygame.draw.rect(screen, white, (a_block))
			if actual_word[3] == 'b':
				pygame.draw.rect(screen, white, (b_block))
			if actual_word[3] == 'c':
				pygame.draw.rect(screen, white, (c_block))
			if actual_word[3] == 'd':
				pygame.draw.rect(screen, white, (d_block))
			if actual_word[3] == 'e':
				pygame.draw.rect(screen, white, (e_block))
			if actual_word[3] == 'f':
				pygame.draw.rect(screen, white, (f_block))
			if actual_word[3] == 'g':
				pygame.draw.rect(screen, white, (g_block))
			if actual_word[3] == 'h':
				pygame.draw.rect(screen, white, (h_block))
			if actual_word[3] == 'i':
				pygame.draw.rect(screen, white, (i_block))
			if actual_word[3] == 'j':
				pygame.draw.rect(screen, white, (j_block))
			if actual_word[3] == 'k':
				pygame.draw.rect(screen, white, (k_block))
			if actual_word[3] == 'l':
				pygame.draw.rect(screen, white, (l_block))
			if actual_word[3] == 'm':
				pygame.draw.rect(screen, white, (m_block))
			if actual_word[3] == 'n':
				pygame.draw.rect(screen, white, (n_block))
			if actual_word[3] == 'o':
				pygame.draw.rect(screen, white, (o_block))
			if actual_word[3] == 'p':
				pygame.draw.rect(screen, white, (p_block))
			if actual_word[3] == 'q':
				pygame.draw.rect(screen, white, (q_block))
			if actual_word[3] == 'r':
				pygame.draw.rect(screen, white, (r_block))
			if actual_word[3] == 's':
				pygame.draw.rect(screen, white, (s_block))
			if actual_word[3] == 't':
				pygame.draw.rect(screen, white, (t_block))
			if actual_word[3] == 'u':
				pygame.draw.rect(screen, white, (u_block))
			if actual_word[3] == 'v':
				pygame.draw.rect(screen, white, (v_block))
			if actual_word[3] == 'w':
				pygame.draw.rect(screen, white, (w_block))
			if actual_word[3] == 'x':
				pygame.draw.rect(screen, white, (x_block))
			if actual_word[3] == 'y':
				pygame.draw.rect(screen, white, (y_block))
			if actual_word[3] == 'z':
				pygame.draw.rect(screen, white, (z_block))
			pygame.display.update()
		if actual_word[4] != '-'and answer_var and letter5:
			a = font4.render(actual_word[4], True, yellow)
			screen.blit(a, (465, 260))
			answer_var = False
			letter5 = False
			hint_len += 1
			if actual_word[4] == 'a':
				pygame.draw.rect(screen, white, (a_block))
			if actual_word[4] == 'b':
				pygame.draw.rect(screen, white, (b_block))
			if actual_word[4] == 'c':
				pygame.draw.rect(screen, white, (c_block))
			if actual_word[4] == 'd':
				pygame.draw.rect(screen, white, (d_block))
			if actual_word[4] == 'e':
				pygame.draw.rect(screen, white, (e_block))
			if actual_word[4] == 'f':
				pygame.draw.rect(screen, white, (f_block))
			if actual_word[4] == 'g':
				pygame.draw.rect(screen, white, (g_block))
			if actual_word[4] == 'h':
				pygame.draw.rect(screen, white, (h_block))
			if actual_word[4] == 'i':
				pygame.draw.rect(screen, white, (i_block))
			if actual_word[4] == 'j':
				pygame.draw.rect(screen, white, (j_block))
			if actual_word[4] == 'k':
				pygame.draw.rect(screen, white, (k_block))
			if actual_word[4] == 'l':
				pygame.draw.rect(screen, white, (l_block))
			if actual_word[4] == 'm':
				pygame.draw.rect(screen, white, (m_block))
			if actual_word[4] == 'n':
				pygame.draw.rect(screen, white, (n_block))
			if actual_word[4] == 'o':
				pygame.draw.rect(screen, white, (o_block))
			if actual_word[4] == 'p':
				pygame.draw.rect(screen, white, (p_block))
			if actual_word[4] == 'q':
				pygame.draw.rect(screen, white, (q_block))
			if actual_word[4] == 'r':
				pygame.draw.rect(screen, white, (r_block))
			if actual_word[4] == 's':
				pygame.draw.rect(screen, white, (s_block))
			if actual_word[4] == 't':
				pygame.draw.rect(screen, white, (t_block))
			if actual_word[4] == 'u':
				pygame.draw.rect(screen, white, (u_block))
			if actual_word[4] == 'v':
				pygame.draw.rect(screen, white, (v_block))
			if actual_word[4] == 'w':
				pygame.draw.rect(screen, white, (w_block))
			if actual_word[4] == 'x':
				pygame.draw.rect(screen, white, (x_block))
			if actual_word[4] == 'y':
				pygame.draw.rect(screen, white, (y_block))
			if actual_word[4] == 'z':
				pygame.draw.rect(screen, white, (z_block))
			pygame.display.update()
		if actual_word[5] != '-'and answer_var and letter6:
			a = font4.render(actual_word[5], True, yellow)
			screen.blit(a, (500, 260))
			answer_var = False
			letter6 = False
			hint_len += 1
			if actual_word[5] == 'a':
				pygame.draw.rect(screen, white, (a_block))
			if actual_word[5] == 'b':
				pygame.draw.rect(screen, white, (b_block))
			if actual_word[5] == 'c':
				pygame.draw.rect(screen, white, (c_block))
			if actual_word[5] == 'd':
				pygame.draw.rect(screen, white, (d_block))
			if actual_word[5] == 'e':
				pygame.draw.rect(screen, white, (e_block))
			if actual_word[5] == 'f':
				pygame.draw.rect(screen, white, (f_block))
			if actual_word[5] == 'g':
				pygame.draw.rect(screen, white, (g_block))
			if actual_word[5] == 'h':
				pygame.draw.rect(screen, white, (h_block))
			if actual_word[5] == 'i':
				pygame.draw.rect(screen, white, (i_block))
			if actual_word[5] == 'j':
				pygame.draw.rect(screen, white, (j_block))
			if actual_word[5] == 'k':
				pygame.draw.rect(screen, white, (k_block))
			if actual_word[5] == 'l':
				pygame.draw.rect(screen, white, (l_block))
			if actual_word[5] == 'm':
				pygame.draw.rect(screen, white, (m_block))
			if actual_word[5] == 'n':
				pygame.draw.rect(screen, white, (n_block))
			if actual_word[5] == 'o':
				pygame.draw.rect(screen, white, (o_block))
			if actual_word[5] == 'p':
				pygame.draw.rect(screen, white, (p_block))
			if actual_word[5] == 'q':
				pygame.draw.rect(screen, white, (q_block))
			if actual_word[5] == 'r':
				pygame.draw.rect(screen, white, (r_block))
			if actual_word[5] == 's':
				pygame.draw.rect(screen, white, (s_block))
			if actual_word[5] == 't':
				pygame.draw.rect(screen, white, (t_block))
			if actual_word[5] == 'u':
				pygame.draw.rect(screen, white, (u_block))
			if actual_word[5] == 'v':
				pygame.draw.rect(screen, white, (v_block))
			if actual_word[5] == 'w':
				pygame.draw.rect(screen, white, (w_block))
			if actual_word[5] == 'x':
				pygame.draw.rect(screen, white, (x_block))
			if actual_word[5] == 'y':
				pygame.draw.rect(screen, white, (y_block))
			if actual_word[5] == 'z':
				pygame.draw.rect(screen, white, (z_block))
			pygame.display.update()
		if actual_word[6] != '-'and answer_var and letter7:
			a = font4.render(actual_word[6], True, yellow)
			screen.blit(a, (535, 260))
			answer_var = False
			letter7 = False
			hint_len += 1
			if actual_word[6] == 'a':
				pygame.draw.rect(screen, white, (a_block))
			if actual_word[6] == 'b':
				pygame.draw.rect(screen, white, (b_block))
			if actual_word[6] == 'c':
				pygame.draw.rect(screen, white, (c_block))
			if actual_word[6] == 'd':
				pygame.draw.rect(screen, white, (d_block))
			if actual_word[6] == 'e':
				pygame.draw.rect(screen, white, (e_block))
			if actual_word[6] == 'f':
				pygame.draw.rect(screen, white, (f_block))
			if actual_word[6] == 'g':
				pygame.draw.rect(screen, white, (g_block))
			if actual_word[6] == 'h':
				pygame.draw.rect(screen, white, (h_block))
			if actual_word[6] == 'i':
				pygame.draw.rect(screen, white, (i_block))
			if actual_word[6] == 'j':
				pygame.draw.rect(screen, white, (j_block))
			if actual_word[6] == 'k':
				pygame.draw.rect(screen, white, (k_block))
			if actual_word[6] == 'l':
				pygame.draw.rect(screen, white, (l_block))
			if actual_word[6] == 'm':
				pygame.draw.rect(screen, white, (m_block))
			if actual_word[6] == 'n':
				pygame.draw.rect(screen, white, (n_block))
			if actual_word[6] == 'o':
				pygame.draw.rect(screen, white, (o_block))
			if actual_word[6] == 'p':
				pygame.draw.rect(screen, white, (p_block))
			if actual_word[6] == 'q':
				pygame.draw.rect(screen, white, (q_block))
			if actual_word[6] == 'r':
				pygame.draw.rect(screen, white, (r_block))
			if actual_word[6] == 's':
				pygame.draw.rect(screen, white, (s_block))
			if actual_word[6] == 't':
				pygame.draw.rect(screen, white, (t_block))
			if actual_word[6] == 'u':
				pygame.draw.rect(screen, white, (u_block))
			if actual_word[6] == 'v':
				pygame.draw.rect(screen, white, (v_block))
			if actual_word[6] == 'w':
				pygame.draw.rect(screen, white, (w_block))
			if actual_word[6] == 'x':
				pygame.draw.rect(screen, white, (x_block))
			if actual_word[6] == 'y':
				pygame.draw.rect(screen, white, (y_block))
			if actual_word[6] == 'z':
				pygame.draw.rect(screen, white, (z_block))
			pygame.display.update()
		if actual_word[7] != '-'and answer_var and letter8:
			a = font4.render(actual_word[7], True, yellow)
			screen.blit(a, (570, 260))
			answer_var = False
			letter8 = False
			hint_len += 1
			if actual_word[7] == 'a':
				pygame.draw.rect(screen, white, (a_block))
			if actual_word[7] == 'b':
				pygame.draw.rect(screen, white, (b_block))
			if actual_word[7] == 'c':
				pygame.draw.rect(screen, white, (c_block))
			if actual_word[7] == 'd':
				pygame.draw.rect(screen, white, (d_block))
			if actual_word[7] == 'e':
				pygame.draw.rect(screen, white, (e_block))
			if actual_word[7] == 'f':
				pygame.draw.rect(screen, white, (f_block))
			if actual_word[7] == 'g':
				pygame.draw.rect(screen, white, (g_block))
			if actual_word[7] == 'h':
				pygame.draw.rect(screen, white, (h_block))
			if actual_word[7] == 'i':
				pygame.draw.rect(screen, white, (i_block))
			if actual_word[7] == 'j':
				pygame.draw.rect(screen, white, (j_block))
			if actual_word[7] == 'k':
				pygame.draw.rect(screen, white, (k_block))
			if actual_word[7] == 'l':
				pygame.draw.rect(screen, white, (l_block))
			if actual_word[7] == 'm':
				pygame.draw.rect(screen, white, (m_block))
			if actual_word[7] == 'n':
				pygame.draw.rect(screen, white, (n_block))
			if actual_word[7] == 'o':
				pygame.draw.rect(screen, white, (o_block))
			if actual_word[7] == 'p':
				pygame.draw.rect(screen, white, (p_block))
			if actual_word[7] == 'q':
				pygame.draw.rect(screen, white, (q_block))
			if actual_word[7] == 'r':
				pygame.draw.rect(screen, white, (r_block))
			if actual_word[7] == 's':
				pygame.draw.rect(screen, white, (s_block))
			if actual_word[7] == 't':
				pygame.draw.rect(screen, white, (t_block))
			if actual_word[7] == 'u':
				pygame.draw.rect(screen, white, (u_block))
			if actual_word[7] == 'v':
				pygame.draw.rect(screen, white, (v_block))
			if actual_word[7] == 'w':
				pygame.draw.rect(screen, white, (w_block))
			if actual_word[7] == 'x':
				pygame.draw.rect(screen, white, (x_block))
			if actual_word[7] == 'y':
				pygame.draw.rect(screen, white, (y_block))
			if actual_word[7] == 'z':
				pygame.draw.rect(screen, white, (z_block))
			pygame.display.update()
	if len(word) == 9:
		if actual_word[0] != '-'and answer_var and letter1:
			a = font4.render(actual_word[0], True, yellow)
			screen.blit(a, (290, 260))
			answer_var = False
			letter1 = False
			hint_len += 1
			if actual_word[0] == 'a':
				pygame.draw.rect(screen, white, (a_block))
			if actual_word[0] == 'b':
				pygame.draw.rect(screen, white, (b_block))
			if actual_word[0] == 'c':
				pygame.draw.rect(screen, white, (c_block))
			if actual_word[0] == 'd':
				pygame.draw.rect(screen, white, (d_block))
			if actual_word[0] == 'e':
				pygame.draw.rect(screen, white, (e_block))
			if actual_word[0] == 'f':
				pygame.draw.rect(screen, white, (f_block))
			if actual_word[0] == 'g':
				pygame.draw.rect(screen, white, (g_block))
			if actual_word[0] == 'h':
				pygame.draw.rect(screen, white, (h_block))
			if actual_word[0] == 'i':
				pygame.draw.rect(screen, white, (i_block))
			if actual_word[0] == 'j':
				pygame.draw.rect(screen, white, (j_block))
			if actual_word[0] == 'k':
				pygame.draw.rect(screen, white, (k_block))
			if actual_word[0] == 'l':
				pygame.draw.rect(screen, white, (l_block))
			if actual_word[0] == 'm':
				pygame.draw.rect(screen, white, (m_block))
			if actual_word[0] == 'n':
				pygame.draw.rect(screen, white, (n_block))
			if actual_word[0] == 'o':
				pygame.draw.rect(screen, white, (o_block))
			if actual_word[0] == 'p':
				pygame.draw.rect(screen, white, (p_block))
			if actual_word[0] == 'q':
				pygame.draw.rect(screen, white, (q_block))
			if actual_word[0] == 'r':
				pygame.draw.rect(screen, white, (r_block))
			if actual_word[0] == 's':
				pygame.draw.rect(screen, white, (s_block))
			if actual_word[0] == 't':
				pygame.draw.rect(screen, white, (t_block))
			if actual_word[0] == 'u':
				pygame.draw.rect(screen, white, (u_block))
			if actual_word[0] == 'v':
				pygame.draw.rect(screen, white, (v_block))
			if actual_word[0] == 'w':
				pygame.draw.rect(screen, white, (w_block))
			if actual_word[0] == 'x':
				pygame.draw.rect(screen, white, (x_block))
			if actual_word[0] == 'y':
				pygame.draw.rect(screen, white, (y_block))
			if actual_word[0] == 'z':
				pygame.draw.rect(screen, white, (z_block))
			pygame.display.update()
		if actual_word[1] != '-'and answer_var and letter2:
			a = font4.render(actual_word[1], True, yellow)
			screen.blit(a, (325, 260))
			answer_var = False
			letter2 = False
			hint_len += 1
			if actual_word[1] == 'a':
				pygame.draw.rect(screen, white, (a_block))
			if actual_word[1] == 'b':
				pygame.draw.rect(screen, white, (b_block))
			if actual_word[1] == 'c':
				pygame.draw.rect(screen, white, (c_block))
			if actual_word[1] == 'd':
				pygame.draw.rect(screen, white, (d_block))
			if actual_word[1] == 'e':
				pygame.draw.rect(screen, white, (e_block))
			if actual_word[1] == 'f':
				pygame.draw.rect(screen, white, (f_block))
			if actual_word[1] == 'g':
				pygame.draw.rect(screen, white, (g_block))
			if actual_word[1] == 'h':
				pygame.draw.rect(screen, white, (h_block))
			if actual_word[1] == 'i':
				pygame.draw.rect(screen, white, (i_block))
			if actual_word[1] == 'j':
				pygame.draw.rect(screen, white, (j_block))
			if actual_word[1] == 'k':
				pygame.draw.rect(screen, white, (k_block))
			if actual_word[1] == 'l':
				pygame.draw.rect(screen, white, (l_block))
			if actual_word[1] == 'm':
				pygame.draw.rect(screen, white, (m_block))
			if actual_word[1] == 'n':
				pygame.draw.rect(screen, white, (n_block))
			if actual_word[1] == 'o':
				pygame.draw.rect(screen, white, (o_block))
			if actual_word[1] == 'p':
				pygame.draw.rect(screen, white, (p_block))
			if actual_word[1] == 'q':
				pygame.draw.rect(screen, white, (q_block))
			if actual_word[1] == 'r':
				pygame.draw.rect(screen, white, (r_block))
			if actual_word[1] == 's':
				pygame.draw.rect(screen, white, (s_block))
			if actual_word[1] == 't':
				pygame.draw.rect(screen, white, (t_block))
			if actual_word[1] == 'u':
				pygame.draw.rect(screen, white, (u_block))
			if actual_word[1] == 'v':
				pygame.draw.rect(screen, white, (v_block))
			if actual_word[1] == 'w':
				pygame.draw.rect(screen, white, (w_block))
			if actual_word[1] == 'x':
				pygame.draw.rect(screen, white, (x_block))
			if actual_word[1] == 'y':
				pygame.draw.rect(screen, white, (y_block))
			if actual_word[1] == 'z':
				pygame.draw.rect(screen, white, (z_block))
			pygame.display.update()
		if actual_word[2] != '-'and answer_var and letter3:
			a = font4.render(actual_word[2], True, yellow)
			screen.blit(a, (360, 260))
			answer_var = False
			letter3 = False
			hint_len += 1
			if actual_word[2] == 'a':
				pygame.draw.rect(screen, white, (a_block))
			if actual_word[2] == 'b':
				pygame.draw.rect(screen, white, (b_block))
			if actual_word[2] == 'c':
				pygame.draw.rect(screen, white, (c_block))
			if actual_word[2] == 'd':
				pygame.draw.rect(screen, white, (d_block))
			if actual_word[2] == 'e':
				pygame.draw.rect(screen, white, (e_block))
			if actual_word[2] == 'f':
				pygame.draw.rect(screen, white, (f_block))
			if actual_word[2] == 'g':
				pygame.draw.rect(screen, white, (g_block))
			if actual_word[2] == 'h':
				pygame.draw.rect(screen, white, (h_block))
			if actual_word[2] == 'i':
				pygame.draw.rect(screen, white, (i_block))
			if actual_word[2] == 'j':
				pygame.draw.rect(screen, white, (j_block))
			if actual_word[2] == 'k':
				pygame.draw.rect(screen, white, (k_block))
			if actual_word[2] == 'l':
				pygame.draw.rect(screen, white, (l_block))
			if actual_word[2] == 'm':
				pygame.draw.rect(screen, white, (m_block))
			if actual_word[2] == 'n':
				pygame.draw.rect(screen, white, (n_block))
			if actual_word[2] == 'o':
				pygame.draw.rect(screen, white, (o_block))
			if actual_word[2] == 'p':
				pygame.draw.rect(screen, white, (p_block))
			if actual_word[2] == 'q':
				pygame.draw.rect(screen, white, (q_block))
			if actual_word[2] == 'r':
				pygame.draw.rect(screen, white, (r_block))
			if actual_word[2] == 's':
				pygame.draw.rect(screen, white, (s_block))
			if actual_word[2] == 't':
				pygame.draw.rect(screen, white, (t_block))
			if actual_word[2] == 'u':
				pygame.draw.rect(screen, white, (u_block))
			if actual_word[2] == 'v':
				pygame.draw.rect(screen, white, (v_block))
			if actual_word[2] == 'w':
				pygame.draw.rect(screen, white, (w_block))
			if actual_word[2] == 'x':
				pygame.draw.rect(screen, white, (x_block))
			if actual_word[2] == 'y':
				pygame.draw.rect(screen, white, (y_block))
			if actual_word[2] == 'z':
				pygame.draw.rect(screen, white, (z_block))
			pygame.display.update()
		if actual_word[3] != '-'and answer_var and letter4:
			a = font4.render(actual_word[3], True, yellow)
			screen.blit(a, (395, 260))
			answer_var = False
			letter4 = False
			hint_len += 1
			if actual_word[3] == 'a':
				pygame.draw.rect(screen, white, (a_block))
			if actual_word[3] == 'b':
				pygame.draw.rect(screen, white, (b_block))
			if actual_word[3] == 'c':
				pygame.draw.rect(screen, white, (c_block))
			if actual_word[3] == 'd':
				pygame.draw.rect(screen, white, (d_block))
			if actual_word[3] == 'e':
				pygame.draw.rect(screen, white, (e_block))
			if actual_word[3] == 'f':
				pygame.draw.rect(screen, white, (f_block))
			if actual_word[3] == 'g':
				pygame.draw.rect(screen, white, (g_block))
			if actual_word[3] == 'h':
				pygame.draw.rect(screen, white, (h_block))
			if actual_word[3] == 'i':
				pygame.draw.rect(screen, white, (i_block))
			if actual_word[3] == 'j':
				pygame.draw.rect(screen, white, (j_block))
			if actual_word[3] == 'k':
				pygame.draw.rect(screen, white, (k_block))
			if actual_word[3] == 'l':
				pygame.draw.rect(screen, white, (l_block))
			if actual_word[3] == 'm':
				pygame.draw.rect(screen, white, (m_block))
			if actual_word[3] == 'n':
				pygame.draw.rect(screen, white, (n_block))
			if actual_word[3] == 'o':
				pygame.draw.rect(screen, white, (o_block))
			if actual_word[3] == 'p':
				pygame.draw.rect(screen, white, (p_block))
			if actual_word[3] == 'q':
				pygame.draw.rect(screen, white, (q_block))
			if actual_word[3] == 'r':
				pygame.draw.rect(screen, white, (r_block))
			if actual_word[3] == 's':
				pygame.draw.rect(screen, white, (s_block))
			if actual_word[3] == 't':
				pygame.draw.rect(screen, white, (t_block))
			if actual_word[3] == 'u':
				pygame.draw.rect(screen, white, (u_block))
			if actual_word[3] == 'v':
				pygame.draw.rect(screen, white, (v_block))
			if actual_word[3] == 'w':
				pygame.draw.rect(screen, white, (w_block))
			if actual_word[3] == 'x':
				pygame.draw.rect(screen, white, (x_block))
			if actual_word[3] == 'y':
				pygame.draw.rect(screen, white, (y_block))
			if actual_word[3] == 'z':
				pygame.draw.rect(screen, white, (z_block))
			pygame.display.update()
		if actual_word[4] != '-'and answer_var and letter5:
			a = font4.render(actual_word[4], True, yellow)
			screen.blit(a, (430, 260))
			answer_var = False
			letter5 = False
			hint_len += 1
			if actual_word[4] == 'a':
				pygame.draw.rect(screen, white, (a_block))
			if actual_word[4] == 'b':
				pygame.draw.rect(screen, white, (b_block))
			if actual_word[4] == 'c':
				pygame.draw.rect(screen, white, (c_block))
			if actual_word[4] == 'd':
				pygame.draw.rect(screen, white, (d_block))
			if actual_word[4] == 'e':
				pygame.draw.rect(screen, white, (e_block))
			if actual_word[4] == 'f':
				pygame.draw.rect(screen, white, (f_block))
			if actual_word[4] == 'g':
				pygame.draw.rect(screen, white, (g_block))
			if actual_word[4] == 'h':
				pygame.draw.rect(screen, white, (h_block))
			if actual_word[4] == 'i':
				pygame.draw.rect(screen, white, (i_block))
			if actual_word[4] == 'j':
				pygame.draw.rect(screen, white, (j_block))
			if actual_word[4] == 'k':
				pygame.draw.rect(screen, white, (k_block))
			if actual_word[4] == 'l':
				pygame.draw.rect(screen, white, (l_block))
			if actual_word[4] == 'm':
				pygame.draw.rect(screen, white, (m_block))
			if actual_word[4] == 'n':
				pygame.draw.rect(screen, white, (n_block))
			if actual_word[4] == 'o':
				pygame.draw.rect(screen, white, (o_block))
			if actual_word[4] == 'p':
				pygame.draw.rect(screen, white, (p_block))
			if actual_word[4] == 'q':
				pygame.draw.rect(screen, white, (q_block))
			if actual_word[4] == 'r':
				pygame.draw.rect(screen, white, (r_block))
			if actual_word[4] == 's':
				pygame.draw.rect(screen, white, (s_block))
			if actual_word[4] == 't':
				pygame.draw.rect(screen, white, (t_block))
			if actual_word[4] == 'u':
				pygame.draw.rect(screen, white, (u_block))
			if actual_word[4] == 'v':
				pygame.draw.rect(screen, white, (v_block))
			if actual_word[4] == 'w':
				pygame.draw.rect(screen, white, (w_block))
			if actual_word[4] == 'x':
				pygame.draw.rect(screen, white, (x_block))
			if actual_word[4] == 'y':
				pygame.draw.rect(screen, white, (y_block))
			if actual_word[4] == 'z':
				pygame.draw.rect(screen, white, (z_block))
			pygame.display.update()
		if actual_word[5] != '-'and answer_var and letter6:
			a = font4.render(actual_word[5], True, yellow)
			screen.blit(a, (465, 260))
			answer_var = False
			letter6 = False
			hint_len += 1
			if actual_word[5] == 'a':
				pygame.draw.rect(screen, white, (a_block))
			if actual_word[5] == 'b':
				pygame.draw.rect(screen, white, (b_block))
			if actual_word[5] == 'c':
				pygame.draw.rect(screen, white, (c_block))
			if actual_word[5] == 'd':
				pygame.draw.rect(screen, white, (d_block))
			if actual_word[5] == 'e':
				pygame.draw.rect(screen, white, (e_block))
			if actual_word[5] == 'f':
				pygame.draw.rect(screen, white, (f_block))
			if actual_word[5] == 'g':
				pygame.draw.rect(screen, white, (g_block))
			if actual_word[5] == 'h':
				pygame.draw.rect(screen, white, (h_block))
			if actual_word[5] == 'i':
				pygame.draw.rect(screen, white, (i_block))
			if actual_word[5] == 'j':
				pygame.draw.rect(screen, white, (j_block))
			if actual_word[5] == 'k':
				pygame.draw.rect(screen, white, (k_block))
			if actual_word[5] == 'l':
				pygame.draw.rect(screen, white, (l_block))
			if actual_word[5] == 'm':
				pygame.draw.rect(screen, white, (m_block))
			if actual_word[5] == 'n':
				pygame.draw.rect(screen, white, (n_block))
			if actual_word[5] == 'o':
				pygame.draw.rect(screen, white, (o_block))
			if actual_word[5] == 'p':
				pygame.draw.rect(screen, white, (p_block))
			if actual_word[5] == 'q':
				pygame.draw.rect(screen, white, (q_block))
			if actual_word[5] == 'r':
				pygame.draw.rect(screen, white, (r_block))
			if actual_word[5] == 's':
				pygame.draw.rect(screen, white, (s_block))
			if actual_word[5] == 't':
				pygame.draw.rect(screen, white, (t_block))
			if actual_word[5] == 'u':
				pygame.draw.rect(screen, white, (u_block))
			if actual_word[5] == 'v':
				pygame.draw.rect(screen, white, (v_block))
			if actual_word[5] == 'w':
				pygame.draw.rect(screen, white, (w_block))
			if actual_word[5] == 'x':
				pygame.draw.rect(screen, white, (x_block))
			if actual_word[5] == 'y':
				pygame.draw.rect(screen, white, (y_block))
			if actual_word[5] == 'z':
				pygame.draw.rect(screen, white, (z_block))
		if actual_word[6] != '-'and answer_var and letter7:
			a = font4.render(actual_word[6], True, yellow)
			screen.blit(a, (500, 260))
			answer_var = False
			letter7 = False
			hint_len += 1
			if actual_word[6] == 'a':
				pygame.draw.rect(screen, white, (a_block))
			if actual_word[6] == 'b':
				pygame.draw.rect(screen, white, (b_block))
			if actual_word[6] == 'c':
				pygame.draw.rect(screen, white, (c_block))
			if actual_word[6] == 'd':
				pygame.draw.rect(screen, white, (d_block))
			if actual_word[6] == 'e':
				pygame.draw.rect(screen, white, (e_block))
			if actual_word[6] == 'f':
				pygame.draw.rect(screen, white, (f_block))
			if actual_word[6] == 'g':
				pygame.draw.rect(screen, white, (g_block))
			if actual_word[6] == 'h':
				pygame.draw.rect(screen, white, (h_block))
			if actual_word[6] == 'i':
				pygame.draw.rect(screen, white, (i_block))
			if actual_word[6] == 'j':
				pygame.draw.rect(screen, white, (j_block))
			if actual_word[6] == 'k':
				pygame.draw.rect(screen, white, (k_block))
			if actual_word[6] == 'l':
				pygame.draw.rect(screen, white, (l_block))
			if actual_word[6] == 'm':
				pygame.draw.rect(screen, white, (m_block))
			if actual_word[6] == 'n':
				pygame.draw.rect(screen, white, (n_block))
			if actual_word[6] == 'o':
				pygame.draw.rect(screen, white, (o_block))
			if actual_word[6] == 'p':
				pygame.draw.rect(screen, white, (p_block))
			if actual_word[6] == 'q':
				pygame.draw.rect(screen, white, (q_block))
			if actual_word[6] == 'r':
				pygame.draw.rect(screen, white, (r_block))
			if actual_word[6] == 's':
				pygame.draw.rect(screen, white, (s_block))
			if actual_word[6] == 't':
				pygame.draw.rect(screen, white, (t_block))
			if actual_word[6] == 'u':
				pygame.draw.rect(screen, white, (u_block))
			if actual_word[6] == 'v':
				pygame.draw.rect(screen, white, (v_block))
			if actual_word[6] == 'w':
				pygame.draw.rect(screen, white, (w_block))
			if actual_word[6] == 'x':
				pygame.draw.rect(screen, white, (x_block))
			if actual_word[6] == 'y':
				pygame.draw.rect(screen, white, (y_block))
			if actual_word[6] == 'z':
				pygame.draw.rect(screen, white, (z_block))
			pygame.display.update()
		if actual_word[7] != '-'and answer_var and letter8:
			a = font4.render(actual_word[7], True, yellow)
			screen.blit(a, (535, 260))
			answer_var = False
			letter8 = False
			hint_len += 1
			if actual_word[7] == 'a':
				pygame.draw.rect(screen, white, (a_block))
			if actual_word[7] == 'b':
				pygame.draw.rect(screen, white, (b_block))
			if actual_word[7] == 'c':
				pygame.draw.rect(screen, white, (c_block))
			if actual_word[7] == 'd':
				pygame.draw.rect(screen, white, (d_block))
			if actual_word[7] == 'e':
				pygame.draw.rect(screen, white, (e_block))
			if actual_word[7] == 'f':
				pygame.draw.rect(screen, white, (f_block))
			if actual_word[7] == 'g':
				pygame.draw.rect(screen, white, (g_block))
			if actual_word[7] == 'h':
				pygame.draw.rect(screen, white, (h_block))
			if actual_word[7] == 'i':
				pygame.draw.rect(screen, white, (i_block))
			if actual_word[7] == 'j':
				pygame.draw.rect(screen, white, (j_block))
			if actual_word[7] == 'k':
				pygame.draw.rect(screen, white, (k_block))
			if actual_word[7] == 'l':
				pygame.draw.rect(screen, white, (l_block))
			if actual_word[7] == 'm':
				pygame.draw.rect(screen, white, (m_block))
			if actual_word[7] == 'n':
				pygame.draw.rect(screen, white, (n_block))
			if actual_word[7] == 'o':
				pygame.draw.rect(screen, white, (o_block))
			if actual_word[7] == 'p':
				pygame.draw.rect(screen, white, (p_block))
			if actual_word[7] == 'q':
				pygame.draw.rect(screen, white, (q_block))
			if actual_word[7] == 'r':
				pygame.draw.rect(screen, white, (r_block))
			if actual_word[7] == 's':
				pygame.draw.rect(screen, white, (s_block))
			if actual_word[7] == 't':
				pygame.draw.rect(screen, white, (t_block))
			if actual_word[7] == 'u':
				pygame.draw.rect(screen, white, (u_block))
			if actual_word[7] == 'v':
				pygame.draw.rect(screen, white, (v_block))
			if actual_word[7] == 'w':
				pygame.draw.rect(screen, white, (w_block))
			if actual_word[7] == 'x':
				pygame.draw.rect(screen, white, (x_block))
			if actual_word[7] == 'y':
				pygame.draw.rect(screen, white, (y_block))
			if actual_word[7] == 'z':
				pygame.draw.rect(screen, white, (z_block))
			pygame.display.update()
		if actual_word[8] != '-'and answer_var and letter9:
			a = font4.render(actual_word[8], True, yellow)
			screen.blit(a, (570, 260))
			answer_var = False
			letter9 = False
			hint_len += 1
			if actual_word[8] == 'a':
				pygame.draw.rect(screen, white, (a_block))
			if actual_word[8] == 'b':
				pygame.draw.rect(screen, white, (b_block))
			if actual_word[8] == 'c':
				pygame.draw.rect(screen, white, (c_block))
			if actual_word[8] == 'd':
				pygame.draw.rect(screen, white, (d_block))
			if actual_word[8] == 'e':
				pygame.draw.rect(screen, white, (e_block))
			if actual_word[8] == 'f':
				pygame.draw.rect(screen, white, (f_block))
			if actual_word[8] == 'g':
				pygame.draw.rect(screen, white, (g_block))
			if actual_word[8] == 'h':
				pygame.draw.rect(screen, white, (h_block))
			if actual_word[8] == 'i':
				pygame.draw.rect(screen, white, (i_block))
			if actual_word[8] == 'j':
				pygame.draw.rect(screen, white, (j_block))
			if actual_word[8] == 'k':
				pygame.draw.rect(screen, white, (k_block))
			if actual_word[8] == 'l':
				pygame.draw.rect(screen, white, (l_block))
			if actual_word[8] == 'm':
				pygame.draw.rect(screen, white, (m_block))
			if actual_word[8] == 'n':
				pygame.draw.rect(screen, white, (n_block))
			if actual_word[8] == 'o':
				pygame.draw.rect(screen, white, (o_block))
			if actual_word[8] == 'p':
				pygame.draw.rect(screen, white, (p_block))
			if actual_word[8] == 'q':
				pygame.draw.rect(screen, white, (q_block))
			if actual_word[8] == 'r':
				pygame.draw.rect(screen, white, (r_block))
			if actual_word[8] == 's':
				pygame.draw.rect(screen, white, (s_block))
			if actual_word[8] == 't':
				pygame.draw.rect(screen, white, (t_block))
			if actual_word[8] == 'u':
				pygame.draw.rect(screen, white, (u_block))
			if actual_word[8] == 'v':
				pygame.draw.rect(screen, white, (v_block))
			if actual_word[8] == 'w':
				pygame.draw.rect(screen, white, (w_block))
			if actual_word[8] == 'x':
				pygame.draw.rect(screen, white, (x_block))
			if actual_word[8] == 'y':
				pygame.draw.rect(screen, white, (y_block))
			if actual_word[8] == 'z':
				pygame.draw.rect(screen, white, (z_block))
	if len(word) == 10:
		if actual_word[0] != '-'and answer_var and letter1:
			a = font4.render(actual_word[0], True, yellow)
			screen.blit(a, (290, 260))
			answer_var = False
			letter1 = False
			hint_len += 1
			if actual_word[0] == 'a':
				pygame.draw.rect(screen, white, (a_block))
			if actual_word[0] == 'b':
				pygame.draw.rect(screen, white, (b_block))
			if actual_word[0] == 'c':
				pygame.draw.rect(screen, white, (c_block))
			if actual_word[0] == 'd':
				pygame.draw.rect(screen, white, (d_block))
			if actual_word[0] == 'e':
				pygame.draw.rect(screen, white, (e_block))
			if actual_word[0] == 'f':
				pygame.draw.rect(screen, white, (f_block))
			if actual_word[0] == 'g':
				pygame.draw.rect(screen, white, (g_block))
			if actual_word[0] == 'h':
				pygame.draw.rect(screen, white, (h_block))
			if actual_word[0] == 'i':
				pygame.draw.rect(screen, white, (i_block))
			if actual_word[0] == 'j':
				pygame.draw.rect(screen, white, (j_block))
			if actual_word[0] == 'k':
				pygame.draw.rect(screen, white, (k_block))
			if actual_word[0] == 'l':
				pygame.draw.rect(screen, white, (l_block))
			if actual_word[0] == 'm':
				pygame.draw.rect(screen, white, (m_block))
			if actual_word[0] == 'n':
				pygame.draw.rect(screen, white, (n_block))
			if actual_word[0] == 'o':
				pygame.draw.rect(screen, white, (o_block))
			if actual_word[0] == 'p':
				pygame.draw.rect(screen, white, (p_block))
			if actual_word[0] == 'q':
				pygame.draw.rect(screen, white, (q_block))
			if actual_word[0] == 'r':
				pygame.draw.rect(screen, white, (r_block))
			if actual_word[0] == 's':
				pygame.draw.rect(screen, white, (s_block))
			if actual_word[0] == 't':
				pygame.draw.rect(screen, white, (t_block))
			if actual_word[0] == 'u':
				pygame.draw.rect(screen, white, (u_block))
			if actual_word[0] == 'v':
				pygame.draw.rect(screen, white, (v_block))
			if actual_word[0] == 'w':
				pygame.draw.rect(screen, white, (w_block))
			if actual_word[0] == 'x':
				pygame.draw.rect(screen, white, (x_block))
			if actual_word[0] == 'y':
				pygame.draw.rect(screen, white, (y_block))
			if actual_word[0] == 'z':
				pygame.draw.rect(screen, white, (z_block))
			pygame.display.update()
		if actual_word[1] != '-'and answer_var and letter2:
			a = font4.render(actual_word[1], True, yellow)
			screen.blit(a, (325, 260))
			answer_var = False
			letter2 = False
			hint_len += 1
			if actual_word[1] == 'a':
				pygame.draw.rect(screen, white, (a_block))
			if actual_word[1] == 'b':
				pygame.draw.rect(screen, white, (b_block))
			if actual_word[1] == 'c':
				pygame.draw.rect(screen, white, (c_block))
			if actual_word[1] == 'd':
				pygame.draw.rect(screen, white, (d_block))
			if actual_word[1] == 'e':
				pygame.draw.rect(screen, white, (e_block))
			if actual_word[1] == 'f':
				pygame.draw.rect(screen, white, (f_block))
			if actual_word[1] == 'g':
				pygame.draw.rect(screen, white, (g_block))
			if actual_word[1] == 'h':
				pygame.draw.rect(screen, white, (h_block))
			if actual_word[1] == 'i':
				pygame.draw.rect(screen, white, (i_block))
			if actual_word[1] == 'j':
				pygame.draw.rect(screen, white, (j_block))
			if actual_word[1] == 'k':
				pygame.draw.rect(screen, white, (k_block))
			if actual_word[1] == 'l':
				pygame.draw.rect(screen, white, (l_block))
			if actual_word[1] == 'm':
				pygame.draw.rect(screen, white, (m_block))
			if actual_word[1] == 'n':
				pygame.draw.rect(screen, white, (n_block))
			if actual_word[1] == 'o':
				pygame.draw.rect(screen, white, (o_block))
			if actual_word[1] == 'p':
				pygame.draw.rect(screen, white, (p_block))
			if actual_word[1] == 'q':
				pygame.draw.rect(screen, white, (q_block))
			if actual_word[1] == 'r':
				pygame.draw.rect(screen, white, (r_block))
			if actual_word[1] == 's':
				pygame.draw.rect(screen, white, (s_block))
			if actual_word[1] == 't':
				pygame.draw.rect(screen, white, (t_block))
			if actual_word[1] == 'u':
				pygame.draw.rect(screen, white, (u_block))
			if actual_word[1] == 'v':
				pygame.draw.rect(screen, white, (v_block))
			if actual_word[1] == 'w':
				pygame.draw.rect(screen, white, (w_block))
			if actual_word[1] == 'x':
				pygame.draw.rect(screen, white, (x_block))
			if actual_word[1] == 'y':
				pygame.draw.rect(screen, white, (y_block))
			if actual_word[1] == 'z':
				pygame.draw.rect(screen, white, (z_block))
			pygame.display.update()
		if actual_word[2] != '-'and answer_var and letter3:
			a = font4.render(actual_word[2], True, yellow)
			screen.blit(a, (360, 260))
			answer_var = False
			letter3 = False
			hint_len += 1
			if actual_word[2] == 'a':
				pygame.draw.rect(screen, white, (a_block))
			if actual_word[2] == 'b':
				pygame.draw.rect(screen, white, (b_block))
			if actual_word[2] == 'c':
				pygame.draw.rect(screen, white, (c_block))
			if actual_word[2] == 'd':
				pygame.draw.rect(screen, white, (d_block))
			if actual_word[2] == 'e':
				pygame.draw.rect(screen, white, (e_block))
			if actual_word[2] == 'f':
				pygame.draw.rect(screen, white, (f_block))
			if actual_word[2] == 'g':
				pygame.draw.rect(screen, white, (g_block))
			if actual_word[2] == 'h':
				pygame.draw.rect(screen, white, (h_block))
			if actual_word[2] == 'i':
				pygame.draw.rect(screen, white, (i_block))
			if actual_word[2] == 'j':
				pygame.draw.rect(screen, white, (j_block))
			if actual_word[2] == 'k':
				pygame.draw.rect(screen, white, (k_block))
			if actual_word[2] == 'l':
				pygame.draw.rect(screen, white, (l_block))
			if actual_word[2] == 'm':
				pygame.draw.rect(screen, white, (m_block))
			if actual_word[2] == 'n':
				pygame.draw.rect(screen, white, (n_block))
			if actual_word[2] == 'o':
				pygame.draw.rect(screen, white, (o_block))
			if actual_word[2] == 'p':
				pygame.draw.rect(screen, white, (p_block))
			if actual_word[2] == 'q':
				pygame.draw.rect(screen, white, (q_block))
			if actual_word[2] == 'r':
				pygame.draw.rect(screen, white, (r_block))
			if actual_word[2] == 's':
				pygame.draw.rect(screen, white, (s_block))
			if actual_word[2] == 't':
				pygame.draw.rect(screen, white, (t_block))
			if actual_word[2] == 'u':
				pygame.draw.rect(screen, white, (u_block))
			if actual_word[2] == 'v':
				pygame.draw.rect(screen, white, (v_block))
			if actual_word[2] == 'w':
				pygame.draw.rect(screen, white, (w_block))
			if actual_word[2] == 'x':
				pygame.draw.rect(screen, white, (x_block))
			if actual_word[2] == 'y':
				pygame.draw.rect(screen, white, (y_block))
			if actual_word[2] == 'z':
				pygame.draw.rect(screen, white, (z_block))
			pygame.display.update()
		if actual_word[3] != '-'and answer_var and letter4:
			a = font4.render(actual_word[3], True, yellow)
			screen.blit(a, (395, 260))
			answer_var = False
			letter4 = False
			hint_len += 1
			if actual_word[3] == 'a':
				pygame.draw.rect(screen, white, (a_block))
			if actual_word[3] == 'b':
				pygame.draw.rect(screen, white, (b_block))
			if actual_word[3] == 'c':
				pygame.draw.rect(screen, white, (c_block))
			if actual_word[3] == 'd':
				pygame.draw.rect(screen, white, (d_block))
			if actual_word[3] == 'e':
				pygame.draw.rect(screen, white, (e_block))
			if actual_word[3] == 'f':
				pygame.draw.rect(screen, white, (f_block))
			if actual_word[3] == 'g':
				pygame.draw.rect(screen, white, (g_block))
			if actual_word[3] == 'h':
				pygame.draw.rect(screen, white, (h_block))
			if actual_word[3] == 'i':
				pygame.draw.rect(screen, white, (i_block))
			if actual_word[3] == 'j':
				pygame.draw.rect(screen, white, (j_block))
			if actual_word[3] == 'k':
				pygame.draw.rect(screen, white, (k_block))
			if actual_word[3] == 'l':
				pygame.draw.rect(screen, white, (l_block))
			if actual_word[3] == 'm':
				pygame.draw.rect(screen, white, (m_block))
			if actual_word[3] == 'n':
				pygame.draw.rect(screen, white, (n_block))
			if actual_word[3] == 'o':
				pygame.draw.rect(screen, white, (o_block))
			if actual_word[3] == 'p':
				pygame.draw.rect(screen, white, (p_block))
			if actual_word[3] == 'q':
				pygame.draw.rect(screen, white, (q_block))
			if actual_word[3] == 'r':
				pygame.draw.rect(screen, white, (r_block))
			if actual_word[3] == 's':
				pygame.draw.rect(screen, white, (s_block))
			if actual_word[3] == 't':
				pygame.draw.rect(screen, white, (t_block))
			if actual_word[3] == 'u':
				pygame.draw.rect(screen, white, (u_block))
			if actual_word[3] == 'v':
				pygame.draw.rect(screen, white, (v_block))
			if actual_word[3] == 'w':
				pygame.draw.rect(screen, white, (w_block))
			if actual_word[3] == 'x':
				pygame.draw.rect(screen, white, (x_block))
			if actual_word[3] == 'y':
				pygame.draw.rect(screen, white, (y_block))
			if actual_word[3] == 'z':
				pygame.draw.rect(screen, white, (z_block))
			pygame.display.update()
		if actual_word[4] != '-'and answer_var and letter5:
			a = font4.render(actual_word[4], True, yellow)
			screen.blit(a, (430, 260))
			answer_var = False
			letter5 = False
			hint_len += 1
			if actual_word[4] == 'a':
				pygame.draw.rect(screen, white, (a_block))
			if actual_word[4] == 'b':
				pygame.draw.rect(screen, white, (b_block))
			if actual_word[4] == 'c':
				pygame.draw.rect(screen, white, (c_block))
			if actual_word[4] == 'd':
				pygame.draw.rect(screen, white, (d_block))
			if actual_word[4] == 'e':
				pygame.draw.rect(screen, white, (e_block))
			if actual_word[4] == 'f':
				pygame.draw.rect(screen, white, (f_block))
			if actual_word[4] == 'g':
				pygame.draw.rect(screen, white, (g_block))
			if actual_word[4] == 'h':
				pygame.draw.rect(screen, white, (h_block))
			if actual_word[4] == 'i':
				pygame.draw.rect(screen, white, (i_block))
			if actual_word[4] == 'j':
				pygame.draw.rect(screen, white, (j_block))
			if actual_word[4] == 'k':
				pygame.draw.rect(screen, white, (k_block))
			if actual_word[4] == 'l':
				pygame.draw.rect(screen, white, (l_block))
			if actual_word[4] == 'm':
				pygame.draw.rect(screen, white, (m_block))
			if actual_word[4] == 'n':
				pygame.draw.rect(screen, white, (n_block))
			if actual_word[4] == 'o':
				pygame.draw.rect(screen, white, (o_block))
			if actual_word[4] == 'p':
				pygame.draw.rect(screen, white, (p_block))
			if actual_word[4] == 'q':
				pygame.draw.rect(screen, white, (q_block))
			if actual_word[4] == 'r':
				pygame.draw.rect(screen, white, (r_block))
			if actual_word[4] == 's':
				pygame.draw.rect(screen, white, (s_block))
			if actual_word[4] == 't':
				pygame.draw.rect(screen, white, (t_block))
			if actual_word[4] == 'u':
				pygame.draw.rect(screen, white, (u_block))
			if actual_word[4] == 'v':
				pygame.draw.rect(screen, white, (v_block))
			if actual_word[4] == 'w':
				pygame.draw.rect(screen, white, (w_block))
			if actual_word[4] == 'x':
				pygame.draw.rect(screen, white, (x_block))
			if actual_word[4] == 'y':
				pygame.draw.rect(screen, white, (y_block))
			if actual_word[4] == 'z':
				pygame.draw.rect(screen, white, (z_block))
			pygame.display.update()
		if actual_word[5] != '-'and answer_var and letter6:
			a = font4.render(actual_word[5], True, yellow)
			screen.blit(a, (465, 260))
			answer_var = False
			letter6 = False
			hint_len += 1
			if actual_word[5] == 'a':
				pygame.draw.rect(screen, white, (a_block))
			if actual_word[5] == 'b':
				pygame.draw.rect(screen, white, (b_block))
			if actual_word[5] == 'c':
				pygame.draw.rect(screen, white, (c_block))
			if actual_word[5] == 'd':
				pygame.draw.rect(screen, white, (d_block))
			if actual_word[5] == 'e':
				pygame.draw.rect(screen, white, (e_block))
			if actual_word[5] == 'f':
				pygame.draw.rect(screen, white, (f_block))
			if actual_word[5] == 'g':
				pygame.draw.rect(screen, white, (g_block))
			if actual_word[5] == 'h':
				pygame.draw.rect(screen, white, (h_block))
			if actual_word[5] == 'i':
				pygame.draw.rect(screen, white, (i_block))
			if actual_word[5] == 'j':
				pygame.draw.rect(screen, white, (j_block))
			if actual_word[5] == 'k':
				pygame.draw.rect(screen, white, (k_block))
			if actual_word[5] == 'l':
				pygame.draw.rect(screen, white, (l_block))
			if actual_word[5] == 'm':
				pygame.draw.rect(screen, white, (m_block))
			if actual_word[5] == 'n':
				pygame.draw.rect(screen, white, (n_block))
			if actual_word[5] == 'o':
				pygame.draw.rect(screen, white, (o_block))
			if actual_word[5] == 'p':
				pygame.draw.rect(screen, white, (p_block))
			if actual_word[5] == 'q':
				pygame.draw.rect(screen, white, (q_block))
			if actual_word[5] == 'r':
				pygame.draw.rect(screen, white, (r_block))
			if actual_word[5] == 's':
				pygame.draw.rect(screen, white, (s_block))
			if actual_word[5] == 't':
				pygame.draw.rect(screen, white, (t_block))
			if actual_word[5] == 'u':
				pygame.draw.rect(screen, white, (u_block))
			if actual_word[5] == 'v':
				pygame.draw.rect(screen, white, (v_block))
			if actual_word[5] == 'w':
				pygame.draw.rect(screen, white, (w_block))
			if actual_word[5] == 'x':
				pygame.draw.rect(screen, white, (x_block))
			if actual_word[5] == 'y':
				pygame.draw.rect(screen, white, (y_block))
			if actual_word[5] == 'z':
				pygame.draw.rect(screen, white, (z_block))
			pygame.display.update()
		if actual_word[6] != '-'and answer_var and letter7:
			a = font4.render(actual_word[6], True, yellow)
			screen.blit(a, (500, 260))
			answer_var = False
			letter7 = False
			hint_len += 1
			if actual_word[6] == 'a':
				pygame.draw.rect(screen, white, (a_block))
			if actual_word[6] == 'b':
				pygame.draw.rect(screen, white, (b_block))
			if actual_word[6] == 'c':
				pygame.draw.rect(screen, white, (c_block))
			if actual_word[6] == 'd':
				pygame.draw.rect(screen, white, (d_block))
			if actual_word[6] == 'e':
				pygame.draw.rect(screen, white, (e_block))
			if actual_word[6] == 'f':
				pygame.draw.rect(screen, white, (f_block))
			if actual_word[6] == 'g':
				pygame.draw.rect(screen, white, (g_block))
			if actual_word[6] == 'h':
				pygame.draw.rect(screen, white, (h_block))
			if actual_word[6] == 'i':
				pygame.draw.rect(screen, white, (i_block))
			if actual_word[6] == 'j':
				pygame.draw.rect(screen, white, (j_block))
			if actual_word[6] == 'k':
				pygame.draw.rect(screen, white, (k_block))
			if actual_word[6] == 'l':
				pygame.draw.rect(screen, white, (l_block))
			if actual_word[6] == 'm':
				pygame.draw.rect(screen, white, (m_block))
			if actual_word[6] == 'n':
				pygame.draw.rect(screen, white, (n_block))
			if actual_word[6] == 'o':
				pygame.draw.rect(screen, white, (o_block))
			if actual_word[6] == 'p':
				pygame.draw.rect(screen, white, (p_block))
			if actual_word[6] == 'q':
				pygame.draw.rect(screen, white, (q_block))
			if actual_word[6] == 'r':
				pygame.draw.rect(screen, white, (r_block))
			if actual_word[6] == 's':
				pygame.draw.rect(screen, white, (s_block))
			if actual_word[6] == 't':
				pygame.draw.rect(screen, white, (t_block))
			if actual_word[6] == 'u':
				pygame.draw.rect(screen, white, (u_block))
			if actual_word[6] == 'v':
				pygame.draw.rect(screen, white, (v_block))
			if actual_word[6] == 'w':
				pygame.draw.rect(screen, white, (w_block))
			if actual_word[6] == 'x':
				pygame.draw.rect(screen, white, (x_block))
			if actual_word[6] == 'y':
				pygame.draw.rect(screen, white, (y_block))
			if actual_word[6] == 'z':
				pygame.draw.rect(screen, white, (z_block))
			pygame.display.update()
		if actual_word[7] != '-'and answer_var and letter8:
			a = font4.render(actual_word[7], True, yellow)
			screen.blit(a, (535, 260))
			answer_var = False
			letter8 = False
			hint_len += 1
			if actual_word[7] == 'a':
				pygame.draw.rect(screen, white, (a_block))
			if actual_word[7] == 'b':
				pygame.draw.rect(screen, white, (b_block))
			if actual_word[7] == 'c':
				pygame.draw.rect(screen, white, (c_block))
			if actual_word[7] == 'd':
				pygame.draw.rect(screen, white, (d_block))
			if actual_word[7] == 'e':
				pygame.draw.rect(screen, white, (e_block))
			if actual_word[7] == 'f':
				pygame.draw.rect(screen, white, (f_block))
			if actual_word[7] == 'g':
				pygame.draw.rect(screen, white, (g_block))
			if actual_word[7] == 'h':
				pygame.draw.rect(screen, white, (h_block))
			if actual_word[7] == 'i':
				pygame.draw.rect(screen, white, (i_block))
			if actual_word[7] == 'j':
				pygame.draw.rect(screen, white, (j_block))
			if actual_word[7] == 'k':
				pygame.draw.rect(screen, white, (k_block))
			if actual_word[7] == 'l':
				pygame.draw.rect(screen, white, (l_block))
			if actual_word[7] == 'm':
				pygame.draw.rect(screen, white, (m_block))
			if actual_word[7] == 'n':
				pygame.draw.rect(screen, white, (n_block))
			if actual_word[7] == 'o':
				pygame.draw.rect(screen, white, (o_block))
			if actual_word[7] == 'p':
				pygame.draw.rect(screen, white, (p_block))
			if actual_word[7] == 'q':
				pygame.draw.rect(screen, white, (q_block))
			if actual_word[7] == 'r':
				pygame.draw.rect(screen, white, (r_block))
			if actual_word[7] == 's':
				pygame.draw.rect(screen, white, (s_block))
			if actual_word[7] == 't':
				pygame.draw.rect(screen, white, (t_block))
			if actual_word[7] == 'u':
				pygame.draw.rect(screen, white, (u_block))
			if actual_word[7] == 'v':
				pygame.draw.rect(screen, white, (v_block))
			if actual_word[7] == 'w':
				pygame.draw.rect(screen, white, (w_block))
			if actual_word[7] == 'x':
				pygame.draw.rect(screen, white, (x_block))
			if actual_word[7] == 'y':
				pygame.draw.rect(screen, white, (y_block))
			if actual_word[7] == 'z':
				pygame.draw.rect(screen, white, (z_block))
			pygame.display.update()
		if actual_word[8] != '-'and answer_var and letter9:
			a = font4.render(actual_word[8], True, yellow)
			screen.blit(a, (570, 260))
			answer_var = False
			letter9 = False
			hint_len += 1
			if actual_word[8] == 'a':
				pygame.draw.rect(screen, white, (a_block))
			if actual_word[8] == 'b':
				pygame.draw.rect(screen, white, (b_block))
			if actual_word[8] == 'c':
				pygame.draw.rect(screen, white, (c_block))
			if actual_word[8] == 'd':
				pygame.draw.rect(screen, white, (d_block))
			if actual_word[8] == 'e':
				pygame.draw.rect(screen, white, (e_block))
			if actual_word[8] == 'f':
				pygame.draw.rect(screen, white, (f_block))
			if actual_word[8] == 'g':
				pygame.draw.rect(screen, white, (g_block))
			if actual_word[8] == 'h':
				pygame.draw.rect(screen, white, (h_block))
			if actual_word[8] == 'i':
				pygame.draw.rect(screen, white, (i_block))
			if actual_word[8] == 'j':
				pygame.draw.rect(screen, white, (j_block))
			if actual_word[8] == 'k':
				pygame.draw.rect(screen, white, (k_block))
			if actual_word[8] == 'l':
				pygame.draw.rect(screen, white, (l_block))
			if actual_word[8] == 'm':
				pygame.draw.rect(screen, white, (m_block))
			if actual_word[8] == 'n':
				pygame.draw.rect(screen, white, (n_block))
			if actual_word[8] == 'o':
				pygame.draw.rect(screen, white, (o_block))
			if actual_word[8] == 'p':
				pygame.draw.rect(screen, white, (p_block))
			if actual_word[8] == 'q':
				pygame.draw.rect(screen, white, (q_block))
			if actual_word[8] == 'r':
				pygame.draw.rect(screen, white, (r_block))
			if actual_word[8] == 's':
				pygame.draw.rect(screen, white, (s_block))
			if actual_word[8] == 't':
				pygame.draw.rect(screen, white, (t_block))
			if actual_word[8] == 'u':
				pygame.draw.rect(screen, white, (u_block))
			if actual_word[8] == 'v':
				pygame.draw.rect(screen, white, (v_block))
			if actual_word[8] == 'w':
				pygame.draw.rect(screen, white, (w_block))
			if actual_word[8] == 'x':
				pygame.draw.rect(screen, white, (x_block))
			if actual_word[8] == 'y':
				pygame.draw.rect(screen, white, (y_block))
			if actual_word[8] == 'z':
				pygame.draw.rect(screen, white, (z_block))
			pygame.display.update()
		if actual_word[9] != '-'and answer_var and letter10:
			a = font4.render(actual_word[9], True, yellow)
			screen.blit(a, (605, 260))
			answer_var = False
			letter10 = False
			hint_len += 1
			if actual_word[9] == 'a':
				pygame.draw.rect(screen, white, (a_block))
			if actual_word[9] == 'b':
				pygame.draw.rect(screen, white, (b_block))
			if actual_word[9] == 'c':
				pygame.draw.rect(screen, white, (c_block))
			if actual_word[9] == 'd':
				pygame.draw.rect(screen, white, (d_block))
			if actual_word[9] == 'e':
				pygame.draw.rect(screen, white, (e_block))
			if actual_word[9] == 'f':
				pygame.draw.rect(screen, white, (f_block))
			if actual_word[9] == 'g':
				pygame.draw.rect(screen, white, (g_block))
			if actual_word[9] == 'h':
				pygame.draw.rect(screen, white, (h_block))
			if actual_word[9] == 'i':
				pygame.draw.rect(screen, white, (i_block))
			if actual_word[9] == 'j':
				pygame.draw.rect(screen, white, (j_block))
			if actual_word[9] == 'k':
				pygame.draw.rect(screen, white, (k_block))
			if actual_word[9] == 'l':
				pygame.draw.rect(screen, white, (l_block))
			if actual_word[9] == 'm':
				pygame.draw.rect(screen, white, (m_block))
			if actual_word[9] == 'n':
				pygame.draw.rect(screen, white, (n_block))
			if actual_word[9] == 'o':
				pygame.draw.rect(screen, white, (o_block))
			if actual_word[9] == 'p':
				pygame.draw.rect(screen, white, (p_block))
			if actual_word[9] == 'q':
				pygame.draw.rect(screen, white, (q_block))
			if actual_word[9] == 'r':
				pygame.draw.rect(screen, white, (r_block))
			if actual_word[9] == 's':
				pygame.draw.rect(screen, white, (s_block))
			if actual_word[9] == 't':
				pygame.draw.rect(screen, white, (t_block))
			if actual_word[9] == 'u':
				pygame.draw.rect(screen, white, (u_block))
			if actual_word[9] == 'v':
				pygame.draw.rect(screen, white, (v_block))
			if actual_word[9] == 'w':
				pygame.draw.rect(screen, white, (w_block))
			if actual_word[9] == 'x':
				pygame.draw.rect(screen, white, (x_block))
			if actual_word[9] == 'y':
				pygame.draw.rect(screen, white, (y_block))
			if actual_word[9] == 'z':
				pygame.draw.rect(screen, white, (z_block))
			pygame.display.update()
	if len(word) == 11:
		if actual_word[0] != '-'and answer_var and letter1:
			a = font4.render(actual_word[0], True, yellow)
			screen.blit(a, (255, 260))
			answer_var = False
			letter1 = False
			hint_len += 1
			if actual_word[0] == 'a':
				pygame.draw.rect(screen, white, (a_block))
			if actual_word[0] == 'b':
				pygame.draw.rect(screen, white, (b_block))
			if actual_word[0] == 'c':
				pygame.draw.rect(screen, white, (c_block))
			if actual_word[0] == 'd':
				pygame.draw.rect(screen, white, (d_block))
			if actual_word[0] == 'e':
				pygame.draw.rect(screen, white, (e_block))
			if actual_word[0] == 'f':
				pygame.draw.rect(screen, white, (f_block))
			if actual_word[0] == 'g':
				pygame.draw.rect(screen, white, (g_block))
			if actual_word[0] == 'h':
				pygame.draw.rect(screen, white, (h_block))
			if actual_word[0] == 'i':
				pygame.draw.rect(screen, white, (i_block))
			if actual_word[0] == 'j':
				pygame.draw.rect(screen, white, (j_block))
			if actual_word[0] == 'k':
				pygame.draw.rect(screen, white, (k_block))
			if actual_word[0] == 'l':
				pygame.draw.rect(screen, white, (l_block))
			if actual_word[0] == 'm':
				pygame.draw.rect(screen, white, (m_block))
			if actual_word[0] == 'n':
				pygame.draw.rect(screen, white, (n_block))
			if actual_word[0] == 'o':
				pygame.draw.rect(screen, white, (o_block))
			if actual_word[0] == 'p':
				pygame.draw.rect(screen, white, (p_block))
			if actual_word[0] == 'q':
				pygame.draw.rect(screen, white, (q_block))
			if actual_word[0] == 'r':
				pygame.draw.rect(screen, white, (r_block))
			if actual_word[0] == 's':
				pygame.draw.rect(screen, white, (s_block))
			if actual_word[0] == 't':
				pygame.draw.rect(screen, white, (t_block))
			if actual_word[0] == 'u':
				pygame.draw.rect(screen, white, (u_block))
			if actual_word[0] == 'v':
				pygame.draw.rect(screen, white, (v_block))
			if actual_word[0] == 'w':
				pygame.draw.rect(screen, white, (w_block))
			if actual_word[0] == 'x':
				pygame.draw.rect(screen, white, (x_block))
			if actual_word[0] == 'y':
				pygame.draw.rect(screen, white, (y_block))
			if actual_word[0] == 'z':
				pygame.draw.rect(screen, white, (z_block))
			pygame.display.update()
		if actual_word[1] != '-'and answer_var and letter2:
			a = font4.render(actual_word[1], True, yellow)
			screen.blit(a, (290, 260))
			answer_var = False
			letter2 = False
			hint_len += 1
			if actual_word[1] == 'a':
				pygame.draw.rect(screen, white, (a_block))
			if actual_word[1] == 'b':
				pygame.draw.rect(screen, white, (b_block))
			if actual_word[1] == 'c':
				pygame.draw.rect(screen, white, (c_block))
			if actual_word[1] == 'd':
				pygame.draw.rect(screen, white, (d_block))
			if actual_word[1] == 'e':
				pygame.draw.rect(screen, white, (e_block))
			if actual_word[1] == 'f':
				pygame.draw.rect(screen, white, (f_block))
			if actual_word[1] == 'g':
				pygame.draw.rect(screen, white, (g_block))
			if actual_word[1] == 'h':
				pygame.draw.rect(screen, white, (h_block))
			if actual_word[1] == 'i':
				pygame.draw.rect(screen, white, (i_block))
			if actual_word[1] == 'j':
				pygame.draw.rect(screen, white, (j_block))
			if actual_word[1] == 'k':
				pygame.draw.rect(screen, white, (k_block))
			if actual_word[1] == 'l':
				pygame.draw.rect(screen, white, (l_block))
			if actual_word[1] == 'm':
				pygame.draw.rect(screen, white, (m_block))
			if actual_word[1] == 'n':
				pygame.draw.rect(screen, white, (n_block))
			if actual_word[1] == 'o':
				pygame.draw.rect(screen, white, (o_block))
			if actual_word[1] == 'p':
				pygame.draw.rect(screen, white, (p_block))
			if actual_word[1] == 'q':
				pygame.draw.rect(screen, white, (q_block))
			if actual_word[1] == 'r':
				pygame.draw.rect(screen, white, (r_block))
			if actual_word[1] == 's':
				pygame.draw.rect(screen, white, (s_block))
			if actual_word[1] == 't':
				pygame.draw.rect(screen, white, (t_block))
			if actual_word[1] == 'u':
				pygame.draw.rect(screen, white, (u_block))
			if actual_word[1] == 'v':
				pygame.draw.rect(screen, white, (v_block))
			if actual_word[1] == 'w':
				pygame.draw.rect(screen, white, (w_block))
			if actual_word[1] == 'x':
				pygame.draw.rect(screen, white, (x_block))
			if actual_word[1] == 'y':
				pygame.draw.rect(screen, white, (y_block))
			if actual_word[1] == 'z':
				pygame.draw.rect(screen, white, (z_block))
			pygame.display.update()
		if actual_word[2] != '-'and answer_var and letter3:
			a = font4.render(actual_word[2], True, yellow)
			screen.blit(a, (325, 260))
			answer_var = False
			letter3 = False
			hint_len += 1
			if actual_word[2] == 'a':
				pygame.draw.rect(screen, white, (a_block))
			if actual_word[2] == 'b':
				pygame.draw.rect(screen, white, (b_block))
			if actual_word[2] == 'c':
				pygame.draw.rect(screen, white, (c_block))
			if actual_word[2] == 'd':
				pygame.draw.rect(screen, white, (d_block))
			if actual_word[2] == 'e':
				pygame.draw.rect(screen, white, (e_block))
			if actual_word[2] == 'f':
				pygame.draw.rect(screen, white, (f_block))
			if actual_word[2] == 'g':
				pygame.draw.rect(screen, white, (g_block))
			if actual_word[2] == 'h':
				pygame.draw.rect(screen, white, (h_block))
			if actual_word[2] == 'i':
				pygame.draw.rect(screen, white, (i_block))
			if actual_word[2] == 'j':
				pygame.draw.rect(screen, white, (j_block))
			if actual_word[2] == 'k':
				pygame.draw.rect(screen, white, (k_block))
			if actual_word[2] == 'l':
				pygame.draw.rect(screen, white, (l_block))
			if actual_word[2] == 'm':
				pygame.draw.rect(screen, white, (m_block))
			if actual_word[2] == 'n':
				pygame.draw.rect(screen, white, (n_block))
			if actual_word[2] == 'o':
				pygame.draw.rect(screen, white, (o_block))
			if actual_word[2] == 'p':
				pygame.draw.rect(screen, white, (p_block))
			if actual_word[2] == 'q':
				pygame.draw.rect(screen, white, (q_block))
			if actual_word[2] == 'r':
				pygame.draw.rect(screen, white, (r_block))
			if actual_word[2] == 's':
				pygame.draw.rect(screen, white, (s_block))
			if actual_word[2] == 't':
				pygame.draw.rect(screen, white, (t_block))
			if actual_word[2] == 'u':
				pygame.draw.rect(screen, white, (u_block))
			if actual_word[2] == 'v':
				pygame.draw.rect(screen, white, (v_block))
			if actual_word[2] == 'w':
				pygame.draw.rect(screen, white, (w_block))
			if actual_word[2] == 'x':
				pygame.draw.rect(screen, white, (x_block))
			if actual_word[2] == 'y':
				pygame.draw.rect(screen, white, (y_block))
			if actual_word[2] == 'z':
				pygame.draw.rect(screen, white, (z_block))
			pygame.display.update()
		if actual_word[3] != '-'and answer_var and letter4:
			a = font4.render(actual_word[3], True, yellow)
			screen.blit(a, (360, 260))
			answer_var = False
			letter4 = False
			hint_len += 1
			if actual_word[3] == 'a':
				pygame.draw.rect(screen, white, (a_block))
			if actual_word[3] == 'b':
				pygame.draw.rect(screen, white, (b_block))
			if actual_word[3] == 'c':
				pygame.draw.rect(screen, white, (c_block))
			if actual_word[3] == 'd':
				pygame.draw.rect(screen, white, (d_block))
			if actual_word[3] == 'e':
				pygame.draw.rect(screen, white, (e_block))
			if actual_word[3] == 'f':
				pygame.draw.rect(screen, white, (f_block))
			if actual_word[3] == 'g':
				pygame.draw.rect(screen, white, (g_block))
			if actual_word[3] == 'h':
				pygame.draw.rect(screen, white, (h_block))
			if actual_word[3] == 'i':
				pygame.draw.rect(screen, white, (i_block))
			if actual_word[3] == 'j':
				pygame.draw.rect(screen, white, (j_block))
			if actual_word[3] == 'k':
				pygame.draw.rect(screen, white, (k_block))
			if actual_word[3] == 'l':
				pygame.draw.rect(screen, white, (l_block))
			if actual_word[3] == 'm':
				pygame.draw.rect(screen, white, (m_block))
			if actual_word[3] == 'n':
				pygame.draw.rect(screen, white, (n_block))
			if actual_word[3] == 'o':
				pygame.draw.rect(screen, white, (o_block))
			if actual_word[3] == 'p':
				pygame.draw.rect(screen, white, (p_block))
			if actual_word[3] == 'q':
				pygame.draw.rect(screen, white, (q_block))
			if actual_word[3] == 'r':
				pygame.draw.rect(screen, white, (r_block))
			if actual_word[3] == 's':
				pygame.draw.rect(screen, white, (s_block))
			if actual_word[3] == 't':
				pygame.draw.rect(screen, white, (t_block))
			if actual_word[3] == 'u':
				pygame.draw.rect(screen, white, (u_block))
			if actual_word[3] == 'v':
				pygame.draw.rect(screen, white, (v_block))
			if actual_word[3] == 'w':
				pygame.draw.rect(screen, white, (w_block))
			if actual_word[3] == 'x':
				pygame.draw.rect(screen, white, (x_block))
			if actual_word[3] == 'y':
				pygame.draw.rect(screen, white, (y_block))
			if actual_word[3] == 'z':
				pygame.draw.rect(screen, white, (z_block))
			pygame.display.update()
		if actual_word[4] != '-'and answer_var and letter5:
			a = font4.render(actual_word[4], True, yellow)
			screen.blit(a, (395, 260))
			answer_var = False
			letter5 = False
			hint_len += 1
			if actual_word[4] == 'a':
				pygame.draw.rect(screen, white, (a_block))
			if actual_word[4] == 'b':
				pygame.draw.rect(screen, white, (b_block))
			if actual_word[4] == 'c':
				pygame.draw.rect(screen, white, (c_block))
			if actual_word[4] == 'd':
				pygame.draw.rect(screen, white, (d_block))
			if actual_word[4] == 'e':
				pygame.draw.rect(screen, white, (e_block))
			if actual_word[4] == 'f':
				pygame.draw.rect(screen, white, (f_block))
			if actual_word[4] == 'g':
				pygame.draw.rect(screen, white, (g_block))
			if actual_word[4] == 'h':
				pygame.draw.rect(screen, white, (h_block))
			if actual_word[4] == 'i':
				pygame.draw.rect(screen, white, (i_block))
			if actual_word[4] == 'j':
				pygame.draw.rect(screen, white, (j_block))
			if actual_word[4] == 'k':
				pygame.draw.rect(screen, white, (k_block))
			if actual_word[4] == 'l':
				pygame.draw.rect(screen, white, (l_block))
			if actual_word[4] == 'm':
				pygame.draw.rect(screen, white, (m_block))
			if actual_word[4] == 'n':
				pygame.draw.rect(screen, white, (n_block))
			if actual_word[4] == 'o':
				pygame.draw.rect(screen, white, (o_block))
			if actual_word[4] == 'p':
				pygame.draw.rect(screen, white, (p_block))
			if actual_word[4] == 'q':
				pygame.draw.rect(screen, white, (q_block))
			if actual_word[4] == 'r':
				pygame.draw.rect(screen, white, (r_block))
			if actual_word[4] == 's':
				pygame.draw.rect(screen, white, (s_block))
			if actual_word[4] == 't':
				pygame.draw.rect(screen, white, (t_block))
			if actual_word[4] == 'u':
				pygame.draw.rect(screen, white, (u_block))
			if actual_word[4] == 'v':
				pygame.draw.rect(screen, white, (v_block))
			if actual_word[4] == 'w':
				pygame.draw.rect(screen, white, (w_block))
			if actual_word[4] == 'x':
				pygame.draw.rect(screen, white, (x_block))
			if actual_word[4] == 'y':
				pygame.draw.rect(screen, white, (y_block))
			if actual_word[4] == 'z':
				pygame.draw.rect(screen, white, (z_block))
			pygame.display.update()
		if actual_word[5] != '-'and answer_var and letter6:
			a = font4.render(actual_word[5], True, yellow)
			screen.blit(a, (430, 260))
			answer_var = False
			letter6 = False
			hint_len += 1
			if actual_word[5] == 'a':
				pygame.draw.rect(screen, white, (a_block))
			if actual_word[5] == 'b':
				pygame.draw.rect(screen, white, (b_block))
			if actual_word[5] == 'c':
				pygame.draw.rect(screen, white, (c_block))
			if actual_word[5] == 'd':
				pygame.draw.rect(screen, white, (d_block))
			if actual_word[5] == 'e':
				pygame.draw.rect(screen, white, (e_block))
			if actual_word[5] == 'f':
				pygame.draw.rect(screen, white, (f_block))
			if actual_word[5] == 'g':
				pygame.draw.rect(screen, white, (g_block))
			if actual_word[5] == 'h':
				pygame.draw.rect(screen, white, (h_block))
			if actual_word[5] == 'i':
				pygame.draw.rect(screen, white, (i_block))
			if actual_word[5] == 'j':
				pygame.draw.rect(screen, white, (j_block))
			if actual_word[5] == 'k':
				pygame.draw.rect(screen, white, (k_block))
			if actual_word[5] == 'l':
				pygame.draw.rect(screen, white, (l_block))
			if actual_word[5] == 'm':
				pygame.draw.rect(screen, white, (m_block))
			if actual_word[5] == 'n':
				pygame.draw.rect(screen, white, (n_block))
			if actual_word[5] == 'o':
				pygame.draw.rect(screen, white, (o_block))
			if actual_word[5] == 'p':
				pygame.draw.rect(screen, white, (p_block))
			if actual_word[5] == 'q':
				pygame.draw.rect(screen, white, (q_block))
			if actual_word[5] == 'r':
				pygame.draw.rect(screen, white, (r_block))
			if actual_word[5] == 's':
				pygame.draw.rect(screen, white, (s_block))
			if actual_word[5] == 't':
				pygame.draw.rect(screen, white, (t_block))
			if actual_word[5] == 'u':
				pygame.draw.rect(screen, white, (u_block))
			if actual_word[5] == 'v':
				pygame.draw.rect(screen, white, (v_block))
			if actual_word[5] == 'w':
				pygame.draw.rect(screen, white, (w_block))
			if actual_word[5] == 'x':
				pygame.draw.rect(screen, white, (x_block))
			if actual_word[5] == 'y':
				pygame.draw.rect(screen, white, (y_block))
			if actual_word[5] == 'z':
				pygame.draw.rect(screen, white, (z_block))
			pygame.display.update()
		if actual_word[6] != '-'and answer_var and letter7:
			a = font4.render(actual_word[6], True, yellow)
			screen.blit(a, (465, 260))
			answer_var = False
			letter7 = False
			hint_len += 1
			if actual_word[6] == 'a':
				pygame.draw.rect(screen, white, (a_block))
			if actual_word[6] == 'b':
				pygame.draw.rect(screen, white, (b_block))
			if actual_word[6] == 'c':
				pygame.draw.rect(screen, white, (c_block))
			if actual_word[6] == 'd':
				pygame.draw.rect(screen, white, (d_block))
			if actual_word[6] == 'e':
				pygame.draw.rect(screen, white, (e_block))
			if actual_word[6] == 'f':
				pygame.draw.rect(screen, white, (f_block))
			if actual_word[6] == 'g':
				pygame.draw.rect(screen, white, (g_block))
			if actual_word[6] == 'h':
				pygame.draw.rect(screen, white, (h_block))
			if actual_word[6] == 'i':
				pygame.draw.rect(screen, white, (i_block))
			if actual_word[6] == 'j':
				pygame.draw.rect(screen, white, (j_block))
			if actual_word[6] == 'k':
				pygame.draw.rect(screen, white, (k_block))
			if actual_word[6] == 'l':
				pygame.draw.rect(screen, white, (l_block))
			if actual_word[6] == 'm':
				pygame.draw.rect(screen, white, (m_block))
			if actual_word[6] == 'n':
				pygame.draw.rect(screen, white, (n_block))
			if actual_word[6] == 'o':
				pygame.draw.rect(screen, white, (o_block))
			if actual_word[6] == 'p':
				pygame.draw.rect(screen, white, (p_block))
			if actual_word[6] == 'q':
				pygame.draw.rect(screen, white, (q_block))
			if actual_word[6] == 'r':
				pygame.draw.rect(screen, white, (r_block))
			if actual_word[6] == 's':
				pygame.draw.rect(screen, white, (s_block))
			if actual_word[6] == 't':
				pygame.draw.rect(screen, white, (t_block))
			if actual_word[6] == 'u':
				pygame.draw.rect(screen, white, (u_block))
			if actual_word[6] == 'v':
				pygame.draw.rect(screen, white, (v_block))
			if actual_word[6] == 'w':
				pygame.draw.rect(screen, white, (w_block))
			if actual_word[6] == 'x':
				pygame.draw.rect(screen, white, (x_block))
			if actual_word[6] == 'y':
				pygame.draw.rect(screen, white, (y_block))
			if actual_word[6] == 'z':
				pygame.draw.rect(screen, white, (z_block))
			pygame.display.update()
		if actual_word[7] != '-'and answer_var and letter8:
			a = font4.render(actual_word[7], True, yellow)
			screen.blit(a, (500, 260))
			answer_var = False
			letter8 = False
			hint_len += 1
			if actual_word[7] == 'a':
				pygame.draw.rect(screen, white, (a_block))
			if actual_word[7] == 'b':
				pygame.draw.rect(screen, white, (b_block))
			if actual_word[7] == 'c':
				pygame.draw.rect(screen, white, (c_block))
			if actual_word[7] == 'd':
				pygame.draw.rect(screen, white, (d_block))
			if actual_word[7] == 'e':
				pygame.draw.rect(screen, white, (e_block))
			if actual_word[7] == 'f':
				pygame.draw.rect(screen, white, (f_block))
			if actual_word[7] == 'g':
				pygame.draw.rect(screen, white, (g_block))
			if actual_word[7] == 'h':
				pygame.draw.rect(screen, white, (h_block))
			if actual_word[7] == 'i':
				pygame.draw.rect(screen, white, (i_block))
			if actual_word[7] == 'j':
				pygame.draw.rect(screen, white, (j_block))
			if actual_word[7] == 'k':
				pygame.draw.rect(screen, white, (k_block))
			if actual_word[7] == 'l':
				pygame.draw.rect(screen, white, (l_block))
			if actual_word[7] == 'm':
				pygame.draw.rect(screen, white, (m_block))
			if actual_word[7] == 'n':
				pygame.draw.rect(screen, white, (n_block))
			if actual_word[7] == 'o':
				pygame.draw.rect(screen, white, (o_block))
			if actual_word[7] == 'p':
				pygame.draw.rect(screen, white, (p_block))
			if actual_word[7] == 'q':
				pygame.draw.rect(screen, white, (q_block))
			if actual_word[7] == 'r':
				pygame.draw.rect(screen, white, (r_block))
			if actual_word[7] == 's':
				pygame.draw.rect(screen, white, (s_block))
			if actual_word[7] == 't':
				pygame.draw.rect(screen, white, (t_block))
			if actual_word[7] == 'u':
				pygame.draw.rect(screen, white, (u_block))
			if actual_word[7] == 'v':
				pygame.draw.rect(screen, white, (v_block))
			if actual_word[7] == 'w':
				pygame.draw.rect(screen, white, (w_block))
			if actual_word[7] == 'x':
				pygame.draw.rect(screen, white, (x_block))
			if actual_word[7] == 'y':
				pygame.draw.rect(screen, white, (y_block))
			if actual_word[7] == 'z':
				pygame.draw.rect(screen, white, (z_block))
			pygame.display.update()
		if actual_word[8] != '-'and answer_var and letter9:
			a = font4.render(actual_word[8], True, yellow)
			screen.blit(a, (535, 260))
			answer_var = False
			letter9 = False
			hint_len += 1
			if actual_word[8] == 'a':
				pygame.draw.rect(screen, white, (a_block))
			if actual_word[8] == 'b':
				pygame.draw.rect(screen, white, (b_block))
			if actual_word[8] == 'c':
				pygame.draw.rect(screen, white, (c_block))
			if actual_word[8] == 'd':
				pygame.draw.rect(screen, white, (d_block))
			if actual_word[8] == 'e':
				pygame.draw.rect(screen, white, (e_block))
			if actual_word[8] == 'f':
				pygame.draw.rect(screen, white, (f_block))
			if actual_word[8] == 'g':
				pygame.draw.rect(screen, white, (g_block))
			if actual_word[8] == 'h':
				pygame.draw.rect(screen, white, (h_block))
			if actual_word[8] == 'i':
				pygame.draw.rect(screen, white, (i_block))
			if actual_word[8] == 'j':
				pygame.draw.rect(screen, white, (j_block))
			if actual_word[8] == 'k':
				pygame.draw.rect(screen, white, (k_block))
			if actual_word[8] == 'l':
				pygame.draw.rect(screen, white, (l_block))
			if actual_word[8] == 'm':
				pygame.draw.rect(screen, white, (m_block))
			if actual_word[8] == 'n':
				pygame.draw.rect(screen, white, (n_block))
			if actual_word[8] == 'o':
				pygame.draw.rect(screen, white, (o_block))
			if actual_word[8] == 'p':
				pygame.draw.rect(screen, white, (p_block))
			if actual_word[8] == 'q':
				pygame.draw.rect(screen, white, (q_block))
			if actual_word[8] == 'r':
				pygame.draw.rect(screen, white, (r_block))
			if actual_word[8] == 's':
				pygame.draw.rect(screen, white, (s_block))
			if actual_word[8] == 't':
				pygame.draw.rect(screen, white, (t_block))
			if actual_word[8] == 'u':
				pygame.draw.rect(screen, white, (u_block))
			if actual_word[8] == 'v':
				pygame.draw.rect(screen, white, (v_block))
			if actual_word[8] == 'w':
				pygame.draw.rect(screen, white, (w_block))
			if actual_word[8] == 'x':
				pygame.draw.rect(screen, white, (x_block))
			if actual_word[8] == 'y':
				pygame.draw.rect(screen, white, (y_block))
			if actual_word[8] == 'z':
				pygame.draw.rect(screen, white, (z_block))
			pygame.display.update()
		if actual_word[9] != '-'and answer_var and letter10:
			a = font4.render(actual_word[9], True, yellow)
			screen.blit(a, (570, 260))
			answer_var = False
			letter10 = False
			hint_len += 1
			if actual_word[9] == 'a':
				pygame.draw.rect(screen, white, (a_block))
			if actual_word[9] == 'b':
				pygame.draw.rect(screen, white, (b_block))
			if actual_word[9] == 'c':
				pygame.draw.rect(screen, white, (c_block))
			if actual_word[9] == 'd':
				pygame.draw.rect(screen, white, (d_block))
			if actual_word[9] == 'e':
				pygame.draw.rect(screen, white, (e_block))
			if actual_word[9] == 'f':
				pygame.draw.rect(screen, white, (f_block))
			if actual_word[9] == 'g':
				pygame.draw.rect(screen, white, (g_block))
			if actual_word[9] == 'h':
				pygame.draw.rect(screen, white, (h_block))
			if actual_word[9] == 'i':
				pygame.draw.rect(screen, white, (i_block))
			if actual_word[9] == 'j':
				pygame.draw.rect(screen, white, (j_block))
			if actual_word[9] == 'k':
				pygame.draw.rect(screen, white, (k_block))
			if actual_word[9] == 'l':
				pygame.draw.rect(screen, white, (l_block))
			if actual_word[9] == 'm':
				pygame.draw.rect(screen, white, (m_block))
			if actual_word[9] == 'n':
				pygame.draw.rect(screen, white, (n_block))
			if actual_word[9] == 'o':
				pygame.draw.rect(screen, white, (o_block))
			if actual_word[9] == 'p':
				pygame.draw.rect(screen, white, (p_block))
			if actual_word[9] == 'q':
				pygame.draw.rect(screen, white, (q_block))
			if actual_word[9] == 'r':
				pygame.draw.rect(screen, white, (r_block))
			if actual_word[9] == 's':
				pygame.draw.rect(screen, white, (s_block))
			if actual_word[9] == 't':
				pygame.draw.rect(screen, white, (t_block))
			if actual_word[9] == 'u':
				pygame.draw.rect(screen, white, (u_block))
			if actual_word[9] == 'v':
				pygame.draw.rect(screen, white, (v_block))
			if actual_word[9] == 'w':
				pygame.draw.rect(screen, white, (w_block))
			if actual_word[9] == 'x':
				pygame.draw.rect(screen, white, (x_block))
			if actual_word[9] == 'y':
				pygame.draw.rect(screen, white, (y_block))
			if actual_word[9] == 'z':
				pygame.draw.rect(screen, white, (z_block))
			pygame.display.update()
		if actual_word[10] != '-'and answer_var and letter11:
			a = font4.render(actual_word[10], True, yellow)
			screen.blit(a, (605, 260))
			answer_var = False
			letter11 = False
			hint_len += 1
			if actual_word[10] == 'a':
				pygame.draw.rect(screen, white, (a_block))
			if actual_word[10] == 'b':
				pygame.draw.rect(screen, white, (b_block))
			if actual_word[10] == 'c':
				pygame.draw.rect(screen, white, (c_block))
			if actual_word[10] == 'd':
				pygame.draw.rect(screen, white, (d_block))
			if actual_word[10] == 'e':
				pygame.draw.rect(screen, white, (e_block))
			if actual_word[10] == 'f':
				pygame.draw.rect(screen, white, (f_block))
			if actual_word[10] == 'g':
				pygame.draw.rect(screen, white, (g_block))
			if actual_word[10] == 'h':
				pygame.draw.rect(screen, white, (h_block))
			if actual_word[10] == 'i':
				pygame.draw.rect(screen, white, (i_block))
			if actual_word[10] == 'j':
				pygame.draw.rect(screen, white, (j_block))
			if actual_word[10] == 'k':
				pygame.draw.rect(screen, white, (k_block))
			if actual_word[10] == 'l':
				pygame.draw.rect(screen, white, (l_block))
			if actual_word[10] == 'm':
				pygame.draw.rect(screen, white, (m_block))
			if actual_word[10] == 'n':
				pygame.draw.rect(screen, white, (n_block))
			if actual_word[10] == 'o':
				pygame.draw.rect(screen, white, (o_block))
			if actual_word[10] == 'p':
				pygame.draw.rect(screen, white, (p_block))
			if actual_word[10] == 'q':
				pygame.draw.rect(screen, white, (q_block))
			if actual_word[10] == 'r':
				pygame.draw.rect(screen, white, (r_block))
			if actual_word[10] == 's':
				pygame.draw.rect(screen, white, (s_block))
			if actual_word[10] == 't':
				pygame.draw.rect(screen, white, (t_block))
			if actual_word[10] == 'u':
				pygame.draw.rect(screen, white, (u_block))
			if actual_word[10] == 'v':
				pygame.draw.rect(screen, white, (v_block))
			if actual_word[10] == 'w':
				pygame.draw.rect(screen, white, (w_block))
			if actual_word[10] == 'x':
				pygame.draw.rect(screen, white, (x_block))
			if actual_word[10] == 'y':
				pygame.draw.rect(screen, white, (y_block))
			if actual_word[10] == 'z':
				pygame.draw.rect(screen, white, (z_block))
			pygame.display.update()
	if len(word) == 12:
		if actual_word[0] != '-'and answer_var and letter1:
			a = font4.render(actual_word[0], True, yellow)
			screen.blit(a, (255, 260))
			answer_var = False
			letter1 = False
			hint_len += 1
			if actual_word[0] == 'a':
				pygame.draw.rect(screen, white, (a_block))
			if actual_word[0] == 'b':
				pygame.draw.rect(screen, white, (b_block))
			if actual_word[0] == 'c':
				pygame.draw.rect(screen, white, (c_block))
			if actual_word[0] == 'd':
				pygame.draw.rect(screen, white, (d_block))
			if actual_word[0] == 'e':
				pygame.draw.rect(screen, white, (e_block))
			if actual_word[0] == 'f':
				pygame.draw.rect(screen, white, (f_block))
			if actual_word[0] == 'g':
				pygame.draw.rect(screen, white, (g_block))
			if actual_word[0] == 'h':
				pygame.draw.rect(screen, white, (h_block))
			if actual_word[0] == 'i':
				pygame.draw.rect(screen, white, (i_block))
			if actual_word[0] == 'j':
				pygame.draw.rect(screen, white, (j_block))
			if actual_word[0] == 'k':
				pygame.draw.rect(screen, white, (k_block))
			if actual_word[0] == 'l':
				pygame.draw.rect(screen, white, (l_block))
			if actual_word[0] == 'm':
				pygame.draw.rect(screen, white, (m_block))
			if actual_word[0] == 'n':
				pygame.draw.rect(screen, white, (n_block))
			if actual_word[0] == 'o':
				pygame.draw.rect(screen, white, (o_block))
			if actual_word[0] == 'p':
				pygame.draw.rect(screen, white, (p_block))
			if actual_word[0] == 'q':
				pygame.draw.rect(screen, white, (q_block))
			if actual_word[0] == 'r':
				pygame.draw.rect(screen, white, (r_block))
			if actual_word[0] == 's':
				pygame.draw.rect(screen, white, (s_block))
			if actual_word[0] == 't':
				pygame.draw.rect(screen, white, (t_block))
			if actual_word[0] == 'u':
				pygame.draw.rect(screen, white, (u_block))
			if actual_word[0] == 'v':
				pygame.draw.rect(screen, white, (v_block))
			if actual_word[0] == 'w':
				pygame.draw.rect(screen, white, (w_block))
			if actual_word[0] == 'x':
				pygame.draw.rect(screen, white, (x_block))
			if actual_word[0] == 'y':
				pygame.draw.rect(screen, white, (y_block))
			if actual_word[0] == 'z':
				pygame.draw.rect(screen, white, (z_block))
			pygame.display.update()
		if actual_word[1] != '-'and answer_var and letter2:
			a = font4.render(actual_word[1], True, yellow)
			screen.blit(a, (290, 260))
			answer_var = False
			letter2 = False
			hint_len += 1
			if actual_word[1] == 'a':
				pygame.draw.rect(screen, white, (a_block))
			if actual_word[1] == 'b':
				pygame.draw.rect(screen, white, (b_block))
			if actual_word[1] == 'c':
				pygame.draw.rect(screen, white, (c_block))
			if actual_word[1] == 'd':
				pygame.draw.rect(screen, white, (d_block))
			if actual_word[1] == 'e':
				pygame.draw.rect(screen, white, (e_block))
			if actual_word[1] == 'f':
				pygame.draw.rect(screen, white, (f_block))
			if actual_word[1] == 'g':
				pygame.draw.rect(screen, white, (g_block))
			if actual_word[1] == 'h':
				pygame.draw.rect(screen, white, (h_block))
			if actual_word[1] == 'i':
				pygame.draw.rect(screen, white, (i_block))
			if actual_word[1] == 'j':
				pygame.draw.rect(screen, white, (j_block))
			if actual_word[1] == 'k':
				pygame.draw.rect(screen, white, (k_block))
			if actual_word[1] == 'l':
				pygame.draw.rect(screen, white, (l_block))
			if actual_word[1] == 'm':
				pygame.draw.rect(screen, white, (m_block))
			if actual_word[1] == 'n':
				pygame.draw.rect(screen, white, (n_block))
			if actual_word[1] == 'o':
				pygame.draw.rect(screen, white, (o_block))
			if actual_word[1] == 'p':
				pygame.draw.rect(screen, white, (p_block))
			if actual_word[1] == 'q':
				pygame.draw.rect(screen, white, (q_block))
			if actual_word[1] == 'r':
				pygame.draw.rect(screen, white, (r_block))
			if actual_word[1] == 's':
				pygame.draw.rect(screen, white, (s_block))
			if actual_word[1] == 't':
				pygame.draw.rect(screen, white, (t_block))
			if actual_word[1] == 'u':
				pygame.draw.rect(screen, white, (u_block))
			if actual_word[1] == 'v':
				pygame.draw.rect(screen, white, (v_block))
			if actual_word[1] == 'w':
				pygame.draw.rect(screen, white, (w_block))
			if actual_word[1] == 'x':
				pygame.draw.rect(screen, white, (x_block))
			if actual_word[1] == 'y':
				pygame.draw.rect(screen, white, (y_block))
			if actual_word[1] == 'z':
				pygame.draw.rect(screen, white, (z_block))
			pygame.display.update()
		if actual_word[2] != '-'and answer_var and letter3:
			a = font4.render(actual_word[2], True, yellow)
			screen.blit(a, (325, 260))
			answer_var = False
			letter3 = False
			hint_len += 1
			if actual_word[2] == 'a':
				pygame.draw.rect(screen, white, (a_block))
			if actual_word[2] == 'b':
				pygame.draw.rect(screen, white, (b_block))
			if actual_word[2] == 'c':
				pygame.draw.rect(screen, white, (c_block))
			if actual_word[2] == 'd':
				pygame.draw.rect(screen, white, (d_block))
			if actual_word[2] == 'e':
				pygame.draw.rect(screen, white, (e_block))
			if actual_word[2] == 'f':
				pygame.draw.rect(screen, white, (f_block))
			if actual_word[2] == 'g':
				pygame.draw.rect(screen, white, (g_block))
			if actual_word[2] == 'h':
				pygame.draw.rect(screen, white, (h_block))
			if actual_word[2] == 'i':
				pygame.draw.rect(screen, white, (i_block))
			if actual_word[2] == 'j':
				pygame.draw.rect(screen, white, (j_block))
			if actual_word[2] == 'k':
				pygame.draw.rect(screen, white, (k_block))
			if actual_word[2] == 'l':
				pygame.draw.rect(screen, white, (l_block))
			if actual_word[2] == 'm':
				pygame.draw.rect(screen, white, (m_block))
			if actual_word[2] == 'n':
				pygame.draw.rect(screen, white, (n_block))
			if actual_word[2] == 'o':
				pygame.draw.rect(screen, white, (o_block))
			if actual_word[2] == 'p':
				pygame.draw.rect(screen, white, (p_block))
			if actual_word[2] == 'q':
				pygame.draw.rect(screen, white, (q_block))
			if actual_word[2] == 'r':
				pygame.draw.rect(screen, white, (r_block))
			if actual_word[2] == 's':
				pygame.draw.rect(screen, white, (s_block))
			if actual_word[2] == 't':
				pygame.draw.rect(screen, white, (t_block))
			if actual_word[2] == 'u':
				pygame.draw.rect(screen, white, (u_block))
			if actual_word[2] == 'v':
				pygame.draw.rect(screen, white, (v_block))
			if actual_word[2] == 'w':
				pygame.draw.rect(screen, white, (w_block))
			if actual_word[2] == 'x':
				pygame.draw.rect(screen, white, (x_block))
			if actual_word[2] == 'y':
				pygame.draw.rect(screen, white, (y_block))
			if actual_word[2] == 'z':
				pygame.draw.rect(screen, white, (z_block))
			pygame.display.update()
		if actual_word[3] != '-'and answer_var and letter4:
			a = font4.render(actual_word[3], True, yellow)
			screen.blit(a, (360, 260))
			answer_var = False
			letter4 = False
			hint_len += 1
			if actual_word[3] == 'a':
				pygame.draw.rect(screen, white, (a_block))
			if actual_word[3] == 'b':
				pygame.draw.rect(screen, white, (b_block))
			if actual_word[3] == 'c':
				pygame.draw.rect(screen, white, (c_block))
			if actual_word[3] == 'd':
				pygame.draw.rect(screen, white, (d_block))
			if actual_word[3] == 'e':
				pygame.draw.rect(screen, white, (e_block))
			if actual_word[3] == 'f':
				pygame.draw.rect(screen, white, (f_block))
			if actual_word[3] == 'g':
				pygame.draw.rect(screen, white, (g_block))
			if actual_word[3] == 'h':
				pygame.draw.rect(screen, white, (h_block))
			if actual_word[3] == 'i':
				pygame.draw.rect(screen, white, (i_block))
			if actual_word[3] == 'j':
				pygame.draw.rect(screen, white, (j_block))
			if actual_word[3] == 'k':
				pygame.draw.rect(screen, white, (k_block))
			if actual_word[3] == 'l':
				pygame.draw.rect(screen, white, (l_block))
			if actual_word[3] == 'm':
				pygame.draw.rect(screen, white, (m_block))
			if actual_word[3] == 'n':
				pygame.draw.rect(screen, white, (n_block))
			if actual_word[3] == 'o':
				pygame.draw.rect(screen, white, (o_block))
			if actual_word[3] == 'p':
				pygame.draw.rect(screen, white, (p_block))
			if actual_word[3] == 'q':
				pygame.draw.rect(screen, white, (q_block))
			if actual_word[3] == 'r':
				pygame.draw.rect(screen, white, (r_block))
			if actual_word[3] == 's':
				pygame.draw.rect(screen, white, (s_block))
			if actual_word[3] == 't':
				pygame.draw.rect(screen, white, (t_block))
			if actual_word[3] == 'u':
				pygame.draw.rect(screen, white, (u_block))
			if actual_word[3] == 'v':
				pygame.draw.rect(screen, white, (v_block))
			if actual_word[3] == 'w':
				pygame.draw.rect(screen, white, (w_block))
			if actual_word[3] == 'x':
				pygame.draw.rect(screen, white, (x_block))
			if actual_word[3] == 'y':
				pygame.draw.rect(screen, white, (y_block))
			if actual_word[3] == 'z':
				pygame.draw.rect(screen, white, (z_block))
			pygame.display.update()
		if actual_word[4] != '-'and answer_var and letter5:
			a = font4.render(actual_word[4], True, yellow)
			screen.blit(a, (395, 260))
			answer_var = False
			letter5 = False
			hint_len += 1
			if actual_word[4] == 'a':
				pygame.draw.rect(screen, white, (a_block))
			if actual_word[4] == 'b':
				pygame.draw.rect(screen, white, (b_block))
			if actual_word[4] == 'c':
				pygame.draw.rect(screen, white, (c_block))
			if actual_word[4] == 'd':
				pygame.draw.rect(screen, white, (d_block))
			if actual_word[4] == 'e':
				pygame.draw.rect(screen, white, (e_block))
			if actual_word[4] == 'f':
				pygame.draw.rect(screen, white, (f_block))
			if actual_word[4] == 'g':
				pygame.draw.rect(screen, white, (g_block))
			if actual_word[4] == 'h':
				pygame.draw.rect(screen, white, (h_block))
			if actual_word[4] == 'i':
				pygame.draw.rect(screen, white, (i_block))
			if actual_word[4] == 'j':
				pygame.draw.rect(screen, white, (j_block))
			if actual_word[4] == 'k':
				pygame.draw.rect(screen, white, (k_block))
			if actual_word[4] == 'l':
				pygame.draw.rect(screen, white, (l_block))
			if actual_word[4] == 'm':
				pygame.draw.rect(screen, white, (m_block))
			if actual_word[4] == 'n':
				pygame.draw.rect(screen, white, (n_block))
			if actual_word[4] == 'o':
				pygame.draw.rect(screen, white, (o_block))
			if actual_word[4] == 'p':
				pygame.draw.rect(screen, white, (p_block))
			if actual_word[4] == 'q':
				pygame.draw.rect(screen, white, (q_block))
			if actual_word[4] == 'r':
				pygame.draw.rect(screen, white, (r_block))
			if actual_word[4] == 's':
				pygame.draw.rect(screen, white, (s_block))
			if actual_word[4] == 't':
				pygame.draw.rect(screen, white, (t_block))
			if actual_word[4] == 'u':
				pygame.draw.rect(screen, white, (u_block))
			if actual_word[4] == 'v':
				pygame.draw.rect(screen, white, (v_block))
			if actual_word[4] == 'w':
				pygame.draw.rect(screen, white, (w_block))
			if actual_word[4] == 'x':
				pygame.draw.rect(screen, white, (x_block))
			if actual_word[4] == 'y':
				pygame.draw.rect(screen, white, (y_block))
			if actual_word[4] == 'z':
				pygame.draw.rect(screen, white, (z_block))
			pygame.display.update()
		if actual_word[5] != '-'and answer_var and letter6:
			a = font4.render(actual_word[5], True, yellow)
			screen.blit(a, (430, 260))
			answer_var = False
			letter6 = False
			hint_len += 1
			if actual_word[5] == 'a':
				pygame.draw.rect(screen, white, (a_block))
			if actual_word[5] == 'b':
				pygame.draw.rect(screen, white, (b_block))
			if actual_word[5] == 'c':
				pygame.draw.rect(screen, white, (c_block))
			if actual_word[5] == 'd':
				pygame.draw.rect(screen, white, (d_block))
			if actual_word[5] == 'e':
				pygame.draw.rect(screen, white, (e_block))
			if actual_word[5] == 'f':
				pygame.draw.rect(screen, white, (f_block))
			if actual_word[5] == 'g':
				pygame.draw.rect(screen, white, (g_block))
			if actual_word[5] == 'h':
				pygame.draw.rect(screen, white, (h_block))
			if actual_word[5] == 'i':
				pygame.draw.rect(screen, white, (i_block))
			if actual_word[5] == 'j':
				pygame.draw.rect(screen, white, (j_block))
			if actual_word[5] == 'k':
				pygame.draw.rect(screen, white, (k_block))
			if actual_word[5] == 'l':
				pygame.draw.rect(screen, white, (l_block))
			if actual_word[5] == 'm':
				pygame.draw.rect(screen, white, (m_block))
			if actual_word[5] == 'n':
				pygame.draw.rect(screen, white, (n_block))
			if actual_word[5] == 'o':
				pygame.draw.rect(screen, white, (o_block))
			if actual_word[5] == 'p':
				pygame.draw.rect(screen, white, (p_block))
			if actual_word[5] == 'q':
				pygame.draw.rect(screen, white, (q_block))
			if actual_word[5] == 'r':
				pygame.draw.rect(screen, white, (r_block))
			if actual_word[5] == 's':
				pygame.draw.rect(screen, white, (s_block))
			if actual_word[5] == 't':
				pygame.draw.rect(screen, white, (t_block))
			if actual_word[5] == 'u':
				pygame.draw.rect(screen, white, (u_block))
			if actual_word[5] == 'v':
				pygame.draw.rect(screen, white, (v_block))
			if actual_word[5] == 'w':
				pygame.draw.rect(screen, white, (w_block))
			if actual_word[5] == 'x':
				pygame.draw.rect(screen, white, (x_block))
			if actual_word[5] == 'y':
				pygame.draw.rect(screen, white, (y_block))
			if actual_word[5] == 'z':
				pygame.draw.rect(screen, white, (z_block))
			pygame.display.update()
		if actual_word[6] != '-'and answer_var and letter7:
			a = font4.render(actual_word[6], True, yellow)
			screen.blit(a, (465, 260))
			answer_var = False
			letter7 = False
			hint_len += 1
			if actual_word[6] == 'a':
				pygame.draw.rect(screen, white, (a_block))
			if actual_word[6] == 'b':
				pygame.draw.rect(screen, white, (b_block))
			if actual_word[6] == 'c':
				pygame.draw.rect(screen, white, (c_block))
			if actual_word[6] == 'd':
				pygame.draw.rect(screen, white, (d_block))
			if actual_word[6] == 'e':
				pygame.draw.rect(screen, white, (e_block))
			if actual_word[6] == 'f':
				pygame.draw.rect(screen, white, (f_block))
			if actual_word[6] == 'g':
				pygame.draw.rect(screen, white, (g_block))
			if actual_word[6] == 'h':
				pygame.draw.rect(screen, white, (h_block))
			if actual_word[6] == 'i':
				pygame.draw.rect(screen, white, (i_block))
			if actual_word[6] == 'j':
				pygame.draw.rect(screen, white, (j_block))
			if actual_word[6] == 'k':
				pygame.draw.rect(screen, white, (k_block))
			if actual_word[6] == 'l':
				pygame.draw.rect(screen, white, (l_block))
			if actual_word[6] == 'm':
				pygame.draw.rect(screen, white, (m_block))
			if actual_word[6] == 'n':
				pygame.draw.rect(screen, white, (n_block))
			if actual_word[6] == 'o':
				pygame.draw.rect(screen, white, (o_block))
			if actual_word[6] == 'p':
				pygame.draw.rect(screen, white, (p_block))
			if actual_word[6] == 'q':
				pygame.draw.rect(screen, white, (q_block))
			if actual_word[6] == 'r':
				pygame.draw.rect(screen, white, (r_block))
			if actual_word[6] == 's':
				pygame.draw.rect(screen, white, (s_block))
			if actual_word[6] == 't':
				pygame.draw.rect(screen, white, (t_block))
			if actual_word[6] == 'u':
				pygame.draw.rect(screen, white, (u_block))
			if actual_word[6] == 'v':
				pygame.draw.rect(screen, white, (v_block))
			if actual_word[6] == 'w':
				pygame.draw.rect(screen, white, (w_block))
			if actual_word[6] == 'x':
				pygame.draw.rect(screen, white, (x_block))
			if actual_word[6] == 'y':
				pygame.draw.rect(screen, white, (y_block))
			if actual_word[6] == 'z':
				pygame.draw.rect(screen, white, (z_block))
			pygame.display.update()
		if actual_word[7] != '-'and answer_var and letter8:
			a = font4.render(actual_word[7], True, yellow)
			screen.blit(a, (500, 260))
			answer_var = False
			letter8 = False
			hint_len += 1
			if actual_word[7] == 'a':
				pygame.draw.rect(screen, white, (a_block))
			if actual_word[7] == 'b':
				pygame.draw.rect(screen, white, (b_block))
			if actual_word[7] == 'c':
				pygame.draw.rect(screen, white, (c_block))
			if actual_word[7] == 'd':
				pygame.draw.rect(screen, white, (d_block))
			if actual_word[7] == 'e':
				pygame.draw.rect(screen, white, (e_block))
			if actual_word[7] == 'f':
				pygame.draw.rect(screen, white, (f_block))
			if actual_word[7] == 'g':
				pygame.draw.rect(screen, white, (g_block))
			if actual_word[7] == 'h':
				pygame.draw.rect(screen, white, (h_block))
			if actual_word[7] == 'i':
				pygame.draw.rect(screen, white, (i_block))
			if actual_word[7] == 'j':
				pygame.draw.rect(screen, white, (j_block))
			if actual_word[7] == 'k':
				pygame.draw.rect(screen, white, (k_block))
			if actual_word[7] == 'l':
				pygame.draw.rect(screen, white, (l_block))
			if actual_word[7] == 'm':
				pygame.draw.rect(screen, white, (m_block))
			if actual_word[7] == 'n':
				pygame.draw.rect(screen, white, (n_block))
			if actual_word[7] == 'o':
				pygame.draw.rect(screen, white, (o_block))
			if actual_word[7] == 'p':
				pygame.draw.rect(screen, white, (p_block))
			if actual_word[7] == 'q':
				pygame.draw.rect(screen, white, (q_block))
			if actual_word[7] == 'r':
				pygame.draw.rect(screen, white, (r_block))
			if actual_word[7] == 's':
				pygame.draw.rect(screen, white, (s_block))
			if actual_word[7] == 't':
				pygame.draw.rect(screen, white, (t_block))
			if actual_word[7] == 'u':
				pygame.draw.rect(screen, white, (u_block))
			if actual_word[7] == 'v':
				pygame.draw.rect(screen, white, (v_block))
			if actual_word[7] == 'w':
				pygame.draw.rect(screen, white, (w_block))
			if actual_word[7] == 'x':
				pygame.draw.rect(screen, white, (x_block))
			if actual_word[7] == 'y':
				pygame.draw.rect(screen, white, (y_block))
			if actual_word[7] == 'z':
				pygame.draw.rect(screen, white, (z_block))
			pygame.display.update()
		if actual_word[8] != '-'and answer_var and letter9:
			a = font4.render(actual_word[8], True, yellow)
			screen.blit(a, (535, 260))
			answer_var = False
			letter9 = False
			hint_len += 1
			if actual_word[8] == 'a':
				pygame.draw.rect(screen, white, (a_block))
			if actual_word[8] == 'b':
				pygame.draw.rect(screen, white, (b_block))
			if actual_word[8] == 'c':
				pygame.draw.rect(screen, white, (c_block))
			if actual_word[8] == 'd':
				pygame.draw.rect(screen, white, (d_block))
			if actual_word[8] == 'e':
				pygame.draw.rect(screen, white, (e_block))
			if actual_word[8] == 'f':
				pygame.draw.rect(screen, white, (f_block))
			if actual_word[8] == 'g':
				pygame.draw.rect(screen, white, (g_block))
			if actual_word[8] == 'h':
				pygame.draw.rect(screen, white, (h_block))
			if actual_word[8] == 'i':
				pygame.draw.rect(screen, white, (i_block))
			if actual_word[8] == 'j':
				pygame.draw.rect(screen, white, (j_block))
			if actual_word[8] == 'k':
				pygame.draw.rect(screen, white, (k_block))
			if actual_word[8] == 'l':
				pygame.draw.rect(screen, white, (l_block))
			if actual_word[8] == 'm':
				pygame.draw.rect(screen, white, (m_block))
			if actual_word[8] == 'n':
				pygame.draw.rect(screen, white, (n_block))
			if actual_word[8] == 'o':
				pygame.draw.rect(screen, white, (o_block))
			if actual_word[8] == 'p':
				pygame.draw.rect(screen, white, (p_block))
			if actual_word[8] == 'q':
				pygame.draw.rect(screen, white, (q_block))
			if actual_word[8] == 'r':
				pygame.draw.rect(screen, white, (r_block))
			if actual_word[8] == 's':
				pygame.draw.rect(screen, white, (s_block))
			if actual_word[8] == 't':
				pygame.draw.rect(screen, white, (t_block))
			if actual_word[8] == 'u':
				pygame.draw.rect(screen, white, (u_block))
			if actual_word[8] == 'v':
				pygame.draw.rect(screen, white, (v_block))
			if actual_word[8] == 'w':
				pygame.draw.rect(screen, white, (w_block))
			if actual_word[8] == 'x':
				pygame.draw.rect(screen, white, (x_block))
			if actual_word[8] == 'y':
				pygame.draw.rect(screen, white, (y_block))
			if actual_word[8] == 'z':
				pygame.draw.rect(screen, white, (z_block))
			pygame.display.update()
		if actual_word[9] != '-'and answer_var and letter10:
			a = font4.render(actual_word[9], True, yellow)
			screen.blit(a, (570, 260))
			answer_var = False
			letter10 = False
			hint_len += 1
			if actual_word[9] == 'a':
				pygame.draw.rect(screen, white, (a_block))
			if actual_word[9] == 'b':
				pygame.draw.rect(screen, white, (b_block))
			if actual_word[9] == 'c':
				pygame.draw.rect(screen, white, (c_block))
			if actual_word[9] == 'd':
				pygame.draw.rect(screen, white, (d_block))
			if actual_word[9] == 'e':
				pygame.draw.rect(screen, white, (e_block))
			if actual_word[9] == 'f':
				pygame.draw.rect(screen, white, (f_block))
			if actual_word[9] == 'g':
				pygame.draw.rect(screen, white, (g_block))
			if actual_word[9] == 'h':
				pygame.draw.rect(screen, white, (h_block))
			if actual_word[9] == 'i':
				pygame.draw.rect(screen, white, (i_block))
			if actual_word[9] == 'j':
				pygame.draw.rect(screen, white, (j_block))
			if actual_word[9] == 'k':
				pygame.draw.rect(screen, white, (k_block))
			if actual_word[9] == 'l':
				pygame.draw.rect(screen, white, (l_block))
			if actual_word[9] == 'm':
				pygame.draw.rect(screen, white, (m_block))
			if actual_word[9] == 'n':
				pygame.draw.rect(screen, white, (n_block))
			if actual_word[9] == 'o':
				pygame.draw.rect(screen, white, (o_block))
			if actual_word[9] == 'p':
				pygame.draw.rect(screen, white, (p_block))
			if actual_word[9] == 'q':
				pygame.draw.rect(screen, white, (q_block))
			if actual_word[9] == 'r':
				pygame.draw.rect(screen, white, (r_block))
			if actual_word[9] == 's':
				pygame.draw.rect(screen, white, (s_block))
			if actual_word[9] == 't':
				pygame.draw.rect(screen, white, (t_block))
			if actual_word[9] == 'u':
				pygame.draw.rect(screen, white, (u_block))
			if actual_word[9] == 'v':
				pygame.draw.rect(screen, white, (v_block))
			if actual_word[9] == 'w':
				pygame.draw.rect(screen, white, (w_block))
			if actual_word[9] == 'x':
				pygame.draw.rect(screen, white, (x_block))
			if actual_word[9] == 'y':
				pygame.draw.rect(screen, white, (y_block))
			if actual_word[9] == 'z':
				pygame.draw.rect(screen, white, (z_block))
			pygame.display.update()
		if actual_word[10] != '-'and answer_var and letter11:
			a = font4.render(actual_word[10], True, yellow)
			screen.blit(a, (605, 260))
			answer_var = False
			letter11 = False
			hint_len += 1
			if actual_word[10] == 'a':
				pygame.draw.rect(screen, white, (a_block))
			if actual_word[10] == 'b':
				pygame.draw.rect(screen, white, (b_block))
			if actual_word[10] == 'c':
				pygame.draw.rect(screen, white, (c_block))
			if actual_word[10] == 'd':
				pygame.draw.rect(screen, white, (d_block))
			if actual_word[10] == 'e':
				pygame.draw.rect(screen, white, (e_block))
			if actual_word[10] == 'f':
				pygame.draw.rect(screen, white, (f_block))
			if actual_word[10] == 'g':
				pygame.draw.rect(screen, white, (g_block))
			if actual_word[10] == 'h':
				pygame.draw.rect(screen, white, (h_block))
			if actual_word[10] == 'i':
				pygame.draw.rect(screen, white, (i_block))
			if actual_word[10] == 'j':
				pygame.draw.rect(screen, white, (j_block))
			if actual_word[10] == 'k':
				pygame.draw.rect(screen, white, (k_block))
			if actual_word[10] == 'l':
				pygame.draw.rect(screen, white, (l_block))
			if actual_word[10] == 'm':
				pygame.draw.rect(screen, white, (m_block))
			if actual_word[10] == 'n':
				pygame.draw.rect(screen, white, (n_block))
			if actual_word[10] == 'o':
				pygame.draw.rect(screen, white, (o_block))
			if actual_word[10] == 'p':
				pygame.draw.rect(screen, white, (p_block))
			if actual_word[10] == 'q':
				pygame.draw.rect(screen, white, (q_block))
			if actual_word[10] == 'r':
				pygame.draw.rect(screen, white, (r_block))
			if actual_word[10] == 's':
				pygame.draw.rect(screen, white, (s_block))
			if actual_word[10] == 't':
				pygame.draw.rect(screen, white, (t_block))
			if actual_word[10] == 'u':
				pygame.draw.rect(screen, white, (u_block))
			if actual_word[10] == 'v':
				pygame.draw.rect(screen, white, (v_block))
			if actual_word[10] == 'w':
				pygame.draw.rect(screen, white, (w_block))
			if actual_word[10] == 'x':
				pygame.draw.rect(screen, white, (x_block))
			if actual_word[10] == 'y':
				pygame.draw.rect(screen, white, (y_block))
			if actual_word[10] == 'z':
				pygame.draw.rect(screen, white, (z_block))
			pygame.display.update()
		if actual_word[11] != '-'and answer_var and letter12:
			a = font4.render(actual_word[11], True, yellow)
			screen.blit(a, (640, 260))
			answer_var = False
			letter12 = False
			hint_len += 1
			if actual_word[11] == 'a':
				pygame.draw.rect(screen, white, (a_block))
			if actual_word[11] == 'b':
				pygame.draw.rect(screen, white, (b_block))
			if actual_word[11] == 'c':
				pygame.draw.rect(screen, white, (c_block))
			if actual_word[11] == 'd':
				pygame.draw.rect(screen, white, (d_block))
			if actual_word[11] == 'e':
				pygame.draw.rect(screen, white, (e_block))
			if actual_word[11] == 'f':
				pygame.draw.rect(screen, white, (f_block))
			if actual_word[11] == 'g':
				pygame.draw.rect(screen, white, (g_block))
			if actual_word[11] == 'h':
				pygame.draw.rect(screen, white, (h_block))
			if actual_word[11] == 'i':
				pygame.draw.rect(screen, white, (i_block))
			if actual_word[11] == 'j':
				pygame.draw.rect(screen, white, (j_block))
			if actual_word[11] == 'k':
				pygame.draw.rect(screen, white, (k_block))
			if actual_word[11] == 'l':
				pygame.draw.rect(screen, white, (l_block))
			if actual_word[11] == 'm':
				pygame.draw.rect(screen, white, (m_block))
			if actual_word[11] == 'n':
				pygame.draw.rect(screen, white, (n_block))
			if actual_word[11] == 'o':
				pygame.draw.rect(screen, white, (o_block))
			if actual_word[11] == 'p':
				pygame.draw.rect(screen, white, (p_block))
			if actual_word[11] == 'q':
				pygame.draw.rect(screen, white, (q_block))
			if actual_word[11] == 'r':
				pygame.draw.rect(screen, white, (r_block))
			if actual_word[11] == 's':
				pygame.draw.rect(screen, white, (s_block))
			if actual_word[11] == 't':
				pygame.draw.rect(screen, white, (t_block))
			if actual_word[11] == 'u':
				pygame.draw.rect(screen, white, (u_block))
			if actual_word[11] == 'v':
				pygame.draw.rect(screen, white, (v_block))
			if actual_word[11] == 'w':
				pygame.draw.rect(screen, white, (w_block))
			if actual_word[11] == 'x':
				pygame.draw.rect(screen, white, (x_block))
			if actual_word[11] == 'y':
				pygame.draw.rect(screen, white, (y_block))
			if actual_word[11] == 'z':
				pygame.draw.rect(screen, white, (z_block))
			pygame.display.update()
	pygame.display.update()

game = True
lives = 10
click = False
correct_guess = 0
lives_txt = 10
hint_len = 0
draw_screen()
# main loop
while True:

	if click:
		guesses()
		guesses()
		guesses()
		guesses()
		guesses()
		click = False

	if guess in alphabet:
		if guess != '':
			alphabet.remove(guess)
			if guess in word:
				correct_guess += 1
			if guess not in word:
				lives -= 1
				lives_txt -= 1
				lives_txt_render = font3.render("You have " + str(lives_txt) + " lives", True, black)
				pygame.draw.rect(screen, white, lives_block)
				screen.blit(lives_txt_render, (5, 150))
				pygame.display.update()
				pass
			word2 = set(word)
			if correct_guess == len(word2):
				print('you won!')
				game = False
				hints += 1
				hint_txt = font3.render("HINTS: " + str(hints), True, black)
				pygame.draw.rect(screen, actual_yellow, hint_block)
				pygame.draw.rect(screen, black, hint_block, 1)
				screen.blit(hint_txt, (480,138))
				
				pygame.display.update()

	if hint_len == len(actual_word):
		game = False
	if (hint_len + correct_guess) == len(actual_word):
		game = False

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
		five = screen.blit(head, (150, 250))
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
		screen.blit(head2, (150, 250))
		pygame.display.update()
		game = False
		answer_var = True
		answer()


	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
		if event.type == pygame.MOUSEBUTTONDOWN:
			click = True
		if event.type == pygame.MOUSEBUTTONUP:
			click = False

		if restart_block.collidepoint(mouse_pos) and click:
			alphabet = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x',
			'c', 'v', 'b', 'n', 'm']
			word = random.choice(word_list)
			actual_word = word
			correct_guess = 0
			game = True
			lives = 10
			click = False
			correct_guess = 0
			lives_txt = 10
			guess = ''
			hint_len = 0
			idk_var = True
			letter1, letter2, letter3, letter4, letter5, letter6 = True, True, True, True, True, True
			letter7, letter8, letter9, letter10, letter11, letter12 = True, True, True, True, True, True
			draw_screen()

		if hint_block.collidepoint(mouse_pos) and click and hints >= 1:
			answer_var = True
			hintFinder()
			hints -= 1
			hint_txt = font3.render("HINTS: " + str(hints), True, black)
			pygame.draw.rect(screen, actual_yellow, hint_block)
			pygame.draw.rect(screen, black, hint_block, 1)
			screen.blit(hint_txt, (480,138))
			
			pygame.display.update()
		if idk_block.collidepoint(mouse_pos) and click and not game and idk_var:
			pywhatkit.search('define ' + word)
			idk_var = False

	mouse_pos = pygame.mouse.get_pos()



	pygame.display.update()