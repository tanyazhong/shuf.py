#!/usr/bin/python
import random
import sys
import argparse


def main():

    parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter,
                                   description="""Write a random permutaion of the input lines to standard output.

With no FILE, or when FILE is -, read standard input.""")
    parser.add_argument("-i", "--input-range", action ='store', dest='range',
                        help="treat each number LO through HI as an input line", metavar='LO-HI')
    parser.add_argument("-n", "--head-count", action='store', dest='headcount', type=int,
                        help="output at most COUNT lines", metavar="COUNT")
    parser.add_argument("-r", "--repeat", action='store_true', help="output lines can be repeated")
    parser.add_argument('FILE', nargs='?')


    args = parser.parse_args()
    argsd = vars(args) 

    """
    print("range =", argsd['range'])
    print("count = ", argsd['headcount'])
    print("repeat =", argsd['repeat'])
    print("file =", argsd['FILE'])
    """
 
    shuf_range = 0
    count_set = False
    file_set = False
    lines = []

    
    if argsd['headcount'] != None:
        count_set = True

    if argsd['FILE'] != None:
        file_set = True
           
    #if -n is set, check if negative 
    if count_set:
        if argsd['headcount'] < 0:                 
            parser.error(f"invalid line count: '{args.headcount}'")
            
    string = ""
    range_string = argsd['range']

    #if -i is set, extract integers and make a list called  lines
    #if -i is not set check for a file
    if argsd['range'] != None:
        #-i cannot be used with a file
        if file_set:
            parser.error(f"extra operand: '{args.FILE}'")

        #if not make a list from integers
        ints = range_string.split('-', 1)

        #attempt to convert the list items to integers
        if len(ints) != 2:
            parser.error(f"invalid input range: '{ints[0]}'")
            
        try:
            int(ints[0])
        except:
            parser.error(f"invalid input range: '{ints[0]}'")

        try:
            int(ints[1])
        except:
            parser.error(f"invalid input range: '{ints[1]}'")

        begin = int(ints[0])
        end = int(ints[1])  
        difference = end - begin

        if difference < 0:
            parser.error(f"invalid input range: '{range_string}'")

        if difference == 0:
            lines.append(str(begin))
        else:
        #make a for loop that inserts integers into lines.
            list_item = begin
            for i in range(difference+1):
                lines.append(str(list_item))
                list_item += 1
            
    #else if -i is not set         
    else:
        #check if need to get from stdin. if so, make a list of lines
        #if not, make a list of lines from the file
        if argsd['FILE'] == None or argsd['FILE'] == '-':
            try:
                string = sys.stdin.read()
            except KeyboardInterrupt:
                exit
            lines = string.splitlines(True)
        else:
            try:
                file = open(argsd['FILE'], 'r')
            except:
                parser.error(f"{args.FILE}: no such file or directory")
            file = open(argsd['FILE'], 'r')
            lines = file.readlines()
            file.close()
            string = "something"

    #by default set shuf_range to the number of lines in the file    
    shuf_range = len(lines)
    
    #if -n is set, set shuf_range to argument integer
    if count_set and string != "":
        shuf_range = argsd['headcount']

    #make a list with (shuf_range) randomized lines
    shuffled_list = random.sample(lines, shuf_range)

    #output the randomized lines
    if argsd['repeat']:
        #if -n is set with -r, allow for repeated lines
        if count_set:
           for i in range(shuf_range):
               print(random.choice(lines).rstrip())
        else:
            try:
                while True:
                    print(random.choice(lines).rstrip())
            except KeyboardInterrupt:
                exit
    else:
        for i in range(shuf_range):
            print(shuffled_list[i].rstrip())

  
if __name__ == "__main__":
    main()

