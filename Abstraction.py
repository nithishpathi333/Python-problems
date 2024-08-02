class Animal():
    def sound(self):
        pass
class dog(Animal):
    def sound(self):
        return "bow"
class cat(Animal):
    def sound(self):
        return "meow"
        
print("dog says:",dog().sound())
print("cat says:",cat().sound())

Output: 
        dog says: bow
        cat says: meow
