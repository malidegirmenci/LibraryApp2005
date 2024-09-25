from HelperFuncs import centeredTitle, showMenu, showMessage

from DB_USERS import USERS

subMenuAccount = [
    'Üye Ol', 'Giriş Yap', 'Kitaplarıma Bak', 'Bakiye', 'Çıkış Yap',
    'Üst Menüye Çık'
]
subMenuBalance = [ 'Bakiye Sorgula', 'Bakiye Ekle', 'Üst Menüye Çık']

loginStatus = False
activeUser = {}

def checkUsernameExists(username):
  existing_users = list(filter(lambda user:user['username'] == username, USERS))
  if len(existing_users) > 0:
    return existing_users[0]
  else:
    return []

def registerService():
  print(centeredTitle('KAYIT OL'))
  while True:
    username = input('Kullanıcı Adı: ')
    lengthOfList = len(checkUsernameExists(username))
    if lengthOfList > 0:
      showMessage(f'{username} adı zaten mevcut, başka bir kullanıcı adı giriniz')
    else:
      break
  password = input('Parola: ')
  while True:
    passwordRepeat = input('Parola (Tekrar): ')
    if password == passwordRepeat:
      break
    else:
      showMessage('Parolalar eşleşmiyor, parolayı tekrar giriniz')
  name = input('İsim: ')
  surname = input('Soyisim: ')
  age = input('Yaş: ')
  address = input('Adres: ')
  phone = input('Telefon: ')
  email = input('E-Mail: ')
  gender = input('Cinsiyet: ')
  user = {
      'username': username,
      'password': password,
      'name': name,
      'surname': surname,
      'age': age,
      'address': address,
      'phone': phone,
      'email': email,
      'balance': 0,
      'gender': gender,
      'status': True,
      'myBooks': []
  }
  USERS.append(user)
  showMessage(f'{username} kullanıcısı başarıyla kayıt edildi')

def loginService():
  global loginStatus
  global activeUser
  print(centeredTitle('GİRİŞ YAP'))
  entered_username = input('Kullanıcı Adı: ')
  entered_password = input('Parola: ')
  user = checkUsernameExists(entered_username)
  if user['username'] == entered_username and user['password'] == entered_password:
    showMessage('Giriş başarılı')
    showMessage(f'Hoşgeldiniz {user["name"]}')
    loginStatus = True
    activeUser = user
  else:
    showMessage('Kullanıcı adı veya parola hatalı')

def balanceService():
  global activeUser
  while True:
    showMenu(subMenuBalance, 'Bakiye İşlemleri')
    choice = input('Seçiminiz: ')
    if choice == '1':
      showMessage(f"Bakiyeniz: {activeUser['balance']}")
    if choice == '2':
      amount = int(input('Ekleyeceğiniz miktar giriniz: '))
      activeUser['balance'] += amount
      showMessage(f"Güncel Bakiyeniz: {activeUser['balance']}")
    if choice == '3':
      break

def logoutService():
  global activeUser
  global loginStatus
  activeUser = {}
  loginStatus = False
  showMessage('Çıkış yapıldı')
  
def accountService():
  while True:
    showMenu(subMenuAccount, 'HESAP İŞLEMLERİ')
    choice = input('Seçiminiz: ')
    if choice == '1':
      registerService()
    elif choice == '2':
      loginService()
    elif choice == '3':
      print('KİTAPLARIM SERVICE')
    elif choice == '4':
      if loginStatus and activeUser:
        balanceService()
      else:
        showMessage('Giriş yapmadınız. Lütfen öncelikle giriş yapınız.')
    elif choice == '5':
      logoutService()
    elif choice == '6':
      break
    else:
      showMessage(f'{choice} geçersiz bir seçim')