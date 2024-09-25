def showMessage(message):
  print()
  print(message)
  print()

def centeredTitle(title, width=50):
  print()
  if len(title) >= width:
    return title[:width]
  else:
    padding = (width - len(title)) // 2 # =20 
    return padding * '-' + f' {title} ' + padding * '-'


def showMenu(menu, nameOfMenu):
  title = centeredTitle(nameOfMenu)
  print(title)
  row = 1
  for menuRow in menu:
    print(f'{row}. {menuRow}')
    row += 1
  print('-' * len(title))
  