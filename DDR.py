# -*- coding: utf-8 -*-
"""
Created on Sun Oct 14 22:08:45 2018

@author: Omar Salah
"""
import numpy as np

class dynamic_distributer:
    def __init__(self,token_id,initOwnerShare,blocktime):
        #this must be limited to Master-admin privilages
        self.token_id=token_id
        self.price= get_price(token_id)
        self.owner=initOwnerShare
        self.public=100-self.owner
        self.rapid=1
        self.slow=1
        self.blocktime=blocktime
        
    def get_pricefactor(self,timedays):
         self.ROC=get_change(self.token_id,timedays)
         y=self.ROC
         k=self.rapid
         s=self.slow
         self.pricefactor= ((-4)/(1+np.exp(((y^2)/(-4*s))))+(1/(0.5+(k*(y^2))))-2)
         return self.pricefactor # only an output, not used for calculations

    def get_change(self,timedays):
         cur_block=Get_Height(self.token_id)
         #blocktime should be replaced by the average
         n=(timedays*24*60*60)/self.blocktime
         #number of blocks to go back
         self.ROC=(get_price(self.token_id,cur_block)- get_price(self.token_id,cur_block-n))
         return self.ROC
#             
    def set_coef(self,rapid,slow):
         
        if rapid> 0.5:
             self.rapid=rapid
        if  0.5 < slow < 8:
            self.slow=slow
    
    def time_decay(self,halfduration,maxSupply,slowcoef,rapidcoef):
        #a defining function for a static decay.
        #for the first time definition of the decay.
        # needs adaptation for realtime dynamic changes
        self.halfduration=(halfduration*365*24*60*60)/self.blocktime
        c=self.duration*2
        self.max=maxSupply
        a=maxSupply;
        y=self.ROC
        k=rapidcoef
        s=slowcoef
        x=GetHeight(self.token_id)
        self.blockreward=-((np.ln(2)*a*(( -1*(4/(np.exp(((y^2)/(4*s)))+1)))+(1/((k*(y^2))+0.5))-2)*2^(x*(( -1*(4/(np.exp(((y^2)/(4*s)))+1))+(1/((k*(y^2))+0.5))-2))))/c)
        return self.blockreward
