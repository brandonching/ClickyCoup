import psycopg2

DBname='dropfu2fh9s54'
DBuser='twtdpbrncuknog'
DBpassword='750683d7f02a5706e0aef1cad6eef3d4085b2766e51253a52c59a17556d552ad'
DBhost='ec2-174-129-236-147.compute-1.amazonaws.com'
DBport='5432'


conn = psycopg2.connect(dbname=DBname,
                        user=DBuser,
                        password=DBpassword,
                        host=DBhost,
                        port=DBport,
                        connect_timeout='10')
cur = conn.cursor()
conn.autocommit = True


def mark_lap(day, team_id, time_stamp, judge):
    cur = conn.cursor()
    try:
        query = "INSERT INTO public.score_rawclickeydata (day, team_id, time_stamp, judge) VALUES (%s, %s, %s, %s)"
        cur.execute(query, (day, team_id, time_stamp, judge))
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

def undo_lap(day, team_id, time_stamp, judge):
    cur = conn.cursor()
    try:
        query = "INSERT INTO public.score_rawundodata (day, team_id, time_stamp, judge) VALUES (%s, %s, %s, %s)"
        cur.execute(query, (day, team_id, time_stamp, judge))
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

mark_lap(4, 13, '2021-07-18 23:07:47.628037', 'William')
