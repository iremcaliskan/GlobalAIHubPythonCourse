class Person:
    def __init__(self, fname, lname, age, position):
        self.fname = fname
        self.lname = lname
        self.age = age
        self.position = position

    def Add(self):
        print(f'{self.fname} {self.lname} is added to {self.position} Table.')

    def ShowPosition(self):
        if self.position == "Employee":
            print(f'{self.fname} {self.lname} is an {self.position}.')
        elif self.position == "Manager":
            print(f'{self.fname} {self.lname} is a {self.position}.')
        else:
            print("The appropriate position is not defined. Enter 'Manager' or 'Employee'")

class Employee(Person):
    def __init__(self, fname, lname, age, position):
        super().__init__(fname,lname,age, position)
        self.language = []
    
    def Welcome(self):
        print(f'Hello, {self.fname} {self.lname}.')
    
    def AddLanguage(self, new_lang):
        print("New language Adding:")
        self.language.append(new_lang)
        print(new_lang)
        
    def ShowDetail(self):
        print("{} {} is {} years old.".format(self.fname,self.lname,self.age))
        print(f'{self.fname} can speak:')
        for lang in self.language:
              print(lang)

class Manager(Person):
    def __init__(self, fname, lname, age, position):
        super().__init__(fname,lname,age,position)
        self.language = []

    def Welcome(self):
        print(f'Hello, {self.fname} {self.lname}.')
    
    def AddLanguage(self, new_lang):
        print("New language Adding:")
        self.language.append(new_lang)
        print(new_lang)
        
    def ShowDetail(self):
        print("{} {} is {} years old.".format(self.fname,self.lname,self.age))
        print(f'{self.fname} can speak:')
        for lang in self.language:
              print(lang)

print("---Manager Test---")
manager1 = Manager("İrem", "Çalışkan", 24, "Manager")
manager1.Add()
manager1.ShowPosition()
manager1.Welcome()
manager1.AddLanguage("English")
manager1.AddLanguage("German")
manager1.ShowDetail()

print("\n---Employee Test---")
employee1 = Employee("Ceren", "Yıldız", 28, "Employee")
employee1.Add()
employee1.ShowPosition()
employee1.Welcome()
employee1.AddLanguage("English")
employee1.AddLanguage("Italian")
employee1.ShowDetail()