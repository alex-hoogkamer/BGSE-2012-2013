#!/usr/bin/python
import time
import os
'''
Created on 20 Sep. 2012

@author: Alex
'''

if __name__ == '__main__':
    pass

def QCscript():
    reads = 0
    index = 0
    lengthlist = []
    GCcontent = []
    GClist = []
    listreadcount = [] # a list for counting the number of reads. this is for calculating the GC content per position
    totalGCcontent = 0
    totallength = 0
    maxlength = 0
    minlength = 0
    with open("{filename}.txt".format(filename = filename), 'rU') as file1:# open the file
        for line in file1:
            '''
            this counts the number of reads
            if it encounters an @ it adds 1
            to reads.
            '''
            if line[0] == '@':
                reads = reads + 1 # this counts the number of reads
            else:
                index = index + 1 # this counter is used to identify the contents of the line
                    
            '''
            this if statement checks if the current line contains a sequence
            '''
            if (index % 3) == 1: # if index divided by 3 leaves 1 than the current line is a line with a DNA sequence
                '''
                this block calculates the GC contents per read and entire dataset.
                it counts the number of G and C per read, adds it together and 
                devides it by 1% of the read length.
                the GC content of the read is added to the GC content list.
                for the global GC content only the total length of the read
                is added to the totallength variable for later use. 
                ''' 
                line = line.strip("\n")
                line = line.strip("N")# if the sequence starts with an N it needs to be removed
                lenread = len(line)
                lengthlist.append(lenread)# make a list with length of all reads
                Gcontent = line.count('C')# count the number of C
                Ccontent = line.count('G')# count the number of G
                GCcontentread = Gcontent + Ccontent# calculate the GC content of the read
                totalGCcontent = totalGCcontent + GCcontentread # this is used to store the total GC content of all reads
                totallength = totallength + lenread # this is used to store the total length of all reads
                GCcontentread = GCcontentread/(lenread*0.01) # GC content of read
                GCcontent.append(GCcontentread) # add GC percentage to the list
                
                '''
                if and elif statements for finding the minimum and miximum read length
                '''             
                if lenread > maxlength: # if the read length is larger than maxlength it is the largest read
                    maxlength = lenread
                elif minlength == 0:# if the minlength = 0 the current read length will be assigned as the smallest read
                    minlength = lenread
                elif lenread < minlength: # if the read length is smaller than minlength it is the smallest read
                    minlength = lenread # if the minlength = 0 than all raeds are of the same length
                                
                '''
                the next block calulates the GC content per position.
                the code check per position in a read if a G or C is present
                if they are present it adds a 1 to GClist and continues to 
                the next position in the same read. it also adds a 1 to listreadcount
                in order to calculate the number of reads for each position.
                this is neccesary to calculate the correct %GC.
                '''
                positionindex = 0
                for position in line:
                    Ccount = position.count("C") # count the G content of the position
                    Gcount = position.count("G") # count the G content of the position
                    GCcount = Gcount + Ccount
                    if index == 1: # if it is the first sequence the values need to be appended to the list
                        GClist.append(GCcount)
                        listreadcount.append(1)# when calculating the percentage of G and C the number of reads is neccecary
                    else: # if it is not the first sequence the values need to be added to the existing values or append to the end of the list
                        try:
                            GClist[positionindex] = GClist[positionindex] + GCcount
                            listreadcount[positionindex] = listreadcount[positionindex] +1
                        except: # when a read is longer than the list the values will be appended to the list
                            GClist.append(GCcount)
                            listreadcount.append(1)
                    positionindex = positionindex +1
                    #print(GClist)
            else:
                pass        
                                
        '''
        this calulates the global reads by dividing the totalGCcontent with 1% of the totallength
        '''
        mean = totallength / reads # the total length is divided by the total number of reads to calculade the mean length        
        globalGC = totalGCcontent/(totallength*0.01) # calculate global GC content
        for position in range(len(GClist)): # add GC content per position to list
            GClist[position] = GClist[position]/(listreadcount[position]*0.01) # calculate percentage GC per position and add it to list
        
    '''
    these values are returned to be written to file
    '''
    return(reads, mean, minlength, maxlength, GCcontent, globalGC, GClist)
    file1.close

filename = 's_2_1_sequence-trimmed'
localtime = time.asctime(time.localtime(time.time()))
#print("Local current time :", localtime)
file2 = open("%s results" %filename,'a')
file2.write("script started at:")
file2.write("%s\n" % localtime)
file2.write("this is the results file of %s" %filename)
results = QCscript()
file2.write("these are the results of the QC script.\n")
file2.write("the number of reads is: %s.\n" %results[0])
file2.write("the longest read is: %s.\n" %results[3])
file2.write("the shortest read is: %s.\n" %results[2])
file2.write("the mean of reads is: %s.\n" %results[1])
file2.write("the GC content of all reads is: %s.\n" %results[5])
file2.write("the GC content per read is: %s.\n" %results[4])
file2.write("the GC content per position is: %s.\n" %results[6])
localtime = time.asctime( time.localtime(time.time()) )
#print("Local current time :", localtime)
file2.write("script Finished at:")
file2.write("%s\n\n" % localtime)
file2.close
print('finished')