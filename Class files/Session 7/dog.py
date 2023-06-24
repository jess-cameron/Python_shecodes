class Dog:
    

    def __init__(self, dog_name, dog_age, dog_breed):
    #attributes
        self.name = "Jett"
        self.age = 4
        self.breed = "pug"

    #methods/behaviours. i.e. every dog I create under this class can do these things.
    def eat(self):
        print("Nom Nom")

    def talk(self):
        print("Bark Bark")       

#create a unique dog. It will inherit the attributes and and behaviours of the class.
dog1 = Dog("Jett", 4, "Pug") #this instantiates the class
dog1.talk() #this instructs what to run/print






