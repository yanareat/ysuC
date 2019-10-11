# 导入cmdline
from scrapy import cmdline
# os
import os
# json
import json
# sys
import sys

print(sys.argv[1])

# 读取规则文件
def readFile():
    f = open('../res/rule1.txt', 'r', encoding='utf-8')
    return json.loads(f.read()) # 将规则文件转换成json

# 程序入口
if __name__ == '__main__':
    param = {}
    # 定位python工作目录到A:/0_document/pythonWorkSpace/ysu/ysu
    # os.chdir("A:/0_document/pythonWorkSpace/ysu/ysu");
    # 初始化param
    param['start'] = readFile()
    param['args'] = eval(sys.argv[1])
    # param['args'] = {'num': 5, 'b2e': ['2019-09-22', '2019-01-01'], 'urls': ['http://ysu.edu.cn/index/xwtx.htm']}

    print(param)
    # 执行爬虫
    cmdline.execute(['scrapy', 'crawl', 'ysu_spider','-a','param= %r' % param,'-s','LOG_FILE=wiki.log'])
    # cmdline.execute(['scrapy', 'crawl', 'ysu_spider', '-a', 'param= %s' % param])