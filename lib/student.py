class Student:
    def __init__(self):
        pass
    def hello(self):
        return print("Hey there! I'm so excited to learn stuff.")
    
    def raise_hand(self):
        print("Pick me!")

class ChattyStudent(Student):
    def hello(self):
        super().hello()
        print("How are you doing today? I'm okay, but I'm kind of tired. Did you watch The Walking Dead last night? You didn't?! Oh man, it was so crazy! What, you don't want any spoilers? Okay well let me just tell you who died...")
    
    def raise_hand(self):
        i = 10
        while i > 0:
            super().raise_hand()
            i-=1
        
matt = ChattyStudent()
print(matt.raise_hand())