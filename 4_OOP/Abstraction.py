"""
Abstraction
 - Abstraction is hiding all information (abstracting away) and giving access to only
   whats necessary, to only what the user needs.
 - Like we don't really need to know how exactly the code runs behind the scene, as much
   as we care about the results.
 - we use _variable this means this variable is private in Python, and we shouldn't touch
   it.
"""

class PlayerChar:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def char_details(self):
        return f'Characters details:\nName: {self.name}\nAge: {self.age}'

print('')
player_1 = PlayerChar('Ali', 45)
print(PlayerChar.char_details(self=player_1))
print('')
