from random import randint
print("¡Entrenamientos depresente de indicativo y vocabulario de español!")
print("Programa de 5to grado.")
print(" ")
def uno():
    on = randint(1, 6)
    if on == 1:
        on = randint(1, 3)
        if on == 1:
            ono("Vivir con yo.", "vives", "vivir", "vivimos", "vivo")
        elif on == 2:
            ono("Hablar con yo.", "hablas", "hablar", "hablamos", "hablo")
        else:
            ono("Comer con yo.", "comas", "comer", "comemos", "como")
    elif on == 2:
        on = randint(1, 3)
        if on == 1:
            ono("Vivir con tú.", "vivo", "vivir", "vivimos", "vives")
        elif on == 2:
            ono("Hablar con tú.", "hablo", "hablar", "hablamos", "hablas")
        else:
            ono("Comer con tú.", "como", "comer", "comemos", "comes")
    elif on == 3:
        on = randint(1, 5)
        if on == 1:
            on = randint(1, 3)
            if on == 1:
                ono("Vivir con él.", "vivo", "vivi", "vivimos", "vive")
            elif on == 2:
                ono("Hablar con él.", "hablo", "hablar", "hablamos", "habla")
            else:
                ono("Comer con él.", "como", "comer", "comemos", "come")
        elif on == 2:
            on = randint(1, 3)
            if on == 1:
                ono("Vivir con ella.", "vivo", "vivi", "vivimos", "vive")
            elif on == 2:
                ono("Hablar con ella.", "hablo", "hablar", "hablamos", "habla")
            else:
                ono("Comer con ella.", "como", "comer", "comemos", "come")
        elif on == 3:
            on = randint(1, 3)
            if on == 1:
                ono("Vivir con Juan.", "vivo", "vivi", "vivimos", "vive")
            elif on == 2:
                ono("Hablar con Juan.", "hablo", "hablar", "hablamos", "habla")
            else:
                ono("Comer con Juan.", "como", "comer", "comemos", "come")
        elif on == 4:
            on = randint(1, 3)
            if on == 1:
                ono("Vivir con Carla.", "vivo", "vivi", "vivimos", "vive")
            elif on == 2:
                ono("Hablar con Carla.", "hablo", "hablar", "hablamos", "habla")
            else:
                ono("Comer con Carla.", "como", "comer", "comemos", "come")
        else:
            on = randint(1, 3)
            if on == 1:
                ono("Vivir con usted.", "vivo", "vivi", "vivimos", "vive")
            elif on == 2:
                ono("Hablar con usted.", "hablo", "hablar", "hablamos", "habla")
            else:
                ono("Comer con usted.", "como", "comer", "comemos", "come")
    elif on == 4:
        on = randint(1, 2)
        if on == 1:
            on = randint(1, 3)
            if on == 1:
                ono("Vivir con nosotros.", "vivo", "vivir", "vives", "vivimos")
            elif on == 2:
                ono("Hablar con nosotros.", "hablo", "hablar", "hablas", "hablamos")
            else:
                ono("Comer con nosotros.", "como", "comer", "comes", "comemos")
        else:
            on = randint(1, 3)
            if on == 1:
                ono("Vivir con nosotras.", "vivo", "vivir", "vives", "vivimos")
            elif on == 2:
                ono("Hablar con nosotras.", "hablo", "hablar", "hablas", "hablamos")
            else:
                ono("Comer con nosotras.", "como", "comer", "comes", "comemos")
    elif on == 5:
        on = randint(1, 2)
        if on == 1:
            on = randint(1, 3)
            if on == 1:
                ono("Vivir con vosotros.", "vivo", "vivir", "vives", "vivís")
            elif on == 2:
                ono("Hablar con vosotros.", "hablo", "hablar", "hablas", "habláis")
            else:
                ono("Comer con vosotros.", "como", "comer", "comes", "coméis")
        else:
            on = randint(1, 3)
            if on == 1:
                ono("Vivir con vosotras.", "vivo", "vivir", "vives", "vivís")
            elif on == 2:
                ono("Hablar con vosotras.", "hablo", "hablar", "hablas", "habláis")
            else:
                ono("Comer con vosotras.", "como", "comer", "comes", "coméis")
    else:
        on = randint(1, 4)
        if on == 1:
            on = randint(1, 3)
            if on == 1:
                ono("Vivir con ellos.", "vivo", "vivimos", "vives", "viven")
            elif on == 2:
                ono("Hablar con ellos.", "hablo", "hablamos", "hablas", "hablan")
            else:
                ono("Comer con ellos.", "como", "comemos", "comes", "comen")
        elif on == 2:
            on = randint(1, 3)
            if on == 1:
                ono("Vivir con ellas.", "vivo", "vivimos", "vives", "viven")
            elif on == 2:
                ono("Hablar con ellas.", "hablo", "hablamos", "hablas", "hablan")
            else:
                ono("Comer con ellas.", "como", "comemos", "comes", "comen")
        elif on == 3:
            on = randint(1, 3)
            if on == 1:
                ono("Vivir con Carla y Juan.", "vivo", "vivimos", "vives", "viven")
            elif on == 2:
                ono("Hablar con Carla y Juan.", "hablo", "hablamos", "hablas", "hablan")
            else:
                ono("Comer con Carla y Juan.", "como", "comemos", "comes", "comen")
        else:
            on = randint(1, 3)
            if on == 1:
                ono("Vivir con ustedes.", "vivo", "vivimos", "vives", "viven")
            elif on == 2:
                ono("Hablar con ustedes.", "hablo", "hablamos", "hablas", "hablan")
            else:
                ono("Comer con ustedes.", "como", "comemos", "comes", "comen")
def dos():
    on = randint(1, 6)
    if on == 1:
        on = randint(1, 3)
        if on == 1:
            ono("Tener con yo.", "tiene", "tener", "tenemos", "tengo")
        elif on == 2:
            ono("Ser con yo.", "es", "ser", "somos", "soy")
        else:
            ono("Ir con yo.", "va", "ir", "vamos", "voy")
    elif on == 2:
        on = randint(1, 3)
        if on == 1:
            ono("Tener con yo.", "tiene", "tener", "tenemos", "tengo")
        elif on == 2:
            ono("Ser con yo.", "es", "ser", "somos", "soy")
        else:
            ono("Ir con yo.", "va", "ir", "vamos", "voy")
    elif on == 3:
        on = randint(1, 5)
        if on == 1:
            on = randint(1, 3)
            if on == 1:
                ono("Tener con él.", "tengo", "tener", "tenemos", "tiene")
            elif on == 2:
                ono("Ser con él.", "soy", "ser", "somos", "es")
            else:
                ono("Ir con él.", "voy", "ir", "vamos", "va")
        elif on == 2:
            on = randint(1, 3)
            if on == 1:
                ono("Tener con ella.", "tengo", "tener", "tenemos", "tiene")
            elif on == 2:
                ono("Ser con ella.", "soy", "ser", "somos", "es")
            else:
                ono("Ir con ella.", "voy", "ir", "vamos", "va")
        elif on == 3:
            on = randint(1, 3)
            if on == 1:
                ono("Tener con Juan.", "tengo", "tener", "tenemos", "tiene")
            elif on == 2:
                ono("Ser con Juan.", "soy", "ser", "somos", "es")
            else:
                ono("Ir con Juan.", "voy", "ir", "vamos", "va")
        elif on == 4:
            on = randint(1, 3)
            if on == 1:
                ono("Tener con Carla.", "tengo", "tener", "tenemos", "tiene")
            elif on == 2:
                ono("Ser con Carla.", "soy", "ser", "somos", "es")
            else:
                ono("Ir con Carla.", "voy", "ir", "vamos", "va")
        else:
            on = randint(1, 3)
            if on == 1:
                ono("Tener con usted.", "tengo", "tener", "tenemos", "tiene")
            elif on == 2:
                ono("Ser con usted.", "soy", "ser", "somos", "es")
            else:
                ono("Ir con usted.", "voy", "ir", "vamos", "va")
    elif on == 4:
        on = randint(1, 2)
        if on == 1:
            on = randint(1, 3)
            if on == 1:
                ono("Tener con nosotros.", "tengo", "tener", "tienes", "tenemos")
            elif on == 2:
                ono("Ser con nosotros.", "soy", "ser", "eres", "somos")
            else:
                ono("Ir con nosotros.", "voy", "ir", "vas", "vamos")
        else:
            on = randint(1, 3)
            if on == 1:
                ono("Tener con nosotras.", "tengo", "tener", "tienes", "tenemos")
            elif on == 2:
                ono("Ser con nosotras.", "soy", "ser", "eres", "somos")
            else:
                ono("Ir con nosotras.", "voy", "ir", "vas", "vamos")
    elif on == 5:
        on = randint(1, 2)
        if on == 1:
            on = randint(1, 3)
            if on == 1:
                ono("Tener con vosotros.", "tengo", "tener", "tienes", "teneis")
            elif on == 2:
                ono("Ser con vosotros.", "soy", "ser", "eres", "sois")
            else:
                ono("Ir con vosotros.", "voy", "ir", "vas", "vais")
        else:
            on = randint(1, 3)
            if on == 1:
                ono("Tener con vosotras.", "tengo", "tener", "tienes", "teneis")
            elif on == 2:
                ono("Ser con vosotras.", "soy", "ser", "eres", "sois")
            else:
                ono("Ir con vosotras.", "voy", "ir", "vas", "vais")
    else:
        on = randint(1, 4)
        if on == 1:
            on = randint(1, 3)
            if on == 1:
                ono("Tener con ellos.", "tengo", "tener", "tienes", "tienen")
            elif on == 2:
                ono("Ser con ellos.", "soy", "ser", "eres", "son")
            else:
                ono("Ir con ellos.", "voy", "ir", "vas", "van")
        elif on == 2:
            on = randint(1, 3)
            if on == 1:
                ono("Tener con ellas.", "tengo", "tener", "tienes", "tienen")
            elif on == 2:
                ono("Ser con ellas.", "soy", "ser", "eres", "son")
            else:
                ono("Ir con ellas.", "voy", "ir", "vas", "van")
        elif on == 3:
            on = randint(1, 3)
            if on == 1:
                ono("Tener con Carla y Juan.", "tengo", "tener", "tienes", "tienen")
            elif on == 2:
                ono("Ser con Carla y Juan.", "soy", "ser", "eres", "son")
            else:
                ono("Ir con Carla y Juan.", "voy", "ir", "vas", "van")
        else:
            on = randint(1, 3)
            if on == 1:
                ono("Tener con ustedes.", "tengo", "tener", "tienes", "tienen")
            elif on == 2:
                ono("Ser con ustedes.", "soy", "ser", "eres", "son")
            else:
                ono("Ir con ustedes.", "voy", "ir", "vas", "van")
def tres():
    on = randint(1, 6)
    if on == 1:
        on = randint(1, 3)
        if on == 1:
            ono("Dormirse con yo.", "te duermes", "se duerme", "nos dormemos", "me duermo")
        elif on == 2:
            ono("Llamarse con yo.", "te llamas", "se llama", "nos llamamos", "me llamo")
        else:
            ono("Levantarse con yo.", "te levantas", "se levanta", "nos levantamos", "me levantamo")
    elif on == 2:
        on = randint(1, 3)
        if on == 1:
            ono("Dormirse con tú.", "se duerme", "nos dormemos", "me duermo", "te duermes")
        elif on == 2:
            ono("Llamarse con tú.", "se llama", "nos llamamos", "me llamo", "te llamas")
        else:
            ono("Levantarse con tú.", "se levanta", "nos levantamos", "me levantamo", "te levantas")
    elif on == 3:
        on = randint(1, 5)
        if on == 1:
            on = randint(1, 3)
            if on == 1:
                ono("Dormirse con él.", "te duermes", "nos dormemos", "me duermo", "se duerme")
            elif on == 2:
                ono("Llamarse con él.", "te llamas", "nos llamamos", "me llamo", "se llama")
            else:
                ono("Levantarse con él.", "te levantas", "nos levantamos", "me levantamo", "se levanta")
        elif on == 2:
            on = randint(1, 3)
            if on == 1:
                ono("Dormirse con ella.", "te duermes", "nos dormemos", "me duermo", "se duerme")
            elif on == 2:
                ono("Llamarse con ella.", "te llamas", "nos llamamos", "me llamo", "se llama")
            else:
                ono("Levantarse con ella.", "te levantas", "nos levantamos", "me levantamo", "se levanta")
        elif on == 3:
            on = randint(1, 3)
            if on == 1:
                ono("Dormirse con Juan.", "te duermes", "nos dormemos", "me duermo", "se duerme")
            elif on == 2:
                ono("Llamarse con Juan.", "te llamas", "nos llamamos", "me llamo", "se llama")
            else:
                ono("Levantarse con Juan.", "te levantas", "nos levantamos", "me levantamo", "se levanta")
        elif on == 4:
            on = randint(1, 3)
            if on == 1:
                ono("Dormirse con Carla.", "te duermes", "nos dormemos", "me duermo", "se duerme")
            elif on == 2:
                ono("Llamarse con Carla.", "te llamas", "nos llamamos", "me llamo", "se llama")
            else:
                ono("Levantarse con Carla.", "te levantas", "nos levantamos", "me levantamo", "se levanta")
        else:
            on = randint(1, 3)
            if on == 1:
                ono("Dormirse con usted.", "te duermes", "nos dormemos", "me duermo", "se duerme")
            elif on == 2:
                ono("Llamarse con usted.", "te llamas", "nos llamamos", "me llamo", "se llama")
            else:
                ono("Levantarse con usted.", "te levantas", "nos levantamos", "me levantamo", "se levanta")
    elif on == 4:
        on = randint(1, 2)
        if on == 1:
            on = randint(1, 3)
            if on == 1:
                ono("Dormirse con nosotros.", "te duermes", "se duerme", "me duermo", "nos dormemos")
            elif on == 2:
                ono("Llamarse con nosotros.", "te llamas", "se llama", "me llamo", "nos llamamos")
            else:
                ono("Levantarse con nosotros.", "te levantas", "se levanta", "me levantamo", "nos levantamos")
        else:
            on = randint(1, 3)
            if on == 1:
                ono("Dormirse con nosotras.", "te duermes", "se duerme", "me duermo", "nos dormemos")
            elif on == 2:
                ono("Llamarse con nosotras.", "te llamas", "se llama", "me llamo", "nos llamamos")
            else:
                ono("Levantarse con nosotras.", "te levantas", "se levanta", "me levantamo", "nos levantamos")
    elif on == 5:
        on = randint(1, 2)
        if on == 1:
            on = randint(1, 3)
            if on == 1:
                ono("Dormirse con vosotros.", "te duermes", "se duerme", "nos dormemos", "os dormís")
            elif on == 2:
                ono("Llamarse con vosotros.", "te llamas", "se llama", "nos llamamos", "os llamáis")
            else:
                ono("Levantarse con vosotros.", "te levantas", "se levanta", "nos levantamos", "os levantáis")
        else:
            on = randint(1, 3)
            if on == 1:
                ono("Dormirse con vosotras.", "te duermes", "se duerme", "nos dormemos", "os dormís")
            elif on == 2:
                ono("Llamarse con vosotras.", "te llamas", "se llama", "nos llamamos", "os llamáis")
            else:
                ono("Levantarse con vosotras.", "te levantas", "se levanta", "nos levantamos", "os levantáis")
    else:
        on = randint(1, 4)
        if on == 1:
            on = randint(1, 3)
            if on == 1:
                ono("Dormirse con ellos.", "te duermes", "se duerme", "nos dormemos", "se duermen")
            elif on == 2:
                ono("Llamarse con ellos.", "te llamas", "se llama", "nos llamamos", "se llaman")
            else:
                ono("Levantarse con ellos.", "te levantas", "se levanta", "nos levantamos", "se levantaman")
        elif on == 2:
            on = randint(1, 3)
            if on == 1:
                ono("Dormirse con ellas.", "te duermes", "se duerme", "nos dormemos", "se duermen")
            elif on == 2:
                ono("Llamarse con ellas.", "te llamas", "se llama", "nos llamamos", "se llaman")
            else:
                ono("Levantarse con ellas.", "te levantas", "se levanta", "nos levantamos", "se levantaman")
        elif on == 3:
            on = randint(1, 3)
            if on == 1:
                ono("Dormirse con Carla y Juan.", "te duermes", "se duerme", "nos dormemos", "se duermen")
            elif on == 2:
                ono("Llamarse con Carla y Juan.", "te llamas", "se llama", "nos llamamos", "se llaman")
            else:
                ono("Levantarse con Carla y Juan.", "te levantas", "se levanta", "nos levantamos", "se levantaman")
        else:
            on = randint(1, 3)
            if on == 1:
                ono("Dormirse con ustedes.", "te duermes", "se duerme", "nos dormemos", "se duermen")
            elif on == 2:
                ono("Llamarse con ustedes.", "te llamas", "se llama", "nos llamamos", "se llaman")
            else:
                ono("Levantarse con ustedes.", "te levantas", "se levanta", "nos levantamos", "se levantaman")  
def cuatro():
    on = randint(1, 6)
    if on == 1:
        on = randint(1, 3)
        if on == 1:
            ono("Poder con yo.", "podo", "puedes", "podoy", "puedo")
        elif on == 2:
            ono("Pensar con yo.", "penso", "piensas", "pensoy", "pienso")
        else:
            ono("Jugar con yo.", "jugo", "juegas", "jugoy", "juego")
    elif on == 2:
        on = randint(1, 3)
        if on == 1:
            ono("Poder con tú.", "podes", "podoy", "puedo", "puedes")
        elif on == 2:
            ono("Pensar con tú.", "pensas", "pensoy", "pienso", "piensas")
        else:
            ono("Jugar con tú.", "jugas", "jugoy", "juego", "juegas")
    elif on == 3:
        on = randint(1, 5)
        if on == 1:
            on = randint(1, 3)
            if on == 1:
                ono("Poder con él.", "podo", "podoy", "puedo", "puede")
            elif on == 2:
                ono("Pensar con él.", "penso", "pensoy", "pienso", "piensa")
            else:
                ono("Jugar con él.", "jugo", "jugoy", "juego", "juega")
        elif on == 2:
            on = randint(1, 3)
            if on == 1:
                ono("Poder con ella.", "podo", "podoy", "puedo", "puede")
            elif on == 2:
                ono("Pensar con ella.", "penso", "pensoy", "pienso", "piensa")
            else:
                ono("Jugar con ella.", "jugo", "jugoy", "juego", "juega")
        elif on == 3:
            on = randint(1, 3)
            if on == 1:
                ono("Poder con usted.", "podo", "podoy", "puedo", "puede")
            elif on == 2:
                ono("Pensar con usted.", "penso", "pensoy", "pienso", "piensa")
            else:
                ono("Jugar con usted.", "jugo", "jugoy", "juego", "juega")
        elif on == 4:
            on = randint(1, 3)
            if on == 1:
                ono("Poder con Carla.", "podo", "podoy", "puedo", "puede")
            elif on == 2:
                ono("Pensar con Carla.", "penso", "pensoy", "pienso", "piensa")
            else:
                ono("Jugar con Carla.", "jugo", "jugoy", "juego", "juega")
        else:
            on = randint(1, 3)
            if on == 1:
                ono("Poder con Juan.", "podo", "podoy", "puedo", "puede")
            elif on == 2:
                ono("Pensar con Juan.", "penso", "pensoy", "pienso", "piensa")
            else:
                ono("Jugar con Juan.", "jugo", "jugoy", "juego", "juega")
    elif on == 4:
        on = randint(1, 2)
        if on == 1:
            on = randint(1, 3)
            if on == 1:
                ono("Poder con nosotros.", "puedemos", "puedéis", "podéis", "podemos")
            elif on == 2:
                ono("Pensar con nosotros.", "piensamos", "piensáis", "pensáis", "pensamos")
            else:
                ono("Jugar con nosotros.", "juegamos", "juegáis", "jugáis", "jugamos")
        else:
            on = randint(1, 3)
            if on == 1:
                ono("Poder con nosotras.", "puedemos", "puedéis", "podéis", "podemos")
            elif on == 2:
                ono("Pensar con nosotras.", "piensamos", "piensáis", "pensáis", "pensamos")
            else:
                ono("Jugar con nosotras.", "juegamos", "juegáis", "jugáis", "jugamos")
    elif on == 5:
        on = randint(1, 2)
        if on == 1:
            on = randint(1, 3)
            if on == 1:
                ono("Poder con vosotros.", "puedemos", "puedéis", "podemos", "podéis")
            elif on == 2:
                ono("Pensar con vosotros.", "piensamos", "piensáis", "pensamos", "pensáis")
            else:
                ono("Jugar con vosotros.", "juegamos", "juegáis", "jugamos", "jugáis")
        else:
            on = randint(1, 3)
            if on == 1:
                ono("Poder con vosotras.", "puedemos", "puedéis", "podemos", "podéis")
            elif on == 2:
                ono("Pensar con vosotras.", "piensamos", "piensáis", "pensamos", "pensáis")
            else:
                ono("Jugar con vosotras.", "juegamos", "juegáis", "jugamos", "jugáis")
    else:
        on = randint(1, 4)
        if on == 1:
            on = randint(1, 3)
            if on == 1:
                ono("Poder con ellos.", "puedemos", "podemos", "poden", "pueden")
            elif on == 2:
                ono("Pensar con ellos.", "piensamos", "pensamos", "pensan", "piensan")
            else:
                ono("Jugar con ellos.", "juegamos", "jugamos", "jugan", "juegan")
        elif on == 2:
            on = randint(1, 3)
            if on == 1:
                ono("Poder con ellas.", "puedemos", "podemos", "poden", "pueden")
            elif on == 2:
                ono("Pensar con ellas.", "piensamos", "pensamos", "pensan", "piensan")
            else:
                ono("Jugar con ellas.", "juegamos", "jugamos", "jugan", "juegan")
        elif on == 3:
            on = randint(1, 3)
            if on == 1:
                ono("Poder con ustedes.", "puedemos", "podemos", "poden", "pueden")
            elif on == 2:
                ono("Pensar con ustedes.", "piensamos", "pensamos", "pensan", "piensan")
            else:
                ono("Jugar con ustedes.", "juegamos", "jugamos", "jugan", "juegan")
        else:
            on = randint(1, 3)
            if on == 1:
                ono("Poder con Carla y Juan.", "puedemos", "podemos", "poden", "pueden")
            elif on == 2:
                ono("Pensar con Carla y Juan.", "piensamos", "pensamos", "pensan", "piensan")
            else:
                ono("Jugar con Carla y Juan.", "juegamos", "jugamos", "jugan", "juegan")
def cinco():
    on = randint(1, 6)
    if on == 1:
        on = randint(1, 2)
        if on == 1:
            ono("Medir con yo.", "medo", "mides", "medes", "mido")
        else:
            ono("Vestir con yo.", "vesto", "vistes", "vestes", "visto")
    elif on == 2:
        on = randint(1, 2)
        if on == 1:
            ono("Medir con tú.", "medo", "medes", "mido", "mides")
        else:
            ono("Vestir con tú.", "vesto", "vestes", "visto", "vistes")
    elif on == 3:
        on = randint(1, 5)
        if on == 1:
            on = randint(1, 2)
            if on == 1:
                ono("Medir con él.", "medo", "mido", "mede", "mide")
            else:
                ono("Vestir con él.", "vesto", "visto", "veste", "viste")
        elif on == 2:
            on = randint(1, 2)
            if on == 1:
                ono("Medir con ella.", "medo", "mido", "mede", "mide")
            else:
                ono("Vestir con ella.", "vesto", "visto", "veste", "viste")
        elif on == 3:
            on = randint(1, 2)
            if on == 1:
                ono("Medir con Carla.", "medo", "mido", "mede", "mide")
            else:
                ono("Vestir con Carla.", "vesto", "visto", "veste", "viste")
        elif on == 4:
            on = randint(1, 2)
            if on == 1:
                ono("Medir con Juan.", "medo", "mido", "mede", "mide")
            else:
                ono("Vestir con Juan.", "vesto", "visto", "veste", "viste")
        else:
            on = randint(1, 2)
            if on == 1:
                ono("Medir con usted.", "medo", "mido", "mede", "mide")
            else:
                ono("Vestir con usted.", "vesto", "visto", "veste", "viste")
    elif on == 4:
        on = randint(1, 2)
        if on == 1:
            on = randint(1, 2)
            if on == 1:
                ono("Medir con nosotros.", "medís", "midemos", "midéis", "medimos")
            else:
                ono("Vestir con nosotros.", "vestís", "vistemos", "vistéis", "vestimos")
        else:
            on = randint(1, 2)
            if on == 1:
                ono("Medir con nosotros.", "medís", "midemos", "midéis", "medimos")
            else:
                ono("Vestir con nosotros.", "vestís", "vistemos", "vistéis", "vestimos")
    elif on == 5:
        on = randint(1, 2)
        if on == 1:
            on = randint(1, 2)
            if on == 1:
                ono("Medir con vosotros.", "midemos", "midéis", "medimos", "medís")
            else:
                ono("Vestir con vosotros.", "vistemos", "vistéis", "vestimos", "vestís")
        else:
            on = randint(1, 2)
            if on == 1:
                ono("Medir con vosotros.", "midemos", "midéis", "medimos", "medís")
            else:
                ono("Vestir con vosotros.", "vistemos", "vistéis", "vestimos", "vestís")
    else:
        on = randint(1, 4)
        if on == 1:
            on = randint(1, 2)
            if on == 1:
                ono("Medir con ellos.", "midemos", "medimos", "medin", "miden")
            else:
                ono("Vestir con ellos.", "vistemos", "vestimos", "vestin", "visten")
        elif on == 2:
            on = randint(1, 2)
            if on == 1:
                ono("Medir con ellas.", "midemos", "medimos", "medin", "miden")
            else:
                ono("Vestir con ellas.", "vistemos", "vestimos", "vestin", "visten")
        elif on == 3:
            on = randint(1, 2)
            if on == 1:
                ono("Medir con Carla y Juan.", "midemos", "medimos", "medin", "miden")
            else:
                ono("Vestir con Carla y Juan.", "vistemos", "vestimos", "vestin", "visten")
        else:
            on = randint(1, 2)
            if on == 1:
                ono("Medir con ustedes.", "midemos", "medimos", "medin", "miden")
            else:
                ono("Vestir con ustedes.", "vistemos", "vestimos", "vestin", "visten")  
def seis():
    on = randint(1, 2)
    if on == 1:
        on = randint(1, 5)
        if on == 1:
            on = randint(1, 3)
            if on == 1:
                ono("Vivir con él en imperatovo.", "vivo", "vivi", "vivimos", "vive")
            elif on == 2:
                ono("Hablar con él en imperatovo.", "hablo", "hablar", "hablamos", "habla")
            else:
                ono("Comer con él en imperatovo.", "como", "comer", "comemos", "come")
        elif on == 2:
            on = randint(1, 3)
            if on == 1:
                ono("Vivir con ella en imperatovo.", "vivo", "vivi", "vivimos", "vive")
            elif on == 2:
                ono("Hablar con ella en imperatovo.", "hablo", "hablar", "hablamos", "habla")
            else:
                ono("Comer con ella en imperatovo.", "como", "comer", "comemos", "come")
        elif on == 3:
            on = randint(1, 3)
            if on == 1:
                ono("Vivir con Juan en imperatovo.", "vivo", "vivi", "vivimos", "vive")
            elif on == 2:
                ono("Hablar con Juan en imperatovo.", "hablo", "hablar", "hablamos", "habla")
            else:
                ono("Comer con Juan en imperatovo.", "como", "comer", "comemos", "come")
        elif on == 4:
            on = randint(1, 3)
            if on == 1:
                ono("Vivir con Carla en imperatovo.", "vivo", "vivi", "vivimos", "vive")
            elif on == 2:
                ono("Hablar con Carla en imperatovo.", "hablo", "hablar", "hablamos", "habla")
            else:
                ono("Comer con Carla en imperatovo.", "como", "comer", "comemos", "come")
        else:
            on = randint(1, 3)
            if on == 1:
                ono("Vivir con usted en imperatovo.", "vivo", "vivi", "vivimos", "vive")
            elif on == 2:
                ono("Hablar con usted en imperatovo.", "hablo", "hablar", "hablamos", "habla")
            else:
                ono("Comer con usted en imperatovo.", "como", "comer", "comemos", "come")
    else:
        on = randint(1, 2)
        if on == 1:
            on = randint(1, 3)
            if on == 1:
                ono("Vivir con vosotros en imperatovo.", "vivo", "vivir", "vivís", "vivid")
            elif on == 2:
                ono("Hablar con vosotros en imperatovo.", "hablo", "hablar", "habláis", "hablad")
            else:
                ono("Comer con vosotros en imperatovo.", "como", "comer", "coméis", "comed")
        else:
            on = randint(1, 3)
            if on == 1:
                ono("Vivir con vosotras en imperatovo.", "vivo", "vivir", "vivís", "vivid")
            elif on == 2:
                ono("Hablar con vosotras en imperatovo.", "hablo", "hablar", "habláis", "hablad")
            else:
                ono("Comer con vosotras en imperatovo.", "como", "comer", "coméis", "comed")
def siete():
    on = randint(1, 8)
    if on == 1:
        ona("¿Cómo ... tú?", "ser", "estar")
    elif on == 2:
        ona("¡Yo ... superbién!", "ser", "estar")
    elif on == 3:
        ona("¿Dónde ... el estadio Bernabéu?", "ser", "estar")
    elif on == 4:
        ona("El estadio Bernabéu ... en Madrid.", "ser", "estar")
    elif on == 5:
        ona("¿De dónde ... tú?", "estar", "ser")
    elif on == 6:
        ona("Yo ... de españa", "estar", "ser")
    elif on == 7:
        ona("¿De qué nacionalidad ... tú?", "estar", "ser")
    else:
        ona("Yo ... de nacionalidad española.", "estar", "ser")
def ocho():
    on = randint(1, 12)
    if on == 1:
        oni("Peru", "Perú")
    elif on == 2:
        oni("Chili", "Chile")
    elif on == 3:
        oni("USA", "Estados Unidos")
    elif on == 4:
        oni("Canada", "Canadá")
    elif on == 5:
        oni("Morocco", "Marruecos")
    elif on == 6:
        oni("Algeria", "Argelia")
    elif on == 7:
        oni("Australia", "Australia")
    elif on == 8:
        oni("New Zealand", "Nueva Zelanda")
    elif on == 9:
        oni("Spain", "España")
    elif on == 10:
        oni("France", "Francia")
    elif on == 11:
        oni("China", "China")
    else:
        oni("India", "India")
def nueve():
    on = randint(1, 9)
    if on == 1:
        one("el cuaderno", "Los cuadernos")
    elif on == 2:
        one("la profesora", "Las profesoras")
    elif on == 3:
        one("la isla", "Las islas")
    elif on == 4:
        one("la capital", "Las capitales")
    elif on == 5:
        one("el animal", "Los animales")
    elif on == 6:
        one("el mes", "Los meses")
    elif on == 7:
        one("el pez", "Los peces")
    elif on == 8:
        one("el juez", "Los jueces")
    else:
        one("el nuez", "los nueces")
def diez():
    on = randint(1, 23)
    if on == 1:
        oni("monday", "Lunes")
    elif on == 2:
        oni("tuesday", "Martes")
    elif on == 3:
        oni("wednesday", "Miécroles")
    elif on == 4:
        oni("thursday", "Juves")
    elif on == 5:
        oni("friday", "Viernes")
    elif on == 6:
        oni("saturday", "Sábado")
    elif on == 7:
        oni("sunday", "Domingo")
    elif on == 8:
        oni("january", "Enero")
    elif on == 9:
        oni("february", "Febrero")
    elif on == 10:
        oni("march", "Marzo")
    elif on == 11:
        oni("april", "Abril")
    elif on == 12:
        oni("may", "Mayo")
    elif on == 13:
        oni("june", "Junio")
    elif on == 14:
        oni("july", "Jullio")
    elif on == 15:
        oni("august", "Agosto")
    elif on == 16:
        oni("september", "Septiembre")
    elif on == 17:
        oni("october", "Octubre")
    elif on == 18:
        oni("november", "Noviemvre")
    elif on == 19:
        oni("december", "Diciembre")
    elif on == 20:
        oni("the spring", "La primavera")
    elif on == 21:
        oni("thesummer", "El verano")
    elif on == 22:
        oni("the automn", "El otoño")
    else:
        oni("the winter", "El inverno")
def once():
    on = randint(1, 39)
    if on == 1:
        oni("1", "Uno")
    elif on == 2:
        oni("2", "Dos")
    elif on == 3:
        oni("3", "Tres")
    elif on == 4:
        oni("4", "Cuatro")
    elif on == 5:
        oni("5", "Cinco")
    elif on == 6:
        oni("6", "Seis")
    elif on == 7:
        oni("7", "Siete")
    elif on == 8:
        oni("8", "Ocho")
    elif on == 9:
        oni("9", "Nueve")
    elif on == 10:
        oni("10", "Diez")
    elif on == 11:
        oni("11", "Once")
    elif on == 12:
        oni("12", "Doce")
    elif on == 13:
        oni("13", "Trece")
    elif on == 14:
        oni("14", "Catorce")
    elif on == 15:
        oni("15", "Quince")
    elif on == 16:
        oni("16", "Dieciséis")
    elif on == 17:
        oni("17", "Diecisiete")
    elif on == 18:
        oni("18", "Dieciocho")
    elif on == 19:
        oni("19", "Diecinueve")
    elif on == 20:
        oni("20", "Viente")
    elif on == 21:
        oni("21", "Ventiuno")
    elif on == 22:
        oni("22", "Ventidós")
    elif on == 23:
        oni("23", "Ventitrés")
    elif on == 24:
        oni("24", "Venticuatro")
    elif on == 25:
        oni("25", "Venticinco")
    elif on == 26:
        oni("26", "Ventiséis")
    elif on == 27:
        oni("27", "Ventisiete")
    elif on == 28:
        oni("28", "Ventiocho")
    elif on == 29:
        oni("29", "Ventinueve")
    elif on == 30:
        oni("30", "Trienta")
    elif on == 31:
        oni("40", "Cuarenta")
    elif on == 32:
        oni("50", "Cincuenta")
    elif on == 33:
        oni("60", "Sesenta")
    elif on == 34:
        oni("70", "Setenta")
    elif on == 35:
        oni("80", "Ochenta")
    elif on == 36:
        oni("90", "Noventa")
    elif on == 37:
        oni("100", "Cien")
    elif on == 38:
        oni("1000", "Mil")
    else:
        oni("1000000", "Millón")
def one (pr, pra):
    print("¿Qué es " + pr + " en plural?")
    inp = input()
    if pra == inp:
        print("Sí!")
    else:
        print("No, la respuesta es " + pra + ".")
    print(" ")
def oni (pr, pra):
    print("¿Qué es " + pr + " en español?")
    inp = input()
    if pra == inp:
        print("Sí!")
    else:
        print("No, la respuesta es " + pra + ".")
    print(" ")
def ona (pr, ne, pra):
    print(pr)
    global randint
    vopros = randint(1, 2)
    if vopros == 1:
        print("1 --> " + pra)
        print("2 --> " + ne)
    else:
        print("1 --> " + ne)
        print("2 --> " + pra)
    inp = input()
    if (inp == "1" and vopros == 1) or (inp == "2" and vopros == 2):
        print("Sí!")
    else:
        print("No, la respuesta es " + pra + ".")
    print(" ")
def ono (pr, ne1, ne2, ne3, pra):
    print(pr)
    global randint
    vopros = randint(1, 4)
    if vopros == 1:
        print("1 --> " + pra)
        print("2 --> " + ne1)
        print("3 --> " + ne2)
        print("4 --> " + ne3)
    elif vopros == 2:
        print("1 --> " + ne1)
        print("2 --> " + pra)
        print("3 --> " + ne2)
        print("4 --> " + ne3)
    elif vopros == 3:
        print("1 --> " + ne1)
        print("2 --> " + ne2)
        print("3 --> " + pra)
        print("4 --> " + ne3)
    else:
        print("1 --> " + ne1)
        print("2 --> " + ne2)
        print("3 --> " + ne3)
        print("4 --> " + pra)
    inp = input()
    if (inp == "1" and vopros == 1) or (inp == "2" and vopros == 2) or (inp == "3" and vopros == 3) or (inp == "4" and vopros == 4):
        print("Sí!")
    else:
        print("No, la respuesta es " + pra + ".")
    print(" ")
def verificacion():
    for _ in range(5):
        if ver == "1":
            uno()
        elif ver == "2":
            dos()
        elif ver == "3":
            tres()
        elif ver == "4":
            cuatro()
        elif ver == "5":
            cinco()     
        elif ver == "6":
            seis()
        elif ver == "7":
            siete()
        elif ver == "8":
            ocho()
        elif ver == "9":
            nueve()
        elif ver == "10":
            diez()
        elif ver == "11":
            once()
        elif ver == "12":
            for _ in range (4):
                on = randint(1, 11)
                if on == 1:
                    uno()
                elif on == 2:
                    dos()
                elif on == 3:
                    tres()
                elif on == 4:
                    cuatro()
                elif on == 5:
                    cinco()
                elif on == 6:
                    seis()
                elif on == 7:
                    siete()
                elif on == 8:
                    ocho()
                elif on == 9:
                    nueve()
                elif on == 10:
                    diez()
                else:
                    once()
        elif ver == "100":
            print("Verbos normales con la terminación:")
            print("   AR      ER     IR")
            print("----------------------")
            print("   O       O      O")
            print("   AS      ES     ES")
            print("   A       E      E")
            print("   AMOS    EMOS   IMOS")
            print("   ÁIS     ÉIS    ÍS")
            print("   AN      EN     EN")
            print(" ")
            break
        elif ver == "200":
            print("Verbos irregulares:")
            print("   TENER      SER     IR")
            print("---------------------------")
            print("   TENGO      SOY     VOY")
            print("   TIENES     ERES    VAS")
            print("   TIENE      ES      VA")
            print("   TENEMOS    SOMOS   VAMOS")
            print("   TENEIS     SOIS    VAIS")
            print("   TIENEN     SON     VAN")
            print(" ")
            break
        elif ver == "300":
            print("Verbos pronominales:")
            print("   YO     -->   ME")
            print("   TÚ     -->   TE")
            print("   ÉL     -->   SE")
            print("   VOS.   -->   NOS")
            print("   NOS.   -->   OS")
            print("   ELLOS  -->   SE")   
            print(" ")
            break
        elif ver == "400":
            print("Para verbos en diptongo en:")
            print("   O ==> UE")         
            print("   U ==> UE")  
            print("   E ==> IE")  
            print("EXEPTO VOSOTROS Y NOSOTROS")
            print(" ")
            break
        elif ver == "500":
            print("Para verbos debilitantes:")
            print("    E <--> I de IR ")
            print(" ")
            break
        elif ver == "600":
            print("Imperativo para:")
            print("    ÉL:        Verbo en él sin el pronombre.")
            print("    VOSOTROS:  Verbo en infinitivo sin R con D.    (Verbo - R + D)")
            print(" ")
            break
        elif ver == "700":
            print("Ser / Estar")
            print("    Ser para nacionalidad / de dónde.")
            print("    Estar para cómo estás / dónde estás.")
            break
        elif ver == "800":
            print("Países:")
            print("    INGLÉS              ESPAÑOL")
            print("  -------------------------------")
            print("    Perú             =   Peru")
            print("    Chile            =   Chili")
            print("    Estados Unidos   =   USA")        
            print("    Canadá           =   Canada")
            print("    Marruecos        =   Morocco")   
            print("    Argelia          =   Algeria") 
            print("    Australia        =   Australia")      
            print("    Nueva Zelanda    =   New Zealand")        
            print("    España           =   Spain")
            print("    Francia          =   France") 
            print("    China            =   China")
            print("    India            =   India") 
            print(" ")
            break
        elif ver == "900":
            print("Para palabras que terminan en consonante excepto z:")
            print("     Añade ES")
            print("Para palabras que terminan en vocal:")
            print("     Añade S.")
            print("Para palabras que terminan en z:")
            print("     Elimina Z y añade CES.")
            print("Y los artículos:")
            print("     el --> los")
            print("     la --> las")
            print(" ")
            break
        elif ver == "1000":
            print("Lunes          Monday")
            print("Martes         Tuesday")
            print("Miécroles      Wednesday")
            print("Jueves         Thursday")
            print("Viernes        Friday")
            print("Sábado         Saturday")
            print("Domingo        Sunday")
            print(" ")  
            print("Enero          January")
            print("Febrero        February")
            print("Marzo          March")
            print("Abril          April")
            print("Mayo           May")
            print("Junio          June")
            print("Julio          July")
            print("Agosto         August")
            print("Septiembre     September")
            print("Octubre        October")
            print("Noviembre      November")
            print("Diciembre      December")
            print(" ")  
            print("La Primavera   Spring")
            print("El Verano      Summer")
            print("El Otoño       Automn")
            print("El Inverno     Winter")
            print(" ")
            break
        elif ver == "1100":
            print("1  =  Uno")
            print("2  =  Dos")
            print("3  =  Tres")
            print("4  =  Cuatro")
            print("5  =  Cinco")
            print("6  =  Seis")
            print("7  =  Siete")
            print("8  =  Ocho")
            print("9  =  Nueve")
            print(" ")
            print("10  =  Diez")
            print("11  =  Once")
            print("12  =  Doce")
            print("13  =  Trece")
            print("14  =  Catorce")
            print("15  =  Quince")
            print("16  =  Dieciséis")
            print("17  =  Diecisiete")
            print("18  =  Dieciocho")
            print("19  =  Deicinueve")
            print(" ")
            print("20  =  Viente")
            print("21  =  Ventiuno")
            print("22  =  Ventidós")
            print("23  =  Ventitrés")
            print("24  =  Venticuatro")
            print("25  =  Venticinco")
            print("26  =  Ventiséis")
            print("27  =  Ventisiete")
            print("28  =  Ventiocho")
            print("29  =  Ventinueve")
            print(" ")
            print("30  =  Trienta")
            print("40  =  Cuarenta")
            print("50  =  Cincuenta")
            print("60  =  Sesenta")
            print("70  =  Setenta")
            print("80  =  Ochenta")
            print("90  =  Noventa")
            print("100  =  Cien")
            print("1000  =  Mil")
            print("1000000  =  Millón")
            print(" ")
            break
        else:
            print("¿Qué? Repita por favor.")
            break
    print(" ")
    print("Bien, terminaste el entrenamiento")
    print("¿Quizás quieras empezar otro?")
def menu ():
    print("Posibles entrenamientos:")
    print("1   =  verbos normales.")
    print("2   =  verbos irregulares.")
    print("3   =  verbos pronominales.")
    print("4   =  verbos en diptongo.")
    print("5   =  verbos debilitantes.")
    print("6   =  verbos imperatovos.")
    print("7   =  SER / ESTAR.")
    print("8   =  países.")
    print("9   =  plural de los palabras.")
    print("10  =  fechas.")
    print("11  =  números.")
    print("12  =  ¡Gran final!  (¡Si entendiste todo!)")
    print(" ")
    print("¡Para leer la teoría --> número de entrenamiento + 00!")
    print(" ")
menu()
ver = input("¿Cuál es el tema del curso que quieres aprender?")
print(" ")
verificacion()
while True:
    print(" ")
    menu()
    ver = input()
    verificacion()
#fin