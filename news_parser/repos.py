import sqlite3


class Repos:

    db_path='data/db.db'


    def select_all_from_table(self, table_name="resources"):

        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()

            select_query = f"select * from {table_name};"
            cursor.execute(select_query)
            records = cursor.fetchall()
            cursor.close()

        except sqlite3.Error as error:
            return f"Error while connecting to sqlite: {error}"

        finally:
            if conn:
                conn.close()
                return records
            
    
    def insert_data_to_items(self, data: list):

        try:
            conn = sqlite3.connect(self.db_path)
            cur = conn.cursor()
            sql = '''INSERT INTO items
                     VALUES(?,?,?,?,?,?,?,?)'''
            cur.executemany(sql, data)
            conn.commit()
            
            print(f"ROWCOUNT: {cur.rowcount}")
            conn.commit()
            cur.close()

        except sqlite3.Error as error:
            print(f"Error while connecting to sqlite: {error}")

        finally:
            if conn:
                conn.close()
                print("The SQLite connection is closed")
            

    def get_resource_id(self, resource_name: str):
        
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()

            select_query = f'''
                select RESOURCE_ID
                from resources 
                where RESOURCE_NAME = ?;
            '''
            cursor.execute(select_query, (resource_name,))
            records = cursor.fetchall()
            cursor.close()

        except sqlite3.Error as error:
            return f"Error while connecting to sqlite: {error}"

        finally:
            if conn:
                conn.close()
                return records