
class DbFunctions:
    """
        Class DbFunctions is for database controlling. It allows to create new table and insert data.
        ...
        Attributes
        ----------
        connection :
            let connect with the database

        cursor :
            let operate on the database

        Methods
        -------
         createTableIfNotExists():
            creates new table if does not exist

        insertData():
            add new record to the table
        """
    def __init__(self, database, cursor):
        self.connection = database
        self.c = cursor

    def createTableIfNotExists(self):
        self.connection.execute('''CREATE TABLE IF NOT EXISTS passwords (username text, password text, salt text)''')
        self.connection.commit()

    def insertData(self, username, key, salt):
        sql = ''' INSERT INTO passwords (username, password, salt) VALUES (?,?,?)'''
        self.c.execute(sql, (username, key, salt))
        self.connection.commit()
        print('The record has been added to the database.')


