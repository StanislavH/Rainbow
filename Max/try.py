try:
    print(1/0)
except Exception:
    print('низя')
else:
    print('Все хорошо')
finally:
    print('Конец программы')