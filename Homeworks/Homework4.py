class AnimalManager:
    def __init__(self,name,age,typ):
        self.name = name
        self.age = age
        self.typ = typ
        print("Animal class is created.")
    
    def guessWho(self):
        print(f'I am {self.name} and I am a {self.age} years old {self.typ}.')

    def sleep(self):
        print(f'{self.name} is sleeping.')

    def eat(self):
        print(f'{self.name} is eating.')
    
class DogManager(AnimalManager):
    def __init__(self, name, age, typ):
        super().__init__(name, age, typ)
        print("Dog class is created.")
    
    def woof(self):
        print(f'The {self.typ} {self.name} makes a WOOF sound.')
    
    def showAdulthood(self):
        if self.age >=0:
            if self.age < 2:
                print(f'{self.name} is a puppy {self.typ}.')
            elif self.age >=2 and self.age <= 7:
                print(f'{self.name} is an adult {self.typ}.')
            else:
                print(f'{self.name} is an aging {self.typ}.')
        else:
            print("Enter the appropriate number for the dog's age.")        

class CatManager(AnimalManager):
    def __init__(self,name,age,typ):
        super().__init__(name, age, typ)
        print("Cat class is created.")

    def meow(self):
        print(f'The {self.typ} {self.name} makes a MEOW sound.')

    def showAdulthood(self):
        if self.age >=0:
            if self.age < 3:
                print(f'{self.name} is a kitten {self.typ}.')
            elif self.age >=3 and self.age <= 6:
                print(f'{self.name} is an adult {self.typ}.')
            else:
                print(f'{self.name} is an aging {self.typ}.')
        else:
            print("Enter the appropriate number for the cat's age.")

cat1 = AnimalManager("Kitty",1,"cat")
cat1.guessWho()
cat1.eat()
cat1.sleep()

dog1 = AnimalManager("Tim",2.5,"dog")
dog1.guessWho()
dog1.eat()
dog1.sleep()

cat2 = CatManager("Marshmallow",1.5,"cat")
cat2.meow()
cat2.guessWho()
cat2.showAdulthood()

dog2 = DogManager("Zeus",2.5,"dog")
dog2.woof()
dog2.eat()
dog2.showAdulthood()