import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
# import matplotlib.pyplot as plt

class Visual:
    def __init__(self, data):
        self.data = data
    def graph(self):
        print("enter -1 to go back..")
        while 1:
            tasks=['1.Bar plot','2.Area plot','3.Scatter','4.Boxplot','5.Pie chart']
            print(self.data)
            for task in tasks:
                print(task)
            choice=int(input('Select one ploting method : '))
            if choice==-1:
                break
            if choice==1:
                print('selected Barplot')
                a=input('select X asix column: ')
                b=input('select y axis column: ')
                # plt.plot(a, b)
                plt.bar(self.data[a],self.data[b])

                plt.show()
                # res=sns.barplot(x =a, y =b, data = self.data)
                # print(res)
            # if choice==2:
            #     a=input('select X asix column: ')
            #     b=input('select y axis column: ')
            #     sns.relplot(data=self.data, x=self.data[a], y=self.data[b], sizes=(15, 200),hue=self.data['year'],style=self.data['year'], kind="line")
            if choice==3:
                a=input('select X asix column: ')
                b=input('select y axis column: ')
                plt.scatter(self.data[a],self.data[b])
                plt.show()
            if choice==4:
                plt.boxplot(self.data)
                plt.show()
            if choice==2:
                a=input('select X asix column: ')
                b=input('select y1 axis column: ')
                c=input('select y2 axis column: ')
                # b=b.to_numpy()
                plt.plot(self.data[a],self.data[b], label='Line 1', marker='o')
                plt.plot(self.data[a],self.data[b], label='Line 2', marker='o')
                plt.show()
            if choice==5:
                li=[]
                for column in self.data.columns.values:
                    # if self.data[column]=='population':
                    #     continue
                    li.append(self.data[column].mean())
                sizes=[]
                for m in li:
                    sizes.append((m/sum(li))*100)
                print(sizes)
                print(sum(sizes))
                degrees = [percent * 3.6 for percent in sizes]
                print(degrees)

                plt.pie(degrees,labels=self.data.columns.values, autopct='%1.1f%%', startangle=90)
                plt.show()
            else:
                continue