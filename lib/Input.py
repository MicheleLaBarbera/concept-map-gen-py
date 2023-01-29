class Input:
  def ask_integer(text, min_val):
    while True:
      try:
        x = int(input(text + " "))
        if x >= min_val:
          break
        else: 
          print("Devi inserire un numero superiore o uguale a " + str(min_val) + "!")
      except ValueError:
        print("Devi inserire un numero superiore o uguale a " + str(min_val) + "!")
    return x
