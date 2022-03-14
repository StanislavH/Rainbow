try:
    res=1+1
    f=open('test.txt', 'w')
except Exception:
    print('Hе Hy ты тупой')
else:
    print('МАЛАДЕЦ')
try:
    f=open('test.txt', 'w')
except Exception:
    print('фийла нема')
else:
    f.write(str(res))
    print(res)
finally:
    f.close()
