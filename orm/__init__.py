import datetime

from sqlalchemy import *
from sqlalchemy import create_engine


class Saver:
    def __init__(self):
        self.db = create_engine('sqlite:///test.db', echo=False)

        self.metadata = MetaData(self.db)

        now = datetime.datetime.now()
        table_name = 'merchants - ' + now.isoformat()
        # TODO Check, if Database is created, else create DB MySQL
        #engine = create_engine('mysql://Jasper:Moy@localhost/?')
        self.merchants_table = Table(table_name, self.metadata,
                                     Column('id', Integer, primary_key=True),
                                     Column('name', String(100)),
                                     Column('cost', String)
                                     )
        self.init_db()

    def init_db(self):
        # Create DB table with name from date?
        self.merchants_table.create()

#m = merchants_table.insert()
#print m.execute(name='1-800', cost='4')
#
#
#s = merchants_table.select()
#rs = s.execute()
#row = rs.fetchone()
#print 'Name:', row[2]

if __name__ == '__main__':
    init_db()