import MySQLdb
def connection():
    conn = MySQLdb.connect(host="localhost", user="root", passwd="raj1804", db="warzone")
    c = conn.cursor()
    return c, conn
