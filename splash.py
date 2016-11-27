import os

def prompt():
  """ Prompt the user for a line"""
  try:
    in_string = input("splash$ ")

    # split string, stripping empty strings with filter
    args = list(filter(None, in_string.split(' ')))

    return args 
  except (NameError, SyntaxError):
    print("Invalid input. \n")


while (True):
  args = prompt()
  command = args[0]
  # print("command: %s \nargs: %s" % (command, args))
  p = os.fork()
  if p:
    os.waitpid(p, 0)
  else:
    os.execvp(command, args) 

