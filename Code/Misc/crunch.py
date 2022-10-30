import argparse
import sys

low_charset = "abcdefghijklmnopqrstuvwxyz"
upp_charset = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
num_charset = "0123456789"
sym_charset = r"!@#$%^&*()-_+=~`[]{}|\:;\"'<>,.?/ "

charlist = []
loopList = []

i = 0
n = 0
loop = True

parser = argparse.ArgumentParser()
   
parser.add_argument('-o', '--options', type=str, nargs=3, help="options argument", 
        metavar='<min> <max> <chars>', dest='opt')
parser.add_argument("-t", "--template", type=str, nargs='*',
        help="Use a preset character set", dest="temp")

args = parser.parse_args()

print("")

if args.temp:
    if args.temp[0] == "low_charset":
        charset = low_charset
    elif args.temp[0] == "upp_charset":
        charset = upp_charset
    elif args.temp[0] == "num_charset":
        charset = num_charset
    elif args.temp[0] == "sym_charset":
        charset = sym_charset
    elif args.temp[0] == "*":
        charset = low_charset + upp_charset + num_charset + sym_charset
    else:
        print("Invalid charset")
        print("")
        parser.print_help()
        sys.exit()
elif args.opt:
    charset = args.opt[2]
else:
    print("Please provide at least one argument!")
    print("")
    parser.print_help()
    sys.exit()

def recurseCharList(charListX, nX, iX):
    for char in charListX:
        #loopList.append(charListX[nX])
        #print(loopList)
        print(nX, end=' ')
        print(charListX, charListX[nX])
        print(iX+1, charListX[nX] + char)

        #nX += 1
        iX += 1
        return iX
        

print(args.opt)
n=0
while True:
    charlist = list(charset)
    if len(charset) > 1:
        if loop:
            for char in list(charset):
                print(i+1, char)
                i += 1
            loop = False

        print("Stating function")
        i = recurseCharList(charlist, n, i)
        print(n)
        if n != len(charset) - 1:
            n += 1
        print("Function finished")
        if i == (len(charset)**2) + len(charset):
            print("Threshold reached, stopping")
            break

    else:
        for char in list(charset):
            print(i+1, char)
            i += 1 
        break

sys.exit()