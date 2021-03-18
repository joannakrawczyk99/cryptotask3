
class DbFunctions:
    """Class DbFunctions is for database controlling. It allows to create new table and insert data. """
    def __init__(self, database, cursor):
        self.connection = database
        self.c = cursor

    def createTableIfNotExists(self):
        """For creating a table that I need."""
        self.connection.execute('''CREATE TABLE IF NOT EXISTS passwords (username text, password text, salt text)''')
        self.connection.commit()

    def insertData(self, username, key, salt):
        """For inserting data into the table created in previous method (createTable)."""
        sql = ''' INSERT INTO passwords (username, password, salt) VALUES (?,?,?)'''
        self.c.execute(sql, (username, key, salt))
        self.connection.commit()
        print('The record has been added to the database.')


