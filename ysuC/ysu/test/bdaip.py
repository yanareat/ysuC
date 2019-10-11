# coding=gbk

from aip import AipNlp
import re
""" 你的 APPID AK SK """
APP_ID = '17071811' #'你的 App ID'
API_KEY = 'lH6SZclq3RKzariCpD8aF9HS' #'你的 Api Key'
SECRET_KEY = 'zEuGzZfVIZMiiywDtk0QfIo9gCv1dRCn' #'你的 Secret Key'

client = AipNlp(APP_ID, API_KEY, SECRET_KEY)

# text = "【新闻中心讯】8月18日下午，校党委书记赵险峰、校长赵丁选一行拜访了我校杰出校友、全国人大常委会原副委员长、民革中央原主席周铁农。"
text = '''
    <p><img src="http://localhost:8080/__local/F/09/D8/667BD7A18E408ABC5196998589D_B07EDD91_11E17.jpg"></p>
    <p>全体学员和培训导师合影</p>
    <p>7月15日-19日，我院在行政楼413成功举办2019年秦皇岛市红十字会应急救护师资培训活动。此次培训由中国红十字会总会训练中心讲师孙素萍担任理论老师。我院学生工作部组织部分辅导员、学生工作人员和学生退伍士兵共25人参加培训。</p>
    <p><img src="http://localhost:8080/__local/9/CF/00/CD5980FC85A74D1381EA0C25AE5_B8E13AFD_1D92B.jpg"></p>
    <p>2019年应急救护师资培训开班仪式</p>
    <p>7月15日上午，培训班在里仁学院行政楼举行开班典礼。</p>
    <p>秦皇岛市红十字会专职副会长刘冬青、秦皇岛市红十字会秘书长王玉梅、里仁学院党委书记张向前出席开班典礼。副院长常鑫主持开班仪式。</p>
    <p>张向前在开班仪式上致辞，他希望参训学员认真学习救护技能，并将这种技能传授给更多的老师，学生，乃至全社会，同时将人道主义精神传递开来，让更多的人携起手共同提高自我保护和应急救护的能力。</p>
    <p>刘冬青在开班仪式上讲话，随着社会发展，应急救护培训被更多人了解认可，珍惜学习机会，真正提高救护能力，为以后的培训打好基础。最后他对学院给予红十字会工作的支持和帮助表示衷心的感谢。</p>
    <p>开班仪式结束后，紧接着就开始理论教学。</p>
    <p><img src="http://localhost:8080/__local/6/62/B4/8F71614CB40425307309D5CC305_4ED1810C_1236C.jpg"></p>
    <p>孙素萍老师在为学员讲解理论知识</p>
    <p><img src="http://localhost:8080/__local/3/1F/43/C9F8B4B8266919428414634C47F_5F6D45D1_2039F.jpg"></p>
    <p>孙素萍老师在为学员讲解理论知识</p>
    <p><img src="http://localhost:8080/__local/1/B9/1C/C31E3B9EB6D377DF28DAEF79627_B8569A47_1D9E1.jpg"></p>
    <p>实操老师带领学员做实操练习</p>
    <p><img src="http://localhost:8080/__local/5/DF/ED/B96F3355112B7ACC4AE825CBB39_CDE4B4D3_1D28A.jpg"></p>
    <p>实操老师带领学员做实操练习</p>
    <p>本次培训在课程设置、师资选聘、办班形式等方面重点体现高校校园的特点和师生的需求，实效性和针对性强。学员们先后学习了《救护概论与教学法》、《心肺复苏与创伤救护》、《常见急症与避险逃生》，他们在培训中积极向各位老师学习，通过人体模型亲身体验学习了心肺复苏、人工呼吸、现场包扎、骨折固定等救护技能。</p>
    <p><img src="http://localhost:8080/__local/0/12/EF/49EAAEC68DD85BC2DB661B055AF_97059866_14A2E.jpg"></p>
    <p>学员通过人体模型学习徒手心肺复苏</p>
    <p>结合校园环境和学生工作特点，参训辅导员以“如何避险逃生”作为授课考核内容。通过讲授“着火了怎么办”、“地震时刻”“有人晕倒了”等和学生密切相关的内容，为开学后安全教育做了初步准备。</p>
    <p>图六</p>
    <p><img src="http://localhost:8080/__local/6/B0/46/5FD459ABFD8B5C2291EE8D07C0A_EF811A70_1BDDA.jpg"></p>
    <p>参训学员现场考核</p>
    <p><img src="http://localhost:8080/__local/D/6F/0C/10D18E8D664F9A4D734E6F48AB0_DD92DEA3_1B48F.jpg"></p>
    <p>参训学员现场考核</p>
    <p>经过五天紧张的理论学习和实操练习，通过严格的闭卷理论考试，实操考试，试讲考试，此次培训班圆满结束，参训学员纷纷表示这次应急救护培训给他们带来了很大的帮助，让他们今后在遇到类似突发情况时不再手足无措，在今后给学生讲授安全防范知识时多了一项专业规范的内容，并将在以后的工作和生活中弘扬红十字人道主义精神，帮助更多的学生老师规范救护技能，提高救护水平。</p>
    <p><img src="http://localhost:8080/__local/A/33/53/790995BE2131C09A01CAB7FD762_C654313A_18E42.jpg"></p>
    <p>全省第五届红十字应急救护大赛颁奖现场</p>
    <p>今年3月，燕山大学里仁学院向秦皇岛市红十字会郑重提出申请并成立了里仁学院红十字会。</p>
    <p>7月11日，由河北省红十字会主办的全省第五届红十字应急救护大赛在省会石家庄举行。里仁学院党委高度重视，学生工作部积极组织配合，选派学院优秀退伍大学生士兵组队代表秦皇岛市参赛，在前后近3个月的准备时间里，市红会的工作人员和培训教师辛苦指导，里仁学子不负众望，获得总成绩第四名和1个单项二等奖，2个单项三等奖的历史最好成绩。</p>
'''

# """ 调用词法分析（定制版） """
# ysu_result = client.lexerCustom(text);
# print(ysu_result)
#
# time={}
#
# items = ysu_result['items']
# for item in items:
#     print(item)
#     if item['ne'] == "TIME":
#         if item['item'] in time:
#             time[item['item']] = time[item['item']] + 1
#         else:
#             time[item['item']] = 1

maxSummaryLen = 300

""" 调用新闻摘要接口 """
ysu_result = client.newsSummary(text, maxSummaryLen);
print(ysu_result)

text2="<p>7月15日-19日，我院在行政楼413成功举办2019年秦皇岛市红十字会应急救护师资培训活动。此次培训由中国红十字会总会训练中心讲师孙素萍担任理论老师。我院学生工作部组织部分辅导员、学生工作人员和学生退伍士兵共25人参加培训。<p>7月15日上午，培训班在里仁学院行政楼举行开班典礼。<p>秦皇岛市红十字会专职副会长刘冬青、秦皇岛市红十字会秘书长王玉梅、里仁学院党委书记张向前出席开班典礼。最后他对学院给予红十字会工作的支持和帮助表示衷心的感谢。<p>7月11日，由河北省红十字会主办的全省第五届红十字应急救护大赛在省会石家庄举行。"
content=re.findall(">[^<>\n]+<|src=\".*g\"",text2)
for i in range(len(content)):
    if content[i].find('>')==-1:
        content[i]="^split^"+content[i]+"^split^"
        content[i+1]=">"+content[i+1][1:-1]+"^split^<"
    else:
        content[i] = content[i][1:-1].replace('?','').replace(' ','')
        if content[i][-1:]=='。':
            content[i]=content[i]+"^split^"
    print(content[i])
strc=''.join(content)
str=[s for s in strc.split("^split^") if s!='']
print('\n'.join(str))

# """ 如果有可选参数 """
# options = {}
# options["title"] = "标题"
#
# """ 带参数调用新闻摘要接口 """
# client.newsSummary(text, maxSummaryLen, options)

# rule=["\d+年\d+月\d+日","\d+月\d+日"]

# print(time)
# sort_time=sorted(time,key=time.__getitem__,reverse=True)
# print(sort_time)
# if re.findall(r"\d+年\d+",sort_time[0]):
#     print(re.findall(r"\d+年\d+",sort_time[0]))
# print("text:"+re.findall(r"\d+月\d+日",text)[0])

# text1 = """
# <div id="vsb_content"><p style="margin: 0px;line-height: 2em;text-indent: 28px;mso-char-indent-count: 2.0000"><span style="font-family: 宋体;font-size: 14px;mso-spacerun: 'yes';mso-ascii-font-family: calibri;mso-hansi-font-family: calibri;mso-bidi-font-family: 'times new roman';mso-font-kerning: 1px"><span style="font-family: 黑体, simhei;font-size: 16px"></span></span></p>
# <table align="center" class="imgtable" uetable="null" ue_class="imgtable" ue_style="border-width:0px;float:none;" style="border-width: 0px;margin: 0px auto">
#  <tbody>
#   <tr>
#    <td align="middle" valign="center" ue_style="border-width:0px;text-align:center;" style="border-width: 0px;text-align: center"><img width="600" title="全体学员和培训导师合影" id="11E17" src="http://localhost:8080/__local/F/09/D8/667BD7A18E408ABC5196998589D_B07EDD91_11E17.jpg" border="0" hspace="0"></td>
#   </tr>
#   <tr>
#    <td ue_style="text-align:center;border-width:0px" style="border-width: 0px;text-align: center"><span style="font-family: 微软雅黑, microsoft yahei">全体学员和培训导师合影</span></td>
#   </tr>
#  </tbody>
# </table>
# <p style="margin: 0px;line-height: 2em;text-indent: 28px;mso-char-indent-count: 2.0000"><span style="font-family: 宋体;font-size: 14px;mso-spacerun: 'yes';mso-ascii-font-family: calibri;mso-hansi-font-family: calibri;mso-bidi-font-family: 'times new roman';mso-font-kerning: 1px"><span style="font-family: 黑体, simhei;font-size: 16px"></span></span><span style="font-family: calibri;font-size: 14px;mso-spacerun: 'yes';mso-bidi-font-family: 'times new roman';mso-font-kerning: 1px;mso-fareast-font-family: 宋体">
#   <!--?xml:namespace prefix="o" /-->
#   <p></p></span></p>
# <p style="margin: 0px;line-height: 2em;text-indent: 28px;mso-char-indent-count: 2.0000"><span style="font-family: 宋体;font-size: 14px;mso-spacerun: 'yes';mso-ascii-font-family: calibri;mso-hansi-font-family: calibri;mso-bidi-font-family: 'times new roman';mso-font-kerning: 1px"><span style="font-family: 黑体, simhei;font-size: 16px;mso-spacerun: 'yes';mso-ascii-font-family: calibri;mso-hansi-font-family: calibri;mso-bidi-font-family: 'times new roman';mso-font-kerning: 1px"></span></span></p>
# <p style="margin: 0px;line-height: 2em;text-indent: 28px;mso-char-indent-count: 2.0000"><span style="font-family: 宋体;font-size: 14px;mso-spacerun: 'yes';mso-ascii-font-family: calibri;mso-hansi-font-family: calibri;mso-bidi-font-family: 'times new roman';mso-font-kerning: 1px"><span style="font-family: 微软雅黑, microsoft yahei;font-size: 16px;mso-spacerun: 'yes';mso-ascii-font-family: calibri;mso-hansi-font-family: calibri;mso-bidi-font-family: 'times new roman';mso-font-kerning: 1px">7</span><span style="font-family: 微软雅黑, microsoft yahei;font-size: 16px">月</span><span style="font-family: 微软雅黑, microsoft yahei;font-size: 16px">15</span><span style="font-family: 微软雅黑, microsoft yahei;font-size: 16px">日</span><span style="font-family: 微软雅黑, microsoft yahei;font-size: 16px">-19</span><span style="font-family: 微软雅黑, microsoft yahei;font-size: 16px">日，我院在行政楼</span><span style="font-family: 微软雅黑, microsoft yahei;font-size: 16px">413</span><span style="font-family: 微软雅黑, microsoft yahei;font-size: 16px">成功举办</span><span style="font-family: 微软雅黑, microsoft yahei;font-size: 16px">2019</span><span style="font-family: 微软雅黑, microsoft yahei;font-size: 16px">年秦皇岛市红十字会</span></span><span style="font-family: 微软雅黑, microsoft yahei;font-size: 16px;mso-spacerun: 'yes';mso-ascii-font-family: calibri;mso-hansi-font-family: calibri;mso-bidi-font-family: 'times new roman';mso-font-kerning: 1px">应急救护师资培训活动。此次培训由中国红十字会总会训练中心讲师孙素萍担任理论老师。我院学生工作部</span><span style="font-family: 微软雅黑, microsoft yahei;font-size: 16px;mso-spacerun: 'yes';mso-ascii-font-family: calibri;mso-hansi-font-family: calibri;mso-bidi-font-family: 'times new roman';mso-font-kerning: 1px">组织部分辅导员、学生工作人员和学生退伍士兵</span><span style="font-family: 微软雅黑, microsoft yahei;font-size: 16px;mso-spacerun: 'yes';mso-ascii-font-family: calibri;mso-hansi-font-family: calibri;mso-bidi-font-family: 'times new roman';mso-font-kerning: 1px">共</span><span style="font-family: 宋体;font-size: 14px;mso-spacerun: 'yes';mso-ascii-font-family: calibri;mso-hansi-font-family: calibri;mso-bidi-font-family: 'times new roman';mso-font-kerning: 1px"><span style="font-family: 微软雅黑, microsoft yahei;font-size: 16px;mso-spacerun: 'yes';mso-ascii-font-family: calibri;mso-hansi-font-family: calibri;mso-bidi-font-family: 'times new roman';mso-font-kerning: 1px">25</span><span style="font-family: 微软雅黑, microsoft yahei;font-size: 16px">人参加培训。</span></span><span style="font-family: 宋体;font-size: 14px;mso-spacerun: 'yes';mso-ascii-font-family: calibri;mso-hansi-font-family: calibri;mso-bidi-font-family: 'times new roman';mso-font-kerning: 1px">
#   <p></p></span></p>
# <p style="margin: 0px;line-height: 2em;text-indent: 28px;mso-char-indent-count: 2.0000"><span style="font-family: 宋体;font-size: 14px;mso-spacerun: 'yes';mso-ascii-font-family: calibri;mso-hansi-font-family: calibri;mso-bidi-font-family: 'times new roman';mso-font-kerning: 1px"><span style="font-family: 黑体, simhei;font-size: 16px"></span></span></p>
# <table align="center" class="imgtable" uetable="null" ue_class="imgtable" ue_style="border-width:0px;float:none;" style="border-width: 0px;margin: 0px auto">
#  <tbody>
#   <tr>
#    <td ue_style="border-width:0px;text-align:center;" style="border-width: 0px;text-align: center"><img width="600" title="2019年应急救护师资培训开班仪式" id="1D92B" src="http://localhost:8080/__local/9/CF/00/CD5980FC85A74D1381EA0C25AE5_B8E13AFD_1D92B.jpg" border="0" hspace="0"></td>
#   </tr>
#   <tr>
#    <td ue_style="text-align:center;border-width:0px" style="border-width: 0px;text-align: center"><span style="font-family: 微软雅黑, microsoft yahei">2019年应急救护师资培训开班仪式</span></td>
#   </tr>
#  </tbody>
# </table>
# <p style="margin: 0px;line-height: 2em;text-indent: 28px;mso-char-indent-count: 2.0000"><span style="font-family: 宋体;font-size: 14px;mso-spacerun: 'yes';mso-ascii-font-family: calibri;mso-hansi-font-family: calibri;mso-bidi-font-family: 'times new roman';mso-font-kerning: 1px"><span style="font-family: 黑体, simhei;font-size: 16px"></span></span><span style="font-family: calibri;font-size: 14px;mso-spacerun: 'yes';mso-bidi-font-family: 'times new roman';mso-font-kerning: 1px;mso-fareast-font-family: 宋体">
#   <p></p></span></p>
# <p style="margin: 0px;line-height: 2em;text-indent: 28px;mso-char-indent-count: 2.0000"><span style="font-family: 宋体;font-size: 14px;mso-spacerun: 'yes';mso-ascii-font-family: calibri;mso-hansi-font-family: calibri;mso-bidi-font-family: 'times new roman';mso-font-kerning: 1px"><span style="font-family: 黑体, simhei;font-size: 16px;mso-spacerun: 'yes';mso-ascii-font-family: calibri;mso-hansi-font-family: calibri;mso-bidi-font-family: 'times new roman';mso-font-kerning: 1px"></span></span></p>
# <p style="margin: 0px;line-height: 2em;text-indent: 28px;mso-char-indent-count: 2.0000"><span style="font-family: 宋体;font-size: 14px;mso-spacerun: 'yes';mso-ascii-font-family: calibri;mso-hansi-font-family: calibri;mso-bidi-font-family: 'times new roman';mso-font-kerning: 1px"><span style="font-family: 微软雅黑, microsoft yahei;font-size: 16px;mso-spacerun: 'yes';mso-ascii-font-family: calibri;mso-hansi-font-family: calibri;mso-bidi-font-family: 'times new roman';mso-font-kerning: 1px">7</span><span style="font-family: 微软雅黑, microsoft yahei;font-size: 16px">月</span><span style="font-family: 微软雅黑, microsoft yahei;font-size: 16px">15</span><span style="font-family: 微软雅黑, microsoft yahei;font-size: 16px">日上午，培训班在里仁学院行政楼举行开班典礼。</span></span><span style="font-family: 微软雅黑, microsoft yahei;font-size: 16px;mso-spacerun: 'yes';mso-ascii-font-family: calibri;mso-hansi-font-family: calibri;mso-bidi-font-family: 'times new roman';mso-font-kerning: 1px">秦皇岛市红十字会专职副会长刘冬青、秦皇岛市红十字会秘书长王玉梅、里仁学院党委书记张向前出席开班典礼。副院长常鑫主持开班仪式。</span><span style="font-family: 宋体;font-size: 14px;mso-spacerun: 'yes';mso-ascii-font-family: calibri;mso-hansi-font-family: calibri;mso-bidi-font-family: 'times new roman';mso-font-kerning: 1px">
#   <p></p></span></p>
# <p style="margin: 0px;line-height: 2em;text-indent: 28px;mso-char-indent-count: 2.0000"><span style="font-family: 微软雅黑, microsoft yahei;font-size: 16px;mso-spacerun: 'yes';mso-ascii-font-family: calibri;mso-hansi-font-family: calibri;mso-bidi-font-family: 'times new roman';mso-font-kerning: 1px">张向前在开班仪式上致辞，他希望参训学员认真学习救护技能，并将这种技能传授给更多的老师，学生，乃至全社会，同时将人道主义精神传递开来，让更多的人携起手共同提高自我保护和应急救护的能力。</span><span style="font-family: 宋体;font-size: 14px;mso-spacerun: 'yes';mso-ascii-font-family: calibri;mso-hansi-font-family: calibri;mso-bidi-font-family: 'times new roman';mso-font-kerning: 1px">
#   <p></p></span></p>
# <p style="margin: 0px;line-height: 2em;text-indent: 28px;mso-char-indent-count: 2.0000"><span style="font-family: 微软雅黑, microsoft yahei;font-size: 16px;mso-spacerun: 'yes';mso-ascii-font-family: calibri;mso-hansi-font-family: calibri;mso-bidi-font-family: 'times new roman';mso-font-kerning: 1px">刘冬青在开班仪式上讲话，随着社会发展，应急救护培训被更多人了解认可，珍惜学习机会，真正提高救护能力，为以后的培训打好基础。最后他对学院给予红十字会工作的支持和帮助表示衷心的感谢。</span><span style="font-family: calibri;font-size: 14px;mso-spacerun: 'yes';mso-bidi-font-family: 'times new roman';mso-font-kerning: 1px;mso-fareast-font-family: 宋体">
#   <p></p></span></p>
# <p style="margin: 0px;line-height: 2em;text-indent: 28px;mso-char-indent-count: 2.0000"><span style="font-family: 微软雅黑, microsoft yahei;font-size: 16px;mso-spacerun: 'yes';mso-ascii-font-family: calibri;mso-hansi-font-family: calibri;mso-bidi-font-family: 'times new roman';mso-font-kerning: 1px">开班仪式结束后，紧接着就开始理论教学。</span></p>
# <p style="margin: 0px;line-height: 2em;text-indent: 28px;mso-char-indent-count: 2.0000"><span style="font-family: 黑体, simhei;font-size: 16px;mso-spacerun: 'yes';mso-ascii-font-family: calibri;mso-hansi-font-family: calibri;mso-bidi-font-family: 'times new roman';mso-font-kerning: 1px"></span><span style="font-family: 宋体;font-size: 14px;mso-spacerun: 'yes';mso-ascii-font-family: calibri;mso-hansi-font-family: calibri;mso-bidi-font-family: 'times new roman';mso-font-kerning: 1px">
#   <p></p></span> ?</p>
# <p style="margin: 0px;line-height: 2em;text-indent: 28px;mso-char-indent-count: 2.0000"><span style="font-family: 黑体, simhei;font-size: 16px;mso-spacerun: 'yes';mso-ascii-font-family: calibri;mso-hansi-font-family: calibri;mso-bidi-font-family: 'times new roman';mso-font-kerning: 1px"></span> ?</p>
# <table align="center" class="imgtable" uetable="null" ue_class="imgtable" ue_style="border-width:0px;float:none;" style="border-width: 0px;margin: 0px auto">
#  <tbody>
#   <tr>
#    <td ue_style="border-width:0px;text-align:center;" style="border-width: 0px;text-align: center"><img width="600" title="孙素萍老师在为学员讲解理论知识" id="1236C" src="http://localhost:8080/__local/6/62/B4/8F71614CB40425307309D5CC305_4ED1810C_1236C.jpg" border="0" hspace="0"></td>
#   </tr>
#   <tr>
#    <td ue_style="text-align:center;border-width:0px" style="border-width: 0px;text-align: center"><span style="font-family: 微软雅黑, microsoft yahei">孙素萍老师在为学员讲解理论知识</span>
#     <table class="imgtable" uetable="null" ue_class="imgtable" ue_style="border-width:0px;float:none;" style="border-width: 0px;float: none">
#      <tbody>
#       <tr>
#        <td ue_style="border-width:0px;text-align:center;" style="border-width: 0px;text-align: center"><img width="600" title="孙素萍老师在为学员讲解理论知识" id="2039F" src="http://localhost:8080/__local/3/1F/43/C9F8B4B8266919428414634C47F_5F6D45D1_2039F.jpg" border="0" hspace="0"></td>
#       </tr>
#       <tr>
#        <td ue_style="text-align:center;border-width:0px" style="border-width: 0px;text-align: center"><span style="font-family: 微软雅黑, microsoft yahei">孙素萍老师在为学员讲解理论知识</span></td>
#       </tr>
#      </tbody>
#     </table></td>
#   </tr>
#  </tbody>
# </table>
# <p style="margin: 0px;line-height: 2em;text-indent: 28px;mso-char-indent-count: 2.0000"><span style="font-family: 宋体;font-size: 14px;mso-spacerun: 'yes';mso-ascii-font-family: calibri;mso-hansi-font-family: calibri;mso-bidi-font-family: 'times new roman';mso-font-kerning: 1px"><span style="font-family: 黑体, simhei;font-size: 16px"></span></span></p>
# <table align="center" class="imgtable" uetable="null" ue_class="imgtable" ue_style="border-width:0px;float:none;" style="border-width: 0px;margin: 0px auto">
#  <tbody>
#   <tr>
#    <td ue_style="border-width:0px;text-align:center;" style="border-width: 0px;text-align: center"><img width="600" title="实操老师带领学员做实操练习" id="1D9E1" src="http://localhost:8080/__local/1/B9/1C/C31E3B9EB6D377DF28DAEF79627_B8569A47_1D9E1.jpg" hspace="0"></td>
#   </tr>
#   <tr>
#    <td ue_style="text-align:center;border-width:0px" style="border-width: 0px;text-align: center"><span style="font-family: 微软雅黑, microsoft yahei">实操老师带领学员做实操练习</span></td>
#   </tr>
#  </tbody>
# </table>
# <p><br> ?</p>
# <table align="center" class="imgtable" uetable="null" ue_class="imgtable" ue_style="border-width:0px;float:none;" style="border-width: 0px;margin: 0px auto">
#  <tbody>
#   <tr>
#    <td ue_style="border-width:0px;text-align:center;" style="border-width: 0px;text-align: center"><img width="600" title="实操老师带领学员做实操练习" id="1D28A" src="http://localhost:8080/__local/5/DF/ED/B96F3355112B7ACC4AE825CBB39_CDE4B4D3_1D28A.jpg" hspace="0"></td>
#   </tr>
#   <tr>
#    <td ue_style="text-align:center;border-width:0px" style="border-width: 0px;text-align: center"><span style="font-family: 微软雅黑, microsoft yahei">实操老师带领学员做实操练习</span></td>
#   </tr>
#  </tbody>
# </table>
# <p><span style="font-family: 宋体;font-size: 14px;mso-spacerun: 'yes';mso-ascii-font-family: calibri;mso-hansi-font-family: calibri;mso-bidi-font-family: 'times new roman';mso-font-kerning: 1px"><span style="font-family: 黑体, simhei;font-size: 16px"></span></span> ?</p>
# <p style="margin: 0px;line-height: 2em;text-indent: 28px;mso-char-indent-count: 2.0000"><span style="font-family: 微软雅黑, microsoft yahei;font-size: 16px;mso-spacerun: 'yes';mso-ascii-font-family: calibri;mso-hansi-font-family: calibri;mso-bidi-font-family: 'times new roman';mso-font-kerning: 1px">本次培训在课程设置、师资选聘、办班形式等方面重点体现高校校园的特点和师生的需求，实效性和针对性强。学员们先后学习了《救护概论与教学法》、《心肺复苏与创伤救护》、《常见急症与避险逃生》，</span><span style="font-family: 微软雅黑, microsoft yahei;font-size: 16px;mso-spacerun: 'yes';mso-ascii-font-family: calibri;mso-hansi-font-family: calibri;mso-bidi-font-family: 'times new roman';mso-font-kerning: 1px">他们在培训中积极向各位老师学习，通过人体模型亲身体验学习了心肺复苏、人工呼吸、现场包扎、骨折固定等救护技能。</span></p>
# <p style="margin: 0px;line-height: 2em;text-indent: 28px;mso-char-indent-count: 2.0000"><span style="font-family: 黑体, simhei;font-size: 16px;mso-spacerun: 'yes';mso-ascii-font-family: calibri;mso-hansi-font-family: calibri;mso-bidi-font-family: 'times new roman';mso-font-kerning: 1px"></span> ?</p>
# <p style="margin: 0px;line-height: 2em;text-indent: 28px;mso-char-indent-count: 2.0000"><span style="font-family: 黑体, simhei;font-size: 16px;mso-spacerun: 'yes';mso-ascii-font-family: calibri;mso-hansi-font-family: calibri;mso-bidi-font-family: 'times new roman';mso-font-kerning: 1px"></span><span style="font-family: 宋体;font-size: 14px;mso-spacerun: 'yes';mso-ascii-font-family: calibri;mso-hansi-font-family: calibri;mso-bidi-font-family: 'times new roman';mso-font-kerning: 1px"> </span>?</p>
# <p><span style="font-family: 宋体;font-size: 14px;mso-spacerun: 'yes';mso-ascii-font-family: calibri;mso-hansi-font-family: calibri;mso-bidi-font-family: 'times new roman';mso-font-kerning: 1px"></span>?</p>
# <table align="center" class="imgtable" uetable="null" ue_class="imgtable" ue_style="border-width:0px;float:none;" style="border-width: 0px;margin: 0px auto">
#  <tbody>
#   <tr>
#    <td ue_style="border-width:0px;text-align:center;" style="border-width: 0px;text-align: center"><img width="600" title="学员通过人体模型学习徒手心肺复苏" id="14A2E" src="http://localhost:8080/__local/0/12/EF/49EAAEC68DD85BC2DB661B055AF_97059866_14A2E.jpg" border="0" hspace="0"></td>
#   </tr>
#   <tr>
#    <td ue_style="text-align:center;border-width:0px" style="border-width: 0px;text-align: center"><span style="font-family: 微软雅黑, microsoft yahei">学员通过人体模型学习徒手心肺复苏</span></td>
#   </tr>
#  </tbody>
# </table>
# <p></p>
# <p></p>
# <p> ?</p>
# <p style="margin: 0px;line-height: 2em;text-indent: 28px;mso-char-indent-count: 2.0000"><span style="font-family: 微软雅黑, microsoft yahei;font-size: 16px;mso-spacerun: 'yes';mso-ascii-font-family: calibri;mso-hansi-font-family: calibri;mso-bidi-font-family: 'times new roman';mso-font-kerning: 1px">结合校园环境和学生工作特点，参训辅导员以“如何避险逃生”作为授课考核内容。通过讲授“着火了怎么办”、“地震时刻”“有人晕倒了”等和学生密切相关的内容，为开学后安全教育做了初步准备。</span><span style="font-family: 宋体;font-size: 14px;mso-spacerun: 'yes';mso-ascii-font-family: calibri;mso-hansi-font-family: calibri;mso-bidi-font-family: 'times new roman';mso-font-kerning: 1px">
#   <p></p></span></p>
# <p style="margin: 0px;line-height: 2em;text-indent: 28px;mso-char-indent-count: 2.0000"><span style="font-family: 宋体;font-size: 14px;mso-spacerun: 'yes';mso-ascii-font-family: calibri;mso-hansi-font-family: calibri;mso-bidi-font-family: 'times new roman';mso-font-kerning: 1px"><span style="font-family: 微软雅黑, microsoft yahei;font-size: 16px">图六</span></span></p>
# <table align="center" class="imgtable" uetable="null" ue_class="imgtable" ue_style="border-width:0px;float:none;" style="border-width: 0px;margin: 0px auto">
#  <tbody>
#   <tr>
#    <td ue_style="border-width:0px;text-align:center;" style="border-width: 0px;text-align: center"><img width="600" title="参训学员现场考核" id="1BDDA" src="http://localhost:8080/__local/6/B0/46/5FD459ABFD8B5C2291EE8D07C0A_EF811A70_1BDDA.jpg" hspace="0"></td>
#   </tr>
#   <tr>
#    <td ue_style="text-align:center;border-width:0px" style="border-width: 0px;text-align: center"><span style="font-family: 微软雅黑, microsoft yahei">参训学员现场考核</span></td>
#   </tr>
#  </tbody>
# </table>
# <p><br> ?</p>
# <table align="center" class="imgtable" uetable="null" ue_class="imgtable" ue_style="border-width:0px;float:none;" style="border-width: 0px;margin: 0px auto">
#  <tbody>
#   <tr>
#    <td ue_style="border-width:0px;text-align:center;" style="border-width: 0px;text-align: center"><img width="600" title="参训学员现场考核" id="1B48F" src="http://localhost:8080/__local/D/6F/0C/10D18E8D664F9A4D734E6F48AB0_DD92DEA3_1B48F.jpg" hspace="0"></td>
#   </tr>
#   <tr>
#    <td ue_style="text-align:center;border-width:0px" style="border-width: 0px;text-align: center"><span style="font-family: 微软雅黑, microsoft yahei">参训学员现场考核</span></td>
#   </tr>
#  </tbody>
# </table>
# <p> ?</p>
# <p style="margin: 0px;line-height: 2em;text-indent: 28px;mso-char-indent-count: 2.0000"><span style="font-family: 微软雅黑, microsoft yahei;font-size: 16px;mso-spacerun: 'yes';mso-ascii-font-family: calibri;mso-hansi-font-family: calibri;mso-bidi-font-family: 'times new roman';mso-font-kerning: 1px">经过五天紧张的理论学习和实操练习，通过严格的闭卷理论考试，实操考试，试讲考试，此次培训班圆满结束，参训学员纷纷表示这次应急救护培训给他们带来了很大的帮助，让他们今后在遇到类似突发情况时不再手足无措，在今后给学生讲授安全防范知识时多了一项专业规范的内容，并将在以后的工作和生活中弘扬红十字人道主义精神，帮助更多的学生老师</span><span style="font-family: 微软雅黑, microsoft yahei;font-size: 16px;mso-spacerun: 'yes';mso-ascii-font-family: calibri;mso-hansi-font-family: calibri;mso-bidi-font-family: 'times new roman';mso-font-kerning: 1px">规范救护技能，提高救护水平。</span><span style="font-family: 宋体;font-size: 14px;mso-spacerun: 'yes';mso-ascii-font-family: calibri;mso-hansi-font-family: calibri;mso-bidi-font-family: 'times new roman';mso-font-kerning: 1px">
#   <p></p></span></p>
# <p style="margin: 0px;line-height: 2em;text-indent: 28px;mso-char-indent-count: 2.0000"><span style="font-family: 黑体, simhei;font-size: 16px;mso-spacerun: 'yes';mso-ascii-font-family: calibri;mso-hansi-font-family: calibri;mso-bidi-font-family: 'times new roman';mso-font-kerning: 1px"></span> ?</p>
# <table align="center" class="imgtable" uetable="null" ue_class="imgtable" ue_style="border-width:0px;float:none;" style="border-width: 0px;margin: 0px auto">
#  <tbody>
#   <tr>
#    <td ue_style="border-width:0px;text-align:center;" style="border-width: 0px;text-align: center"><img width="600" title="全省第五届红十字应急救护大赛颁奖现场" id="18E42" src="http://localhost:8080/__local/A/33/53/790995BE2131C09A01CAB7FD762_C654313A_18E42.jpg" border="0" hspace="0"></td>
#   </tr>
#   <tr>
#    <td ue_style="text-align:center;border-width:0px" style="border-width: 0px;text-align: center"><span style="font-family: 微软雅黑, microsoft yahei">全省第五届红十字应急救护大赛颁奖现场</span></td>
#   </tr>
#  </tbody>
# </table>
# <p style="margin: 0px;line-height: 2em;text-indent: 28px;mso-char-indent-count: 2.0000"><span style="font-family: 黑体, simhei;font-size: 16px;mso-spacerun: 'yes';mso-ascii-font-family: calibri;mso-hansi-font-family: calibri;mso-bidi-font-family: 'times new roman';mso-font-kerning: 1px"></span> ?</p>
# <p style="margin: 0px;line-height: 2em;text-indent: 28px;mso-char-indent-count: 2.0000"><span style="font-family: 微软雅黑, microsoft yahei;font-size: 16px;mso-spacerun: 'yes';mso-bidi-font-family: 'times new roman';mso-font-kerning: 1px;mso-fareast-font-family: 宋体">今年</span><span style="font-family: 微软雅黑, microsoft yahei;font-size: 16px;mso-spacerun: 'yes';mso-ascii-font-family: calibri;mso-hansi-font-family: calibri;mso-bidi-font-family: 'times new roman';mso-font-kerning: 1px">3</span><span style="font-family: 微软雅黑, microsoft yahei;font-size: 16px;mso-spacerun: 'yes';mso-bidi-font-family: 'times new roman';mso-font-kerning: 1px;mso-fareast-font-family: 宋体">月，燕山大学里仁学院向秦皇岛市红十字会郑重提出申请</span><span style="font-family: 微软雅黑, microsoft yahei;font-size: 16px;mso-spacerun: 'yes';mso-ascii-font-family: calibri;mso-hansi-font-family: calibri;mso-bidi-font-family: 'times new roman';mso-font-kerning: 1px">并</span><span style="font-family: 微软雅黑, microsoft yahei;font-size: 16px;mso-spacerun: 'yes';mso-bidi-font-family: 'times new roman';mso-font-kerning: 1px;mso-fareast-font-family: 宋体">成立</span><span style="font-family: 微软雅黑, microsoft yahei;font-size: 16px;mso-spacerun: 'yes';mso-ascii-font-family: calibri;mso-hansi-font-family: calibri;mso-bidi-font-family: 'times new roman';mso-font-kerning: 1px">了</span><span style="font-family: 微软雅黑, microsoft yahei;font-size: 16px;mso-spacerun: 'yes';mso-bidi-font-family: 'times new roman';mso-font-kerning: 1px;mso-fareast-font-family: 宋体">里仁学院红十字会。</span><span style="font-family: 宋体;font-size: 14px;mso-spacerun: 'yes';mso-ascii-font-family: calibri;mso-hansi-font-family: calibri;mso-bidi-font-family: 'times new roman';mso-font-kerning: 1px"><span style="font-family: 微软雅黑, microsoft yahei;font-size: 16px;mso-spacerun: 'yes';mso-ascii-font-family: calibri;mso-hansi-font-family: calibri;mso-bidi-font-family: 'times new roman';mso-font-kerning: 1px">7</span><span style="font-family: 微软雅黑, microsoft yahei;font-size: 16px">月</span><span style="font-family: 微软雅黑, microsoft yahei;font-size: 16px">11</span><span style="font-family: 微软雅黑, microsoft yahei;font-size: 16px">日，</span></span><span style="font-family: calibri;font-size: 14px;mso-spacerun: 'yes';mso-bidi-font-family: 'times new roman';mso-font-kerning: 1px;mso-fareast-font-family: 宋体"><span style="font-family: 微软雅黑, microsoft yahei;font-size: 16px;mso-spacerun: 'yes';mso-bidi-font-family: 'times new roman';mso-font-kerning: 1px;mso-fareast-font-family: 宋体">由河北省红十字会主办的全省第五届红十字应急救护大赛在省会石家庄举行。里仁学院党委高度重视，学生工作部积极组织配合，选派学院优秀退伍大学生士兵组队代表秦皇岛市参赛，在前后近3</span><span style="font-family: 微软雅黑, microsoft yahei;font-size: 16px">个月的准备时间里，市红会的工作人员和培训教师辛苦指导，里仁学子不负众望，获得总成绩第四名和</span><span style="font-family: 微软雅黑, microsoft yahei;font-size: 16px">1</span><span style="font-family: 微软雅黑, microsoft yahei;font-size: 16px">个单项二等奖，</span><span style="font-family: 微软雅黑, microsoft yahei;font-size: 16px">2</span><span style="font-family: 微软雅黑, microsoft yahei;font-size: 16px">个单项三等奖的历史最好成绩。</span></span><span style="font-family: calibri;font-size: 14px;mso-spacerun: 'yes';mso-bidi-font-family: 'times new roman';mso-font-kerning: 1px;mso-fareast-font-family: 宋体">
#   <p></p></span></p>
# <p style="line-height: 2em"><span style="font-family: 黑体, simhei;font-size: 16px"></span> ?</p></div>
# """
# # \p{Han}\p{P}A-Za-z0-9  \u4E00-\u9FA5
# content=re.findall(">[^<>\n]+<|src=\".*g\"",text1)
# for i in range(len(content)):
#     if content[i].find('>')==-1:
#         content[i]="^split^"+content[i]+"^split^"
#         content[i+1]=">"+content[i+1][1:-1]+"^split^<"
#     else:
#         content[i] = content[i][1:-1].replace('?','').replace(' ','')
#         if content[i][-1:]=='。':
#             content[i]=content[i]+"^split^"
#     print(content[i])
# strCon = ''.join(content)
# str=[s for s in strCon.split("^split^") if s!='']
# print(str)
#
# for i in range(len(str)):
#     if str[i].find('src="')==-1:
#         str[i]="<p>"+str[i]+"</p>"
#     else:
#         str[i]="<p><img "+str[i]+"></p>"
# for s in str:
#     print(s)
# for time in rule:
#     if time != "#":
#         tempH = re.findall(time,strCon)
#         if tempH:
#             print(tempH[0])
#             num = re.findall(r"\d+", tempH[0])
#             s = ""
#             if len(num) == 2:
#                 s = "2019-" + num[0].zfill(2) + "-" + num[1].zfill(2)
#             else:
#                 s = num[0].zfill(4) + "-" + num[1].zfill(2) + "-" + num[2].zfill(2)
#             print(s)
#             break