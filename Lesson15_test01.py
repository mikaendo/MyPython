class Student:

    def __init__(self,name):
        self.name = name

    def calculate_avg(self,data):
        sum = 0

        for num in data:
            num += sum

        avg = num/len(data)
        return avg

    def judge(self,avg):

        if(65 <= avg):
            result = "passed"
        else:
            result = "failured"
        return result
    
a001 = Student("mika")
data = [10,10,10,20,20,20]
avg = a001.calculate_avg(data)
result = a001.judge(avg)

print(a001.name)
print(avg)
print(result)
