import mysql.connector

cnx = mysql.connector.connect(user='scc_scrut',
                              password='SCC!scrut',
                              host='mysql.solarcarchallenge.org',
                              database='scrutineering')
cursor = cnx.cursor(buffered=True)
cnx.autocommit = True


def marklap(day, team_id, time_stamp, judge):
    query = "INSERT INTO score_rawclickydata_mysql " \
            "(day, team_id, time_stamp, judge) VALUES " \
            "(%s, %s, %s, %s)"
    cursor.execute(query, (day, team_id, time_stamp, judge))


def undo(day, team_id, time_stamp, judge):
    query = "UPDATE score_rawclickydata_mysql " \
            "SET append='UNDO' " \
            "WHERE day=%s & team_id=%s & DATE_SUB(time_stamp=%s, INTERVAL 2 HOUR) & judge=%s"
    cursor.execute(query, (day, team_id, time_stamp, judge))


marklap(1, 7, '2021-08-12 12:13:55', 'Brandon')
undo(1, 7, '2021-08-12 12:13:55', 'Brandon')