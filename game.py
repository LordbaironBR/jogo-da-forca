import pygame
import random
import pyautogui



#palheta de cores para facilitar na seleção de cor
cor_branco = (250,250,250)
cor_preto = (0,0,0)

#tela do jogo
janela = pygame.display.set_mode((1000,600))

#font
pygame.font.init()

font = pygame.font.SysFont("Arial", 50)
font_bt_restart = pygame.font.SysFont("Arial", 30)

#banco de dados de palavras
palavras = [
    "OVELHA",
    "RATO",
    "COBRA",
    "CAVALO",
    "RAPOSA",
    "SAPO",
    "GATO",
    "CACHORRO",
    "TATU",
    "ANTA",
    "JAVALI",
    "JACARE",
    "CROCODILO",
    "PORCO",
    "MULA",
    "POLVO",
    "TUBARAO",
    "GALINHA",
    "ARARA",
    "PAPAGAIO",
    "PELICANO",
    "GIRAFA",
    "CISNEY",
    "FLAMINGO",
    "PEIXE",
    "TARTARUGA",
    "BAIACU",
    "AGUIA",
    "FALCAO",
    "BALEIA",
    "ARANHA",
    "DROMEDARIO",
    "CAMELO",
    "BURRO",
    "CANGURU",
    "CAPIVARA",
    "COALA",
    "CORUJA",
    "ESQUILO",
    "LEAO",
    "LOBO",
    "ZEBRA",
    "URSO"
]

tentativa_letra = ['', '-']
palavra_escolhida = ''
palavra_escondida = ''

fim_jogo = True
chance = 0
letra = ''
botao_restart = False



def Desenho_forca(janela,chance):
    pygame.draw.rect(janela, cor_branco, (0, 0, 1000, 600))
    pygame.draw.line(janela, cor_preto, (100, 500), (100, 100), 10)
    pygame.draw.line(janela, cor_preto, (50, 500), (150, 500), 10)
    pygame.draw.line(janela, cor_preto, (100, 100), (300, 100), 10)
    pygame.draw.line(janela, cor_preto, (300, 100), (300, 150), 10)
    if chance >= 1:
        pygame.draw.circle(janela, cor_preto, (300, 200), 50,10)
    if chance >= 2:
        pygame.draw.line(janela, cor_preto, (300, 250), (300,350),10)
    if chance >= 3:
        pygame.draw.line(janela, cor_preto, (300, 260), (225,350),10)
    if chance >= 4:
        pygame.draw.line(janela, cor_preto, (300, 260), (375,350),10)
    if chance >= 5:
        pygame.draw.line(janela, cor_preto, (300, 350), (375,450),10)
    if chance >= 6:
        pygame.draw.line(janela, cor_preto, (300, 350), (225,450),10)

def Desenho_restart_button(janela):
    pygame.draw.rect(janela,cor_preto, (700,100,200,65))
    texto = font_bt_restart.render('Restart', True, cor_branco)
    janela.blit(texto, (740, 120))

def Sorteio_palavra(palavras,palavra_escolhida,fim_jogo):
    if fim_jogo == True:
        palavra_n = random.randint(0, len(palavras) - 1)
        palavra_escolhida = palavras[palavra_n]
        fim_jogo = False
    return palavra_escolhida, fim_jogo

def Escondendo_palavra(palavra_escolhida, palavra_escondida,tentativa_letra):
    palavra_escondida = palavra_escolhida
    for n in range(len(palavra_escondida)):
        if palavra_escondida[n:n + 1] not in tentativa_letra:
            palavra_escondida = palavra_escondida.replace(palavra_escondida[n], '*')
    return palavra_escondida

def Tentando_letra(tentativa_letra, palavra_escolhida,letra,chance):
    if letra not in tentativa_letra:
        tentativa_letra.append(letra)
        if letra not in palavra_escolhida:
            chance +=1
    elif letra in tentativa_letra:
        pass
    return tentativa_letra,chance

def Palavra_jogo(janela,palavra_escondida):
    palavra = font.render(palavra_escondida, True, cor_preto)
    janela.blit(palavra, (200, 500))


def Restart(fim_jogo,tentativa_letra,palavra_escolhida,palavra_escondida,chance,letra):
    for event in pygame.event.get():

        if event.type == pygame.MOUSEBUTTONDOWN:
            clik = 1
            while clik == 1:
                x,y = pyautogui.position()
                print(pyautogui.position())

                if 1150 < x < 1360 and 340 < y < 405:
                    fim_jogo = True
                    tentativa_letra = ['', '-']
                    palavra_escolhida = ''
                    palavra_escondida = ''
                    chance = 0
                    letra = ''

                clik = 0

    return(fim_jogo,tentativa_letra,palavra_escolhida,palavra_escondida,chance,letra)



#lógica do jogo
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        if event.type == pygame.KEYDOWN:
            letra = str(pygame.key.name(event.key)).upper()
            print(letra)


#setando configurações




#dentro do display
    Desenho_forca(janela, chance)
    Desenho_restart_button(janela)
    palavra_escolhida, fim_jogo = Sorteio_palavra(palavras,palavra_escolhida,fim_jogo)
    palavra_escondida = Escondendo_palavra(palavra_escolhida, palavra_escondida,tentativa_letra)
    tentativa_letra, chance = Tentando_letra(tentativa_letra, palavra_escolhida,letra,chance)
    Palavra_jogo(janela,palavra_escondida)
    fim_jogo,tentativa_letra,palavra_escolhida,palavra_escondida,chance,letra = Restart(fim_jogo,tentativa_letra,palavra_escolhida,palavra_escondida,chance,letra)
    pygame.display.update()
