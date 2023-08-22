import sqlite3

class Connection:
    def __init__(self):
        _database = 'SYSWEB.DB'
        _conn = None
        _cursor =None
        _connected = False
        self.database = _database
        self.conn = _conn
        self.cursor = _cursor
        self.connected = _connected
        
    def connect(self):
        if self.connected == False:
            try:
                self.conn = sqlite3.connect(self.database)
            except sqlite3.Error as e:
                print(f"Não foi possivel conectar no banco de dados, erro {e}")
                return False
            else:
                 self.connected = True

        else:
            return True
    def execute_query(self, sql, params=None):
        
        try:
            if self.connected == True:
                self.cursor = self.conn.cursor()
                if params != None:
                    self.cursor.execute(sql, params)
                else:
                    self.cursor.execute(sql)   
            else:
                return False
        except sqlite3.DataError as e:
            print(f"Erro ao executar {e}")


    def persist(self):
        if self.connected == True:
            self.conn.commit()
            return True
        else:
            return False
        
    def fetch_all(self):
        try:
            result = self.cursor.fetchall()
            return result
        except sqlite3.Error as e:
            print(f'Erro {e}')

    def disconect(self):
        self.conn.close()
        self.connected = False



