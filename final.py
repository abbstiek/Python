"""Abygail Stiekman
    aes15d
    CIS4930
    Final Project"""


from __future__ import print_function
import sys, random, enchant, shelve, tempfile, uuid, datetime
from PyQt5 import QtWidgets, QtCore, QtGui

"""boggle is a word game, typically played with a 4x4 grid
used to create different words. The player can only make words
with lettersin the immediate vicinity of the starting letter.
The amount of points earned is based on the length of the word
entered.

This implements a GUI and timed sessions, as well as the ability
to save games and then load them in the future."""

def roll_board():

    """uses a list of 16 random combinations of letters to creates
    a boggle board. this function also prints out the board with
    the appropriate letters based on list board"""

    #holds the different letter combinations to "randomize" board,
    #then shuffles said letter combinations
    board = [random.choice(["A","E","A","N","E","G"]),random.choice(["A","H","S","P","C","O"]),random.choice(["A","S","P","F","F","K"]),random.choice(["O","B","J","O","A","B"]),random.choice(["I","O","T","M","U","C"]),random.choice(["R","Y","V","D","E","L"]),random.choice(["L","R","E","I","X","D"]),random.choice(["E","I","U","N","E","S"]),random.choice(["W","N","G","E","E","H"]),random.choice(["L","N","H","N","R","Z"]),random.choice(["T","S","T","I","Y","D"]),random.choice(["O","W","T","O","A","T"]),random.choice(["E","R","T","T","Y","L"]),random.choice(["T","O","E","S","S","I"]),random.choice(["T","E","R","W","H","V"]),random.choice(["N","U","I","H","M","Qu"])]
    random.shuffle(board)

    fboard = []

    for index in range(0,16):
        fboard.append("["+board[index]+"]")
        #prints 16 letters randomly selected from the above choices
        #into the appropriate slots on the board
    print("{:<5} {:<5} {:<5} {:<5}".format(fboard[0],fboard[1],fboard[2],fboard[3]))

    print("{:<5} {:<5} {:<5} {:<5}".format(fboard[4],fboard[5],fboard[6],fboard[7]))

    print("{:<5} {:<5} {:<5} {:<5}".format(fboard[8],fboard[9],fboard[10],fboard[11]))

    print("{:<5} {:<5} {:<5} {:<5}".format(fboard[12],fboard[13],fboard[14],fboard[15]))

    #works with special case, letter "Qu"
    for i in range(0,16):
        if board[i] == "Qu":
            board[i] = "%"

    print()
    #returns the formatted board
    return board

def get_input():

    """takes a liser of the user's answers to the boggle board.
    It is then added to the list of words. The game will end if the
    user enters the letter 'X' or 'x'. All of the above is to be stored
    in the list "fwords" """

    print("Start typing your words! (press enter after each word and enter 'X' when done):")
    entry = "go"

    global words
    words = []

    while entry != "X" and entry != "x":
        entry = raw_input(">")
        if(entry != "X" and entry != "x"):
            words.append(entry)

    fwords = []
    counter = 0

    for word in words:
        fwords.append(word.upper())

    for word in fwords:
        fwords[counter] = word.replace("QU","%")
        counter = counter + 1

        #returns list of words
    return fwords

def check_word(word,depth,board,used,position):

    """a recurvsive function that checks if the word that is typed
    in matches letters that are next to each other on the board
    returns True if the word is on the board, false otherwise"""


    #uses positions on the board to ensure that the
    #words are of letters that are next to each otehr

    if position == 0:
        adjacents = [1,4,5]

    elif position < 3:
        adjacents = [-1,1,3,4,5]

    elif position == 3:
        adjacents = [-1,3,4]

    elif position == 4 or position == 8:
        adjacents = [-4,-3,1,4,5]

    elif position == 5 or position == 6 or position == 9 or position == 10:
        adjacents = [-5,-4,-3,-1,1,3,4,5]

    elif position == 7 or position == 11:
        adjacents = [-5,-4,-1,3,4]

    elif position == 12:
        adjacents = [-4,-3,1]

    elif position < 15:
        adjacents = [-5,-4,-3,-1,1]

    else:
        adjacents = [-5,-4,-1]

    result = False;

    if depth == len(word):
        return True

    for adjacent in adjacents:

        if position+adjacent > 15 or position+adjacent < 0:
            continue

        if board[position+adjacent] == word[depth] and used[position+adjacent] == False:
            used[position+adjacent] = True;
            result = check_word(word,depth+1,board,used,position+adjacent)

            if result == True:
                break

    used[position] = False

    return result

def check_list(board,fwords):

    """takes in both the board and a list of words to be checked. calls
    the function "check_word", assuming that there are words in the list fwords.
    Verifies that there aren't any duplicates, that it is on the board,
    that it is an actual word in the dictionary, and then adds the appropriate
    amount of points"""

    used = []
    d = enchant.Dict("en_US")
    for i in range(0,16):
        used.append(False)

    position = 0
    counter = 0
    result = False
    score = 0

    for word in fwords:
        skip = False

        if counter > 0:
            for i in range(0,counter):
                if word == fwords[i]:
                    print("The word "+words[counter]+" has already been used.")
                    skip = True
        if skip:
            counter = counter + 1
            continue
        length = len(word)

        #verifies the length of the word, gives the appropriate
        #amount of points based on the length of the word

        if length < 3:
            print("The word "+words[counter]+" is too short.")
            counter = counter + 1
            continue

        elif length < 5:
            value = 1

        elif length < 6:
            value = 2

        elif length < 7:
            value = 3

        elif length < 8:
            value = 5

        else:
            value = 11

        #verifies position of letters, tracks to make sure that
        #they are actually next to each other on the board

        for position in range(0,16):
            if board[position] == word[0]:
                depth = 1
                used[position] = True
                result = check_word(word,depth,board,used,position)

            #prints the amount of points earned
            if result:
                if d.check(words[counter]):
                    print("The word "+words[counter]+" is worth "+str(value)+" point",end='')
                    if value == 1:
                        print(".")
                    else:
                        print("s.")
                    score = score + value
                #prints this if the word is invalid
                else:
                    print("The word "+words[counter]+" is ... not word.")
                break

        #prints this if the word is not on the board
        if not result:
            print("The word "+words[counter]+" is not present.")

        counter = counter + 1
        #reassigns value of result, regardless of if the word
        #is found or not
        result = False
        i = 0

        #counter iteration
        for n in used:
            used[i] = False
            i = i+1
    #returns the score earned by words inputted
    return score

def play_boggle():

    """ actually executes the boggle game. Calls the main functions, fills
    in the board appropriately, takes user input, checks to make sure that
    it is actually a word, then prints the score earned for the legnth of
    the words that were entered"""

    board = roll_board()
    fwords = get_input()
    score = check_list(board,fwords)

    print("Your total score is "+str(score)+" point",end='')

    if score == 1:
        print("!")

    else:
        print("s!")
    #returns the total score earned in the game
    return score

def format_words(words):

    """formats words to be checked in the dictionary"""

    fwords = []
    counter = 0
    for word in words:
        fwords.append(word.upper())
    for word in fwords:
        fwords[counter] = word.replace("QU","%")
        counter += 1;
    return fwords

class BoggleWindow(QtWidgets.QMainWindow):

    """ actually launches the game window + widgets """

    def __init__(self):

        QtWidgets.QMainWindow.__init__(self)
        popup = StartScreen()
        choice = popup.exec_()

        #if the user chooses to start a saved game

        if choice == QtWidgets.QMessageBox.Yes:
            self.setup()
            self.loadGame()

        #if the user does not want to load an old game,
        #it creates a fresh game and the score is 0

        else:
            self.setup()


    def setup(self):
        #sets the names of the game and presents the Welcome
        #message
        self.setWindowTitle('Boggle Game')
        self.setToolTip("Let's Play Boggle!")

        self.boggle_game = BoggleGame(self)
        self.setCentralWidget(self.boggle_game)

        exit_action = QtWidgets.QAction('Exit', self)
        exit_action.triggered.connect(QtWidgets.qApp.quit)
        #creates a menu with the options to save or load
        #previous games
        #also creates a menu bar with options under "File"
        menu_bar = self.menuBar()
        menu_bar.setNativeMenuBar(False)

        #at the top left of the screen, filemenu
        file_menu = menu_bar.addMenu('File')
        file_menu.addAction(exit_action)
	file_menu.addAction("New",self.newGame)
        file_menu.addAction("Save",self.saveGame)
        file_menu.addAction("Load",self.loadGame)

        #shows the menu options
        self.show()

    def closeEvent(self, event):

        #creates a message if the user wants to end the game,
        #must confirm via popup event

        popup = QuitMessage()
        reply = popup.exec_()

        #if the user chooses to exit, does so
        if reply == QtWidgets.QMessageBox.Yes:
            event.accept()

        #if the user does chooses No, does not proceed with
        #ending the game
        else:
            event.ignore()


    def newGame(self):
	"""Creates a new game, part of the menu_bar
	need to get this to close current window and open
	a new one or update current window"""
	#self.setup()
        self.loadGame()


    def saveGame(self):

        """saves the users game. Will save the date and time
        that the game was played to play later, as well as
        formats appropriately"""

        s = shelve.open('boggle.save')
        ids = open("boggle.ids", "a")
        uid = str(uuid.uuid4())
        ids.write(uid+"\n")
        ids.close()

        s[uid] = {"when": datetime.datetime.now(), "title": datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d %H:%M:%S'), "uid": uid, "letters": self.boggle_game.board.letters, "words": self.boggle_game.list.words, "text": self.boggle_game.input.text(), "time": self.boggle_game.timer.time.remainingTime(), "ticker": self.boggle_game.timer.ticker.remainingTime(), "display": self.boggle_game.timer.display.intValue()}

        s.close()

    def loadGame(self):

        """Loads previously saved games. Has error checking so that
        if there aren't any previously saved games, will print message.
        Also loads the past saved information to current game board"""

        global suid

        try:
            s = shelve.open('boggle.save')

        except:
            print("No Saves to Load")
            return

        dialog = LoadDialog(self,s)
        dialog.exec_()


        self.boggle_game.board.letters = s[suid]["letters"]
        self.boggle_game.board.update()
        self.boggle_game.list.words = s[suid]["words"]
        self.boggle_game.list.update()
        self.boggle_game.input.setText(s[suid]["text"])
        self.boggle_game.input.setReadOnly(False)
        self.boggle_game.timer.time.stop()
        self.boggle_game.timer.time.start(s[suid]["time"])
        self.boggle_game.timer.ticker.stop()
        self.boggle_game.timer.ticker.start(s[suid]["ticker"])
        self.boggle_game.timer.display.display(s[suid]["display"])

class LoadDialog(QtWidgets.QDialog):

    """gets all saved games and sets the suid to represent
    the game to be loaded"""

    def __init__(self, parent, s):

        QtWidgets.QDialog.__init__(self, parent)
        self.setup(s)

    def setup(self, s):

        global suid
        self.grid = QtWidgets.QGridLayout()
        self.setLayout(self.grid)
        keys = []

        try:
            ids = open("boggle.ids", "r")
        #error checking for saved files
        except:
            print("Error!! .ids file deleted or no files ever saved!!")
            return

        for line in ids.readlines():
            keys.append(line.rstrip())

        #works with available loadable files
        self.text = QtWidgets.QLabel("Please select a file to load: ")
        self.list = QtWidgets.QListWidget(self)
        self.grid.addWidget(self.text,1,1,1,1)
        self.grid.addWidget(self.list,2,1,4,1)
        self.allFiles = []

        for key in keys:
            print(s[key])
            print(type(s[key]))
            self.allFiles.append(s[key])

        self.allFiles = sorted(self.allFiles, key=lambda k: k['when'], reverse=True)
        self.list.itemClicked.connect(self.item_click)

        for save in self.allFiles:
            self.list.addItem(save["title"])

    def item_click(self, item):

        #global unique identifier

        global suid
        suid = self.allFiles[self.list.row(item)]["uid"]
        self.close()

class BoggleGame(QtWidgets.QWidget):

    #mirrors the main component

    def __init__(self, parent):
        QtWidgets.QWidget.__init__(self, parent)
        self.setup()

    def setup(self):

        self.board = BoggleBoard(self)
        self.list = TextList(self)
        self.input = InputBox(self)
        self.timer = BoggleTimer(self)

        self.grid = QtWidgets.QGridLayout()
        self.setLayout(self.grid)

        self.grid.addWidget(self.board, 1, 1, 4, 4)
        self.grid.addWidget(self.list, 1, 5, 4, 1)
        self.grid.addWidget(self.input, 5, 1, 1, 5)
        self.grid.addWidget(self.timer, 5, 5, 1, 1, QtCore.Qt.AlignRight)

        self.input.returnPressed.connect(self.make_message())
        self.input.returnPressed.connect(self.input.setup)
        self.timer.time.timeout.connect(self.stoptime)

    def stoptime(self):

        #evaulation execution

        global words
        words = self.list.words
        self.timer.time.stop()
        self.input.setReadOnly(True)
        score = check_list(self.board.letters,format_words(self.list.words))
        popup = ScoreScreen(score)
        reply = popup.exec_()

        if reply == QtWidgets.QMessageBox.Yes:

            self.board.letters = roll_board()
            self.board.update()
            self.list.setup()
            self.input.setText("")
            self.input.setReadOnly(False)
            self.timer.restart()

    def make_message(self):

        def message():

            self.list.addWord(self.input.text())

        return message

class BoggleBoard(QtWidgets.QWidget):

    """The boggle grid."""

    def __init__(self, parent):

        QtWidgets.QWidget.__init__(self, parent)
        self.setup()

    def setup(self):

        self.letters = []
        self.letters = roll_board()
        #get a board from the boggle function loaded in letters
        #make labels out of the board and store them in labels
        self.labels = []
        for letter in self.letters:
            if letter == '%':
                letter = "Qu"
            self.labels.append(QtWidgets.QLabel(letter))
            if letter == "Qu":
                letter = '%'
        for label in self.labels:
            label.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
            label.setStyleSheet("border:1px solid rgb(180, 180, 180); font: bold 48px arial, sans-serif; color: black") #isn't this cool!? CSS in a python program!
        self.setFixedSize(500,500)

        self.grid = QtWidgets.QGridLayout()
        self.setLayout(self.grid)

        #adds widget to appropriate spot on the board

        self.grid.addWidget(self.labels[0], 1, 1, 1, 1)
        self.grid.addWidget(self.labels[1], 1, 2, 1, 1)
        self.grid.addWidget(self.labels[2], 1, 3, 1, 1)
        self.grid.addWidget(self.labels[3], 1, 4, 1, 1)
        self.grid.addWidget(self.labels[4], 2, 1, 1, 1)
        self.grid.addWidget(self.labels[5], 2, 2, 1, 1)
        self.grid.addWidget(self.labels[6], 2, 3, 1, 1)
        self.grid.addWidget(self.labels[7], 2, 4, 1, 1)
        self.grid.addWidget(self.labels[8], 3, 1, 1, 1)
        self.grid.addWidget(self.labels[9], 3, 2, 1, 1)
        self.grid.addWidget(self.labels[10], 3, 3, 1, 1)
        self.grid.addWidget(self.labels[11], 3, 4, 1, 1)
        self.grid.addWidget(self.labels[12], 4, 1, 1, 1)
        self.grid.addWidget(self.labels[13], 4, 2, 1, 1)
        self.grid.addWidget(self.labels[14], 4, 3, 1, 1)
        self.grid.addWidget(self.labels[15], 4, 4, 1, 1)

    def update(self):

        counter = 0
        for letter in self.letters:
            if letter == '%':
                letter = "Qu"
            self.labels[counter].setText(letter)

            if letter == "Qu":
                letter = '%'
            counter += 1

class TextList(QtWidgets.QTextEdit):

    """the user's inputted words - places them on
    the right side of the boggle board, above the timer"""

    def __init__(self, parent):

        QtWidgets.QTextEdit.__init__(self, parent)
        self.setup()


    def setup(self):

        self.words = []
        self.setFixedSize(300,500)
        self.text = ""
        self.setReadOnly(True)
        self.setText(self.text)

    def addWord(self, word):

        if(word == ""):
            return
        self.words.append(word)
        self.text = ""
        for word in self.words:
            self.text = self.text + word + "\n"
        self.setText(self.text)

    def update(self):

        self.text = ""
        for word in self.words:
            self.text = self.text + word + "\n"
        self.setText(self.text)

class InputBox(QtWidgets.QLineEdit):

    """takes the user's input - to be placed
    on right side of the boggle board after input"""

    def __init__(self, parent):

        QtWidgets.QLineEdit.__init__(self, parent)
        self.setup()

    def setup(self):

        self.setText("")
        self.setFixedWidth(690);

class BoggleTimer(QtWidgets.QWidget):

    """the timer - set for 3 minutes (180 seconds)
    also the setup for the background widget and layout"""

    def __init__(self, parent):

        QtWidgets.QWidget.__init__(self,parent)
        self.setup()

    def setup(self):

        self.time = QtCore.QTimer()
        self.ticker = QtCore.QTimer()
        self.ticker.start(1000)
        self.time.start(180000)
        self.display = QtWidgets.QLCDNumber()
        self.display.setSegmentStyle(self.display.Flat)
        self.display.setStyleSheet("color: black;")
        self.display.display(180)
        self.ticker.timeout.connect(self.ticktime)
        self.grid = QtWidgets.QGridLayout()
        self.setLayout(self.grid)
        self.display.setFixedWidth(100)
        self.grid.addWidget(self.display,1,1,1,1)

    def ticktime(self):

        self.display.display(self.display.intValue() - 1)

        if(self.display.intValue() != 0):
            self.ticker.start(1000)
        else:
            self.ticker.stop()

    def restart(self):

        self.time.start(180000)
        self.ticker.start(1000)
        self.display.display(180)

"""Here are some different message boxes that will
come up at the start of the game, after the game,
or the end of the game"""

class ScoreScreen(QtWidgets.QMessageBox):

    """prints user's score - prompts them to see if they
    would like to play another game"""

    def __init__(self,score):

        QtWidgets.QMessageBox.__init__(self)
        self.setText("Time's Up!\nScore: "+str(score)+"\nWould you like to play again?")
        self.addButton(self.No)
        self.addButton(self.Yes)

class StartScreen(QtWidgets.QMessageBox):

    """Start message - will load saved games if user
    chooses to and has saved games available"""

    def __init__(self):

        QtWidgets.QMessageBox.__init__(self)
        self.setText("Welcome to boggle! Would you like to load a saved game?")
        self.addButton(self.No)
        self.addButton(self.Yes)

class QuitMessage(QtWidgets.QMessageBox):

    """If user presses "exit", will be prompted
    confirming them quitting"""

    def __init__(self):

        QtWidgets.QMessageBox.__init__(self)
        self.setText("Are you sure that you want to quit?")
        self.addButton(self.No)
        self.addButton(self.Yes)

if __name__ == "__main__":

    """runs program - gets widgets working with command line args"""

    app = QtWidgets.QApplication(sys.argv)
    main_window = BoggleWindow()
    app.exec_()
