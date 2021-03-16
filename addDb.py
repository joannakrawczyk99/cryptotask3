
class dbFunctions:

    def __init__(self, database, cursor):
        self.connection = database
        self.c = cursor

    def createTable(self):
        self.connection.execute('''CREATE TABLE passwords (username text, password text, salt text)''')
        self.connection.commit()
        print('The table has been added to the database.')


    def insertData(self, username, key, salt):
        sql = ''' INSERT INTO passwords (username, password, salt) VALUES (?,?,?)'''
        self.c.execute(sql, (username, key, salt))
        self.connection.commit()
        print('The record has been added to the database.')
