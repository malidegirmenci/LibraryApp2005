# IMPORTS
from BookService import bookService
from HelperFuncs import *
from DB_BOOKS import BOOKS
from DB_USERS import USERS
from AccountService import accountService

# MENU LISTS
mainMenu = ['Kütüphane Giriş', 'Hesap İşlemleri', 'Çıkış Yap']


# APP
def app():
  # HEADLINE
  print(centeredTitle('LIBRARY APP 2005'))

  while True:
    showMenu(mainMenu, 'ANA MENÜ')
    choice = input('Seçiminiz: ')
    if choice == '1':
      bookService()
    elif choice == '2':
      accountService()
    elif choice == '3':
      print('Program kapatıldı')
      break

app()
