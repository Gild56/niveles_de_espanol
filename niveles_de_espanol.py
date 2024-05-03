# Niveles de Español

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
exercice_music = pygame.mixer.Sound(resource_path("el_rio_fluye.mp3"))
test_music = pygame.mixer.Sound(resource_path("demon_slayer_cats_instrumental.mp3"))
lesson_music = pygame.mixer.Sound(resource_path("glorious_morning.mp3"))

exercice_music.set_volume(0.3)

menu_music.play(-1)


# Layouts

main_layout = QVBoxLayout()

top_layout = QHBoxLayout()
bottom_comments_layout= QHBoxLayout()
top_comments_layout = QHBoxLayout()
ans_layout1 = QHBoxLayout() # top
ans_layout2 = QHBoxLayout() # bottom
layout1 = QHBoxLayout() # top
layout2 = QHBoxLayout() # middle
layout3 = QHBoxLayout() # bottom


# Variables

language = 1 # 1 = Français, 2 = Українська
lesson_page1 = ""
lesson_page2 = ""
lesson_page3 = ""
lesson_page4 = ""
lesson_page5 = ""
lesson_page = 1
test_finished = False
test_note = 0
test_notes = []
test = False
test_questions = 0
tests = 0
menu_mode = True
note = 20
notes = []
right_ans_button = None
exercice = None
questions = 0
true_answer_variable = ""


# QLabels (nothing help to alignement)

nothing1 = QLabel("") # quit button or it
nothing2 = QLabel("") # visible in the answer verification
top_comments_label = QLabel("")
bottom_comments_label = QLabel("")
top_of_screen = QLabel("Niveles de Español")
stats = QLabel("v.1.2" + "\n"
    "Nota : -" + "\n"
    "Un juego @gild56gmd")

stats.setFont(QFont("Arial", 7))
top_of_screen.setFont(QFont("Impact", 17))
top_comments_label.setFont(QFont("Arial", 15))
bottom_comments_label.setFont(QFont("Arial", 15))

bottom_comments_label.setTextInteractionFlags(Qt.TextSelectableByMouse)
stats.setTextInteractionFlags(Qt.TextSelectableByMouse)
bottom_comments_label.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)

nothing1.hide()
nothing2.hide()
top_comments_label.hide()
bottom_comments_label.hide()


# Buttons and line

answer_line = QLineEdit()

ans_button1 = QPushButton("")   #top left button
ans_button2 = QPushButton("")   #top right button
ans_button3 = QPushButton("")   #bottom left button
ans_button4 = QPushButton("")   #bottom right button

menu_mode_button = QPushButton("Lecciónes")
ok_button = QPushButton("OK")
send_answer_button = QPushButton("OK")
quit_button = QPushButton("<--")
next_button = QPushButton("Siguiente")
change_of_language_button = QPushButton("Français")

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

ans_button1.hide()
ans_button2.hide()
ans_button3.hide()
ans_button4.hide()
ok_button.hide()
send_answer_button.hide()
answer_line.hide()
quit_button.hide()
next_button.hide()
change_of_language_button.hide()


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

menu_mode_button.setFont(QFont("Arial", 15))
next_button.setFont(QFont("Arial", 15))
change_of_language_button.setFont(QFont("Arial", 15))

ok_button.setFixedSize(165, 80)
answer_line.setFixedSize(570, 40)
send_answer_button.setFixedSize(100, 40)
next_button.setFixedSize(150, 70)
quit_button.setFixedSize(100, 40)
menu_mode_button.setFixedSize(150, 70)
change_of_language_button.setFixedSize(165, 90)


# Functions

def menu_mode_button_clicked():
    global menu_mode
    click.play()
    if menu_mode:
        menu_mode = False
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
        change_of_language_button.show()
        menu_mode_button.setText("Ejercicios")
    else:
        menu_mode = True
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
        change_of_language_button.hide()
        menu_mode_button.setText("Lecciónes")

def open_a_lesson(lesson1, lesson2=False, lesson3=False, lesson4=False, lesson5=False):
    global lesson_page, lesson_page1, lesson_page2, lesson_page3, lesson_page4, lesson_page5
    click.play()
    lesson_page1 = lesson1
    lesson_page2 = lesson2
    lesson_page3 = lesson3
    lesson_page4 = lesson4
    lesson_page5 = lesson5
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
    change_of_language_button.hide()
    menu_mode_button.hide()
    quit_button.show()
    next_button.show()
    bottom_comments_label.show()
    bottom_comments_label.setText(lesson1)

def next_page_of_lesson():
    global lesson_page, lesson_page1, lesson_page2, lesson_page3, lesson_page4, lesson_page5
    click.play()
    if lesson_page == 1 and lesson_page2 != False:
        lesson_page = 2
        bottom_comments_label.setText(lesson_page2)

    elif lesson_page == 2 and lesson_page3 != False:
        lesson_page = 3
        bottom_comments_label.setText(lesson_page3)

    elif lesson_page == 3 and lesson_page4 != False:
        lesson_page = 4
        bottom_comments_label.setText(lesson_page4)

    elif lesson_page == 4 and lesson_page5 != False:
        lesson_page = 5
        bottom_comments_label.setText(lesson_page5)

    else:
        lesson_page = 1
        bottom_comments_label.setText(lesson_page1)

def next_language():
    global language
    click.play()
    if language == 1:
        language = 2
        change_of_language_button.setText("Українська")

    else:
        language = 1
        change_of_language_button.setText("Français")

def note_calculating():
    global test, notes, test_notes, test_note
    all_notes = 0
    if not test:
        for i in range(len(notes)):
            all_notes += notes[i]
        note = round(all_notes / len(notes), 2)

        stats.setText("v.1.2" + "\n"
            "Nota : " + str(note) + "\n"
            "Un juego de @gild56gmd")

    if test == True:
        for i in range(len(test_notes)):
            all_notes += test_notes[i]
        test_note = round(all_notes / len(test_notes), 2)

def answer_verification(button_clicked=None):
    global true_answer_variable, true_answer, exercice, test, test_notes
    click.play()
    ans_button1.hide()
    ans_button2.hide()
    ans_button3.hide()
    ans_button4.hide()
    send_answer_button.hide()
    answer_line.hide()
    if not test:
        nothing1.hide()
    stats.hide()
    bottom_comments_label.show()
    top_comments_label.show()
    nothing2.show()
    ok_button.show()
    answer = answer_line.text()
    answer = answer.lower()
    if exercice < 8:
        if right_ans_button == button_clicked:
            top_of_screen.setText("Sí")
            si.play()
            if not test:
                notes.append(20)
            else:
                test_notes.append(20)
            bottom_comments_label.setText("¡Bien!")
            wrong_answer = False

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
            bottom_comments_label.setText("La repuesta es " + str(true_answer_variable) + ".")

    elif true_answer_variable == answer:
        top_of_screen.setText("Sí")
        si.play()
        if not test:
            notes.append(20)
        else:
            test_notes.append(20)
        bottom_comments_label.setText("¡Bien!")
        wrong_answer = False

    else:
        wrong_answer = True
        top_of_screen.setText("No")
        no.play()
        if not test:
            notes.append(0)
        else:
            test_notes.append(0)
        bottom_comments_label.setText("La repuesta es " + str(true_answer_variable) + ".")

    if wrong_answer:
        random_text = randint(1, 10)

        if random_text == 1:
            top_comments_label.setText("¡Qué lástima!")

        elif random_text == 2:
            top_comments_label.setText("¡Tendrás suerte la próxima vez!")

        elif random_text == 3:
            top_comments_label.setText("¡Incorrecto! ¡Inténtalo de nuevo!")

        elif random_text == 4:
            top_comments_label.setText("¡No presiones al azar por favor...")

        elif random_text == 5:
            top_comments_label.setText("¡Vaya! Eso no fue lo que esperaba.")

        elif random_text == 6:
            top_comments_label.setText("¡Ups! Parece que eso no fue lo correcto.")

        elif random_text == 7:
            top_comments_label.setText("¡Sigue intentando!")

        elif random_text == 8:
            top_comments_label.setText("¡Casi lo tienes!")

        elif random_text == 9:
            top_comments_label.setText("¡Eso estuvo cerca!")

        else:
            top_comments_label.setText("¡Ánimo! ¡La próxima vez será mejor!")

    else:
        random_answer = randint(1, 1000)
        if random_answer == 1:
            top_comments_label.setText("Tienes una oportunidad entre mil \n    de obtener este comentario")

        elif random_answer < 250:
            top_comments_label.setText("¡Genial!")

        elif random_answer < 500:
            top_comments_label.setText("¡Sigue así!")

        elif random_answer < 750:
            top_comments_label.setText("No está mal.")

        else:
            top_comments_label.setText("Mejor que mal :)")

    answer_line.clear()
    note_calculating()

def ok_button_clicked():
    global questions, exercice, test, test_questions, test_note, test_finished
    if test_finished:
        finish_exercice()
    else:
        click.play()
        stats.show()
        ok_button.hide()
        top_comments_label.hide()
        nothing2.hide()
        if exercice > 7 and not test:
            answer_line.show()
            send_answer_button.show()

        if not test:
            if questions == 0:
                questions += 1

            if exercice == 1:
                exercice1()

            elif exercice == 2:
                exercice2()

            elif exercice == 3:
                exercice3()

            elif exercice == 4:
                exercice4()

            elif exercice == 5:
                exercice5()

            elif exercice == 6:
                exercice6()

            elif exercice == 7:
                exercice7()

            elif exercice == 8:
                exercice8()

            elif exercice == 9:
                exercice9()

            elif exercice == 10:
                exercice10()

            elif exercice == 11:
                exercice11()

        else:
            test_questions += 1
            if test_questions == 10:
                test = False
                questions = 0
                top_comments_label.hide()
                bottom_comments_label.hide()
                answer_line.hide()
                quit_button.hide()
                nothing2.hide()
                stats.hide()
                nothing1.hide()
                ok_button.show()
                test_finished = True
                top_of_screen.setText("La nota de esta evaluación es " + str(test_note))
                print("La nota de esta evaluación es " + str(test_note))

            else:
                test_exercice()

def finish_exercice():
    global exercice, test_questions, questions, menu_mode
    questions = 0
    test_questions = 0
    click.play()
    menu_music.play(-1)
    exercice_music.stop()
    lesson_music.stop()
    test_music.stop()
    exercice = 0


    ans_button1.hide()
    ans_button2.hide()
    ans_button3.hide()
    ans_button4.hide()
    top_comments_label.hide()
    bottom_comments_label.hide()
    answer_line.hide()
    quit_button.hide()
    nothing2.hide()
    ok_button.hide()
    send_answer_button.hide()
    next_button.hide()

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
    if menu_mode:
        button12.show()
        change_of_language_button.hide()
    else:
        button12.hide()
        change_of_language_button.show()

    menu_mode_button.show()
    stats.show()

    top_of_screen.setText("Niveles de Español")


# Answer modes

def four_answers_mode(question, ans1, ans2, ans3, ans4):
    global shuffle, right_ans_button, true_answer_variable, questions, test
    if not test and questions == 0:
        enter_sound.play()
        exercice_music.play(-1)
    true_answer_variable = ans4
    top_of_screen.setText(question)
    order_of_answers = [1, 2, 3, 4]
    shuffle(order_of_answers)
    right_ans_button = None
    menu_mode_button.hide()

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

    bottom_comments_label.setText("     Tienes que encontrar la forma correcta de \n conjugación y presionar uno de estos botones.")
    bottom_comments_label.show()

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
        exercice_music.play(-1)

    send_answer_button.show()
    top_comments_label.hide()
    menu_mode_button.hide()
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

    bottom_comments_label.setText("Si no tienes un taclado español:  ú  á  ó  é  í  ñ")
    bottom_comments_label.show()

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

    answer_line.show()
    send_answer_button.show()

def two_answers_mode(question, right_answer):
    global right_ans_button, true_answer_variable, questions, test
    if not test and questions == 0:
        enter_sound.play()
        exercice_music.play(-1)

    menu_mode_button.hide()
    top_comments_label.hide()
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

    bottom_comments_label.setText("")
    bottom_comments_label.show()

    top_comments_label.setText("Tienes que encuentre el verbo correcto \n     y presione uno de estos botones.")
    top_comments_label.show()

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

def exercice1():
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

def exercice2():
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

def exercice3():
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

def exercice4():
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

def exercice5():
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

def exercice6():
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

def exercice7():
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
        two_answers_mode("Tú ... muy mal.", 2)

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

def exercice8():
    global exercice
    exercice = 8
    random_question = randint(1, 40)

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

    elif random_question == 39:
        typing_answer_mode("0", "zero")

    else:
        typing_answer_mode("1 000 000", "millión")

    if questions == 0:
        enter_sound.play()
        exercice_music.play(-1)

def exercice9():
    global exercice
    exercice = 9
    random_question = randint(1, 12)
    if language == 2:
        if random_question == 1:
            typing_answer_mode("Перу", "perú")

        elif random_question == 2:
            typing_answer_mode("Чілі", "chile")

        elif random_question == 3:
            typing_answer_mode("Сполучені Штати Америки", "estados unidos")

        elif random_question == 4:
            typing_answer_mode("Канада", "canadá")

        elif random_question == 5:
            typing_answer_mode("Марокко", "marruecos")

        elif random_question == 6:
            typing_answer_mode("Алжерія", "argelia")

        elif random_question == 7:
            typing_answer_mode("Австралія", "australia")

        elif random_question == 8:
            typing_answer_mode("Нова зеландія", "nueva zelanda")

        elif random_question == 9:
            typing_answer_mode("Іспанія", "españa")

        elif random_question == 10:
            typing_answer_mode("Франція", "francia")

        elif random_question == 11:
            typing_answer_mode("Китай", "china")

        else:
            typing_answer_mode("Індія", "india")

    elif language == 1:
        if random_question == 1:
            typing_answer_mode("Pérou", "perú")

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

def exercice10():
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

def exercice11():
    global exercice
    exercice = 11
    random_question = randint(1, 23)
    if language == 2:
        if random_question == 1:
            typing_answer_mode("понеділок", "lunes")

        elif random_question == 2:
            typing_answer_mode("вівторок", "martes")

        elif random_question == 3:
            typing_answer_mode("середа", "miécroles")

        elif random_question == 4:
            typing_answer_mode("четвер", "jueves")

        elif random_question == 5:
            typing_answer_mode("п'ятниця", "viernes")

        elif random_question == 6:
            typing_answer_mode("субота", "sábado")

        elif random_question == 7:
            typing_answer_mode("неділя", "domingo")

        elif random_question == 8:
            typing_answer_mode("Січень", "enero")

        elif random_question == 9:
            typing_answer_mode("лютий", "febrero")

        elif random_question == 10:
            typing_answer_mode("березень", "marzo")

        elif random_question == 11:
            typing_answer_mode("квітень", "abril")

        elif random_question == 12:
            typing_answer_mode("травень", "mayo")

        elif random_question == 13:
            typing_answer_mode("червень", "junio")

        elif random_question == 14:
            typing_answer_mode("липень", "julio")

        elif random_question == 15:
            typing_answer_mode("серпень", "agosto")

        elif random_question == 16:
            typing_answer_mode("вересень", "septiembre")

        elif random_question == 17:
            typing_answer_mode("жовтень", "octubre")

        elif random_question == 18:
            typing_answer_mode("листопад", "noviemvre")

        elif random_question == 19:
            typing_answer_mode("грудень", "diciembre")

        elif random_question == 20:
            typing_answer_mode("весна", "la primavera")

        elif random_question == 21:
            typing_answer_mode("літо", "el verano")

        elif random_question == 22:
            typing_answer_mode("осінь", "el otoño")

        else:
            typing_answer_mode("зима", "el invierno")
    elif language == 1:
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
            typing_answer_mode("l'hiver", "el invierno")

def test_exercice():
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
        exercice1()

    elif random_exercice == 2:
        exercice2()

    elif random_exercice == 3:
        exercice3()

    elif random_exercice == 4:
        exercice4()

    elif random_exercice == 5:
        exercice5()

    elif random_exercice == 6:
        exercice6()

    elif random_exercice == 7:
        exercice7()

    elif random_exercice == 8:
        exercice8()

    elif random_exercice == 9:
        exercice9()

    elif random_exercice == 10:
        exercice10()

    else:
        exercice11()


# When menu buttons were clicked (+ lessons)

def menu_button1():
    global menu_mode, language
    if menu_mode:
        exercice1()
    else:
        if language == 1:
            open_a_lesson(  "      AR \n \n BV + o \n BV + as \n BV + a \n BV + amos \n BV + áis \n BV + an ",
                            "      ER \n \n BV + o \n BV + es \n BV + e \n BV + emos \n BV + éis \n BV + en ",
                            "      IR \n \n BV + o \n BV + es \n BV + e \n BV + imos \n BV + ís  \n BV + en ",
                            " 1ère pers. du sing.: Yo \n 2ème pers. du sing.: Tú \n 3ème pers. du sing.: Él/Ella/Usted/Nom \n \n 1ère pers. du plur.: Nosotr@` \n 2ème pers. du plur.: Vosotr@s \n 3ème pers. du plur.: Ell@s/Ustedes/Noms coordonnés",
                            " VIVIR = vivre \n HABLAR = parler \n COMER = manger")
        elif language == 2:
            open_a_lesson(  "      AR \n \n BV + o \n BV + as \n BV + a \n BV + amos \n BV + áis \n BV + an ",
                            "      ER \n \n BV + o \n BV + es \n BV + e \n BV + emos \n BV + éis \n BV + en ",
                            "      IR \n \n BV + o \n BV + es \n BV + e \n BV + imos \n BV + ís  \n BV + en ",
                            " Перша особа однини: Yo \n Друга особа однини.: Tú \n Третя особа однини: Él/Ella/Usted/Прийменник \n \n Перша особа множини: Nosotr@` \n Друга особа множини: Vosotr@s \n Друга особа множини Ell@s/Ustedes/Прийменники",
                            " VIVIR = жити \n HABLAR = говорити \n COMER = їсти")

def menu_button2():
    global menu_mode, language
    if menu_mode:
        exercice2()
    else:
        if language == 1:
            open_a_lesson(  " TENER \n \n Tengo \n Tienes \n Tiene \n Tenemos \n Teneis \n Tienen",
                            "  SER  \n \n Soy \n Eres \n Es \n Somos \n Sois \n Son",
                            "   IR  \n \n Voy \n Vas \n Va \n Vamos \n Vais \n Van",
                            " ESTAR \n \n Estoy \n Estás \n Está \n Estámos \n Estáis \n Están",
                            "    On ne peut pas deviner qu'un verbe est irrégulié, \n mais on peut l'apprendre. \n Aprrends donc pien tes verbes irréguliés :) \n TENER = avoir / posseder \n SER // ESTAR = être (voir la différence dans le cour №7) \n IR = aller")
        elif language == 2:
            open_a_lesson(  " TENER \n \n Tengo \n Tienes \n Tiene \n Tenemos \n Teneis \n Tienen",
                            "  SER  \n \n Soy \n Eres \n Es \n Somos \n Sois \n Son",
                            "   IR  \n \n Voy \n Vas \n Va \n Vamos \n Vais \n Van",
                            " ESTAR \n \n Estoy \n Estás \n Está \n Estámos \n Estáis \n Están",
                            "    Неможна здогадатися, що дієслово неправильне, \n але це можна вивщити. Тож вивчай неправильні \n дієслова напам'ять :) \n TENER = мати / володіти \n SER // ESTAR = бути (дивитися на різницю в уроці №7) \n IR = йти / їхати / переміщатися")

def menu_button3():
    global menu_mode, language
    if menu_mode:
        exercice3()
    else:
        if language == 1:
            open_a_lesson(  "    Avec les verbes pronominaux tout est relativement simple: \n la particule de 'pronominalisation' SE se colle derrière \n à l'infinitif, donc il est très simple de voir qu'un verbe est \n pronominal. Puis, en conjuguant le verbe on la met devant, \n en la changeant. Voici les formes de cette particule:",
                            "         V + SE \n ME + V Conjugué \n TE + V Conjugué \n SE + V Conjugué \n NOS + V Conjugué \n OS + V Conjugué \n SE + V Conjugué",
                            " DORMIRSE = s'endormir \n LLEVANTARSE = se lever \n LLAMARSE = s'appeller")
        elif language == 2:
            open_a_lesson(  " З дієсловами займенникового відтінку все відносно \n просто: частку 'прономіналізації' SE додають після \n інфінітива, тому дуже легко побачити, що дієслово є \n займенниковим. Потім, при кон'югації дієслова, вона \n ставиться перед ним, змінюючи свою форму. Ось форми \n цієї частки:",
                            "         Дієслово + SE \n ME + Спряжене Дієслово \n TE + Спряжене Дієслово \n SE + Спряжене Дієслово \n NOS + Спряжене Дієслово \n OS + Спряжене Дієслово \n SE + Спряжене Дієслово",
                            " DORMIRSE = засипати \n LLEVANTARSE = вставати \n LLAMARSE = дзвонити / звати / кликати")

def menu_button4():
    global menu_mode, language
    if menu_mode:
        exercice4()
    else:
        if language == 1:
            open_a_lesson(  "    On ne peut pas reconnaître un verbe à diphtongue, \n mais on peut l'apprendre. \n Tout dépend de la lettre qui 'diphtongue': \n 1ère possibilité: O -> UE \n 2ème possibilité: I -> IE \n 3ème possibilité: E -> UE \n    Et souviens-toi que les verbes ne 'diphtonguent' pas \n a la 1aère et 2ème du pluriel :)",
                            " dOrmir \n dUErmo \n dUErmes \n dUErme \n dOrmemos \n dOrmís \n dUErmen",
                            " PODER = pouvoir \n PENSAR = penser \n JUGAR = jouer")
        elif language == 2:
            open_a_lesson(  "    Можна не впізнати дієслово з дифтонгом, \n але можна його вивчити. \n Все залежить від літери, яка утворює дифтонг: \n 1-а можливість: O -> UE \n 2-а можливість: I -> IE \n 3-я можливість: E -> UE \n І пам'ятай, що дієслова не утворюють дифтонгу \n в першій та другій особі множини :)",
                            " dOrmir \n dUErmo \n dUErmes \n dUErme \n dOrmemos \n dOrmís \n dUErmen",
                            " PODER = мігти \n PENSAR = думати \n JUGAR = грати")

def menu_button5():
    global menu_mode, language
    if menu_mode:
        exercice5()
    else:
        if language == 1:
            open_a_lesson(  "    Avec les verbes affaiblissement c'est pareil que avec \n ceux à diphtongue: on ne peut pas le reconnaître. Mais dès \n que l'on connaît que un verbe est affaiblissement il est \n très simple de le conjuguer: en echangeant le I et le E \n (sauf pour nous et vous, comme pour la diphtongue). \n Il est aussi important de noter que un verbe pronominal \n peut être à diphtongue (comme dormirse = s'endormir) ou \n affaiblissement (comme vestirse = se vêtir/s'habiller).",
                            "EXEMPLE: \n   pEdIr \n   pIdO \n   pIdES \n   pIdE \n   pEdIMOS \n   pEdÍS \n   pIdEN",
                            "MEDIR = mesurer \n VESTIR = vêtir/habiller \n PEDIR = demander")
        elif language == 2:
            open_a_lesson(  "    Зі слабкими дієсловами все так само, як і з дієсловами \n з дифтонгом: їх важко впізнати. Але якщо ми знаємо, що \n дієслово є слабким, його дуже легко спрямовувати: ми \n міняємо I на E (за винятком для нас та вас, так само, як \n для дифтонгу). Також важливо зауважити, що \n займенникове дієслово може мати дифтонг \n (як dormirse = засипати) або слабку голосну \n (як vestirse = одягатися).",
                            "ПРИКЛАД: \n   pEdIr \n   pIdO \n   pIdES \n   pIdE \n   pEdIMOS \n   pEdÍS \n   pIdEN",
                            "MEDIR = вимірювати \n VESTIR = одягати \n PEDIR = просити")

def menu_button6():
    global menu_mode, language
    if menu_mode:
        exercice6()
    else:
        if language == 1:
            open_a_lesson(  "    On étudie deux formes d'impératif: toi et vous. Pour la \n première il suffit de mettre le verbe à la 3ème du \n singulier. Pour la deuxième on utilise la formule \n V à'linfinitif - R + D. Voilà quelques exemples:",
                            " BEBER (boire) -> bebe / bebed \n CAMINAR (marcher/cheminer) -> camina / caminad \n SALIR (sortir) -> sale / salid")
        elif language == 2:
            open_a_lesson(  "    Ми вивчаємо дві форми імперативу: для тебе та вас. \n Для першої достатньо поставити дієслово у 3-й особі \n однини. Для другої використовується формула дієслово \n в інфінітиві - R + D. Ось кілька прикладів:",
                            " BEBER (пити) -> bebe / bebed \n CAMINAR (йти) -> camina / caminad \n SALIR (вийти) -> sale / salid")

def menu_button7():
    global menu_mode, language
    if menu_mode:
        exercice7()
    else:
        if language == 1:
            open_a_lesson(  "    On utilise SER pour décrire quelquechose qui ne change \n pas (ou rarement), comme une maladie chronique, une \n nationalité (et d'où on vient), un métier, mais aussi dire \n l'endroit où se trouve une capitale, un anniversaire, quelle \n heure il est, comment est la météo ou encore qui est \n mon (meilleur) ami.",
                            "  Quant à ESTAR, on l'utilise pour décrire quelquechose qui \n change, comme une humeur ou un sentiment, l'état d'un \n lieu, là où quelquechose ou quelqun se trouve, etc...")
        elif language == 2:
            open_a_lesson(  "    Ми використовуємо 'бути' (SER) для опису чогось, що \n не змінюється (або рідко змінюється), наприклад, \n хронічна хвороба, національність (і місце народження), \n професія, а також для вказівки на місце розташування \n столиці, дату народження, час, погодні умови або \n навіть, хто мій (найкращий) друг.",
                            "  Щодо ESTAR, його використовують для опису чогось \n змінного, такого як настрій чи почуття, стан місця, \n де щось або хтось знаходиться, тощо.")

def menu_button8():
    global menu_mode, language
    if menu_mode:
        exercice8()
    else:
        if language == 1:
            open_a_lesson(  "    Il faudra aussi apprendre les chiffres: de 0 à 29 sont \n irréguliés. Puis, il suffira d'apprendre 30, 40, 50, etc... \n et rajouter 'y' puis le nombre d'unités, que tu auras appri. \n C'est pareil pour les centaines, les milliers, \n les millions, etc...",
                            " 0 = zero \n 1 = uno \n 2 = dos \n 3 = tres \n 4 = quatro \n 5 = cinco \n 6 = seis \n 7 = siete \n 8 = ocho \n 9 = nueve",
                            " 10 = diez \n 11 = once \n 12 = doce \n 13 = trece \n 14 = catorce \n 15 = quince \n 16 = dieciséis \n 17 = diecisiete \n 18 = dieciocho \n 19 = diecinueve",
                            " 20 = veinte \n 21 = ventiuno \n 22 = ventidós \n 23 = ventitrés \n 24 = ventiquatro \n 25 = venticinco \n 26 = ventiséis \n 27 = ventisiete \n 28 = ventiocho \n 29 = ventinueve",
                            " 30 = trienta \n 40 = cuatenta \n 50 = cincuenta \n 60 = sesenta \n 70 = setenta \n 80 = ochenta \n 90 = noventa \n 100 = cien \n 1 000 = mil \n 1 000 000 = millón")
        elif language == 2:
            open_a_lesson(  "    Тобі також доведеться вивчити цифри: від 0 до 29 \n неправильні. Потім, треба буде тільки вивчити \n цифри 30, 40, 50... , написати 'y' та кількість одиниць, що \n ти вивчив/чила. Теж саме для сотень, тисач, мілліонів і \n так далі.",
                            " 0 = zero \n 1 = uno \n 2 = dos \n 3 = tres \n 4 = quatro \n 5 = cinco \n 6 = seis \n 7 = siete \n 8 = ocho \n 9 = nueve",
                            " 10 = diez \n 11 = once \n 12 = doce \n 13 = trece \n 14 = catorce \n 15 = quince \n 16 = dieciséis \n 17 = diecisiete \n 18 = dieciocho \n 19 = diecinueve",
                            " 20 = veinte \n 21 = ventiuno \n 22 = ventidós \n 23 = ventitrés \n 24 = ventiquatro \n 25 = venticinco \n 26 = ventiséis \n 27 = ventisiete \n 28 = ventiocho \n 29 = ventinueve",
                            " 30 = trienta \n 40 = cuatenta \n 50 = cincuenta \n 60 = sesenta \n 70 = setenta \n 80 = ochenta \n 90 = noventa \n 100 = cien \n 1 000 = mil \n 1 000 000 = millón")

def menu_button9():
    global menu_mode, language
    if menu_mode:
        exercice9()
    else:
        if language == 1:
            open_a_lesson(  " Il te faudra aussi apprendre une douzaine de pays (deux \n par continent), pour la culture générale. Les voici :)",
                            "    América del Sur = Amérique du Sud \n Perú = Pérou \n Chile = Chili \n \n    América del Norte = Amérique du Nord \n Estados Unidos = Etats Unis d'Amérique \n Canada = Canadá \n",
                            "    África = Afrique \n Marruecos = Maroque \n Algeria = Algérie \n \n   Oceanía = Océanie \n Australia = Australie \n Nueva Zelanda = Nouvelle Zélande",
                            "    Europa = Europe \n España = Espagne \n Francia = France \n \n    Asia = Asie \n China = Chine \n India = Inde")
        elif language == 2:
            open_a_lesson(  " Тобі також доведеться вивчити з десяток країн (дві на \n континент). Ось вони:",
                            "    América del Sur = Південна Америка \n Perú = Перу \n Chile = Чілі \n \n    América del Norte = Північна Америка \n Estados Unidos = Сполучені Штати Америки \n Канада = Canadá \n",
                            "    África = Африка \n Marruecos = Марокко \n Algeria = Алжерія \n \n   Oceanía = Океанія \n Australia = Австралія \n Nueva Zelanda = Нова Зеландія",
                            "    Europa = Європа\n España = Іспанія \n Francia = Франція \n \n    Asia = Азія \n China = Китай \n India = Індія")

def menu_button10():
    global menu_mode, language
    if menu_mode:
        exercice10()
    else:
        if language == 1:
            open_a_lesson(  "    Il est très simple de mettre un mot au pluriel, si l'on \n connaît la règle. Premièrement, il faut le faire pour \n son article: 'la' devient 'las' et 'el' devient 'los'. \n Après avoir fait cela on passe au nom. S'il se termine \n par une voyelle, il suffit juste de mettre 's' à la fin de \n ce mot. S'il se termine par un 'z' on l'enlève on met \n 'ces' à la place. Et si ce mot se termine par toute autre \n consonne on lui colle 'es'. Il est aussi important de noter \n que 'un' et 'una' ne se mettent pas au pluriel, on n'écrit \n rien. Voilà quelques exemles:",
                            "la abuela -> las abuelas \n el perro -> los perros \n la madre -> las madres \n \n la edad -> las edades \n el lugar -> los lugares \n el móvil -> los moviles \n \n el lápiz -> los lapices \n la nariz -> las narices \n la voz -> las voces")
        elif language == 2:
            open_a_lesson(  "    Поставити слово у множину це дуже просто, якщо ти \n знаєш правило. Спочатку потрібно змінити його артикль: 'la' \n стає 'las', а 'el' стає 'los'. Після цього переходимо \n до іменника. Якщо він закінчується на голосну, просто \n додаємо 's' в кінець цього слова. Якщо він закінчується \n на 'z', ми видаляємо 'z' і ставимо 'ces' на його місце. І \n якщо це слово закінчується на будь-яку іншу приголосну, \n ми додаємо до нього 'es'. Також важливо зазначити, що \n 'un' і 'una' не утворюють множини, ми не пишемо нічого. \n Ось кілька прикладів:",
                            "la abuela -> las abuelas \n el perro -> los perros \n la madre -> las madres \n \n la edad -> las edades \n el lugar -> los lugares \n el móvil -> los moviles \n \n el lápiz -> los lapices \n la nariz -> las narices \n la voz -> las voces")

def menu_button11():
    global menu_mode, language
    if menu_mode:
        exercice11()
    else:
        if language == 1:
            open_a_lesson(  " Lunes = Lundi \n Martes = Mardi \n Miércoles = Mercredi \n Jueves = Jeudi \n Viernes = Vendredi \n Sábado = Samedi \n Domingo = Dimanche",
                            " Enero = Janvier \n Febrero = Février \n Marzo = Mars \n Abril = Avril \n Mayo = Mai \n Junio = Juin",
                            " Julio = Juillet \n Agosto = Août \n Septiembre = Septembre \n Octubre = Octobre \n Noviembre = Novembre \n Diciembre = Décembre",
                            " El invierno = L'hiver \n La primavera = Le printemps \n El verano = L'été \n El otoño = L'automne")
        elif language == 2:
            open_a_lesson(  " Lunes = Понеділок \n Martes = Вівторок \n Miércoles = Середа \n Jueves = Четвер \n Viernes = П'ятниця \n Sábado = Субота \n Domingo = Неділя",
                            " Enero = Січень \n Febrero = Лютий \n Marzo = Березень \n Abril = Квітень \n Mayo = Травень \n Junio = Червень",
                            " Julio = Липень \n Agosto = Січень \n Septiembre = Вересень \n Octubre = Жовтень \n Noviembre = Листопад \n Diciembre = Грудень",
                            " El invierno = Зима \n La primavera = Весна \n El verano = Літо \n El otoño = Осінь")


# 4 answer buttons

def ans_button1_clicked():
    global answer_verification
    answer_verification(1)

def ans_button2_clicked():
    global answer_verification
    answer_verification(2)

def ans_button3_clicked():
    global answer_verification
    answer_verification(3)

def ans_button4_clicked():
    global answer_verification
    answer_verification(4)


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
button12.clicked.connect(test_exercice)

change_of_language_button.clicked.connect(next_language)
ok_button.clicked.connect(ok_button_clicked)
send_answer_button.clicked.connect(answer_verification)
next_button.clicked.connect(next_page_of_lesson)

ans_button1.clicked.connect(ans_button1_clicked)
ans_button2.clicked.connect(ans_button2_clicked)
ans_button3.clicked.connect(ans_button3_clicked)
ans_button4.clicked.connect(ans_button4_clicked)

quit_button.clicked.connect(finish_exercice)
menu_mode_button.clicked.connect(menu_mode_button_clicked)


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

layout3.addWidget(change_of_language_button, alignment = Qt.AlignCenter)

bottom_comments_layout.addWidget(bottom_comments_label,  alignment = Qt.AlignCenter)
layout2.addWidget(ok_button,  alignment = Qt.AlignCenter)

ans_layout1.addWidget(ans_button1, alignment = Qt.AlignCenter)
ans_layout1.addWidget(ans_button2, alignment = Qt.AlignCenter)
ans_layout2.addWidget(ans_button3, alignment = Qt.AlignCenter)
ans_layout2.addWidget(ans_button4, alignment = Qt.AlignCenter)

ans_layout2.addWidget(answer_line, alignment = Qt.AlignCenter)
ans_layout2.addWidget(next_button, alignment = Qt.AlignCenter)
ans_layout2.addWidget(send_answer_button, alignment = Qt.AlignCenter)

top_layout.addWidget(menu_mode_button, alignment = Qt.AlignCenter)
top_layout.addWidget(quit_button, alignment = Qt.AlignCenter)
top_layout.addWidget(nothing1, alignment = Qt.AlignCenter)
top_layout.addWidget(top_of_screen, alignment = Qt.AlignCenter)
top_layout.addWidget(stats, alignment = Qt.AlignCenter)
top_layout.addWidget(nothing2, alignment = Qt.AlignCenter)

top_comments_layout.addWidget(top_comments_label, alignment = Qt.AlignCenter)


# Connecting layouts

main_layout.addLayout(top_layout)
main_layout.addLayout(top_comments_layout)
main_layout.addLayout(bottom_comments_layout)
main_layout.addLayout(ans_layout1)
main_layout.addLayout(ans_layout2)
main_layout.addLayout(layout1)
main_layout.addLayout(layout2)
main_layout.addLayout(layout3)

main_win.setLayout(main_layout)
main_win.show()

app.exec()