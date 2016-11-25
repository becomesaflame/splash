
# Repeatedly prompt the user for a line
while (True):
  try:
    command = input("splash$ ")
    print("%s" % command)
  except (NameError, SyntaxError):
    print("Invalid input. \n")
    continue

