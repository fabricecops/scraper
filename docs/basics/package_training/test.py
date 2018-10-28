import package_test

class test_class():

    def __init__(self):
        self.b = 3

if __name__ == '__main__':

    try:
        print(package_test.foo1())
    except Exception as e:
        print('Failed')

    try:
        print(package_test.foo2())
    except Exception as e:
        print('Failed')

    try:
        print(package_test.bar1)
    except package_test as e:
        print('Failed')

    try:
        print(package_test.bar2)
    except Exception as e:
        print('Failed')


    print()
    print('-'*50)
    print('-'*50)
    print('PACKAGE INFORMATION')
    print(package_test.__dir__())
    print(package_test.__name__)
    print()

    print('MODULE INFORMATION')
    print(__name__)
    print()
    print()


    print('-'*50)
    print('-'*50)
    print('CLASS INFORMATION')
    TC = test_class()
    for underscore_var in TC.__dir__():
        print(underscore_var)

    print("dict object  : ",TC.__dict__)
    print("module       : ",TC.__module__)
    print("weakref      : ",TC.__weakref__)
    print("hash         : ",TC.__hash__)
    print("str          : ",TC.__str__)
    print("getattr      : ",TC.__getattribute__)
    print("class        : ",TC.__class__)
    print("repr         : ",TC.__repr__)
    print("sizeof       : ",TC.__sizeof__())
    print("subclasshook :",TC.__subclasshook__)

