
# Connecting modules

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from pygame import mixer
import pygame 
import os, sys
from random import *
pygame.init()
mixer.init()

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


# Notes to not forget:   \n for a new line    Niveles de Español


# Window

app = QApplication([])

main_win = QWidget()

main_win.setFixedSize(700, 500)
main_win.setMaximumSize(10000, 10000)
main_win.setWindowIcon(QIcon(resource_path("flag_of_spain.ico")))

window2 = QWidget()
window2.setFixedSize(200, 100)



# Music & SFX

menu_music = pygame.mixer.Sound(resource_path("bossabossa.mp3"))
enter_sound = pygame.mixer.Sound(resource_path("click.wav"))
click = pygame.mixer.Sound(resource_path("8bitclick.wav"))
no = pygame.mixer.Sound(resource_path("no.mp3"))
si = pygame.mixer.Sound(resource_path("si.mp3"))
el_rio_fluye = pygame.mixer.Sound(resource_path("el_rio_fluye.mp3"))

el_rio_fluye.set_volume(0.3)

menu_music.play(-1)


# Layouts

main_layout = QVBoxLayout()

stats_layout = QHBoxLayout()
nothing_layout = QHBoxLayout()
ans_layout1 = QHBoxLayout() # top
ans_layout2 = QHBoxLayout() # bottom
layout1 = QHBoxLayout() # top
layout2 = QHBoxLayout() # middle
layout3 = QHBoxLayout() # bottom


# Variables

time = 0
evaluations = 0
note = 20
notes = []
right_ans_button = None
exercice = None
questions = 0
true_answer_variable = ""
not_yet_variable = False


# QLabels

line = QLineEdit()
nothing1 = QLabel("")
nothing2 = QLabel("")
true_answer = QLabel("")
top_of_screen = QLabel("Niveles de Español")
stats = QLabel("v.1.1" + "\n"
    "Nota : -" + "\n"
    "Número de pruebas completadas : " + str(evaluations) + "\n"
    "Un juego de Gild56 // @gild56gmd")

stats.setFont(QFont("Arial", 7))
top_of_screen.setFont(QFont("Impact", 15))
nothing2.hide()


# Buttons

ans_button1 = QPushButton("")   #top_left_button
ans_button2 = QPushButton("")   #top_right_button
ans_button3 = QPushButton("")   #bottom_left_button
ans_button4 = QPushButton("")   #bottom_right_button

ok_button = QPushButton("OK")

ans_button1.hide()
ans_button2.hide()
ans_button3.hide()
ans_button4.hide()
ok_button.hide()
line.hide()
true_answer.hide()

button01 = QPushButton("Verbos normales")
button02 = QPushButton("Verbos irregulares")
button03 = QPushButton("Verbos pronominales")
button04 = QPushButton("No está disponible") #Verbos en diptongo
button05 = QPushButton("No está disponible") #Verbos debilitantes
button06 = QPushButton("No está disponible") #Verbos imperatovos
button07 = QPushButton("Ser o Estar")
button08 = QPushButton("No está disponible") #Países
button09 = QPushButton("No está disponible") #Plural de los palabras
button10 = QPushButton("No está disponible") #Fechas
button11 = QPushButton("No está disponible") #Números
button12 = QPushButton("No está disponible") #¡Gran final!


# Functions

def note_calculating():
    a = 0
    for i in range(len(notes)):
        a += notes[i]
    note = round(a / len(notes), 2)

    stats.setText("v.1.1" + "\n"
        "Nota : " + str(note) + "\n"
        "Número de pruebas completadas : " + str(evaluations) + "\n"
        "Un juego de Gild56 // @gild56gmd")

def true_or_false(button_clicked):
    global true_answer_variable, true_answer, exercice
    click.play()
    ans_button1.hide()
    ans_button2.hide()
    ans_button3.hide()
    ans_button4.hide()
    nothing1.hide()
    stats.hide()
    true_answer.show()
    ok_button.show()
    if right_ans_button == button_clicked:
        top_of_screen.setText("Sí")
        si.play()
        notes.append(20)
        true_answer.setText("Bien!")

    else:
        top_of_screen.setText("No")
        no.play()
        notes.append(0)
        if true_answer_variable == 1 or true_answer_variable == 2:
            if true_answer_variable == 1:
                true_answer_variable = "Ser"
            else:
                true_answer_variable = "Estar"
        true_answer.setText("La repuesta es " + str(true_answer_variable) + ".")

    note_calculating()

def ok_button_clicked():
    global questions, exercice
    true_answer.hide()
    click.play()
    stats.show()
    nothing1.show()
    ok_button.hide()
    if questions == 4:
        finish_exercice()
        exrcice = None
        questions = 0

    else:
        questions += 1

        if exercice == 1:
            ex1()

        elif exercice == 2:
            ex2()

        elif exercice == 3:
            ex3()

        elif exercice == 4:
            ex4()

        elif exercice == 5:
            ex5()

        elif exercice == 6:
            ex6()

        elif exercice == 7:
            ex7()
    
def start_exercice():
    global exercice
    menu_music.stop()

    button01.hide()
    button02.hide()
    button03.hide()
    button04.hide()
    button05.hide()
    button06.hide()
    button07.hide()
    button08.hide()
    button09.hide()
    button10.hide()
    button11.hide()
    button12.hide()

    if exercice == 1 or exercice == 2 or exercice == 3 or exercice == 4 or exercice == 5 or exercice == 6:
        ans_button1.show()
        ans_button2.show()
        ans_button3.show()
        ans_button4.show()
        nothing2.show()

def finish_exercice():
    el_rio_fluye.stop()
    menu_music.play(-1)

    ans_button1.hide()
    ans_button2.hide()
    ans_button3.hide()
    ans_button4.hide()
    nothing2.hide()

    button01.show()
    button02.show()
    button03.show()
    button04.show()
    button05.show()
    button06.show()
    button07.show()
    button08.show()
    button09.show()
    button10.show()
    button11.show()
    button12.show()

    top_of_screen.setText("Niveles de Español")


# Answers modes

def four_answers_mode(question, ans1, ans2, ans3, ans4): # ans4 is true
    global shuffle, right_ans_button, true_answer_variable
    true_answer_variable = ans4
    top_of_screen.setText(question)
    order_of_answers = [1, 2, 3, 4]
    shuffle(order_of_answers)
    right_ans_button = None

    if order_of_answers[0] == 1:
        ans_button1.setText(ans1)
    elif order_of_answers[0] == 2:
        ans_button1.setText(ans2)
    elif order_of_answers[0] == 3:
        ans_button1.setText(ans3)        
    elif order_of_answers[0] == 4:
        ans_button1.setText(ans4)
        right_ans_button = 1

    if order_of_answers[1] == 1:
        ans_button2.setText(ans1)
    elif order_of_answers[1] == 2:
        ans_button2.setText(ans2)
    elif order_of_answers[1] == 3:
        ans_button2.setText(ans3)       
    elif order_of_answers[1] == 4:
        ans_button2.setText(ans4)
        right_ans_button = 2

    if order_of_answers[2] == 1:
        ans_button3.setText(ans1)
    elif order_of_answers[2] == 2:
        ans_button3.setText(ans2)
    elif order_of_answers[2] == 3:
        ans_button3.setText(ans3)      
    elif order_of_answers[2] == 4:
        ans_button3.setText(ans4)
        right_ans_button = 3

    if order_of_answers[3] == 1:
        ans_button4.setText(ans1)
    elif order_of_answers[3] == 2:
        ans_button4.setText(ans2)
    elif order_of_answers[3] == 3:
        ans_button4.setText(ans3)        
    elif order_of_answers[3] == 4:
        ans_button4.setText(ans4)
        right_ans_button = 4

def typing_answer_mode(question, true_ans):
    top_of_screen.setText(question)
    line.show()

    # Как сделать свободное печатание?


    #def one (pr, pra):
    #    print("¿Qué es " + pr + " en plural?")
    #    inp = input()
    #    if pra == inp:
    #        print("Sí!")
    #    else:
    #        print("No, la respuesta es " + pra + ".")
    #    print(" ")

def two_answers_mode(question, right_answer):
    global right_ans_button, true_answer_variable
    true_answer_variable = right_answer
    top_of_screen.setText(question)
    right_ans_button = right_answer
    ans_button1.setText("Ser")
    ans_button2.setText("Estar")
    ans_button1.show()
    ans_button2.show()


# Exercices

def ex1():
    global four_answers_mode, start_exercice, finish_exercice, exercice
    exercice = 1
    start_exercice()
    random_question = randint(1, 6)

    if questions == 0:
        enter_sound.play()
        el_rio_fluye.play(-1)

    if random_question == 1:
        random_question = randint(1,3)

        if random_question == 1:
            four_answers_mode("Vivir con yo.", "vives", "vivir", "vivimos", "vivo")

        elif random_question == 2:
            four_answers_mode("Hablar con yo.", "hablas", "hablar", "hablamos", "hablo")

        elif random_question == 3:
            four_answers_mode("Comer con yo.", "comas", "comer", "comemos", "como")

    elif random_question == 2:
        random_question = randint(1,3)

        if random_question == 1:
            four_answers_mode("Vivir con tú.", "vivo", "vivir", "vivimos", "vives")

        elif random_question == 2:
            four_answers_mode("Hablar con tú.", "hablo", "hablar", "hablamos", "hablas")

        elif random_question == 3:
            four_answers_mode("Comer con tú.", "como", "comer", "comemos", "comes")

    elif random_question == 3:
        random_question = randint(1,15)

        if random_question == 1:
            four_answers_mode("Vivir con él.", "vivo", "vivi", "vivimos", "vive")

        elif random_question == 2:
            four_answers_mode("Hablar con él.", "hablo", "hablar", "hablamos", "habla")

        elif random_question == 3:
            four_answers_mode("Comer con él.", "como", "comer", "comemos", "come")

        elif random_question == 4:
            four_answers_mode("Vivir con ella.", "vivo", "vivi", "vivimos", "vive")

        elif random_question == 5:
            four_answers_mode("Hablar con ella.", "hablo", "hablar", "hablamos", "habla")

        elif random_question == 6:
            four_answers_mode("Comer con ella.", "como", "comer", "comemos", "come")
            
        elif random_question == 7:
            four_answers_mode("Vivir con Juan.", "vivo", "vivi", "vivimos", "vive")

        elif random_question == 8:
            four_answers_mode("Hablar con Juan.", "hablo", "hablar", "hablamos", "habla")

        elif random_question == 9:
            four_answers_mode("Comer con Juan.", "como", "comer", "comemos", "come")

        elif random_question == 10:
            four_answers_mode("Vivir con Carla.", "vivo", "vivi", "vivimos", "vive")

        elif random_question == 11:
            four_answers_mode("Hablar con Carla.", "hablo", "hablar", "hablamos", "habla")
            
        elif random_question == 12:
            four_answers_mode("Comer con Carla.", "como", "comer", "comemos", "come")

        elif random_question == 13:
            four_answers_mode("Vivir con usted.", "vivo", "vivi", "vivimos", "vive")

        elif random_question == 14:
            four_answers_mode("Hablar con usted.", "hablo", "hablar", "hablamos", "habla")

        elif random_question == 15:
            four_answers_mode("Comer con usted.", "como", "comer", "comemos", "come")

    elif random_question == 4:
        random_question = randint(1,6)
    
        if random_question == 1:
            four_answers_mode("Vivir con nosotros.", "vivo", "vivir", "vives", "vivimos")

        elif random_question == 2:
            four_answers_mode("Hablar con nosotros.", "hablo", "hablar", "hablas", "hablamos")

        elif random_question == 3:
            four_answers_mode("Comer con nosotros.", "como", "comer", "comes", "comemos")

        elif random_question == 4:
            four_answers_mode("Vivir con nosotras.", "vivo", "vivir", "vives", "vivimos")

        elif random_question == 5:
            four_answers_mode("Hablar con nosotras.", "hablo", "hablar", "hablas", "hablamos")

        else:
            four_answers_mode("Comer con nosotras.", "como", "comer", "comes", "comemos")

    elif random_question == 5:
        random_question = randint(1,6)

        if random_question == 1:
            four_answers_mode("Vivir con vosotros.", "vivo", "vivir", "vives", "vivís")

        elif random_question == 2:
            four_answers_mode("Hablar con vosotros.", "hablo", "hablar", "hablas", "habláis")

        elif random_question == 3:
            four_answers_mode("Comer con vosotros.", "como", "comer", "comes", "coméis")

        elif random_question == 1:
            four_answers_mode("Vivir con vosotras.", "vivo", "vivir", "vives", "vivís")

        elif random_question == 2:
            four_answers_mode("Hablar con vosotras.", "hablo", "hablar", "hablas", "habláis")

        else:
            four_answers_mode("Comer con vosotras.", "como", "comer", "comes", "coméis")

    else:
        random_question = randint(1,12)

        if random_question == 1:
            four_answers_mode("Vivir con ellos.", "vivo", "vivimos", "vives", "viven")

        elif random_question == 2:
            four_answers_mode("Hablar con ellos.", "hablo", "hablamos", "hablas", "hablan")

        elif random_question == 3:
            four_answers_mode("Comer con ellos.", "como", "comemos", "comes", "comen")

        elif random_question == 4:
            four_answers_mode("Vivir con ellas.", "vivo", "vivimos", "vives", "viven")

        elif random_question == 5:
            four_answers_mode("Hablar con ellas.", "hablo", "hablamos", "hablas", "hablan")        
            
        elif random_question == 6:
            four_answers_mode("Comer con ellas.", "como", "comemos", "comes", "comen")

        elif random_question == 7:
            four_answers_mode("Vivir con Carla y Juan.", "vivo", "vivimos", "vives", "viven")

        elif random_question == 8:
            four_answers_mode("Hablar con Carla y Juan.", "hablo", "hablamos", "hablas", "hablan")

        elif random_question == 9:
            four_answers_mode("Comer con Carla y Juan.", "como", "comemos", "comes", "comen")

        elif random_question == 10:
            four_answers_mode("Vivir con ustedes.", "vivo", "vivimos", "vives", "viven")

        elif random_question == 11:
            four_answers_mode("Hablar con ustedes.", "hablo", "hablamos", "hablas", "hablan")        
            
        elif random_question == 12:
            four_answers_mode("Comer con ustedes.", "como", "comemos", "comes", "comen")

def ex2():
    global four_answers_mode, start_exercice, finish_exercice, exercice
    exercice = 2
    start_exercice()
    random_question = randint(1, 6)

    if questions == 0:
        enter_sound.play()
        el_rio_fluye.play(-1)

    if random_question == 1:
        random_question = randint(1,3)

        if random_question == 1:
            four_answers_mode("Tener con yo.", "tiene", "tener", "tenemos", "tengo")

        elif random_question == 2:
            four_answers_mode("Ser con yo.", "es", "ser", "somos", "soy")

        elif random_question == 3:
            four_answers_mode("Ir con yo.", "va", "ir", "vamos", "voy")

    elif random_question == 2:
        random_question = randint(1,3)

        if random_question == 1:
            four_answers_mode("Tener con yo.", "tiene", "tener", "tenemos", "tengo")

        elif random_question == 2:
            four_answers_mode("Ser con yo.", "es", "ser", "somos", "soy")

        elif random_question == 3:
            four_answers_mode("Ir con yo.", "va", "ir", "vamos", "voy")

    elif random_question == 3:
        random_question = randint(1,15)

        if random_question == 1:
            four_answers_mode("Tener con él.", "tengo", "tener", "tenemos", "tiene")

        elif random_question == 2:
            four_answers_mode("Ser con él.", "soy", "ser", "somos", "es")

        elif random_question == 3:
            four_answers_mode("Ir con él.", "voy", "ir", "vamos", "va")

        elif random_question == 4:
            four_answers_mode("Tener con ella.", "tengo", "tener", "tenemos", "tiene")

        elif random_question == 5:
            four_answers_mode("Ser con ella.", "soy", "ser", "somos", "es")

        elif random_question == 6:
            four_answers_mode("Ir con ella.", "voy", "ir", "vamos", "va")
            
        elif random_question == 7:
            four_answers_mode("Tener con Juan.", "tengo", "tener", "tenemos", "tiene")

        elif random_question == 8:
            four_answers_mode("Ser con Juan.", "soy", "ser", "somos", "es")

        elif random_question == 9:
            four_answers_mode("Ir con Juan.", "voy", "ir", "vamos", "va")

        elif random_question == 10:
            four_answers_mode("Tener con Carla.", "tengo", "tener", "tenemos", "tiene")

        elif random_question == 11:
            four_answers_mode("Ser con Carla.", "soy", "ser", "somos", "es")
            
        elif random_question == 12:
            four_answers_mode("Ir con Carla.", "voy", "ir", "vamos", "va")

        elif random_question == 13:
            four_answers_mode("Tener con usted.", "tengo", "tener", "tenemos", "tiene")

        elif random_question == 14:
            four_answers_mode("Ser con usted.", "soy", "ser", "somos", "es")

        elif random_question == 15:
            four_answers_mode("Ir con usted.", "voy", "ir", "vamos", "va")

    elif random_question == 4:
        random_question = randint(1,6)
    
        if random_question == 1:
            four_answers_mode("Tener con nosotros.", "tengo", "tener", "tienes", "tenemos")

        elif random_question == 2:
            four_answers_mode("Ser con nosotros.", "soy", "ser", "eres", "somos")

        elif random_question == 3:
            four_answers_mode("Ir con nosotros.", "voy", "ir", "vas", "vamos")

        elif random_question == 4:
            four_answers_mode("Tener con nosotras.", "tengo", "tener", "tienes", "tenemos")

        elif random_question == 5:
            four_answers_mode("Ser con nosotras.", "soy", "ser", "eres", "somos")

        else:
            four_answers_mode("Ir con nosotras.", "voy", "ir", "vas", "vamos")

    elif random_question == 5:
        random_question = randint(1,6)

        if random_question == 1:
            four_answers_mode("Tener con vosotros.", "tengo", "tener", "tienes", "teneis")

        elif random_question == 2:
            four_answers_mode("Ser con vosotros.", "soy", "ser", "eres", "sois")

        elif random_question == 3:
            four_answers_mode("Ir con vosotros.", "voy", "ir", "vas", "vais")

        elif random_question == 1:
            four_answers_mode("Tener con vosotras.", "tengo", "tener", "tienes", "teneis")

        elif random_question == 2:
            four_answers_mode("Ser con vosotras.", "soy", "ser", "eres", "sois")

        else:
            four_answers_mode("Ir con vosotras.", "voy", "ir", "vas", "vais")

    else:
        random_question = randint(1,12)

        if random_question == 1:
            four_answers_mode("Tener con ellos.", "tengo", "tener", "tienes", "tienen")

        elif random_question == 2:
            four_answers_mode("Ser con ellos.", "soy", "ser", "eres", "son")

        elif random_question == 3:
            four_answers_mode("Ir con ellos.", "voy", "ir", "vas", "van")

        elif random_question == 4:
            four_answers_mode("Tener con ellas.", "tengo", "tener", "tienes", "tienen")

        elif random_question == 5:
            four_answers_mode("Ser con ellas.", "soy", "ser", "eres", "son")        
            
        elif random_question == 6:
            four_answers_mode("Ir con ellas.", "voy", "ir", "vas", "van")

        elif random_question == 7:
            four_answers_mode("Tener con Carla y Juan.", "tengo", "tener", "tienes", "tienen")

        elif random_question == 8:
            four_answers_mode("Ser con Carla y Juan.", "soy", "ser", "eres", "son")

        elif random_question == 9:
            four_answers_mode("Ir con Carla y Juan.", "voy", "ir", "vas", "van")

        elif random_question == 10:
            four_answers_mode("Tener con ustedes.", "tengo", "tener", "tienes", "tienen")

        elif random_question == 11:
            four_answers_mode("Ser con ustedes.", "soy", "ser", "eres", "son")        
            
        elif random_question == 12:
            four_answers_mode("Ir con ustedes.", "voy", "ir", "vas", "van")
 
def ex3():
    global four_answers_mode, start_exercice, finish_exercice, exercice
    exercice = 3
    start_exercice()
    random_question = randint(1, 6)

    if questions == 0:
        enter_sound.play()
        el_rio_fluye.play(-1)

    if random_question == 1:
        random_question = randint(1,3)

        if random_question == 1:
            four_answers_mode("Dormirse con yo.", "te duermes", "se duerme", "nos dormemos", "me duermo")

        elif random_question == 2:
            four_answers_mode("Llamarse con yo.", "te llamas", "se llama", "nos llamamos", "me llamo")

        elif random_question == 3:
            four_answers_mode("Levantarse con yo.", "te levantas", "se levanta", "nos levantamos", "me levantamo")

    elif random_question == 2:
        random_question = randint(1,3)

        if random_question == 1:
            four_answers_mode("Dormirse con tú.", "se duerme", "nos dormemos", "me duermo", "te duermes")

        elif random_question == 2:
            four_answers_mode("Llamarse con tú.", "se llama", "nos llamamos", "me llamo", "te llamas")

        elif random_question == 3:
            four_answers_mode("Levantarse con tú.", "se levanta", "nos levantamos", "me levantamo", "te levantas")

    elif random_question == 3:
        random_question = randint(1,15)

        if random_question == 1:
            four_answers_mode("Dormirse con él.", "te duermes", "nos dormemos", "me duermo", "se duerme")

        elif random_question == 2:
            four_answers_mode("Llamarse con él.", "te llamas", "nos llamamos", "me llamo", "se llama")

        elif random_question == 3:
            four_answers_mode("Levantarse con él.", "te levantas", "nos levantamos", "me levantamo", "se levanta")

        elif random_question == 4:
            four_answers_mode("Dormirse con ella.", "te duermes", "nos dormemos", "me duermo", "se duerme")

        elif random_question == 5:
            four_answers_mode("Llamarse con ella.", "te llamas", "nos llamamos", "me llamo", "se llama")

        elif random_question == 6:
            four_answers_mode("Levantarse con ella.", "te levantas", "nos levantamos", "me levantamo", "se levanta")
            
        elif random_question == 7:
            four_answers_mode("Dormirse con Juan.", "te duermes", "nos dormemos", "me duermo", "se duerme")

        elif random_question == 8:
            four_answers_mode("Llamarse con Juan.", "te llamas", "nos llamamos", "me llamo", "se llama")

        elif random_question == 9:
            four_answers_mode("Levantarse con Juan.", "te levantas", "nos levantamos", "me levantamo", "se levanta")

        elif random_question == 10:
            four_answers_mode("Dormirse con Carla.", "te duermes", "nos dormemos", "me duermo", "se duerme")

        elif random_question == 11:
            four_answers_mode("Llamarse con Carla.", "te llamas", "nos llamamos", "me llamo", "se llama")
            
        elif random_question == 12:
            four_answers_mode("Levantarse con Carla.", "te levantas", "nos levantamos", "me levantamo", "se levanta")

        elif random_question == 13:
            four_answers_mode("Dormirse con usted.", "te duermes", "nos dormemos", "me duermo", "se duerme")

        elif random_question == 14:
            four_answers_mode("Llamarse con usted.", "te llamas", "nos llamamos", "me llamo", "se llama")

        elif random_question == 15:
            four_answers_mode("Levantarse con usted.", "te levantas", "nos levantamos", "me levantamo", "se levanta")

    elif random_question == 4:
        random_question = randint(1,6)
    
        if random_question == 1:
            four_answers_mode("Dormirse con nosotros.", "te duermes", "se duerme", "me duermo", "nos dormemos")

        elif random_question == 2:
            four_answers_mode("Llamarse con nosotros.", "te llamas", "se llama", "me llamo", "nos llamamos")

        elif random_question == 3:
            four_answers_mode("Levantarse con nosotros.", "te levantas", "se levanta", "me levantamo", "nos levantamos")

        elif random_question == 4:
            four_answers_mode("Dormirse con nosotras.", "te duermes", "se duerme", "me duermo", "nos dormemos")

        elif random_question == 5:
            four_answers_mode("Llamarse con nosotras.", "te llamas", "se llama", "me llamo", "nos llamamos")

        else:
            four_answers_mode("Levantarse con nosotras.", "te levantas", "se levanta", "me levantamo", "nos levantamos")

    elif random_question == 5:
        random_question = randint(1,6)

        if random_question == 1:
            four_answers_mode("Dormirse con vosotros.", "te duermes", "se duerme", "nos dormemos", "os dormís")

        elif random_question == 2:
            four_answers_mode("Llamarse con vosotros.", "te llamas", "se llama", "nos llamamos", "os llamáis")

        elif random_question == 3:
            four_answers_mode("Levantarse con vosotros.", "te levantas", "se levanta", "nos levantamos", "os levantáis")

        elif random_question == 1:
            four_answers_mode("Dormirse con vosotras.", "te duermes", "se duerme", "nos dormemos", "os dormís")

        elif random_question == 2:
            four_answers_mode("Llamarse con vosotras.", "te llamas", "se llama", "nos llamamos", "os llamáis")

        else:
            four_answers_mode("Levantarse con vosotras.", "te levantas", "se levanta", "nos levantamos", "os levantáis")

    else:
        random_question = randint(1,12)

        if random_question == 1:
            four_answers_mode("Dormirse con ellos.", "te duermes", "se duerme", "nos dormemos", "se duermen")

        elif random_question == 2:
            four_answers_mode("Llamarse con ellos.", "te llamas", "se llama", "nos llamamos", "se llaman")

        elif random_question == 3:
            four_answers_mode("Levantarse con ellos.", "te levantas", "se levanta", "nos levantamos", "se levantaman")

        elif random_question == 4:
            four_answers_mode("Dormirse con ellas.", "te duermes", "se duerme", "nos dormemos", "se duermen")

        elif random_question == 5:
            four_answers_mode("Llamarse con ellas.", "te llamas", "se llama", "nos llamamos", "se llaman")        
            
        elif random_question == 6:
            four_answers_mode("Levantarse con ellas.", "te levantas", "se levanta", "nos levantamos", "se levantaman")

        elif random_question == 7:
            four_answers_mode("Dormirse con Carla y Juan.", "te duermes", "se duerme", "nos dormemos", "se duermen")

        elif random_question == 8:
            four_answers_mode("Llamarse con Carla y Juan.", "te llamas", "se llama", "nos llamamos", "se llaman")

        elif random_question == 9:
            four_answers_mode("Levantarse con Carla y Juan.", "te levantas", "se levanta", "nos levantamos", "se levantaman")

        elif random_question == 10:
            four_answers_mode("Dormirse con ustedes.", "te duermes", "se duerme", "nos dormemos", "se duermen")

        elif random_question == 11:
            four_answers_mode("Llamarse con ustedes.", "te llamas", "se llama", "nos llamamos", "se llaman")        
            
        elif random_question == 12:
            four_answers_mode("Levantarse con ustedes.", "te levantas", "se levanta", "nos levantamos", "se levantaman")
 
def ex4():  # Not finished
    global four_answers_mode, start_exercice, finish_exercice, exercice
    exercice = 4
    start_exercice()
    random_question = randint(1, 6)

    if questions == 0:
        enter_sound.play()
        el_rio_fluye.play(-1)

    if random_question == 1:
        random_question = randint(1,3)

        if random_question == 1:
            four_answers_mode("Poder con yo.", "podo", "puedes", "podoy", "puedo")

        elif random_question == 2:
            four_answers_mode("Pensar con yo.", "penso", "piensas", "pensoy", "pienso")

        elif random_question == 3:
            four_answers_mode("Jugar con yo.", "jugo", "juegas", "jugoy", "juego")

    elif random_question == 2:
        random_question = randint(1,3)

        if random_question == 1:
            four_answers_mode("Poder con tú.", "podes", "podoy", "puedo", "puedes")

        elif random_question == 2:
            four_answers_mode("Pensar con tú.", "pensas", "pensoy", "pienso", "piensas")

        elif random_question == 3:
            four_answers_mode("Jugar con tú.", "jugas", "jugoy", "juego", "juegas")

    elif random_question == 3:
        random_question = randint(1,15)

        if random_question == 1:
            four_answers_mode("Vivir con él.", "vivo", "vivi", "vivimos", "vive")

        elif random_question == 2:
            four_answers_mode("Hablar con él.", "hablo", "hablar", "hablamos", "habla")

        elif random_question == 3:
            four_answers_mode("Comer con él.", "como", "comer", "comemos", "come")

        elif random_question == 4:
            four_answers_mode("Vivir con ella.", "vivo", "vivi", "vivimos", "vive")

        elif random_question == 5:
            four_answers_mode("Hablar con ella.", "hablo", "hablar", "hablamos", "habla")

        elif random_question == 6:
            four_answers_mode("Comer con ella.", "como", "comer", "comemos", "come")
            
        elif random_question == 7:
            four_answers_mode("Vivir con Juan.", "vivo", "vivi", "vivimos", "vive")

        elif random_question == 8:
            four_answers_mode("Hablar con Juan.", "hablo", "hablar", "hablamos", "habla")

        elif random_question == 9:
            four_answers_mode("Comer con Juan.", "como", "comer", "comemos", "come")

        elif random_question == 10:
            four_answers_mode("Vivir con Carla.", "vivo", "vivi", "vivimos", "vive")

        elif random_question == 11:
            four_answers_mode("Hablar con Carla.", "hablo", "hablar", "hablamos", "habla")
            
        elif random_question == 12:
            four_answers_mode("Comer con Carla.", "como", "comer", "comemos", "come")

        elif random_question == 13:
            four_answers_mode("Vivir con usted.", "vivo", "vivi", "vivimos", "vive")

        elif random_question == 14:
            four_answers_mode("Hablar con usted.", "hablo", "hablar", "hablamos", "habla")

        elif random_question == 15:
            four_answers_mode("Comer con usted.", "como", "comer", "comemos", "come")

    elif random_question == 4:
        random_question = randint(1,6)
    
        if random_question == 1:
            four_answers_mode("Vivir con nosotros.", "vivo", "vivir", "vives", "vivimos")

        elif random_question == 2:
            four_answers_mode("Hablar con nosotros.", "hablo", "hablar", "hablas", "hablamos")

        elif random_question == 3:
            four_answers_mode("Comer con nosotros.", "como", "comer", "comes", "comemos")

        elif random_question == 4:
            four_answers_mode("Vivir con nosotras.", "vivo", "vivir", "vives", "vivimos")

        elif random_question == 5:
            four_answers_mode("Hablar con nosotras.", "hablo", "hablar", "hablas", "hablamos")

        else:
            four_answers_mode("Comer con nosotras.", "como", "comer", "comes", "comemos")

    elif random_question == 5:
        random_question = randint(1,6)

        if random_question == 1:
            four_answers_mode("Vivir con vosotros.", "vivo", "vivir", "vives", "vivís")

        elif random_question == 2:
            four_answers_mode("Hablar con vosotros.", "hablo", "hablar", "hablas", "habláis")

        elif random_question == 3:
            four_answers_mode("Comer con vosotros.", "como", "comer", "comes", "coméis")

        elif random_question == 1:
            four_answers_mode("Vivir con vosotras.", "vivo", "vivir", "vives", "vivís")

        elif random_question == 2:
            four_answers_mode("Hablar con vosotras.", "hablo", "hablar", "hablas", "habláis")

        else:
            four_answers_mode("Comer con vosotras.", "como", "comer", "comes", "coméis")

    else:
        random_question = randint(1,12)

        if random_question == 1:
            four_answers_mode("Vivir con ellos.", "vivo", "vivimos", "vives", "viven")

        elif random_question == 2:
            four_answers_mode("Hablar con ellos.", "hablo", "hablamos", "hablas", "hablan")

        elif random_question == 3:
            four_answers_mode("Comer con ellos.", "como", "comemos", "comes", "comen")

        elif random_question == 4:
            four_answers_mode("Vivir con ellas.", "vivo", "vivimos", "vives", "viven")

        elif random_question == 5:
            four_answers_mode("Hablar con ellas.", "hablo", "hablamos", "hablas", "hablan")        
            
        elif random_question == 6:
            four_answers_mode("Comer con ellas.", "como", "comemos", "comes", "comen")

        elif random_question == 7:
            four_answers_mode("Vivir con Carla y Juan.", "vivo", "vivimos", "vives", "viven")

        elif random_question == 8:
            four_answers_mode("Hablar con Carla y Juan.", "hablo", "hablamos", "hablas", "hablan")

        elif random_question == 9:
            four_answers_mode("Comer con Carla y Juan.", "como", "comemos", "comes", "comen")

        elif random_question == 10:
            four_answers_mode("Vivir con ustedes.", "vivo", "vivimos", "vives", "viven")

        elif random_question == 11:
            four_answers_mode("Hablar con ustedes.", "hablo", "hablamos", "hablas", "hablan")        
            
        elif random_question == 12:
            four_answers_mode("Comer con ustedes.", "como", "comemos", "comes", "comen")
 
def ex5():  # Not finished
    pass
 
def ex6():  # Not finished
    pass
 
def ex7():
    global two_answers_mode, start_exercice, finish_exercice, exercice
    exercice = 7
    start_exercice()
    random_question = randint(1, 20)

    if questions == 0:
        enter_sound.play()
        el_rio_fluye.play(-1)

    if random_question == 1:
        two_answers_mode("¿Cómo ... tú?", 2)

    elif random_question == 2:
        two_answers_mode("¡Yo ... superbién!", 2)

    elif random_question == 3:
        two_answers_mode("¿Dónde ... el estadio Bernabéu?", 2)

    elif random_question == 4:
        two_answers_mode("El estadio Bernabéu ... en Madrid.", 2)

    elif random_question == 5:
        two_answers_mode("Yo ... feliz hoy.", 2)

    elif random_question == 6:
        two_answers_mode("El café ... visitado.", 2)

    elif random_question == 7:
        two_answers_mode("... cansado después de correr.", 2)

    elif random_question == 8:
        two_answers_mode("Nosotros ... en casa.", 2)

    elif random_question == 9:
        two_answers_mode("Pedro ... profesor.", 2)

    elif random_question == 10:
        two_answers_mode("María ... enferma hoy.", 2)


    elif random_question == 11:
        two_answers_mode("¿De dónde ... tú?", 1)

    elif random_question == 12:
        two_answers_mode("Yo ... de españa", 1)

    elif random_question == 13:
        two_answers_mode("¿De qué nacionalidad ... tú?", 1)

    elif random_question == 14:
        two_answers_mode("Yo ... de nacionalidad española.", 1)

    elif random_question == 15:
        two_answers_mode("... mi mejor amigo.", 1)

    elif random_question == 16:
        two_answers_mode("... un día soleado.", 1)

    elif random_question == 17:
        two_answers_mode("La fiesta ... en casa de Ana.", 1)

    elif random_question == 18:
        two_answers_mode("Madrid ... la capital de España.", 1)

    elif random_question == 19:
        two_answers_mode("Pedro ... profesor.", 1)

    elif random_question == 20:
        two_answers_mode("... las 3 de la tarde. ", 1)
 
def ex8():  # Not finished
    pass
 
def ex9():  # Not finished
    pass
 
def ex10(): # Not finished
    pass

def ex11(): # Not finished
    pass

def ex12(): # Not finished
    pass


# 4 answer buttons

def ans_button1_clicked():
    global true_or_false
    true_or_false(1)

def ans_button2_clicked():
    global true_or_false
    true_or_false(2)

def ans_button3_clicked():
    global true_or_false
    true_or_false(3)

def ans_button4_clicked():
    global true_or_false
    true_or_false(4)


# When button was clicked

button01.clicked.connect(ex1)
button02.clicked.connect(ex2)
button03.clicked.connect(ex3)
button04.clicked.connect(ex4)
button05.clicked.connect(ex5)
button06.clicked.connect(ex6)
button07.clicked.connect(ex7)
button08.clicked.connect(ex8)
button09.clicked.connect(ex9)
button10.clicked.connect(ex10)
button11.clicked.connect(ex11)
button12.clicked.connect(ex12)

ok_button.clicked.connect(ok_button_clicked)

ans_button1.clicked.connect(ans_button1_clicked)
ans_button2.clicked.connect(ans_button2_clicked)
ans_button3.clicked.connect(ans_button3_clicked)
ans_button4.clicked.connect(ans_button4_clicked)


# Buttons parameters

button01.setFont(QFont("Arial", 10))
button02.setFont(QFont("Arial", 10))
button03.setFont(QFont("Arial", 10))
button04.setFont(QFont("Arial", 10))
button05.setFont(QFont("Arial", 10))
button06.setFont(QFont("Arial", 10))
button07.setFont(QFont("Arial", 10))
button08.setFont(QFont("Arial", 10))
button09.setFont(QFont("Arial", 10))
button10.setFont(QFont("Arial", 10))
button11.setFont(QFont("Arial", 10))
button12.setFont(QFont("Arial", 10))

true_answer.setFont(QFont("Arial", 10))

button01.setFixedSize(165, 80)
button02.setFixedSize(165, 80)
button03.setFixedSize(165, 80)
button04.setFixedSize(165, 80)
button05.setFixedSize(165, 80)
button06.setFixedSize(165, 80)
button07.setFixedSize(165, 80)
button08.setFixedSize(165, 80)
button09.setFixedSize(165, 80)
button10.setFixedSize(165, 80)
button11.setFixedSize(165, 80)
button12.setFixedSize(165, 80)

ans_button1.setFixedSize(165, 80)
ans_button2.setFixedSize(165, 80)
ans_button3.setFixedSize(165, 80)
ans_button4.setFixedSize(165, 80)

ok_button.setFixedSize(165, 80)


# Adding to layouts

layout1.addWidget(button01,  alignment = Qt.AlignCenter)
layout1.addWidget(button02,  alignment = Qt.AlignCenter)
layout1.addWidget(button03,  alignment = Qt.AlignCenter)
layout1.addWidget(button04,  alignment = Qt.AlignCenter)

layout2.addWidget(button05,  alignment = Qt.AlignCenter)
layout2.addWidget(button06,  alignment = Qt.AlignCenter)
layout2.addWidget(button07,  alignment = Qt.AlignCenter)
layout2.addWidget(button08,  alignment = Qt.AlignCenter)

layout3.addWidget(button09,  alignment = Qt.AlignCenter)
layout3.addWidget(button10, alignment = Qt.AlignCenter)
layout3.addWidget(button11, alignment = Qt.AlignCenter)
layout3.addWidget(button12, alignment = Qt.AlignCenter)

layout2.addWidget(ok_button,  alignment = Qt.AlignCenter)
layout1.addWidget(true_answer,  alignment = Qt.AlignCenter)

ans_layout1.addWidget(ans_button1, alignment = Qt.AlignCenter)
ans_layout1.addWidget(ans_button2, alignment = Qt.AlignCenter)
ans_layout2.addWidget(ans_button3, alignment = Qt.AlignCenter)
ans_layout2.addWidget(ans_button4, alignment = Qt.AlignCenter)

ans_layout2.addWidget(line, alignment = Qt.AlignCenter)

stats_layout.addWidget(nothing1, alignment = Qt.AlignCenter)
stats_layout.addWidget(top_of_screen, alignment = Qt.AlignCenter)
stats_layout.addWidget(stats, alignment = Qt.AlignCenter)

nothing_layout.addWidget(nothing2, alignment = Qt.AlignCenter)


# Connecting layouts

main_layout.addLayout(stats_layout)
main_layout.addLayout(nothing_layout)
main_layout.addLayout(ans_layout1)
main_layout.addLayout(ans_layout2)
main_layout.addLayout(layout1)
main_layout.addLayout(layout2)
main_layout.addLayout(layout3)

main_win.setLayout(main_layout)
main_win.setLayout
main_win.show()

if not_yet_variable == True:
    window2.show()
else:
    window2.hide()

app.exec()