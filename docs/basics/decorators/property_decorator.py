from cached_property import cached_property

class Monopoly(object):

    def __init__(self):
        self.boardwalk_price1 = 500
        self.boardwalk_price2 = 500

    @property
    def boardwalk1(self):
        # In reality, this might represent a database call or time
        # intensive task like calling a third-party API.
        self.boardwalk_price1 += 50
        return self.boardwalk_price1


    @cached_property
    def boardwalk2(self):
        # In reality, this might represent a database call or time
        # intensive task like calling a third-party API.
        self.boardwalk_price2 += 50
        return self.boardwalk_price2


if __name__ == '__main__':
    monopoly = Monopoly()

    print("NOT CACHED")
    print(monopoly.boardwalk1)
    print(monopoly.boardwalk1)

    print("Cached")
    print(monopoly.boardwalk2)
    print(monopoly.boardwalk2)