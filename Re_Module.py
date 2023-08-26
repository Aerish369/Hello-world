import re
import time

#? Regular Expressions are used to find words from text. It can have wide variety of uses. However, I only learned to find text and similar texts. 
#? According to need, I can always expand my knowledge on Regular Expressions and re module. 



pattern = f"Thorfinn"

text = '''Thorfinn Karlsefni Thórdarson was an Icelandic explorer. Around the year 1010, 
he followed Leif Eriksson's route to Vinland in a short-lived attempt to establish a permanent settlement 
there with his wife Gudrid Thorbjarnardóttir and their followers. The byname Karlsefni means "makings of a man" 
according to the preface of Magnus Magnusson and Hermann Pálsson, although the Cleasby-Vigfusson dictionary 
glosses it as "a thorough man",[2] elaborated elsewhere as a "real man", a "sterling man". Thorfinn did the first 
and only attempt of settling icelanders and greenlanders to the America.'''


match = re.search(pattern, text)

# print(match)


#! To find multiple occurance of a word.
matches = re.finditer(pattern, text)
for match in matches:
  print(match.span()) 
  print(text[match.span()[0]: match.span()[1]])

def fixBugs():
  print("Initializing Fix Bugs")
  time.sleep(5)
  print("Fixing Bugs Succcessful !")