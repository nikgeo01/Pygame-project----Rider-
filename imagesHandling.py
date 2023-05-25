import pygame

def resize_image(image, factor):
    size = round(image.get_width() * factor), round(image.get_height() * factor)
    return pygame.transform.scale(image, size)

def rotate_image(screen, image, top_left, angle):
    rotated_image =  pygame.transform.rotate(image, angle)

    #От stackoverflow - https://stackoverflow.com/questions/4183208/how-do-i-rotate-an-image-around-its-center-using-pygame
    #Все още не съм напълно сигурен как работи, но работи :)
    new_rect = rotated_image.get_rect(center = image.get_rect(topleft = top_left).center)

    screen.blit(rotated_image, new_rect.topleft)