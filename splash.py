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
  (command, args) = prompt()
  # print("command: %s \nargs: %s" % (command, args))
  p = os.fork()
  if p:
    os.waitpid(p, 0)
  else:
    os.execvp(command, args) 

