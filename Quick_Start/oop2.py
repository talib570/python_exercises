class AnimalActions():
    def quack(self): return self._doAction('quack')
    def feathers(self): return self._doAction('feathers')
    def bark(self): return self._doAction('bark')
    def fur(self): return self._doAction('fur')

    def _doAction(self, action):
    	if action in self.strings:
    		return self.strings[action]
    	else:
    		return "The {} has no {}".format(self.animalName(), action)

    def animalName(self):
    	return self.__class__.__name__.lower()


class Duck(AnimalActions):
    strings = dict(
        quack="Quacccccck!",
        feathers="The duck has gray and white feathers.",
    )


class Person(AnimalActions):
    strings = dict(
        quack="Ouch!!!",
        feathers="Person uses feathers for cuddling.",
        bark="Person mimick dog bark",
        fur="Person have skin"
    )


class Dog(AnimalActions):
    strings = dict(
        bark="Vooouuuhhhhh",
    )


class Bird(AnimalActions):
    strings = dict(
        feathers="All birds have feathers",
        fur="Ostrich have fur"
    )


def in_the_doghouse(dog):
    print(dog.bark())
    print(dog.fur())


def in_the_forest(duck):
    print(duck.quack())
    print(duck.feathers())


def main():
    donald = Duck()
    john = Person()
    fido = Dog()

    print("- In The Forest")
    for o in (donald, john, fido):
        in_the_forest(o)

    print("- In The Doghouse")
    for o in (donald, john, fido):
        in_the_doghouse(o)

if __name__ == '__main__':
    main()
