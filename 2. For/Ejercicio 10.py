"""Dada la lista de elementos, escriba un programa de Python que tome como parámetro caracteres (letras o palabras). 
El programa debe eliminar la presencia de dicha palabra de todos los elementos de la lista, y luego devolver la lista resultante.
"""
NEVER_GONNA_GIVE_YOU_UP = [
    "We're no strangers to love", "You know the rules and so do I",
    "A full commitment's what I'm thinking of", "You wouldn't get this from any other guy",
    "I just wanna tell you how I'm feeling", "Gotta make you understand", "Never gonna give you up",
    "Never gonna let you down", "Never gonna run around and desert you", "Never gonna make you cry",
    "Never gonna say goodbye", "Never gonna tell a lie and hurt you",
    "We've known each other for so long", "Your heart's been aching but you're too shy to say it",
    "Inside we both know what's been going on", "We know the game and we're gonna play it",
    "And if you ask me how I'm feeling", "Don't tell me you're too blind to see",
    "Never gonna give you up", "Never gonna let you down", "Never gonna run around and desert you",
    "Never gonna make you cry", "Never gonna say goodbye", "Never gonna tell a lie and hurt you",
    "Never gonna give you up", "Never gonna let you down", "Never gonna run around and desert you",
    "Never gonna make you cry", "Never gonna say goodbye", "Never gonna tell a lie and hurt you",
    "Never gonna give, never gonna give", "(Give you up)", "We've known each other for so long",
    "Your heart's been aching but you're too shy to say it",
    "Inside we both know what's been going on", "We know the game and we're gonna play it",
    "I just wanna tell you how I'm feeling", "Gotta make you understand", "Never gonna give you up",
    "Never gonna let you down", "Never gonna run around and desert you", "Never gonna make you cry",
    "Never gonna say goodbye", "Never gonna tell a lie and hurt you", "Never gonna give you up",
    "Never gonna let you down", "Never gonna run around and desert you", "Never gonna make you cry",
    "Never gonna say goodbye", "Never gonna tell a lie and hurt you", "Never gonna give you up",
    "Never gonna let you down", "Never gonna run around and desert you", "Never gonna make you cry",
    "Never gonna say goodbye"]


print("Lista original es:" + str(NEVER_GONNA_GIVE_YOU_UP))

palabra = str(input("¿Qué palabra quiere eliminar?\n"))

for i in range(len(NEVER_GONNA_GIVE_YOU_UP)):
    NEVER_GONNA_GIVE_YOU_UP.remove(palabra) 
print(NEVER_GONNA_GIVE_YOU_UP)

#ole, qué ejercicio tan puto