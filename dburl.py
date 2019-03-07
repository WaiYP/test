import os
import  argparse

def main(database , url_list_file):
    print ( "we are goint work with " + str( database))
    print ("we are going scan " + str( url_list_file))

if __name__ == "__main__":
    parse = argparse.ArgumentParser()
    parse.add_argument("-db","--database",help="SQLite File Name")
    parse.add_argument("-i","--input",help="File containing urls to read" )
    args = parse.parse_args()
    database_file = args.database
    input_file = args.input
    main(database=database_file,url_list_file=input_file)