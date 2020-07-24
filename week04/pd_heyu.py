import pandas as pd
import numpy as np

class SQLtoPD(object):
    def __init__(self):
        self.users = pd.read_csv('C:/Users/86134/Python001-class01/week04/users.csv')
        self.orders = pd.read_csv('C:/Users/86134/Python001-class01/week04/orders.csv')
        self.orders2 = pd.read_csv('C:/Users/86134/Python001-class01/week04/orders_2.csv')
    
    # 1. SELECT * FROM data;
    def select_all_data(self):
      print(self.users)

    # 2. SELECT * FROM data LIMIT 10;
    def select_lim_data(self):
      print(self.users[0:10])

    # 3. SELECT id FROM data;  //id 是 data 表的特定一列
    def select_id_data(self):
      print(self.users['id'])

    # 4. SELECT COUNT(id) FROM data;
    def select_count_data(self):
      print(self.users['id'].count())
    
    # 5. SELECT * FROM data WHERE id<1000 AND age>30;
    def select_where_data(self):
      print(self.users[ (self.users['id']<1000) & (self.users['age']>30) ] )

    # 6. SELECT id,COUNT(DISTINCT order_id) FROM table1 GROUP BY id;
    def group_data(self):
      print(self.orders[['id','user_id']].groupby('user_id').count())
      # print(self.orders.groupby('user_id').agg({'user_id':'count', 'qty':'sum'}))

    # 7. SELECT * FROM table1 t1 INNER JOIN table2 t2 ON t1.id = t2.id;
    def join_data(self):
      # print(pd.merge(self.users, self.orders, on='id', how='inner'))
      print(self.users.merge(self.orders, left_on='id', right_on='user_id'))

    # 8. SELECT * FROM table1 UNION SELECT * FROM table2;
    def union_data(self):
      df = pd.concat([self.orders, self.orders2])
      print(df.drop_duplicates())
    
    # 9. DELETE FROM table1 WHERE id=10;
    def delete_data(self):
      print(self.users[ self.users['id']!=10 ])
      # print(self.users.drop([10], axis=0))
    
    # 10. ALTER TABLE table1 DROP COLUMN column_name;
    def alter_data(self):
      print(self.users.drop('age', axis = 1))

def main():
  c = SQLtoPD()
  c.group_data()

if __name__ == '__main__':
  main()