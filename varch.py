# imports

import sys

# varibles

extension = ".txt"
arch = "<" + extension + ">"
starter = "["
ender = "]"

# functions


def load(name):
    f = open(name, "r")
    read = ""

    while read != ";":
        read = f.readLine()
        print read


def create():
    f = open(raw_input("archive file name = ") + ".varch", "w")
    inf = input("How many files do you want to commpress")
    f.write("// \n")
    i = 1
    while i <= inf:
        name = raw_input("file n." + str(i) + "=")
        f.write(name + "[ \n")
        f.write(open(raw_input("file n."), "r").read())
        f.write("] \n")
        i += 1
    f.write("//")
    f.close()


def afc():
    print "For unload a varch type -load"
    print "For create a varch type -create"

    command = raw_input("-->")

    if command == "load":
        load(raw_input("Filename = "))
    elif command == "create":
        create()


def run():
    afc()

# run

run()