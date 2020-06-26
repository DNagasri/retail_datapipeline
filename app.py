import sys
from config import DB_DETAILS
from util import get_tables

def main():
    # for arg in sys.argv:
    #   print(arg)
    """Program takes atleast one argument"""
    env = sys.argv[1]
    db_details = DB_DETAILS[env]
    # print(db_details)
    tables=get_tables("tables_list")
    for table in tables['table_name']:
        print(table)


if __name__ =='__main__':
    main()
