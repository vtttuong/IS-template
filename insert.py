# import csv, sqlite3

# con = sqlite3.connect(r"C:\Users\DELL\Desktop\MLAPLI-master\app\mpgWebApp\db.sqlite3") # change to 'sqlite:///your_filename.db'
# cur = con.cursor()
# # pandas.read_csv(csvfile).to_sql(table_name, conn, if_exists='append', index=False)
# with open('bongdaduc.csv','r') as fin: # `with` statement available in 2.5+
#     # csv.DictReader uses first line in file for column headings by default
#     dr = csv.DictReader(fin) # comma is default delimiter
#     to_db = [(match['Round'],
#             match['AwayName'],
#             match['AwayGoals'],
#             match['HomeName'],
#             match['HomeGoals'],
#             match['StadiumName'],
#             match['StartDate'],
#             match['StartTime']) for match in dr]

#     cur.executemany('''INSERT INTO bundesliga_schedule_2020
#                     (
#                         round, 
#                         awayname, 
#                         awaygoals, 
#                         homename, 
#                         homegoals, 
#                         stadiumname, 
#                         startdate, 
#                         starttime
#                     )
#                     VALUES(?,?,?,?,?,?,?,?)''', to_db)
# con.commit()
# con.close()

a = "bundesliga"
b = "seria-a"
c = 'premier-league'
aa = c.split('-')
res = ''
for i in aa:
    res += i.capitalize() + ' '
res = res[:len(res)-1]
print(res)

