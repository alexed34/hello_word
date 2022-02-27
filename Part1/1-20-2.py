class Car():
    def __init__(self, color, speed):
        self.speed = speed
        self.color = color

    def beep(self):
        print('BEEEEEEEEEEP')

    def say_speed(self):
        print(f'Speed: {self.speed}')
    def say_color(self):
            print(f'Speed: {self.color}')

porshe = Car('pink', 500)
porshe.beep()
porshe.say_speed()
porshe.say_color()

d = 5
a = d.bit_length()
print(a)


