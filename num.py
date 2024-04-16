import numpy as np
import matplotlib.pyplot as plt

score = []
name = []


with open("class_score.csv","r")as f:
    rows = 1
    for line in f:
        if rows > 1:
            temp = line.strip().split(',')
            score.append([int(i) for i in temp[1:]])
            name.append(temp[0])
        rows += 1


#A,Bの点数をnumpy型の配列に変換
a = np.array(score[0])
b = np.array(score[1])
#numpy配列は足し算できる
total = a + b
print(total)
#numpy配列は引き算もできる
inter = a - b
print(inter)

#行列の入れ替え
np_score = np.array(score)#生徒ごと
np_score2 = np_score.transpose()#教科ごと
print(np_score2)

#救済70点未満の人に２点追加
def add_score(num):
    if num < 70:
        num += 2
    return num
#関数をmap化する
pyfunc = np.vectorize(add_score)
#mapした関数を使って新しい配列の作成
new_score = pyfunc(np_score)

print(new_score)

x1= name
y1 = np_score2[0] #国語
y2 = np_score2[1] #算数
y3 = np_score2[2] #英語
plt.bar(x1, y1, color="green")
plt.bar(x1, y2, bottom=y1, color="orange")
plt.bar(x1, y3, bottom=y1+y2, color="pink")
plt.show()
