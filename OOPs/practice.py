class Teacher:
    def __init__(self, name, age, subject):
        self.name = name             # public
        self._age = age              # protected
        self.__subject = subject     # private

    def display_info(self):
        print(f"Name: {self.name}, Age: {self._age}, Subject: {self.__subject}")

    # Method to access private attribute : getter and setter methods

    def set_subject(self, new_subject):
        self.__subject = new_subject
    
    def get_subject(self):
        return self.__subject


if __name__ == "__main__":
    t1 = Teacher("John Doe", 35, "Mathematics")
    t1.display_info()
    print(t1.get_subject())
    print(t1._age) 

    # Modifying private attribute
    t1.set_subject("Physics")
    print(t1.get_subject())
