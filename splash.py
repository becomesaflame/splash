import os

def prompt():
  """ Prompt the user for a line"""
  try:
    in_string = input("splash$ ")
    command = in_string.split(' ')[0] 
    args = in_string.split(' ')
    return (command, args) 
  except (NameError, SyntaxError):
    print("Invalid input. \n")


while (True):
  print ("prompting\n") 
  (command, args) = prompt()
  # print("command: %s \nargs: %s" % (command, args))
  if not os.fork():
    os.execvp(command, args) 

