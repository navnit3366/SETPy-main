import sqlite3

class SLEEPdatabase:
    def __init__(self, database_src):
        self.database = sqlite3.connect(database_src)
        self.cursr = self.database.cursor()
        self.cursr.execute("""CREATE TABLE IF NOT EXISTS sleep_tracker(
                    date_start TEXT,
                    time_start TEXT,
                    date_end TEXT,
                    time_end TEXT,
                    duration TEXT,
                    remark TEXT
                )""")
        self.cursr.execute("""CREATE TABLE IF NOT EXISTS sleep_plans(
                    date_start TEXT,
                    time_start TEXT,
                    date_end TEXT,
                    time_end TEXT,
                    duration TEXT,
                    remark TEXT
                )""")
        self.database.commit()

    def insert_all(self, table_name, data):
        self.cursr.executemany(f'INSERT INTO {table_name} values (?, ?, ?, ?, ?, ?)', data)
        self.database.commit()
    
    def insert_one(self, table_name, date_start, time_start, date_end, time_end, duration, remark):
        self.cursr.execute(f'''INSERT INTO {table_name} values (?, ?, ?, ?, ?, ?)''',
                            (date_start, time_start, 
                            date_end, time_end,
                            duration, remark))
        self.database.commit()
    
    def fetch(self, table_name):
        self.cursr.execute(f'SELECT rowid, * FROM {table_name}')
        return self.cursr.fetchall()
    
    def remove(self, table_name, id):
        self.cursr.execute(f'DELETE FROM {table_name} WHERE rowid = {id}')
        self.database.commit()

    def update(self, table_name, id, date_start, time_start, date_end, time_end, duration, remark):
        self.cursr.execute(f'''UPDATE {table_name} SET 
                            date_start = ?, time_start = ?,
                            date_end = ?, time_end = ?,
                            duration = ?, remark = ? WHERE rowid = {id}''',
                            (date_start, time_start, 
                            date_end, time_end,
                            duration, remark))
        self.database.commit()

    def delete_table(self, table_name):
        self.cursr.execute(f'DELETE FROM {table_name}')
        self.database.commit()