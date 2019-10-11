# coding=utf8
#导入scrapy框架
import scrapy
# 导入实体类
from ysu.items import YsuItem
# 调用scrapy_splash获取动态生成的标签
from scrapy_splash import SplashRequest
# 正则表达式
import re
from aip import AipNlp


# 爬虫类
class YsuSpiderSpider(scrapy.Spider):
    # 爬虫的名字
    name = 'ysu_spider'
    # 允许的域名
    allowed_domains = ['ysu.edu.cn']
    # 数量
    num = 0
    # 参数
    param={}
    # 时间
    b2e = []
    # Appid ak sk
    """ 你的 APPID AK SK """
    APP_ID = '17071811'  # '你的 App ID'
    API_KEY = 'lH6SZclq3RKzariCpD8aF9HS'  # '你的 Api Key'
    SECRET_KEY = 'zEuGzZfVIZMiiywDtk0QfIo9gCv1dRCn'  # '你的 Secret Key'
    client=None

    # 初始化函数
    def __init__(self, param, **kwargs):
        # 调用父类的初始化函数
        super(YsuSpiderSpider, self).__init__(**kwargs)
        # 参数赋值
        self.param=eval(param)
        self.client = AipNlp(self.APP_ID, self.API_KEY, self.SECRET_KEY)

    # 爬虫启动入口
    def start_requests(self):
        num = self.param['args']['num']
        b2e = self.param['args']['b2e']
        urls = self.param['args']['urls']
        print(b2e)
        # 入口URL、rule
        for url, rule in self.param['start'].items():
            print("->:"+url)
            if url in urls:
                print("<-:"+url)
                # splash方法请求url
                yield SplashRequest(url=url, callback=self.parse,
                                    args={'wait': 1}, endpoint='render.html',meta={'item':url,'rule':rule,'num':num,'b2e':b2e}) #meta 携带的参数
            else:
                print("@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    def parse(self, response):
        # 当前网站的规则
        rule = response.meta['rule']
        b2e = response.meta['b2e']
        # 链接的前缀
        pro = response.url[0:response.url.rfind(rule['char'][0])+rule['num'][0]]
        prou = response.url[0:response.url.rfind(rule['char'][1])+rule['num'][1]]
        # 获取新闻列表
        news_list=None
        for list in rule['news_list']:
            if list != "#":
                temp = response.xpath(list).extract()
                if temp:
                    news_list = temp
                    break
        # 获取新闻时间
        news_date = None
        for date in rule['news_date']:
            if date != "#":
                temp = response.xpath(date).extract()
                if temp:
                    news_date = [t.replace('/','-') for t in temp]
                    break
        news = {i : j for i,j in zip(news_list,news_date)}
        for url,time in news.items():
            if time <= b2e[0] and time >= b2e[1]:
                # print(time)
                # 链接是否完整
                if url.find("http") == -1:
                    url=prou+url
                # 请求单个链接
                yield SplashRequest(url, callback=self.parseone,
                                    args={'wait': 1}, endpoint='render.html',meta={'item':response.meta['item'],'rule':response.meta['rule']})
        # 请求下一页
        next_link = None
        for list in rule['news_list']:
            if list != "#":
                temp = response.xpath(rule['next_link']).extract_first()
                if temp:
                    next_link = temp
                    break
        # 请求页数
        self.num = self.num + 1
        if next_link:
            if self.num < response.meta['num']: #500000000:
                if news_date[len(news_date)-1] > b2e[1]:
                    print("num----------------------->" + str(self.num))
                    yield SplashRequest(pro + next_link, callback=self.parse,
                                        args={'wait': 1}, endpoint='render.html',meta={'item':response.meta['item'],'rule':response.meta['rule'],'num':response.meta['num'],'b2e':response.meta['b2e']})

    def parseone(self, response):
        # 获取时间规则
        t_rule=["\d+年\d+月\d+日","\d+月\d+日","\d+-\d+-\d+"]
        # 当前网址的规则
        rule=response.meta['rule']
        # 创建实体
        ysuItem=YsuItem()
        ysuItem['url']=""
        ysuItem['title']=""
        ysuItem['time']="1900-01-01"
        ysuItem['author']=""
        ysuItem['content']={}
        ysuItem['abstract'] =""
        ysuItem['html']=""
        ysuItem['format'] =""
        ysuItem['image_urls']={}
        ysuItem['image_paths']={}
        ysuItem['url']=response.url
        # 为实体类赋值
        # 标题
        if rule['title'] != "#":
            ysuItem['title']=response.xpath(rule['title']).extract_first()
        # 发布时间
        if rule['time'] != "#":
            time = response.xpath(rule['time']).extract_first()
            for temptime in t_rule:
                if temptime != "#":
                    temT = re.findall(temptime, time)
                    if temT:
                        ysuItem['time'] = temT[0]
                        break
        print(ysuItem['time'])
        # 作者
        if rule['author'] != "#":
            ysuItem['author'] = response.xpath(rule['author']).extract_first()
        # 内容
        for content in rule['content']:
            if content != "#":
                tempC = response.xpath(content).extract()
                if tempC:
                    ysuItem['content'] = tempC
                    break
        # 事件发生时间
        ysuItem['event_time'] = ysuItem['time']
        year=ysuItem['time'][:ysuItem['time'].find('-')]
        strcon=''.join(ysuItem['content']).replace('?', '').replace(' ', '').replace('\u200d','').replace('\ufeff','').replace('\xa0','')
        maxSummaryLen = 300
        # """ 调用新闻摘要接口 """
        while True:
            abs = self.client.newsSummary(strcon, maxSummaryLen)
            if 'summary' in abs:
                ysuItem['abstract'] = abs['summary'];
                break
        print(abs)
        # print(ysuItem['abstract'])

        for ttime in t_rule:
            if ttime != "#":
                tempT = re.findall(ttime,strcon)
                if tempT:
                    num = re.findall(r"\d+", tempT[0])
                    if len(num) == 2:
                        tempT = year.zfill(4)+"-" + num[0].zfill(2) + "-" + num[1].zfill(2)
                    elif len(num) == 3:
                        tempT = num[0].zfill(4) + "-" + num[1].zfill(2) + "-" + num[2].zfill(2)
                    ysuItem['event_time'] = tempT
                    break

        # 内容html
        for html in rule['html']:
            if html != "#":
                tempH = response.xpath(html).extract()
                if tempH:
                    ysuItem['html'] = ''.join(tempH).replace("../../","http://39.106.1.127:8080/")
                    # print(ysuItem['html']+"\n\n\n")
                    break

        format = re.findall(">[^<>\n]+<|src=\".*g\"", ysuItem['html'].replace('?', '').replace(' ', '').replace('\u200d','').replace('\ufeff',''))
        for i in range(len(format)):
            if format[i].find('>') == -1:
                format[i] = "^split^" + format[i] + "^split^"
                format[i + 1] = ">>" + format[i + 1][1:-1] + "^split^<"
            else:
                format[i] = format[i][1:-1] #.replace('?', '').replace(' ', '').replace('\u200d','')
                if format[i][-1:] == '。' or format[i][-1:] == '！':
                    format[i] = format[i] + "^split^"
                if format[i][0] == '(' or format[i][0] == '（':
                    format[i] = ">" + format[i] + "^split^"

        strCon = ''.join(format)
        str = [s for s in strCon.split("^split^") if s != '']
        for i in range(len(str)):
            if str[i].find('src="') != -1:
                str[i] = "<p class=\"ql-align-center\"><img " + str[i] + "></p>"
            elif str[i].find('>') != -1:
                str[i] = "<p class=\"ql-align-center\">" + str[i][1:] + "</p>"
            else:
                str[i] = "<p style=\"text-indent: 2em\">" + str[i] + "</p>"

        ysuItem['format'] = '\n'.join(str)
        # print(ysuItem['format']+"\n\n\n\n\n")

        # 图片网址
        for list_imgs in rule['image_urls']:
            if list_imgs != "#":
                tempL = response.xpath(list_imgs).extract()
                if tempL:
                    for i in range(len(tempL)):
                        if tempL[i].rfind('?') > 0:
                            tempL[i] = tempL[i][0:tempL[i].rfind('?')]
                    ysuItem['image_urls'] = tempL
                    break
        # 储存实体类
        yield ysuItem

