#!/usr/bin/python
'''
Created on 26 sep. 2012

@author: Alex
'''
import time

if __name__ == '__main__':
    pass

def trim(file1):
    file3 = []
    readindex = 0
    with open('%s.txt' %file1, 'rU') as file2:
        for line in file2:
            line = line.strip('\n')
            readindex = readindex + 1
            file3.append(line)
            '''
            the script fills a list of 4 lines form the file
            this list contains a full fastq read which is used
            for the next part.
            '''
            if readindex == 4:
                readindex = 0
                seq = file3[1]
                '''
                some reads begin with a N at the start of the dna sequence
                this is removed
                '''
                if seq[0] == 'N':
                    file3[1] = file3[1].strip('N')
                    tempstring = file3[3]
                    file3[3] = tempstring[1:len(file3[3])]
                else:
                    pass
                length1 = len(file3[1])
                '''
                a quality score of 13 roughly equals a p-value of 0.05
                this means that a base with a score 13 or N has a 5% chance of being incorrect
                any score higher than 13 has less than 5% chance of being incorrect
                I believe this to be a good cutoff point for quality
                
                I have set the trim length to 5 basepares. this means that at least 5 basepares 
                in a row need to have a score of lower than 13 before I trim that from the read
                '''
                file6 = open('scoretable Illumina 1.5.txt','rU')# this loads a scoretable for the specific machine used to make the fastq file
                file7 = file6.readline()
                file6.close
                scoretable = file7.split(' ')
                badscoreseq = 0
                positionindex = 0
                for position in file3[3]:
                    score = (scoretable.index(position)) + 1
                    if badscoreseq < 5:
                        if score < 13:
                            badscoreseq = badscoreseq + 1
                        else:
                            badscoreseq = 0
                    else:
                        if score < 13:
                            badscoreseq = badscoreseq + 1
                            if positionindex == (length1-1):
                                seq = file3[3]
                                seq2 = file3[1]
                                seq = seq[:(positionindex - badscoreseq + 1)]
                                seq2 = seq2[:(positionindex - badscoreseq + 1)]
                                file3[1] = seq2
                                file3[3] = seq
                        else:
                            seq = file3[3]
                            seq2 = file3[1]
                            seq = seq[positionindex:]
                            seq2 = seq2[positionindex:]
                            file3[1] = seq2
                            file3[3] = seq
                            badscoreseq = 0
                            positionindex = 0
                    positionindex = positionindex + 1
                if file3[1] == '':
                    pass
                elif len(file3[1]) < (length1*0.25):
                    pass 
                else:
                    with open('%s-trimmed.txt' %file1, 'a') as file4:#open the file
                        for line in file3:
                            file4.write('%s\n' %line)
			file4.close      
                file3 = []
            else:
                pass
    file2.close

localtime1 = time.asctime(time.localtime(time.time()))
file1 = ('s_2_1_sequence')
file3 = open("%s-time" %file1,'a')
file3.write("script started at:")
file3.write("%s\n"% localtime1)
trim(file1)
file3 = open("%s-results" %file1,'a')
file3.write("this is the time of the trim script on %s.\n" %file1)
file3.write("script finished at:")
localtime2 = time.asctime(time.localtime(time.time()))
file3.write("%s\n" %localtime2)
file3.close
print('finished')
