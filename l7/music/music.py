import pygame
import os


pygame.init()


screen = pygame.display.set_mode((600, 400)) 
pygame.display.set_caption("Music Player")


music_folder = "l7\music\music folder"
music_files = [f for f in os.listdir(music_folder) if f.endswith(".mp3")]
current_track_index = 0


font = pygame.font.SysFont('Arial', 24)


def play_music(index):
    pygame.mixer.music.load(os.path.join(music_folder, music_files[index]))
    pygame.mixer.music.play()

def stop_music():
    pygame.mixer.music.stop()

def next_track():
    global current_track_index
    current_track_index = (current_track_index + 1) % len(music_files)
    play_music(current_track_index)

def previous_track():
    global current_track_index
    current_track_index = (current_track_index - 1) % len(music_files)
    play_music(current_track_index)


def display_instructions():
    instructions = [
        "P - Play current track",
        "S - Stop music",
        "N - Next track",
        "B - Previous track",
        "Have a good mood and listen! ^^"
    ]
    
    y_position = 50 
    for instruction in instructions:
        text = font.render(instruction, True, (255, 255, 255))  
        screen.blit(text, (20, y_position))  
        y_position += 40 

running = True
play_music(current_track_index)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:  
                play_music(current_track_index)
            elif event.key == pygame.K_s:  
                stop_music()
            elif event.key == pygame.K_n:  
                next_track()
            elif event.key == pygame.K_b:  
                previous_track()

   
    screen.fill((0, 0, 0))  
    display_instructions()  
    pygame.display.update()


pygame.quit()
