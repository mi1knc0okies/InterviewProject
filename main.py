
# Exercise 1
class aboveBelow():
    def __init__(self, userList, userNum):
        self.list = userList
        self.num = userNum

    def compare(self):
        numAbove = []
        numBelow = []
        for i in self.list:
            if i == self.num:
                continue
            elif i > self.num:
                numAbove.append(i)
            else:
                numBelow.append(i)
        results = {'above': len(numAbove), 'below': len(numBelow)}
        return results

# Exercise 2
def rotateString(string, amount):
    change = len(string) - amount
    end = string[change:]
    start = string.strip(end)
    return print(f'{end}{start}')


if __name__ == '__main__':
    numList = [1,2,3,4,5,6]
    print(aboveBelow(numList, 4).compare())
    rotateString('string', 4)
