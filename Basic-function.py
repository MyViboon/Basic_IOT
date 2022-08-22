def hello():
      print('hello my friend')

def sawadee():
    print('สวัสดีเพื่อน')

def nihao():
    print('หนีห่าว')

def konijiwa():
    print('โคนิจิวะ')


while True:
    
    friend = input('where are you from? : ')

    if friend == 'thai':
        sawadee()
    elif friend == 'chaina':
        nihao()
    elif friend == 'japan':
        konijiwa()
    else:
        hello()



