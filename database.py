import sqlite3

conn = sqlite3.connect('bot_database.db')
cursor = conn.cursor()
def set_api(chat_id, api_key):
    
    # Save the API key and chat ID in the database
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY,
            chat_id INTEGER UNIQUE,
            api TEXT
        )
    ''')
    conn.commit();
    cursor.execute('''
        INSERT OR REPLACE INTO users (chat_id, api)
        VALUES (?, ?)
    ''', (chat_id, api_key))
    conn.commit()

    # Close the database connection
    conn.close()

def check_api(message,bot):
    chat_id = message.chat.id
    try:
        

        # Execute the SELECT query to retrieve the API key for the user
        cursor.execute('SELECT api_key FROM users WHERE chat_id = ?', (chat_id,))
        result = cursor.fetchone()

        if result:
            api_key = result[0]
            bot.send_message(chat_id, f"Your API key is: {api_key}")
        else:
            bot.send_message(chat_id, "API key not found for your user")

    except Exception as e:
        print(f"Error retrieving API key: {e}")
        bot.send_message(chat_id, "An error occurred while retrieving the API key")