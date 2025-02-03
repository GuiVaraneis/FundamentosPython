import pygame
arquivo = 'heavydirtysoul.mp3'
pygame.init()
pygame.mixer.music.load(arquivo)
pygame.mixer.music.play()
input()
pygame.event.wait()

