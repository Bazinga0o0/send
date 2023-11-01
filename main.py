import mysql.connector

def sendMessage(Message: str, User_id: int, Chat_id: int):
    if not checkUserInChat(User_id, Chat_id):
        return
    else:
        cnx = mysql.connector.connect(user='root', password='', host='localhost', database='saas')
        cursor = cnx.cursor(buffered=True)  
        query = "INSERT INTO messages (user_id, message, chat_id) VALUES (%s, %s, %s)"
        values = (User_id, Message, Chat_id)
        cursor.execute(query, values)
        cnx.commit()
        cursor.close()
        cnx.close()
def createUser(name: str, email: str):
    cnx = mysql.connector.connect(user='root', password='', host='localhost', database='saas')
    cursor = cnx.cursor(buffered=True)  
    query = "INSERT INTO users (name, email) VALUES (%s, %s)"
    values = (name, email)
    cursor.execute(query, values)
    cnx.commit()
    cursor.close()
    cnx.close()
def createChat(name: str, user_id: int):
    cnx = mysql.connector.connect(user='root', password='', host='localhost', database='saas')
    cursor = cnx.cursor(buffered=True)
    query = "INSERT INTO chat (name, user_id) VALUES (%s, %s)"
    values = (name, user_id)
    cursor.execute(query, values)
    cnx.commit()
    cursor.close()
    cnx.close()
def createUserChat(User_id: int, Chat_id: int):
    cnx = mysql.connector.connect(user='root', password='', host='localhost', database='saas')
    cursor = cnx.cursor(buffered=True)
    query = "INSERT INTO userchat (user_id, chat_id) VALUES (%s, %s)"
    values = (User_id, Chat_id)
    cursor.execute(query, values)
    cnx.commit()
    cursor.close()
    cnx.close()
def getChatMessages(chat_id: int):
    cnx = mysql.connector.connect(user='root', password='', host='localhost', database='saas')
    cursor = cnx.cursor(buffered=True)
    
    query = f"SELECT message,user_id, timestamp FROM messages WHERE chat_id = {chat_id} LIMIT 0,100"
    #values = (chat_id)
    cursor.execute(query)#, values)
    results = cursor.fetchall()
    n = []
    for (message, user_id, timestamp) in results:
        print(cursor.rowcount)
        query = f"SELECT name FROM users WHERE id = {user_id}"
        cursor.execute(query)
        for (name) in cursor:
            nname = name             
        print(message, nname , timestamp.strftime("%m/%d/%Y, %H:%M:%S") )
        n.append(timestamp.strftime("%m/%d/%Y, %H:%M:%S").replace(",","") +" "+ str(user_id) +" "+ nname[0]+ ": " + message.replace(",", "%22"))
        print("ja")
    cursor.close()
    cnx.close()
    print(n)
    return n
def checkUserInChat(user_id: int, chat_id: int):
    cnx = mysql.connector.connect(user='root', password='', host='localhost', database='saas')
    cursor = cnx.cursor(buffered=True)
    query = "SELECT * FROM userchat where user_id = %s and chat_id = %s"
    values = (user_id, chat_id)
    cursor.execute(query, values)
    if cursor.fetchone() is None:
        cursor.close()
        cnx.close()
        return False
    else:
        cursor.close()
        cnx.close()
        return True
def onRequest(user_id: int, chat_id: int):
    if checkUserInChat(user_id, chat_id):
        getChatMessages(chat_id)

def getChats(user_id: int):
    cnx = mysql.connector.connect(user='root', password='', host='localhost', database='saas')
    cursor = cnx.cursor(buffered=True)
    query = f"SELECT chat_id FROM userchat WHERE user_id = {user_id}"
    cursor.execute(query)
    chats = dict()
    for (chat_id) in cursor:
        chat_id = chat_id[0]
        query = f"SELECT name FROM chat WHERE id = {chat_id}"
        cursor.execute(query)
        for (name,) in cursor:
            chats[chat_id] = name
    cursor.close()
    cnx.close()
    return chats
def checkUserExists(email: str, password: str):
    cnx = mysql.connector.connect(user='root', password='', host='localhost', database='saas')
    cursor = cnx.cursor(buffered=True)
    query = "SELECT * FROM users where email = %s and pwd = %s"
    values = (email, password)
    cursor.execute(query, values)
    if cursor.fetchone() is None:
        cursor.close()
        cnx.close()
        return False
    else:
        cursor.close()
        cnx.close()
        return True
def getUserId(email: str):
    cnx = mysql.connector.connect(user='root', password='', host='localhost', database='saas')
    cursor = cnx.cursor(buffered=True)
    query = "SELECT id FROM users where email = %s"
    values = (email,)
    cursor.execute(query, values)
    for (id) in cursor:

        idd = id[0]
        print(idd)
    cursor.close()
    cnx.close()
    return idd
