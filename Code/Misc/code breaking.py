def test_password(password):
    if (password ^ 1485) == 40:
        return True
    else:
        return False

for i in range(10000):
    test_password(i)

    if test_password(i) is True:
        print("Sucess! your number is", i )
        


