import oracledb
import csv
import oracle_config

con =oracledb.connect(user=oracle_config.user, password=oracle_config.password, dsn=oracle_config.dsn)
cur = con.cursor()
cur.execute('select * from STORE.CUSTOMERS')
rows = cur.fetchall()
# print(rows)
with open('output.csv','w', newline='') as csvfile:
    write = csv.writer(csvfile)
    write.writerows(rows)
