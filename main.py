# This is a strong password generator

# Guideline for a strong password | by Boston University

# > Use a mix of alphabetical and numeric characters
# > Use a mixture of upper- and lowercase; passwords are case-sensitive
# > Use symbols if the system allows
# > Use a combination of letters and numbers, or a phrase like "many colors" using only the consonants, e.g., mnYcOlOrz
import emoji
import string
import random

print(emoji.emojize(':kissing_face_with_closed_eyes: Welcome to the Strong Password Generator'
                    ' :kissing_face_with_closed_eyes:'))
print("Select which type of password you are looking for: \n"
      " - A) if simple password with numbers and letters;\n"
      " - B) a password with upper and lowercase characters;\n"
      " - C) a super--mega--power password with everything included;")
option = input(emoji.emojize(':writing_hand: | '))


def simple_pass(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def complicated_pass(size=10, chars=string.ascii_letters + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def power_pass(size=12, chars=string.ascii_letters + string.digits + string.punctuation):
      return ''.join(random.choice(chars) for _ in range(size))

match option:
      case "A":
        print(emoji.emojize("Your new pass is: :locked: " + simple_pass()))
      case "B":
        print(emoji.emojize("Your new pass is: :locked: " + complicated_pass()))
      case "C":
        print(emoji.emojize("Your new pass is: :locked: " + power_pass()))
      case _:
        print(emoji.emojize(':warning: You did not chose a possible option! Look again :eyes:'))
