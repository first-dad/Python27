

__author__ = 'Илья'


class BCommand(object):
    def __init__(self, title, cursor):
        self.title = title
        self.cursor = cursor


class PutImage(BCommand):
    def execute(self):
        pass


class PutFromFile(BCommand):
    def execute(self):
        pass


class MainWindow():
     def __init__(self):
         self.cursor = Cursor(self)
         self.actions = [
             PutImage(u"Вставить картинку", self.cursor),
             PutFromFile(u"Вставить текст из файла", self.cursor)
         ]

     def execCurrentAction(self):
         self.curAction.execute()

if __name__ == '__main__':
    pass