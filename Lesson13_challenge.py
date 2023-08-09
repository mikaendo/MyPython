class Studnet:

    def __init__(self,name):
        
        self.name = name
    
    def calculate_avg(self,data):
        sum = 0
        
        for num in data:
            num += sum
            
        #lenがオブジェクトの長さをだす
        avg = num/len(data)
        return avg

a001 = Studnet("poyo")
data = [50,60]
avg = a001.calculate_avg(data)
 
print(a001.name)
print(avg)
     


