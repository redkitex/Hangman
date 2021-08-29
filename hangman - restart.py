import pygame
import random
import sys
from pygame.locals import *

pygame.init()

# var definitions
game = True
screen = pygame.display.set_mode((725, 600))
lives = 10
word_list = ['elbow', 'jazz', 'abruptly', 'bayou', 'dwarves', 'gossip', 'awkward', 'jockey', 'jigsaw', 'zigzagging',
			  'wizard', 'transcript', 'quiz', 'pneumonia', 'oxygen', 'pixel,', 'transplant', 'rhubarb', 'queue',
			  'rhythm', 'topaz', 'swivel', 'unworthy', 'witchcraft', 'wavy', 'whiskey', 'yoke', 'zigzag', 'microwave',
			  'sphinx', 'scratch', 'thrift', 'xylophone', 'zombie', 'vodka', 'syndrome', 'neighbour', 'neighborhood',
			  'occasional', 'independent', 'egypt', 'grandmother', 'official,', 'monkey,', 'explanation', 'arrangement',
			  'mysterious']
word = random.choice(word_list)
actual_word = word
correct_guess = 0
alphabet = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x',
			'c', 'v', 'b', 'n', 'm']
heading = pygame.image.load("hangman_heading.png")
click = False
guess = ''
mouse_pos = pygame.mouse.get_pos()
lives_txt = 10
head = pygame.image.load("head.png")

# colours
white = (255, 255, 255)
black = (0, 0, 0)
blue = (152, 211, 255)
yellow = (0, 124, 255)

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

lives_txt_render = font3.render("You have " + str(lives_txt) + " lives", True, black)

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


def draw_screen():
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

	# screen.blit(a, (350,250))

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

		if b_block.collidepoint(mouse_pos) and click:
			guhess = 'b'
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

game = True
lives = 10
click = False
correct_guess = 0
lives_txt = 10
draw_screen()
# main loop
while True:
	if click:
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
		pygame.display.update()
		game = False

	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
		if event.type == pygame.MOUSEBUTTONDOWN:
			click = True
		if event.type == pygame.MOUSEBUTTONUP:
			click = False

	mouse_pos = pygame.mouse.get_pos()

	pygame.display.update()