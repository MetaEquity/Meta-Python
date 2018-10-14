# -*- coding: utf-8 -*-
"""
Created on Sat Oct 13 20:25:13 2018

@author: Omar
"""
from boa.interop.Neo.Blockchain import GetHeight
class candidate(object):
    def __init__(self,amount,end ): 
        self.VOTING_ID= amount
        self.VOTING_END= end
        self.valid=0

    def add_vote(self,vote):
        current_height=GetHeight()
        if self.VOTING_END < current_height:
            if vote.ID ==self.VOTING_ID:
                if not vote.ctx in self.voters:
                    self.count+=1
                    self.voters+= vote.ctx 
                    vote.valid=1
                elif vote.ctx in self.voters:
                     vote.valid=0
                     
    def __str__(self):
        return '{} - {}'.format(self.VOTING_ID, self.VOTING_END)
    
    
class vote:
    def __init__(self, ID, ctx):
       name= "C" + str(ID)
       self.ID=ID
       self.ctx=ctx
       if name in candidates:
           candidates[name].add_vote(self)
           self.valid=1
       elif self.ID not in candidates: 
            self.valid=0
       #do_refund      
#    def check(self):
#        #check if the voter didn't vote before
#        #check if the ID matches a candidate
#        if  self.ID in candidates:
#            candidates[self.ID].add_vote(self)
#        self.valid=0
#        #do_refund       
    def __str__(self):
        return '{} - {}'.format(self.ID, self.valid)

def add_candidate(ID,end):   
    name= "C" + str(ID)
    if not name in candidates:
        candidates[name]=candidate(ID,end)
        
def see_candidate(ID):
    name= "C" + str(ID)
    if name in candidates:
        return candidates[name].__str__()
    elif not name in candidates:
        return "there's no Candidate with ID " + str(ID)

one=add_candidate(80, 7000)
one=vote(60, 7654876)