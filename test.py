class Student:
    # pass
    # Default constructor
    # def __init__(self) -> None:
    #     print(self)
    #     print("object created\n")

    # perameterized Constructor
    def __init__(self, name, id) -> None:
        # instance variable
        self.name = name
        self.id = id 
        print('self inside pera const: ', self)
        
    # instance method
    def display(self):
        print(self.name, " ", self.id)
        print('self inside instance method: ', self)

s1 = Student("Daud", 20001)
s2 = Student("Saud", 20002)
s1.display()
s2.display()

# print(s1.name + "\n" + s2.name + "\n")
# print(s1.id, "\n", s2.id)
print("\nobjects memory location: ")
print(s1, "\n", s2)