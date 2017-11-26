#----------------------------------------------------#
class GameEntry:

    def __init__(self, name, score):
        self._name = name
        self._score = score

    def __str__(self):
        return '<{0} ----- {1}>'.format(self._name, self._score)

    def getName(self):
        return self._name

    def getScore(self):
        return self._score


#------------------------------------------------------#

class Scoreboard:
    def __init__(self, capacity = 10):
        self._capacity = capacity                                     #Number of entrances in the Scoreboard
        self._names = ['<Empty>'] * capacity
        self._scores = [0] * capacity
        #self.display()

    #Function to display scores from the scoreboard
    def display(self):
        print('*'*20)
        for i in range(self._capacity):
            len_name = len(self._names[i])
            len_score = len(str(self._scores[i]))
            len_dot = 20 - len_name - len_score
            dots = '.' * len_dot
            print(self._names[i] + dots + str(self._scores[i]))


    #Function to add new scores to the scoreboard
    def add(self, person):
        if isinstance(person, GameEntry):
            for item in range(len(self._scores)-1):
                if person.getScore() > self._scores[item]:
                    for i in range(len(self._scores)-1, item, -1):
                        self._scores[i] = self._scores[i-1]
                        self._names[i] = self._names[i-1]
                    self._scores[item] = person.getScore()
                    self._names[item] = person.getName()
                    return
        print("Player cannot be added")

    def remove(self, person):
        if isinstance(person, GameEntry):
            for item in range(len(self._names)-1):
                if self._names[item] == person.getName():
                    for i in range(item, len(self._names)-1):
                        self._names[i] = self._names[i+1]
                        self._scores[i] = self._scores[i+1]
                    self._scores[len(self._names)-1] = 0
                    self._names[len(self._names)-1] = "<Empty>"
                    return
        print("No player found")

if __name__ in '__main__':

    board = Scoreboard()

    Mike = GameEntry('Mike', 5)
    John = GameEntry('John', 10)
    Jack = GameEntry('Jack', 8)
    Andy = GameEntry('Andy', 14)
    Nick = GameEntry('Nick', 22)


    board.add(Mike)
    board.add(John)
    board.add(Jack)
    Max = GameEntry('Max', 14)
    board.add(Max)
    board.add(Andy)
    board.remove(Andy)
    board.display()

    print('-----')
    Miki = 10
    board.add(Miki)
    board.remove(Miki)

