#!/usr/bin/python
#coding=utf-8

import pandas as pd
import matplotlib.pyplot as plt


class visual:
    #根据log_iou修改行数
    lines = 124275
    step = 5000
    start_ite = 0
    end_ite = 50020
    igore = 1000
    data_path =  'test.txt' #log_loss的路径。
    result_path = './res' #保存结果的路径。
    
    def __init__(self, lines, step, start, end, ignore, data_path):
        self.lines = lines
        self.step = step
        self.start = start
        self.end = end
        self.igore = ignore
        self.data_path = data_path

    names = ['Region Avg IOU', 'Class', 'Obj', 'No Obj', '.5_Recall', '.7_Recall', 'count']
    
    #result = pd.read_csv('log_iou.txt', skiprows=[x for x in range(lines) if (x%10==0 or x%10==9)]\
    result = ''

    def setFile(self,File):
        self.data_path = File
    
    def process(self):
        self.result = pd.read_csv(self.data_path, skiprows=[x for x in range(self.lines) \
        if (x<self.lines*1.0/((self.send_ite - self.start_ite)*1.0)*self.igore or x%self.step!=0)]\
    , error_bad_lines=False, names=self.names)
        self.result.head()
        for name in self.names:
            self.result[name] = self.result[name].str.split(': ').str.get(1)
        self.result.head()
        self.result.tail()
        for name in self.names:
            self.result[name] = pd.to_numeric(self.result[name])
        self.result.dtypes
        ####--------------
        x_num = len(self.result['Region Avg IOU'].values)
        tmp = (self.end_ite-self.start_ite - self.igore)/(x_num*1.0)
        x = []
        for i in range(x_num):
            x.append(i*tmp + self.start_ite + self.igore)

        print('total = %d\n' %x_num)
        print('start = %d, end = %d\n' %(x[0], x[-1]))
        ####-------------
        fig = plt.figure()
        ax = fig.add_subplot(1,1,1)
        ax.plot(x, self.result['Region Avg IOU'].values, label='Region Avg IOU')
        #ax.plot(result['Avg Recall'].values, label='Avg Recall')
        plt.grid()
        ax.legend(loc='best')
        ax.set_title('The Region Avg IOU curves')
        ax.set_xlabel('batches')
        fig.savefig(self.result_path)
