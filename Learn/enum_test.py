from enum import Enum, IntEnum


class Seasons(IntEnum):
	Spring = 1
	Summer = 2
	Autumn = 3
	Winter = 4


class Animations(Enum):
	Fade = 'Fade'
	Slide = 'Slide'
	

if __name__ == '__main__':
	print(Seasons.__members__)
	print(Seasons.Winter)
	print(Animations.__members__)
	print(Animations.Fade)
	print(dir(Seasons))
