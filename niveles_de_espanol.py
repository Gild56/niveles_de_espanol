
# Connecting bibliotechs

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

app = QApplication(sys.argv)
main_win = QWidget()
main_win.setFixedSize(700, 500)
main_win.setMaximumSize(10000, 10000)
main_win.setWindowIcon(QIcon(resource_path("logo.ico")))

main_win.show()


# Music & SFX

menu_music = pygame.mixer.Sound(resource_path("bossabossa.mp3"))
enter_sound = pygame.mixer.Sound(resource_path("click.wav"))
click = pygame.mixer.Sound(resource_path("8bitclick.wav"))
no = pygame.mixer.Sound(resource_path("no.mp3"))
si = pygame.mixer.Sound(resource_path("si.mp3"))
el_rio_fluye = pygame.mixer.Sound(resource_path("el_rio_fluye.mp3"))
test_music = pygame.mixer.Sound(resource_path("test.mp3"))
lesson_music = pygame.mixer.Sound(resource_path("everyday_heroes.mp3"))

el_rio_fluye.set_volume(0.3)

menu_music.play(-1)


# Layouts

main_layout = QVBoxLayout()

stats_layout = QHBoxLayout()
true_answer_layout= QHBoxLayout()
nothing_layout = QHBoxLayout()
ans_layout1 = QHBoxLayout() # top
ans_layout2 = QHBoxLayout() # bottom
layout1 = QHBoxLayout() # top
layout2 = QHBoxLayout() # middle
layout3 = QHBoxLayout() # bottom


# Variables

test_finished = False
test_note = 0
test_notes = []
test = False
test_questions = 0
tests = 0
lessons_mode = True
note = 20
notes = []
right_ans_button = None
exercice = None
questions = 0
true_answer_variable = ""


# QLabels

nothing1 = QLabel("")
nothing2 = QLabel("")
nothing3 = QLabel("")
nothing4 = QLabel("                                          ")
true_answer = QLabel("")
top_of_screen = QLabel("Niveles de Español")
stats = QLabel("v.1.2" + "\n"
    "Nota : -" + "\n"
    "Un juego @gild56gmd" + "\n"
    "Por Mme Auregan <3")

stats.setFont(QFont("Arial", 7))
top_of_screen.setFont(QFont("Impact", 17))
true_answer.setTextInteractionFlags(Qt.TextSelectableByMouse)
stats.setTextInteractionFlags(Qt.TextSelectableByMouse)
true_answer.setFont(QFont("Arial", 15))
nothing2.setFont(QFont("Arial", 15))
nothing1.hide()
nothing2.hide()
nothing3.hide()
nothing4.hide()
true_answer.hide()


# Buttons and line

line = QLineEdit()

ans_button1 = QPushButton("")   #top left button
ans_button2 = QPushButton("")   #top right button
ans_button3 = QPushButton("")   #bottom left button
ans_button4 = QPushButton("")   #bottom right button

lessons_button = QPushButton("Lecciónes")
ok_button = QPushButton("OK")
send_answer_button = QPushButton("OK")
quit_button = QPushButton("<--")

ans_button1.hide()
ans_button2.hide()
ans_button3.hide()
ans_button4.hide()
ok_button.hide()
send_answer_button.hide()
line.hide()
quit_button.hide()

button01 = QPushButton("Verbos normales")
button02 = QPushButton("Verbos irregulares")
button03 = QPushButton("Verbos pronominales")
button04 = QPushButton("Verbos en diptongo")
button05 = QPushButton("Verbos debilitantes")
button06 = QPushButton("Verbos imperatovos")
button07 = QPushButton("Ser o Estar")
button08 = QPushButton("Números")
button09 = QPushButton("Países")
button10 = QPushButton("Plural de los palabras")
button11 = QPushButton("Fechas")
button12 = QPushButton("¡Gran final!")


# Functions

def lessons_button_clicked():
    global lessons_mode
    if lessons_mode:
        lessons_mode = False
        button01.setText("Un lección \n que habla de \n los verbos \n normales")
        button02.setText("Un lección \n que habla de \n los verbos \n irregulares")
        button03.setText("Un lección \n que habla de \n los verbos \n pronominales")
        button04.setText("Un lección \n que habla de \n los verbos \n en diptongo")
        button05.setText("Un lección \n que habla de \n los verbos \n debilitantes")
        button06.setText("Un lección \n que habla de \n los verbos \n imperatovos")
        button07.setText("Un lección \n que habla de \n la differencia \n entre ser y estar")
        button08.setText("Un lección \n que habla de \n los números")
        button09.setText("Un lección \n que habla de \n los países")
        button10.setText("Un lección \n que habla del \n plural de \n los palabras")
        button11.setText("Un lección \n que habla de \n las fechas")
        button12.hide()
        nothing4.show()
        lessons_button.setText("Ejercicios")
    else:
        lessons_mode = True
        button01.setText("Verbos normales")
        button02.setText("Verbos irregulares")
        button03.setText("Verbos pronominales")
        button04.setText("Verbos en diptongo")
        button05.setText("Verbos debilitantes")
        button06.setText("Verbos imperatovos")
        button07.setText("Ser o Estar")
        button08.setText("Números")
        button09.setText("Países")
        button10.setText("Plural de los palabras")
        button11.setText("Fechas")
        button12.show()
        nothing4.hide()
        lessons_button.setText("Lecciónes")

def lesson(lesson="Nada"):
    menu_music.stop()
    lesson_music.play(-1)
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
    lessons_button.hide()
    quit_button.show()
    true_answer.show()
    true_answer.setText(lesson)

def note_calculating():
    global test, notes, test_notes, test_note
    all_notes = 0
    if not test:
        for i in range(len(notes)):
            all_notes += notes[i]
        note = round(all_notes / len(notes), 2)

        stats.setText("v.1.2" + "\n"
            "Nota : " + str(note) + "\n"
            "Un juego de @gild56gmd" + "\n"
            "Por Mme Auregan <3")

    if test == True:
        for i in range(len(test_notes)):
            all_notes += test_notes[i]
        test_note = round(all_notes / len(test_notes), 2)

def true_or_false(button_clicked=None):
    global true_answer_variable, true_answer, exercice, test, test_notes
    click.play()
    ans_button1.hide()
    ans_button2.hide()
    ans_button3.hide()
    ans_button4.hide()
    send_answer_button.hide()
    line.hide()
    if not test:
        nothing1.hide()
    stats.hide()
    true_answer.show()
    nothing2.show()
    nothing3.show()
    ok_button.show()
    answer = line.text()
    answer = answer.lower()
    if exercice < 8:
        if right_ans_button == button_clicked:
            top_of_screen.setText("Sí")
            si.play()
            if not test:
                notes.append(20)
            else:
                test_notes.append(20)
            true_answer.setText("Bien!")
            wrong_answer = False
            true_answer.setText("")

        else:
            wrong_answer = True
            top_of_screen.setText("No")
            no.play()
            if not test:
                notes.append(0)
            else:
                test_notes.append(0)
            if true_answer_variable == 1 or true_answer_variable == 2:
                if true_answer_variable == 1:
                    true_answer_variable = "Ser"
                else:
                    true_answer_variable = "Estar"
            true_answer.setText("La repuesta es " + str(true_answer_variable) + ".")

    elif true_answer_variable == answer:
        top_of_screen.setText("Sí")
        si.play()
        if not test:
            notes.append(20)
        else:
            test_notes.append(20)
        true_answer.setText("Bien!")
        wrong_answer = False

    else:
        wrong_answer = True
        top_of_screen.setText("No")
        no.play()
        if not test:
            notes.append(0)
        else:
            test_notes.append(0)
        true_answer.setText("La repuesta es " + str(true_answer_variable) + ".")

    if wrong_answer:
        random_text = randint(1, 10)

        if random_text == 1:
            nothing2.setText("¡Qué lástima!")

        elif random_text == 2:
            nothing2.setText("¡Tendrás suerte la próxima vez!")

        elif random_text == 3:
            nothing2.setText("¡Incorrecto! ¡Inténtalo de nuevo!")

        elif random_text == 4:
            nothing2.setText("¡No presiones al azar por favor...")

        elif random_text == 5:
            nothing2.setText("¡Vaya! Eso no fue lo que esperaba.")

        elif random_text == 6:
            nothing2.setText("¡Ups! Parece que eso no fue lo correcto.")

        elif random_text == 7:
            nothing2.setText("¡Sigue intentando!")

        elif random_text == 8:
            nothing2.setText("¡Casi lo tienes!")

        elif random_text == 9:
            nothing2.setText("¡Eso estuvo cerca!")

        else:
            nothing2.setText("¡Ánimo! ¡La próxima vez será mejor!")

    line.clear()
    note_calculating()

def ok_button_clicked():
    global questions, exercice, test, test_questions, test_note, test_finished
    if test_finished:
        finish_exercice()
    else:
        click.play()
        stats.show()
        ok_button.hide()
        nothing2.hide()
        nothing3.hide()
        if exercice > 7 and not test:
            line.show()
            send_answer_button.show()

        if not test:
            if questions == 0:
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
            
            elif exercice == 8:
                ex8()
                
            elif exercice == 9:
                ex9()
                
            elif exercice == 10:
                ex10()
                
            elif exercice == 11:
                ex11()

        else:
            test_questions += 1
            if test_questions == 10:
                test = False
                questions = 0
                nothing2.hide()
                true_answer.hide()
                line.hide()
                quit_button.hide()
                nothing3.hide()
                stats.hide()
                nothing1.hide()
                ok_button.show()
                test_finished = True
                top_of_screen.setText("La nota de esta evaluación es " + str(test_note))
                print("La nota de esta evaluación es " + str(test_note))

            else:
                ex12()
    
def finish_exercice():
    global exercice, test_questions, questions, lessons_mode
    questions = 0
    test_questions = 0
    click.play()
    exercice = 0
    el_rio_fluye.stop()
    lesson_music.stop()
    test_music.stop()
    menu_music.play(-1)

    ans_button1.hide()
    ans_button2.hide()
    ans_button3.hide()
    ans_button4.hide()
    nothing2.hide()
    true_answer.hide()
    line.hide()
    quit_button.hide()
    nothing3.hide()
    ok_button.hide()
    send_answer_button.hide()

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
    if lessons_mode:
        button12.show()
        nothing4.hide()
    else:
        button12.hide()
        nothing4.show()

    lessons_button.show()
    stats.show()

    top_of_screen.setText("Niveles de Español")


# Answer modes

def four_answers_mode(question, ans1, ans2, ans3, ans4):
    global shuffle, right_ans_button, true_answer_variable, questions, test
    if not test and questions == 0:
        enter_sound.play()
        el_rio_fluye.play(-1)
    true_answer_variable = ans4
    top_of_screen.setText(question)
    order_of_answers = [1, 2, 3, 4]
    shuffle(order_of_answers)
    right_ans_button = None
    lessons_button.hide()

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

    ans_button1.show()
    ans_button2.show()
    ans_button3.show()
    ans_button4.show()

    true_answer.setText("     Tienes que encontrar la forma correcta de \n conjugación y presionar uno de estos botones.")
    true_answer.show()

    if not test:
        quit_button.show()
        nothing1.hide()

    else:
        quit_button.hide()
        nothing1.show()

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
    global exercice, true_answer_variable, questions, test
    if not test and questions == 0:
        enter_sound.play()
        el_rio_fluye.play(-1)

    send_answer_button.show()
    nothing2.hide()
    lessons_button.hide()
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

    true_answer.setText("Si no tienes un taclado español:  ú  á  ó  é  í  ñ")
    true_answer.show()

    if not test:
        quit_button.show()
        nothing1.hide()

    else:
        quit_button.hide()
        nothing1.show()

    true_answer_variable = true_ans
    if exercice == 10:
        top_of_screen.setText('¿Qué es "' + question + '" en plural?')
    else:
        top_of_screen.setText('¿Cómo se dice "' + question + '" en español?')

    line.show()
    send_answer_button.show()

def two_answers_mode(question, right_answer):
    global right_ans_button, true_answer_variable, questions, test
    if not test and questions == 0:
        enter_sound.play()
        el_rio_fluye.play(-1)

    lessons_button.hide()
    nothing2.hide()
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

    true_answer.setText("Tienes que encuentre el verbo correcto \n     y presione uno de estos botones.")
    true_answer.show()
    
    if not test:
        quit_button.show()
        nothing1.hide()

    else:
        quit_button.hide()
        nothing1.show()

    true_answer_variable = right_answer
    top_of_screen.setText(question)
    right_ans_button = right_answer
    ans_button1.setText("Ser")
    ans_button2.setText("Estar")
    ans_button1.show()
    ans_button2.show()


# Exercices

def ex1():
    global exercice
    exercice = 1
    random_question = randint(1, 6)

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
    global exercice
    exercice = 2
    random_question = randint(1, 6)

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
    global exercice
    exercice = 3
    random_question = randint(1, 6)

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
 
def ex4():
    global exercice
    exercice = 4
    random_question = randint(1, 6)

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
            four_answers_mode("Poder con él.", "podo", "podoy", "puedo", "puede")

        elif random_question == 2:
            four_answers_mode("Pensar con él.", "penso", "pensoy", "pienso", "piensa")

        elif random_question == 3:
            four_answers_mode("Jugar con él.", "jugo", "jugoy", "juego", "juega")

        elif random_question == 4:
            four_answers_mode("Poder con ella.", "podo", "podoy", "puedo", "puede")

        elif random_question == 5:
            four_answers_mode("Pensar con ella.", "penso", "pensoy", "pienso", "piensa")

        elif random_question == 6:
            four_answers_mode("Jugar con ella.", "jugo", "jugoy", "juego", "juega")
            
        elif random_question == 7:
            four_answers_mode("Poder con usted.", "podo", "podoy", "puedo", "puede")

        elif random_question == 8:
            four_answers_mode("Pensar con usted.", "penso", "pensoy", "pienso", "piensa")

        elif random_question == 9:
            four_answers_mode("Jugar con usted.", "jugo", "jugoy", "juego", "juega")

        elif random_question == 10:
            four_answers_mode("Poder con Carla.", "podo", "podoy", "puedo", "puede")

        elif random_question == 11:
            four_answers_mode("Pensar con Carla.", "penso", "pensoy", "pienso", "piensa")
            
        elif random_question == 12:
            four_answers_mode("Jugar con Carla.", "jugo", "jugoy", "juego", "juega")

        elif random_question == 13:
            four_answers_mode("Poder con Juan.", "podo", "podoy", "puedo", "puede")

        elif random_question == 14:
            four_answers_mode("Pensar con Juan.", "penso", "pensoy", "pienso", "piensa")

        elif random_question == 15:
            four_answers_mode("Jugar con Juan.", "jugo", "jugoy", "juego", "juega")

    elif random_question == 4:
        random_question = randint(1,6)
    
        if random_question == 1:
            four_answers_mode("Poder con nosotros.", "puedemos", "puedéis", "podéis", "podemos")

        elif random_question == 2:
            four_answers_mode("Pensar con nosotros.", "piensamos", "piensáis", "pensáis", "pensamos")

        elif random_question == 3:
            four_answers_mode("Jugar con nosotros.", "juegamos", "juegáis", "jugáis", "jugamos")

        elif random_question == 4:
            four_answers_mode("Poder con nosotras.", "puedemos", "puedéis", "podéis", "podemos")

        elif random_question == 5:
            four_answers_mode("Pensar con nosotras.", "piensamos", "piensáis", "pensáis", "pensamos")

        else:
            four_answers_mode("Jugar con nosotras.", "juegamos", "juegáis", "jugáis", "jugamos")

    elif random_question == 5:
        random_question = randint(1,6)

        if random_question == 1:
            four_answers_mode("Poder con vosotros.", "puedemos", "puedéis", "podemos", "podéis")

        elif random_question == 2:
            four_answers_mode("Pensar con vosotros.", "piensamos", "piensáis", "pensamos", "pensáis")

        elif random_question == 3:
            four_answers_mode("Jugar con vosotros.", "juegamos", "juegáis", "jugamos", "jugáis")

        elif random_question == 1:
            four_answers_mode("Poder con vosotras.", "puedemos", "puedéis", "podemos", "podéis")

        elif random_question == 2:
            four_answers_mode("Pensar con vosotras.", "piensamos", "piensáis", "pensamos", "pensáis")

        else:
            four_answers_mode("Jugar con vosotras.", "juegamos", "juegáis", "jugamos", "jugáis")

    else:
        random_question = randint(1,12)

        if random_question == 1:
            four_answers_mode("Poder con ellos.", "puedemos", "podemos", "poden", "pueden")

        elif random_question == 2:
            four_answers_mode("Pensar con ellos.", "piensamos", "pensamos", "pensan", "piensan")

        elif random_question == 3:
            four_answers_mode("Jugar con ellos.", "juegamos", "jugamos", "jugan", "juegan")

        elif random_question == 4:
            four_answers_mode("Poder con ellas.", "puedemos", "podemos", "poden", "pueden")

        elif random_question == 5:
            four_answers_mode("Pensar con ellas.", "piensamos", "pensamos", "pensan", "piensan")        
            
        elif random_question == 6:
            four_answers_mode("Jugar con ellas.", "juegamos", "jugamos", "jugan", "juegan")

        elif random_question == 7:
            four_answers_mode("Poder con ustedes.", "puedemos", "podemos", "poden", "pueden")

        elif random_question == 8:
            four_answers_mode("Pensar con ustedes.", "piensamos", "pensamos", "pensan", "piensan")

        elif random_question == 9:
            four_answers_mode("Jugar con ustedes.", "juegamos", "jugamos", "jugan", "juegan")

        elif random_question == 10:
            four_answers_mode("Poder con Carla y Juan.", "puedemos", "podemos", "poden", "pueden")

        elif random_question == 11:
            four_answers_mode("Pensar con Carla y Juan.", "piensamos", "pensamos", "pensan", "piensan")        
            
        elif random_question == 12:
            four_answers_mode("Jugar con Carla y Juan.", "juegamos", "jugamos", "jugan", "juegan")
 
def ex5():
    global exercice
    exercice = 5
    random_question = randint(1, 6)

    if random_question == 1:
        random_question = randint(1,3)

        if random_question == 1:
            four_answers_mode("Medir con yo.", "medo", "mides", "medes", "mido")

        elif random_question == 2:
            four_answers_mode("Vestir con yo.", "vesto", "vistes", "vestes", "visto")

        elif random_question == 3:
            four_answers_mode("Pedir con yo.", "pedo", "pides", "pedes", "pido")

    elif random_question == 2:
        random_question = randint(1,3)

        if random_question == 1:
            four_answers_mode("Medir con tú.", "medo", "medes", "mido", "mides")

        elif random_question == 2:
            four_answers_mode("Vestir con tú.", "vesto", "vestes", "visto", "vistes")

        elif random_question == 3:
            four_answers_mode("Pedir con tú.", "pedo", "pedes", "pido", "pides")

    elif random_question == 3:
        random_question = randint(1,15)

        if random_question == 1:
            four_answers_mode("Medir con él.", "medo", "mido", "mede", "mide")

        elif random_question == 2:
            four_answers_mode("Vestir con él.", "vesto", "visto", "veste", "viste")

        elif random_question == 3:
            four_answers_mode("Pedir con él.", "pedo", "pido", "pede", "pide")

        elif random_question == 4:
            four_answers_mode("Medir con ella.", "medo", "mido", "mede", "mide")

        elif random_question == 5:
            four_answers_mode("Vestir con ella.", "vesto", "visto", "veste", "viste")

        elif random_question == 6:
            four_answers_mode("Pedir con ella.", "pedo", "pido", "pede", "pide")
            
        elif random_question == 7:
            four_answers_mode("Medir con Carla.", "medo", "mido", "mede", "mide")

        elif random_question == 8:
            four_answers_mode("Vestir con Carla.", "vesto", "visto", "veste", "viste")

        elif random_question == 9:
            four_answers_mode("Pedir con Carla.", "pedo", "pido", "pede", "pide")

        elif random_question == 10:
            four_answers_mode("Medir con Juan.", "medo", "mido", "mede", "mide")

        elif random_question == 11:
            four_answers_mode("Vestir con Juan.", "vesto", "visto", "veste", "viste")
            
        elif random_question == 12:
            four_answers_mode("Pedir con Juan.", "pedo", "pido", "pede", "pide")

        elif random_question == 13:
            four_answers_mode("Medir con usted.", "medo", "mido", "mede", "mide")

        elif random_question == 14:
            four_answers_mode("Vestir con usted.", "vesto", "visto", "veste", "viste")

        elif random_question == 15:
            four_answers_mode("Pedir con usted.", "pedo", "pido", "pede", "pide")

    elif random_question == 4:
        random_question = randint(1,6)
    
        if random_question == 1:
            four_answers_mode("Medir con nosotros.", "medís", "midemos", "midéis", "medimos")

        elif random_question == 2:
            four_answers_mode("Vestir con nosotros.", "vestís", "vistemos", "vistéis", "vestimos")

        elif random_question == 3:
            four_answers_mode("Pedir con nosotros.", "pedís", "pidemos", "pidéis", "pedimos")

        elif random_question == 4:
            four_answers_mode("Medir con nosotras.", "medís", "midemos", "midéis", "medimos")

        elif random_question == 5:
            four_answers_mode("Vestir con nosotras.", "vestís", "vistemos", "vistéis", "vestimos")

        else:
            four_answers_mode("Pedir con nosotras.", "pedís", "pidemos", "pidéis", "pedimos")

    elif random_question == 5:
        random_question = randint(1,6)

        if random_question == 1:
            four_answers_mode("Medir con vosotros.", "midemos", "midéis", "medimos", "medís")

        elif random_question == 2:
            four_answers_mode("Vestir con vosotros.", "vistemos", "vistéis", "vestimos", "vestís")

        elif random_question == 3:
            four_answers_mode("Pedir con vosotros.", "pidemos", "pidéis", "pedimos", "pedís")

        elif random_question == 1:
            four_answers_mode("Medir con vosotras.", "midemos", "midéis", "medimos", "medís")

        elif random_question == 2:
            four_answers_mode("Vestir con vosotras.", "vistemos", "vistéis", "vestimos", "vestís")

        else:
            four_answers_mode("Pedir con vosotras.", "pidemos", "pidéis", "pedimos", "pedís")

    else:
        random_question = randint(1,12)

        if random_question == 1:
            four_answers_mode("Medir con ellos.", "midemos", "medimos", "medin", "miden")

        elif random_question == 2:
            four_answers_mode("Vestir con ellos.", "vistemos", "vestimos", "vestin", "visten")

        elif random_question == 3:
            four_answers_mode("Pedir con ellos.", "pidemos", "pedimos", "pedin", "piden")

        elif random_question == 4:
            four_answers_mode("Medir con ellas.", "midemos", "medimos", "medin", "miden")

        elif random_question == 5:
            four_answers_mode("Vestir con ellas.", "vistemos", "vestimos", "vestin", "visten")        
            
        elif random_question == 6:
            four_answers_mode("Pedir con ellas.", "pidemos", "pedimos", "pedin", "piden")

        elif random_question == 7:
            four_answers_mode("Medir con Carla y Juan.", "midemos", "medimos", "medin", "miden")

        elif random_question == 8:
            four_answers_mode("Vestir con Carla y Juan.", "vistemos", "vestimos", "vestin", "visten")

        elif random_question == 9:
            four_answers_mode("Pedir con Carla y Juan.", "pidemos", "pedimos", "pedin", "piden")

        elif random_question == 10:
            four_answers_mode("Medir con ustedes.", "midemos", "medimos", "medin", "miden")

        elif random_question == 11:
            four_answers_mode("Vestir con ustedes.", "vistemos", "vestimos", "vestin", "visten")        
            
        elif random_question == 12:
            four_answers_mode("Pedir con ustedes.", "pidemos", "pedimos", "pedin", "piden")
 
def ex6():
    global exercice
    exercice = 6
    random_question = randint(1, 2)

    if random_question == 1:
        random_question = randint(1,15)

        if random_question == 1:
            four_answers_mode("Vivir con él en imperatovo.", "vivo", "vivi", "vivimos", "vive")

        elif random_question == 2:
            four_answers_mode("Hablar con él en imperatovo.", "hablo", "hablar", "hablamos", "habla")

        elif random_question == 3:
            four_answers_mode("Comer con él en imperatovo.", "como", "comer", "comemos", "come")

        elif random_question == 4:
            four_answers_mode("Vivir con ella en imperatovo.", "vivo", "vivi", "vivimos", "vive")

        elif random_question == 5:
            four_answers_mode("Hablar con ella en imperatovo.", "hablo", "hablar", "hablamos", "habla")

        elif random_question == 6:
            four_answers_mode("Comer con ella en imperatovo.", "como", "comer", "comemos", "come")
            
        elif random_question == 7:
            four_answers_mode("Vivir con Juan en imperatovo.", "vivo", "vivi", "vivimos", "vive")

        elif random_question == 8:
            four_answers_mode("Hablar con Juan en imperatovo.", "hablo", "hablar", "hablamos", "habla")

        elif random_question == 9:
            four_answers_mode("Comer con Juan en imperatovo.", "como", "comer", "comemos", "come")

        elif random_question == 10:
            four_answers_mode("Vivir con Carla en imperatovo.", "vivo", "vivi", "vivimos", "vive")

        elif random_question == 11:
            four_answers_mode("Hablar con Carla en imperatovo.", "hablo", "hablar", "hablamos", "habla")
            
        elif random_question == 12:
            four_answers_mode("Comer con Carla en imperatovo.", "como", "comer", "comemos", "come")

        elif random_question == 13:
            four_answers_mode("Vivir con usted en imperatovo.", "vivo", "vivi", "vivimos", "vive")

        elif random_question == 14:
            four_answers_mode("Hablar con usted en imperatovo.", "hablo", "hablar", "hablamos", "habla")

        elif random_question == 15:
            four_answers_mode("Comer con usted en imperatovo.", "como", "comer", "comemos", "come")

    else:
        random_question = randint(1,6)

        if random_question == 1:
            four_answers_mode("Vivir con vosotros en imperatovo.", "vivo", "vivir", "vivís", "vivid")

        elif random_question == 2:
            four_answers_mode("Hablar con vosotros en imperatovo.", "hablo", "hablar", "habláis", "hablad")

        elif random_question == 3:
            four_answers_mode("Comer con vosotros en imperatovo.", "como", "comer", "coméis", "comed")

        elif random_question == 1:
            four_answers_mode("Vivir con vosotras en imperatovo.", "vivo", "vivir", "vivís", "vivid")

        elif random_question == 2:
            four_answers_mode("Hablar con vosotras en imperatovo.", "hablo", "hablar", "habláis", "hablad")

        else:
            four_answers_mode("Comer con vosotras en imperatovo.", "como", "comer", "coméis", "comed")

def ex7():
    global exercice
    exercice = 7
    random_question = randint(1, 20)

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
 
def ex8():
    global exercice
    exercice = 8
    random_question = randint(1, 39)

    if random_question == 1:
        typing_answer_mode("1", "uno")

    elif random_question == 2:
        typing_answer_mode("2", "dos")

    elif random_question == 3:
        typing_answer_mode("3", "tres")

    elif random_question == 4:
        typing_answer_mode("4", "cuatro")

    elif random_question == 5:
        typing_answer_mode("5", "cinco")

    elif random_question == 6:
        typing_answer_mode("6", "seis")

    elif random_question == 7:
        typing_answer_mode("7", "siete")

    elif random_question == 8:
        typing_answer_mode("8", "ocho")

    elif random_question == 9:
        typing_answer_mode("9", "nueve")

    elif random_question == 10:
        typing_answer_mode("10", "diez")

    elif random_question == 11:
        typing_answer_mode("11", "once")

    elif random_question == 12:
        typing_answer_mode("12", "doce")

    elif random_question == 13:
        typing_answer_mode("13", "trece")

    elif random_question == 14:
        typing_answer_mode("14", "catorce")

    elif random_question == 15:
        typing_answer_mode("15", "quince")

    elif random_question == 16:
        typing_answer_mode("16", "dieciséis")

    elif random_question == 17:
        typing_answer_mode("17", "diecisiete")

    elif random_question == 18:
        typing_answer_mode("18", "dieciocho")

    elif random_question == 19:
        typing_answer_mode("19", "diecinueve")

    elif random_question == 20:
        typing_answer_mode("20", "veinte")

    elif random_question == 21:
        typing_answer_mode("21", "ventiuno")

    elif random_question == 22:
        typing_answer_mode("22", "ventidós")

    elif random_question == 23:
        typing_answer_mode("23", "ventitrés")

    elif random_question == 24:
        typing_answer_mode("24", "venticuatro")

    elif random_question == 25:
        typing_answer_mode("25", "venticinco")

    elif random_question == 26:
        typing_answer_mode("26", "ventiséis")

    elif random_question == 27:
        typing_answer_mode("27", "ventisiete")

    elif random_question == 28:
        typing_answer_mode("28", "ventiocho")

    elif random_question == 29:
        typing_answer_mode("29", "ventinueve")

    elif random_question == 30:
        typing_answer_mode("30", "trienta")

    elif random_question == 31:
        typing_answer_mode("40", "cuarenta")

    elif random_question == 32:
        typing_answer_mode("50", "cincuenta")

    elif random_question == 33:
        typing_answer_mode("60", "sesenta")

    elif random_question == 34:
        typing_answer_mode("70", "setenta")

    elif random_question == 35:
        typing_answer_mode("80", "ochenta")

    elif random_question == 36:
        typing_answer_mode("90", "noventa")

    elif random_question == 37:
        typing_answer_mode("100", "cien")

    elif random_question == 38:
        typing_answer_mode("1 000", "mil")

    else:
        typing_answer_mode("1 000 000", "millión")

    if questions == 0:
        enter_sound.play()
        el_rio_fluye.play(-1)

def ex9():
    global exercice
    exercice = 9
    random_question = randint(1, 12)

    if random_question == 1:
        typing_answer_mode("Perou", "perú")

    elif random_question == 2:
        typing_answer_mode("Chili", "chile")

    elif random_question == 3:
        typing_answer_mode("Etats Unis d'Amérique", "estados unidos")

    elif random_question == 4:
        typing_answer_mode("Canada", "canadá")

    elif random_question == 5:
        typing_answer_mode("Maroque", "marruecos")

    elif random_question == 6:
        typing_answer_mode("Algérie", "argelia")

    elif random_question == 7:
        typing_answer_mode("Australie", "australia")

    elif random_question == 8:
        typing_answer_mode("Nouvelle Zélande", "nueva zelanda")

    elif random_question == 9:
        typing_answer_mode("Espagne", "españa")

    elif random_question == 10:
        typing_answer_mode("France", "francia")

    elif random_question == 11:
        typing_answer_mode("Chine", "china")

    else:
        typing_answer_mode("Inde", "india")

def ex10():
    global exercice
    exercice = 10
    random_question = randint(1, 9)

    if random_question == 1:
        typing_answer_mode("el cuaderno", "los cuadernos")

    elif random_question == 2:
        typing_answer_mode("la profesora", "las profesoras")

    elif random_question == 3:
        typing_answer_mode("la isla", "las islas")

    elif random_question == 4:
        typing_answer_mode("la capital", "las capitales")

    elif random_question == 5:
        typing_answer_mode("el animal", "los animales")

    elif random_question == 6:
        typing_answer_mode("el mes", "los meses")

    elif random_question == 7:
        typing_answer_mode("el pez", "los peces")

    elif random_question == 8:
        typing_answer_mode("el juez", "los jueces")

    else:
        typing_answer_mode("el nuez", "los nueces")

def ex11():
    global exercice
    exercice = 11
    random_question = randint(1, 23)

    if random_question == 1:
        typing_answer_mode("lundi", "lunes")

    elif random_question == 2:
        typing_answer_mode("mardi", "martes")

    elif random_question == 3:
        typing_answer_mode("mercredi", "miécroles")

    elif random_question == 4:
        typing_answer_mode("jeudi", "jueves")

    elif random_question == 5:
        typing_answer_mode("vendredi", "viernes")

    elif random_question == 6:
        typing_answer_mode("samedi", "sábado")

    elif random_question == 7:
        typing_answer_mode("dimanche", "domingo")

    elif random_question == 8:
        typing_answer_mode("janvier", "enero")

    elif random_question == 9:
        typing_answer_mode("février", "febrero")

    elif random_question == 10:
        typing_answer_mode("mars", "marzo")

    elif random_question == 11:
        typing_answer_mode("avril", "abril")

    elif random_question == 12:
        typing_answer_mode("mai", "mayo")

    elif random_question == 13:
        typing_answer_mode("juin", "junio")

    elif random_question == 14:
        typing_answer_mode("juillet", "julio")

    elif random_question == 15:
        typing_answer_mode("août", "agosto")

    elif random_question == 16:
        typing_answer_mode("septembre", "septiembre")

    elif random_question == 17:
        typing_answer_mode("octobre", "octubre")

    elif random_question == 18:
        typing_answer_mode("novembre", "noviemvre")

    elif random_question == 19:
        typing_answer_mode("décembre", "diciembre")

    elif random_question == 20:
        typing_answer_mode("le printemps", "la primavera")

    elif random_question == 21:
        typing_answer_mode("l'été", "el verano")

    elif random_question == 22:
        typing_answer_mode("l'automne", "el otoño")

    else:
        typing_answer_mode("l'hiver", "el inverno")

def ex12(): # the test
    global test, test_questions, test_note, test_finished, exercice
    exercice = 1
    test_finished = False
    test = True
    test_note = 0
    if test_questions == 0:
        test_notes = []
    random_exercice = randint(1, 11)

    if test_questions == 0:
        enter_sound.play()
        test_music.play(-1)

    if random_exercice == 1:
        ex1()

    elif random_exercice == 2:
        ex2()

    elif random_exercice == 3:
        ex3()

    elif random_exercice == 4:
        ex4()

    elif random_exercice == 5:
        ex5()

    elif random_exercice == 6:
        ex6()

    elif random_exercice == 7:
        ex7()

    elif random_exercice == 8:
        ex8()

    elif random_exercice == 9:
        ex9()

    elif random_exercice == 10:
        ex10()

    else:
        ex11()


# When menu buttons were clicked

def menu_button1():
    global lessons_mode
    if lessons_mode:
        ex1()
    else:
        lesson()

def menu_button2():
    global lessons_mode
    if lessons_mode:
        ex2()
    else:
        lesson()

def menu_button3():
    global lessons_mode
    if lessons_mode:
        ex3()
    else:
        lesson()

def menu_button4():
    global lessons_mode
    if lessons_mode:
        ex4()
    else:
        lesson()

def menu_button5():
    global lessons_mode
    if lessons_mode:
        ex5()
    else:
        lesson()

def menu_button6():
    global lessons_mode
    if lessons_mode:
        ex6()
    else:
        lesson()

def menu_button7():
    global lessons_mode
    if lessons_mode:
        ex7()
    else:
        lesson()

def menu_button8():
    global lessons_mode
    if lessons_mode:
        ex8()
    else:
        lesson()

def menu_button9():
    global lessons_mode
    if lessons_mode:
        ex9()
    else:
        lesson()

def menu_button10():
    global lessons_mode
    if lessons_mode:
        ex10()
    else:
        lesson()

def menu_button11():
    global lessons_mode
    if lessons_mode:
        ex11()
    else:
        lesson()


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


# When a button was clicked

button01.clicked.connect(menu_button1)
button02.clicked.connect(menu_button2)
button03.clicked.connect(menu_button3)
button04.clicked.connect(menu_button4)
button05.clicked.connect(menu_button5)
button06.clicked.connect(menu_button6)
button07.clicked.connect(menu_button7)
button08.clicked.connect(menu_button8)
button09.clicked.connect(menu_button9)
button10.clicked.connect(menu_button10)
button11.clicked.connect(menu_button11)
button12.clicked.connect(ex12)

ok_button.clicked.connect(ok_button_clicked)
send_answer_button.clicked.connect(true_or_false)

ans_button1.clicked.connect(ans_button1_clicked)
ans_button2.clicked.connect(ans_button2_clicked)
ans_button3.clicked.connect(ans_button3_clicked)
ans_button4.clicked.connect(ans_button4_clicked)

quit_button.clicked.connect(finish_exercice)
lessons_button.clicked.connect(lessons_button_clicked)


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

button01.setFixedSize(165, 90)
button02.setFixedSize(165, 90)
button03.setFixedSize(165, 90)
button04.setFixedSize(165, 90)
button05.setFixedSize(165, 90)
button06.setFixedSize(165, 90)
button07.setFixedSize(165, 90)
button08.setFixedSize(165, 90)
button09.setFixedSize(165, 90)
button10.setFixedSize(165, 90)
button11.setFixedSize(165, 90)
button12.setFixedSize(165, 90)


ans_button1.setFixedSize(250, 80)
ans_button2.setFixedSize(250, 80)
ans_button3.setFixedSize(250, 80)
ans_button4.setFixedSize(250, 80)

ans_button1.setFont(QFont("Arial", 20))
ans_button2.setFont(QFont("Arial", 20))
ans_button3.setFont(QFont("Arial", 20))
ans_button4.setFont(QFont("Arial", 20))

lessons_button.setFont(QFont("Arial", 15))

ok_button.setFixedSize(165, 80)
line.setFixedSize(570, 40)
send_answer_button.setFixedSize(100, 40)
quit_button.setFixedSize(100, 40)
lessons_button.setFixedSize(150, 70)

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

layout3.addWidget(nothing4, alignment = Qt.AlignCenter)

true_answer_layout.addWidget(true_answer,  alignment = Qt.AlignCenter)
layout2.addWidget(ok_button,  alignment = Qt.AlignCenter)

ans_layout1.addWidget(ans_button1, alignment = Qt.AlignCenter)
ans_layout1.addWidget(ans_button2, alignment = Qt.AlignCenter)
ans_layout2.addWidget(ans_button3, alignment = Qt.AlignCenter)
ans_layout2.addWidget(ans_button4, alignment = Qt.AlignCenter)

ans_layout2.addWidget(line, alignment = Qt.AlignCenter)
ans_layout2.addWidget(send_answer_button, alignment = Qt.AlignCenter)

stats_layout.addWidget(lessons_button, alignment = Qt.AlignCenter)
stats_layout.addWidget(quit_button, alignment = Qt.AlignCenter)
stats_layout.addWidget(nothing1, alignment = Qt.AlignCenter)
stats_layout.addWidget(top_of_screen, alignment = Qt.AlignCenter)
stats_layout.addWidget(stats, alignment = Qt.AlignCenter)
stats_layout.addWidget(nothing3, alignment = Qt.AlignCenter)

nothing_layout.addWidget(nothing2, alignment = Qt.AlignCenter)


# Connecting layouts

main_layout.addLayout(stats_layout)
main_layout.addLayout(nothing_layout)
main_layout.addLayout(true_answer_layout)
main_layout.addLayout(ans_layout1)
main_layout.addLayout(ans_layout2)
main_layout.addLayout(layout1)
main_layout.addLayout(layout2)
main_layout.addLayout(layout3)

main_win.setLayout(main_layout)
main_win.show()

app.exec()