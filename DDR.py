#get_Height is a method of Neo-python library.
#get_price is a method in metaequity oracle.
import numpy as np

class dynamic_distributer:
    def __init__(self,token_id,initOwnerShare,blocktime,ROCinetrvaldays):
        #this must be limited to Master-admin privilages
        self.token_id=token_id
        self.price= get_price(token_id)
        self.owner=initOwnerShare
        self.public=100-self.owner
        self.rapid=1
        self.slow=1
        self.blocktime=blocktime
        self.ROCinetrval=ROCinetrvaldays
        
    def get_pricefactor(self):
         self.ROC=self.get_change()
         y=self.ROC
         k=self.rapid
         s=self.slow
         self.pricefactor= ((-4)/(1+np.exp(((y^2)/(-4*s))))+(1/(0.5+(k*(y^2))))-2)
         return self.pricefactor # only an output, not used for calculations

    def get_change(self):
         cur_block=Get_Height(self.token_id)
         #blocktime should be replaced by the average
         n=(self.ROCinterval*24*60*60)/self.blocktime
         #number of blocks to go back
         self.ROC=(get_price(self.token_id,cur_block)- get_price(self.token_id,cur_block-n))
         return self.ROC
#             
    def set_coef(self,rapid,slow):
         
        if rapid> 0.5:
             self.rapid=rapid
        if  0.5 < slow < 8:
            self.slow=slow
    
    def set_decay(self,halfduration,maxSupply,slowcoef,rapidcoef):
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
    
    def get_reward(self,Height):
        x=Height
        y=self.ROC
        a=self.max
        c=self.duration*2
        s=self.slow
        k=self.rapid
        self.blockreward=-((np.ln(2)*a*(( -1*(4/(np.exp(((y^2)/(4*s)))+1)))+(1/((k*(y^2))+0.5))-2)*2^(x*(( -1*(4/(np.exp(((y^2)/(4*s)))+1))+(1/((k*(y^2))+0.5))-2))))/c)
        return self.blockreward
    
    def get_DDR(self):
        #Only calculates current ratio
        self.ROC=self.get_change()
        b=self.DDRmin
        c=self.DDRrange
        k=self.DDRslope
        self.owner=b+(c/(1+np.exp(-k*self.ROC)))
        self.public=100-self.owner
        
    def set_DDR(self, minimum,rang,slope):
        if 20 <= minimum <=80:
            self.DDRmin=minimum
        if 20 <= rang <=80:
            self.DDRrange=rang
        if 0.05 <= slope <= 10:
            self.DDRslope=slope
            
    def get_DDR_reward(self,ownerFlag):
        H=get_Height(self.token_id)
        ddr=self.get_DDR()
        if ownerFlag==1:
           return self.get_reward(H)*(ddr/100)
        if not ownerFlag==1:
            return self.get_reward(H)*(1-(ddr/100))
            
