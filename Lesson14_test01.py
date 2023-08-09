class Student:

    #初期化メソッド
    def __init__(self,name):
        self.name = name
    
    #5教科の平均を出す計算
    def calculate_avg(self,data):
        sum = 0
        
        #要素数を足し上げてゆく
        for num in data:
            sum += num

        #リストの要素数を求める    
        avg =sum/len(data)
        return avg
    
    #合格か不合格かを判定
    def jedge(self,avg):

        #60以上は合格それ以下は不合格
        if(avg >= 60):
            result = "passed"
        else:
            result = "failed"
        return result

#インスタンス化（初期化メソッド）
a001 = Student("sato") 
#リストを代入
data = [70,30,50,90,30]
#5教科の平均を代入
avg = a001.calculate_avg(data)
#判定を代入
result = a001.jedge(avg)

#5教科平均を表示
print(avg)
#name 判定を表示
print(a001.name + " " + result)