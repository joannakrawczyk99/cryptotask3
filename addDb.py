import logging


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
        """
        If table does not exist this function creates it.
        """
        self.connection.execute('''CREATE TABLE IF NOT EXISTS passwords (username text, password text, salt text)''')
        self.connection.commit()

    def insertData(self, username, key, salt):
        """
        This function inserts data into the database and returns message.

        :param username: username entered by the user
        :param key: hashed password with the salt
        :param salt: random and unique salt
        :return: message about the result of the operation
        """
        sql = ''' INSERT INTO passwords (username, password, salt) VALUES (?,?,?)'''
        self.c.execute(sql, (username, key, salt))
        self.connection.commit()
        logging.info('The record has been added to the database.')




