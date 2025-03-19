import random
import sys

# Preguntas para el juego
questions = [
    "¿Qué función se usa para obtener la longitud de una cadena en Python?",
    "¿Cuál de las siguientes opciones es un número entero en Python?",
    "¿Cómo se solicita entrada del usuario en Python?",
    "¿Cuál de las siguientes expresiones es un comentario válido en Python?",
    "¿Cuál es el operador de comparación para verificar si dos valores son iguales?",
]
# Respuestas posibles para cada pregunta, en el mismo orden que las preguntas
answers = [
    ("size()", "len()", "length()", "count()"),
    ("3.14", "'42'", "10", "True"),
    ("input()", "scan()", "read()", "ask()"),
    (
        "// Esto es un comentario",
        "/* Esto es un comentario */",
        "-- Esto es un comentario",
        "# Esto es un comentario",
    ),
    ("=", "==", "!=", "==="),
]
# Índice de la respuesta correcta para cada pregunta, el el mismo orden que las preguntas
correct_answers_index = [1, 2, 0, 3, 1]
score = 0
# El usuario deberá contestar 3 preguntas
# Zip une los elementos de las 3 listas (las preguntas, respuestas y las respuestas correctas) en tuplas.
# List convierte el resultado de zip en una lista completa para poder ser utilizada por random.choices
# Random.choices selecciona 3 elementos de esa lista generada de manera aleatoria.
questions_to_ask = random.sample(list(zip(questions, answers, correct_answers_index)), k=3)
# Separamos la lista de tuplas para quedarnos sólo con las preguntas, respuestas y respuestas correctas por separado.
for question, answers, correct_answer_index in questions_to_ask:
    print(question)
    for i, answer in enumerate(answers):
        print(f"{i + 1}. {answer}")
    # El usuario tiene 2 intentos para responder correctamente
    for intento in range(2):
        try:
            user_answer = int(input("Respuesta: ")) - 1
        except:
            print("Respuesta inválida, ingresá un número")
            sys.exit(1)
    # Se verifica si la respuesta es correcta
        if user_answer+1 > len(answers) or user_answer < 0:
            print("Respuesta inválida, ingresá un número válido")
            sys.exit(1)
        if user_answer == correct_answer_index:
            score += 1
            print("¡Correcto!")
            break
        else:
            score -= 0.5
    else:
        # Si el usuario no responde correctamente después de 2 intentos,
        # se muestra la respuesta correcta
        print("Incorrecto. La respuesta correcta es:")
        print(f"{correct_answer_index+1}. {answers[correct_answer_index]}")
    # Se imprime un blanco al final de la pregunta
    print()
print(f"El puntaje obtenido es de: {score} puntos")
