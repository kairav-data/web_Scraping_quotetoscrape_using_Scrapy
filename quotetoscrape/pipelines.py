# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


import sqlite3



class QuotetoscrapePipeline(object):

    def __init__(self):
        self.create_connection()
        self.create_table()


    def create_connection(self):
        self.conn=sqlite3.connect("myquotes.db")
        self.curr=self.conn.cursor()

    def create_table(self):
        self.curr.execute("""DROP TABLE IF EXISTS quotes_tb""")
        self.curr.execute("""CREATE TABLE quotes_tb(
                        text text,
                        author text,
                        tag text
                        )""")

    def process_item(self, item, spider):
        self.store_db(item)
        return item
    def store_db(self,item):
        self.curr.execute("""INSERT INTO quotes_tb VALUES (?,?,?)""",(
            item['text'],
            item['author'],
            ','.join(item['tags'])  # Join the tags list into a single string
        ))

        self.conn.commit()
