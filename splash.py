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

def cd(command, args):
  """ Change directory"""
  if len(args) > 2: 
    print ("-splash: cd: too many arguments")
  else:
    try:
      os.chdir(args[1]) 
    except (FileNotFoundError): 
      print ("-splash: cd: %s: No such file or directory" % args[1])
  
    # cd called with no arguments
    except (IndexError):
      pass

def main():
  while (True):
    args = prompt()
    command = args[0]
    # print("command: %s \nargs: %s" % (command, args))

    # builtins
    if command == 'cd':
      cd(command, args)
    elif command == 'exit':
      print("goodbye!")
      exit()
    else:
      fork_exec(command, args)
  
if __name__ == '__main__':
  main()


