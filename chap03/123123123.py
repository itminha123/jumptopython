diamond = int(input("diamond: "))
for i in range(diamond*2):
     if i<=diamond:
          spaces = diamond - i
          stars = i
          print(" "*spaces + "* "*stars)
     else:
          spaces = i - diamond
          stars = 2*diamond - i
          print(" "*spaces + "* "*stars)