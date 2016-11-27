import os

def prompt():
  """ Prompt the user for a line"""
  try:
    in_string = input("splash$ ")

    # split string, stripping empty strings with filter
    args = list(filter(None, in_string.split(' ')))

    return args 
  except (NameError, SyntaxError):
    print("Invalid input.")

  # Exit gracefully with Ctrl-D
  except (EOFError):
    print("Goodbye!")
    exit()

def fork_exec(command, args):
  """ Fork a new process and execute a command"""
  p = os.fork()
  if p:
    os.waitpid(p, 0)
  else:
    os.execvp(command, args) 


while (True):
  args = prompt()
  command = args[0]
  # print("command: %s \nargs: %s" % (command, args))

  # builtins
  if command == 'cd':
    os.chdir(args[1]) 
  elif command == 'exit':
    print("goodbye!")
    exit()
  else:
    fork_exec(command, args)
  


