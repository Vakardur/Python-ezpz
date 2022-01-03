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
    "Never gonna say goodbye"
]

word_to_remove = input('Ingrese una palabra a eliminar: \n')

new_lyrics_list = []

for text in NEVER_GONNA_GIVE_YOU_UP:
    if word_to_remove in text:
        altered_element = text.replace(word_to_remove, '')
        new_lyrics_list.append(altered_element)
    else:
        new_lyrics_list.append(text)

print(new_lyrics_list)
