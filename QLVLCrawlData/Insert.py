
import mysql.connector

# connection = mysql.connector.connect(user='root', password='1234', host='localhost', database='pbl3')
# cursor = connection.cursor()
# iid = "SELECT id FROM industry WHERE `NAME` = " + str("'IT'") 

# # sql = "INSERT INTO company(id, name, address, industry_id) VALUES (0, 'quang da', 'ha noi', iid)"
# cursor.execute(iid)
# id = cursor.fetchone()
# id = ''.join(str(x) for x in id)
# print(id)

#cursor.execute(sql)

# connection.commit()
# connection.close()

# l = [1, 2, 3, 4, 5, 6, 7]

# print(l[3:6]) # include 3 , exclude 6
# a = [2, 1]
# a.extend(l[3:6])
# print(len(a))

l = [1, 1, 2, None, 4, None]
for i in l:
    if i is None:
        print("none")
    else:
        print("not none")