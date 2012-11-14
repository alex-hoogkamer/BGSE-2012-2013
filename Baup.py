#! \user\bin\python3
'''
Created on 4 okt. 2012

@author: Alex

this is a program for the main asaignment for Baup. 
'''
import os

if __name__ == '__main__':
    pass

def listinput():
    a = False
    b = [1,2,3,4]
    c = ['fungi','protists','plants','animals']
    d = 1
    print("welcome to this program.\nif u type '0' the program will exit")
    print("u can chose between:\n")
    for i in c:
        print(d,"=",i)
        d = d + 1
    while a == False:
        var = input("Enter a number between 1 and 4: ")
        var = int(var)
        if var in b:
            a = True
            return(c[var-1])
        elif var == 0:
            print("u typed '0' the program will now exit.")
            break
        else:
            os.system("clear")
            print("what u typed is incorrect.\nonly  the numbers 1 through 4 are allowed.\ntype '0' to exit the program.")

def listdo(a):
    spelist = []
    if a != None:
        print("u chose %s" %a)
        if a == "animals":
            a = "metazoa"
        os.system("wget 'ftp://ftp.ensemblgenomes.org/pub/%s/current/fasta/'" %a)
        os.system("cat index.html | awk '{print $7}' > spe")
        with open("spe","r") as file1:
            c = file1.readlines()
        file1.close
        for line in c:
            line = line.strip("\n")
            line = line.strip("</a>")
            if line != "":
                line = line[(line.index(">")):]
                line = line.strip(">")
                line = line.replace("_", " ")
                spelist.append(line)
        return(spelist)
        os.system("echo 'Done!'")
    else:
        pass
        
def listinput2(spelist):
    a = False
    b = len(spelist)
    c = 1
    print("this is the species chooser.\nif u type '0' the program will exit")
    print("u can chose between:\n")
    for i in spelist:
        print(c,"=",i)
        c = c + 1
    while a == False:
        var = input("Enter a number between 1 and %s: " %b)
        var = int(var)
        if var in range(1,b):
            a = True
            return(spelist[var-1])
        elif var == 0:
            print("u typed '0' the program will now exit.")
            break
        else:
            os.system("clear")
            print("what u typed is incorrect.\nonly  the numbers 1 through %s are allowed.\ntype '0' to exit the program." %b)

def listdo2(a,c):
    if a != None:
        if a == "animals":
            a = "metazoa"
        print("u chose %s" %c)
        c = c.replace(" ","_")
        file1 = open("species","w")
        file1.write(c)
        file1.close
        os.system("wget 'ftp://ftp.ensemblgenomes.org/pub/{classa}/current/fasta/{species}/dna/'".format(classa = a,species = c))
        os.system("cat index.html | awk '{print $7}' | egrep 'toplevel' > dna")
        with open("dna","r") as file1:
            line = file1.readline()
        file1.close
        line = line.strip("\n")
        line = line.strip('href=')
        line = line[1:line.index('">')]
        print(line)
        os.system("wget '{adress}'".format(adress = line))
        os.system("echo 'Done!'")
    else:
        pass
    

a = listinput()
spelist = listdo(a)
c = listinput2(spelist)
os.system("rm index.html*;rm spe")
listdo2(a,c)
os.system("rm index.html*;rm dna")