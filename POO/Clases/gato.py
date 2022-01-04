import random


class Gato:

    # Atributos
    color = "white"
    size = 30
    weight = 20
    breed = "Siamese"
    max_jump_height = 0

    # Métodos

    def jump(self):
        jump_height = random.randint(1, 50)
        self.max_jump_height = jump_height

    def __init__(self, color):
        self.color = color


new_cat_1 = Gato(color='black')
new_cat_2 = Gato(color='white')


new_cat_1.jump()
new_cat_2.jump()
print(new_cat_1.max_jump_height)
print(new_cat_2.max_jump_height)
print(new_cat_1.color)
print(new_cat_2.color)