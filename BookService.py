from DB_BOOKS import BOOKS
from HelperFuncs import centeredTitle, showMenu, showMessage

subMenuBook = ['Kitap Ara', 'Üst Menüye Çık']
subMenuSearchBook = ['İsme göre', "ISBN'e göre", 'Yayın tarihine göre', 'Türe Göre', 'Üst Menüye Çık']

currentBookList = []

def detailsBook(book):
  showMessage('-'*50)
  print(f"İsmi: {book['name']}")
  print(f"Yazar: {book['author']}")
  print(f"Yayınlanma Tarihi: {book['releaseDate']}")
  print(f"Konusu: {book['subject']}")
  print(f"ISBN: {book['ISBN']}")
  print(f"Yayın Evi: {book['publishingHouse']}")
  print(f"Sayfa Sayısı: {book['pages']}")
  print(f"Puan: {book['ratings']}")
  print(f"Stok: {book['stock']}")
  print(f"Ücret: {book['price']}")
  showMessage('-'*50)

def showBooks(bookList):
  row = 1
  for book in bookList:
    print(centeredTitle(f'{row}. Kitap'))
    print(f"İsmi: {book['name']}")
    print(f"Yazar: {book['author']}")
    if book['borrowingStatusOfTheBook']:
      print("Ödünç alınabilir")
    else:
      print('Ödünç alınamaz')
    if book['purchaseStatusOfTheBook']:
      print('Satın alınabilir')
    else:
      print('Satın alınamaz')
    row += 1

'''
--> Kitap arama kriterini seçin
--> 1. İsme göre (seçildi)
--> Kitap ismini seçin (Yıl - Tür - ISBN de olabilir)
--> Harry 
--> criteria = 'name' searchText = 'Harry'
--> bookList = list(filter(lambda book: searchText in book['name'], BOOKS))
--> bookList['Harry Potter Kitapları']
'''
def searchWithCriteria(criteria, searchText):
  global currentBookList
  currentBookList = list(filter(lambda book: searchText in book[criteria], BOOKS))
  if len(currentBookList) == 0:
    if criteria == 'name':
      showMessage(f'Aradığınız {searchText} isimli kitap bulunamadı.')
    elif criteria == 'ISBN':
      showMessage(f'Aradığınız {searchText} ISBN numarasına uygun kitap bulunamadı.')
    elif criteria == 'releaseDate':
      showMessage(f'Aradığınız {searchText} tarihine uygun kitap bulunamadı.')
    elif criteria == 'genre':
      showMessage(f'Aradığınız {searchText} türüne uygun kitap bulunamadı.')
  showBooks(currentBookList)
  

def searchBook(): 
  while True:
    showMenu(subMenuSearchBook, 'ARAMA KRITERİ')
    choice = input('Seçiminiz: ')
    if choice == '1':
      searchText = input('Aramak istediğiniz kitabın ismini giriniz: ')
      searchWithCriteria('name', searchText)
      text = input(f'Kitap ödünç almak ya da satın almak istiyor musunuz?: ')
    elif choice == '2':
      searchText = input('Aramak istediğiniz kitabın ISBN giriniz: ')
      searchWithCriteria('ISBN', searchText)
    elif choice == '3':
      searchText = input('Aramak istediğiniz kitabın yayım yılını giriniz: ')
      searchWithCriteria('releaseDate', searchText)
    elif choice == '4':
      searchText = input('Aramak istediğiniz kitabın türünü giriniz: ')
      searchWithCriteria('genre', searchText)
    elif choice == '5':
      break
    else:
      showMessage(f'{choice} geçersiz bir seçim')

def bookService():
  while True:
    showMenu(subMenuBook, 'Kitap İşlemleri') 
    choice = input('Seçiminiz: ')
    if choice == '1':
      searchBook()
    if choice == '2':
      break