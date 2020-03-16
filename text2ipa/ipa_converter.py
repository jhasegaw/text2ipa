import os,math,os.path
import numpy as np

class Converter:
    '''A converter to convert from text to ipa.  Usage: 
    converter = text2ipa.converter(English)
    outputtext = converter.convert(inputtext)
    '''
    def __init__(self, langname):
        '''Reads in data/langname/letters.txt as an FST'''
        self.fst = { 0:{} }   # self.fst[q][i] = edge leaving state q with input string i
        self.maxlen = 0   # self.maxlen = maximum length of inputstrings 
        with open('text2ipa/data/%s/letters.txt'%(langname)) as f:
            for line in f:
                a = line.rstrip().split()  # a[0] is the inputstring, a[1] is the outputstring
                if len(a)>0:
                    self.fst[0][a[0]] = (0,a[1])  # edge = endstate, outputstring
                    if len(a[0]) > self.maxlen:
                        self.maxlen = len(a[0])
        self.langname = langname
        
    def convert(self, inputtext):
        '''Convert inputtext to outputtext using shortest-path conversion'''
        costs = [ [ math.inf for e in range(len(self.fst)) ] for tau in range(len(inputtext)+1) ]
        paths = [ [ '' for e in range(len(self.fst)) ] for tau in range(len(inputtext)+1) ]
        for tau in range(1,len(inputtext)+1):  # end time
            costs[tau][0] = costs[tau-1][0]+1.5  # initialize with the null edge,
            paths[tau][0] = paths[tau-1][0]+inputtext[tau-1]
            for t in range(tau-1,max(-1,tau-self.maxlen-1),-1):  # start time from tau-1 to tau-maxlen
                for b in range(len(self.fst)):  # starting state
                    if inputtext[t:tau] in self.fst[b]: # if the inputstr is an edge
                        e = self.fst[b][inputtext[t:tau]][0]  # ending state
                        o = self.fst[b][inputtext[t:tau]][1]  # outputstring
                        costs[tau][e] = costs[t][b]+1
                        paths[tau][e] = paths[t][b]+o
        # Backtrace
        e = np.argmin(costs[len(inputtext)])
        outputtext = paths[len(inputtext)][e]
        return(outputtext)
    
