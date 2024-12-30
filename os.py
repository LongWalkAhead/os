import os
question_1 = input("would you like to see the directory path, yes/no?")

def list_directory_contents(path):
   for content in os.listdir(path):
      print(content)

if question_1 == "yes":
    list_directory_contents("C:/Users\Bluel\OneDrive\Documents\codingtemple\my-coding-temple-ship.log")
else:
   print("okay, have a great day!")