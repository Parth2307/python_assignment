

class sposts:
    def __init__(self,football,hockey,*kabaddi,**cricket):
        
        self.cricket1=cricket
        self.hockey=hockey
        self.football=football
        self.kabaddi=kabaddi



champion=sposts(1950,1975,2016,2007,2004,odi=2011,t20=2007)

print("India Win World cup in cricket ",champion.cricket1)
print("India In Football qulifia world cup in ",champion.football)
print("India Win world cup in Hockey ",champion.hockey)
print("India Win World cup in Kabaddi ",champion.kabaddi)