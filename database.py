import sqlite3

users_table = '''
            CREATE TABLE IF NOT EXISTS api_keys(
                chat_id INTEGER PRIMARY KEY,
                api TEXT,
                temperature DECIMAL(2,1) DEFAULT 0.5,
                models VARCHAR(20) DEFAULT 'text-davinci-003',
                tokens SMALLINT DEFAULT 400
            )'''
class Database:
    def __init__(self):
        self.conn = sqlite3.connect('chatgpt.db');
        self.c = self.conn.cursor()
        self.c.execute(users_table)
        self.conn.commit()

    def stop(self):
        self.c.close();
        self.conn.close();

def set_api(bot,message):
    chat_id = message.chat.id
    api_key = message.text.split("setapi")[1].strip()

    conn = sqlite3.connect('chatgpt.db')
    cursor = conn.cursor()

    put_data = 'INSERT OR REPLACE INTO api_keys (chat_id, api) VALUES (?, ?)'
    cursor.execute(put_data, (chat_id, api_key))
    conn.commit()

    api_query = 'SELECT api FROM api_keys WHERE chat_id = ?'
    cursor.execute(api_query, (chat_id,))
    api_key = cursor.fetchone()[0]

    conn.close()

    bot.send_message(chat_id, api_key)