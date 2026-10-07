import pygame
from time import sleep

def valida_email(email):
    return email[-8:] == "@puc.com"

def possui_maiuscula(senha):
    for carac in senha:
        if 'A' <= carac <= 'Z':
            return True
    return False

def possui_minuscula(senha):
    for carac in senha:
        if 'a' <= carac <= 'z':
            return True
    return False

def possui_numero(senha):
    for carac in senha:
        if carac.isnumeric():
            return True
    return False

def valida_senha(senha):
    if len(senha) < 8:
        return False
    if not possui_maiuscula(senha):
        return False
    if not possui_minuscula(senha):
        return False
    if not possui_numero(senha):
        return False
    
    return True

def criptografa(senha):
    senha_cripto = ""
    for carac in senha:
        if carac.isalpha():
            pos_alpha = ord(carac) - ord('a')
            pos_alpha = (pos_alpha + 3) % 26
            pos_ascii = pos_alpha + ord('a')
            senha_cripto += chr(pos_ascii)
        elif carac.isnumeric():
            pos_num = (int(carac) + 3) % 10
            senha_cripto += str(pos_num) 
    return senha_cripto

## Configurar e utilizar o pygame
pygame.init()
screen = pygame.display.set_mode((1280, 720))
running = True

input_string = ""
valid_email = False
valid_password = False
pressed_enter = False
email_valid_time = 0
fonte = pygame.font.Font(size=50)
fonte_validation = pygame.font.Font(size=25)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                input_string = input_string[:-1]
            elif event.key == pygame.K_RETURN:
                if not valid_email:
                    pressed_enter = True
                    valid_email = valida_email(input_string)
                    if valid_email:
                        input_string = ""
                        email_valid_time = pygame.time.get_ticks()
                elif valid_email and not valid_password:
                    pressed_enter = True
                    valid_password = valida_senha(input_string)
            else:
                input_string += event.unicode



    screen.fill("white")
    pygame.draw.rect(screen, "black", (100, 100, 500, 50), 3)
    input_text = fonte.render(input_string, True, "#000000")
    screen.blit(input_text, (120, 105))
    if pressed_enter:
        current_time = pygame.time.get_ticks()
        if valid_email and (current_time - email_valid_time) < 2000:
            valid_text = fonte_validation.render("Parabéns, o seu e-mail é válido!", True, "green")
            screen.blit(valid_text, (120, 180))
        elif valid_password and not valid_password:
            valid_text = fonte_validation.render("A sua senha não é válida. Digite novamente!", True, "red")
            screen.blit(valid_text, (120, 180))   
        elif valid_email and valid_password:
            senha_cripto = criptografa(input_string)
            valid_text = fonte_validation.render(f"Senha válida! Senha criptografada: {senha_cripto}", True, "green")
            screen.blit(valid_text, (120, 180))
        elif not valid_email:
            valid_text = fonte_validation.render("O seu e-mail não é válido. Digite novamente!", True, "red")
            screen.blit(valid_text, (120, 180))

    pygame.display.update()