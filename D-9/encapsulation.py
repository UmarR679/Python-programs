class bikes:
    def __init__(self,name,cc,m,cost):
        self.name = name
        self.cc = cc
        self.m = m
        self.cost = cost
    def performance(self):
        print("abt bikes:",self.name,self.cc,self.m,self.cost)
gt = bikes("GT",650,12,4)
duke=bikes("duke",390,30,2)
gt.performance()
duke.performance()