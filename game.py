import random

# Lista de palabras posibles
words = ["python", "programacion", "computadora", "codigo", "desarrollo", "inteligencia"]

# Elegir una palabra al azar
secret_word = random.choice(words)

# Número máximo de intentos permitidos
max_failures = 10

# Lista para almacenar las letras adivinadas
guessed_letters = []

print("¡Bienvenido al juego de adivinanzas!")
print("Estoy pensando en una palabra. ¿Puedes adivinar cuál es?")

word_displayed ="_" * len(secret_word)

# Mostrar la palabra parcialmente adivinada
print (f"Palabra: {word_displayed}")

# Inicializo un contador de fallos
fallos = 0

# Mientras que el contador no alcance al máximo de fallos posibles sigue adivinando letras
while fallos != max_failures:
    # Pedir al jugador que ingrese una letra
    letter = input ("ingresa una letra: ").lower()
    
    # Verificar si se ha insertado alguna letra
    if not letter:
       print("ERROR: No se ha ingresado ninguna letra")
       # Incremento el contador de fallos si no se ingresa ninguna letra    
       fallos = fallos + 1
       continue
    else:
      # Verificar si la letra ya ha sido adivinada
      if letter in guessed_letters:
         print("Ya has intentado con esa letra. Intenta con otra")
         # Incremento el contador de fallos si se ingresa una letra que ya fue ingresada previamente     
         fallos = fallos + 1
         continue
      
      # Agregar la letra a la lista de letras adivinadas
      guessed_letters.append(letter)

      # Verificar si la letra está en la palabra secreta
      if letter in secret_word:
        print("¡Bien hecho! La letra está en la palabra.")
      else:
        print("Lo siento, la letra no está en la palabra.")
        # Incremento el contador de fallos si se ingresa una letra que ya fue ingresada previamente     
        fallos = fallos + 1

      # Mostrar la palabra parcialmente adivinada
      letters = []
      for letter in secret_word:
           if letter in guessed_letters:
               letters.append(letter)
           else:
               letters.append("_")
    
      word_displayed = "".join(letters)
      print(f"Palabra: {word_displayed}")

    # Verificar si se ha adivinado la palabra completa 
    if word_displayed == secret_word:
       print(f"¡Felicidades! Has adivinado la palabra secreta: {secret_word}")
       break

    
else:
    print(f"¡Oh no! Has agotado tus {max_failures} intentos.")
    print(f"La palabra secreta era: {secret_word}")

