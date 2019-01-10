#!/usr/bin/python
#coding=utf-8

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class loss:
    #根据自己的log_loss.txt中的行数修改lines, 修改训练时的迭代起始次数(start_ite)和结束次 end_ite)
    lines = 70000
    start_ite = 500  # log_loss.txt里面的最小迭代次
    end_ite = 26000  # log_loss.txt里面的最大迭代次
    step = 200  # 跳行数，决定画图的稠密程
    igore = 1000  # 当开始的loss较大时，你需要忽略前igore次迭代，注意这里是迭代次
    y_ticks = np.linspace(0.1, 5, 0.2)

    data_path =  'test.txt' #log_loss的路径 
    result_name = 'newLossName' #保存结果的路径 

    names = ['avg', 'rate', 'seconds', 'images']
    #names = ['loss', 'avg', 'rate', 'seconds', 'images']
    result = ''
    def __init__(self, lines, step, start, end, ignore, data_path, picName):
        self.lines = lines
        self.step = step
        self.start = start
        self.end = end
        self.igore = ignore
        self.data_path = data_path
        self.result_name = picName

    def process(self):
        self.result = pd.read_csv(self.data_path, skiprows=[x for x in range(self.lines) \
                if (x<self.lines*1.0/((self.end_ite - self.start_ite)*1.0)*self.igore or x%self.step!=9)], error_bad_lines=\
                False, names=self.names)
        self.result.head()

        for name in self.names:
            self.result[name] = self.result[name].str.split(' ').str.get(1)

        self.result.head()
        self.result.tail()

        for name in self.names:
            self.result[name] = pd.to_numeric(self.result[name])
        self.result.dtypes
        print(self.result['avg'].values)

        fig = plt.figure()
        ax = fig.add_subplot(1, 1, 1)

        x_num = len(self.result['avg'].values)
        tmp = (self.end_ite-self.start_ite - self.igore)/(x_num*1.0)
        x = []
        for i in range(x_num):
            x.append(i*tmp + self.start_ite + self.igore)
        #print(x)
        print('total = %d\n' %x_num)
        print('start = %d, end = %d\n' %(x[0], x[-1]))

        ax.plot(x, self.result['avg'].values, label='avg_loss')
        #ax.plot(result['loss'].values, label='loss')
        plt.yticks(self.y_ticks)#如果不想自己设置纵坐标，可以注释掉 
        plt.grid()
        ax.legend(loc = 'best')
        ax.set_title('The loss curves')
        ax.set_xlabel('batches')
        fig.savefig(self.result_name)

if __name__ == "__main__":
    #def __init__(self, lines, step, start, end, ignore, data_path):
    l = loss(10000, 20, 200, 10000, 20, './test.txt')
    l.process()
