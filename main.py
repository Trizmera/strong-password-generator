# This is a strong password generator

# Guideline for a strong password | by Boston University

# > Use a mix of alphabetical and numeric characters
# > Use a mixture of upper- and lowercase; passwords are case-sensitive
# > Use symbols if the system allows
# > Use a combination of letters and numbers, or a phrase like "many colors" using only the consonants, e.g., mnYcOlOrz
import emoji

print(emoji.emojize(':kissing_face_with_closed_eyes: Welcome to the Strong Password Generator :kissing_face_with_closed_eyes:'))
print("Select which type of password you are looking for: \n"
      " - A) if simple password with numbers and letters;\n"
      " - B) a password with upper and lowercase characters;\n"
      " - C) a super--mega--power password with everything included;")
option = input(emoji.emojize(':writing_hand: | '))

match option:
      case "A":
      # simple_pass()
          print(option)
      case "B":
      # complicated_pass()
            print(option)
      case "C":
      # power_pass()
            print(option)
      case default:
            print(emoji.emojize(':warning: You did not chose a possible option! Look again :eyes:'))