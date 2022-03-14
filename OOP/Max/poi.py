try:
    f=open('test.txt','w')
except Exception:
    print('Ощебка файл не найден')
else:
    f.write('privet')
    print('Файл найден')
finally:
    f.close()
try:
    f=open('test.txt','r')
    text=f.read()
    print(text)
except Exception:
    print('Ощибка')
finally:
    f.close()
