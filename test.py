import psycopg2

DBname='dropfu2fh9s54'
DBuser='twtdpbrncuknog'
DBpassword='750683d7f02a5706e0aef1cad6eef3d4085b2766e51253a52c59a17556d552ad'
DBhost='ec2-174-129-236-147.compute-1.amazonaws.com'
DBport='5432'

'''
DBname='d53cm3obkeu1rv'
DBuser='u2jr1ckgkg0pf2'
DBpassword='p8271178052023deb982000fe1a7628add214ec18ef723f6fce1bc11846596d7a'
DBhost='ec2-3-212-58-54.compute-1.amazonaws.com'
DBport='5432'
'''

conn = psycopg2.connect(dbname=DBname,
                        user=DBuser,
                        password=DBpassword,
                        host=DBhost,
                        port=DBport,
                        connect_timeout='10')
cur = conn.cursor()
# conn.autocommit = True


def mark_lap(day, team_id, time_stamp, judge):
    print("hi")
    #conn = None
    DBname = 'd53cm3obkeu1rv'
    DBuser = 'u2jr1ckgkg0pf2'
    DBpassword = 'p8271178052023deb982000fe1a7628add214ec18ef723f6fce1bc11846596d7a'
    DBhost = 'ec2-3-212-58-54.compute-1.amazonaws.com'
    DBport = '5432'
    conn = psycopg2.connect(dbname=DBname,
                            user=DBuser,
                            password=DBpassword,
                            host=DBhost,
                            port=DBport,
                            connect_timeout='10')
    cur = conn.cursor()
    try:
        print("hi2")
        #params = config()
        #conn = psycopg2.connect(**params)
        #conn = psycopg2.connect()
        #cur = conn.cursor()
        query = "INSERT INTO public.score_rawclickeydata (day, team_id, time_stamp, judge) VALUES (%s, %s, %s, %s)"
        print("hi3")
        cur.execute(query, (day, team_id, time_stamp, judge))
        cur.execute(query, (1,2,'2021-07-18 23:07:47.628037', '4'))
        cur.close()
        print("here4")
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
'''
def undo(day, team_id, time_stamp, judge):
    conn.connect()
    query = "INSERT INTO public.score_rawundodata (day, team_id, time_stamp, judge) VALUES (%s, %s, %s, %s)"
    cur.execute(query, (day, team_id, time_stamp, judge))
    conn.close()
'''

mark_lap(2, 23, '2021-07-18 23:07:47.628037', 'William')