import logging
import mysql.connector
from settings.Config import Config
from libs.Loggers import Loggers

class Database:
    def __init__(
            self,
            host = Config.DB["HOST"],
            port = Config.DB["PORT"],
            user = Config.DB["USER"],
            password = Config.DB["PASS"],
            database = Config.DB["NAME"],
            table_name = Config.DB["TABLE_NAME"]
        ) -> None:
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.database = database
        self.table_name = table_name
        Loggers()
        super().__init__()

    def connect(self) -> None:
        try:
            self.mydb = mysql.connector.connect(
                host=self.host,
                port=self.port,
                user=self.user,
                password=self.password,
                database=self.database
            )
            self.mycursor = self.mydb.cursor(buffered=True)
        except Exception as e:
            logging.error(e)

    def close(self) -> None:
        self.mydb.close()

    @staticmethod
    def query_log(interval:int) -> str:
        return F"SELECT status, count(*) as total FROM logs WHERE timestamp >= DATE_SUB(NOW(), INTERVAL {interval} MINUTE) GROUP BY status ORDER BY total DESC;"

    def execute(self, query, values=None) -> bool|str|None:
        try:
            self.connect()
            self.mycursor.execute(query, values)
            self.mydb.commit()
            self.close()
            return True, None
        except Exception as e:
            return False, str(e)

    def insert(self, fields:dict, data:dict) -> None|str|bool:
        try:
            query = F"INSERT INTO {self.table_name} ({', '.join(fields)}) VALUES ({', '.join(['%s' for i in range(len(fields))])})"
            values = tuple([data[field] for field in fields])
            self.execute(query, values)
            self.close()
            return True, None
        except Exception as e:
            return False, str(e)
        
    def select(self, query:str) -> None|str|list:
        try:
            self.connect()
            self.mycursor.execute(query)
            column = [column[0] for column in self.mycursor.description]
            data = self.mycursor.fetchall()
            result = []
            for row in data:
                result.append(dict(zip(column, row)))
            self.close()
            return result, None
        except Exception as e:
            return [], str(e)