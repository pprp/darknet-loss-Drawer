#coding=utf-8
#该文件用于提取训练log，去除不可解析的log后使log文件格式化，生成新的log文件供可视化工具绘图

def extract_log(log_file, new_log_file, key_word):
    with open(log_file, 'r') as f:
        with open(new_log_file, 'w') as train_log:
            for line in f:
                #去除多GPU的同步log；去除除零错误的log
                if ('Syncing' in line) or ('nan' in line) or ('Saving' in line):
                    continue
                if key_word in line:
                    train_log.write(line)
    f.close()
    train_log.close()

file = './v3tiny_dpj.log'

#extract_log(file, 'log_loss2.txt', 'images')
#extract_log(file, 'log_iou2.txt', 'IOU')
