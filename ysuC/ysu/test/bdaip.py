# coding=gbk

from aip import AipNlp
import re
""" ��� APPID AK SK """
APP_ID = '17071811' #'��� App ID'
API_KEY = 'lH6SZclq3RKzariCpD8aF9HS' #'��� Api Key'
SECRET_KEY = 'zEuGzZfVIZMiiywDtk0QfIo9gCv1dRCn' #'��� Secret Key'

client = AipNlp(APP_ID, API_KEY, SECRET_KEY)

# text = "����������Ѷ��8��18�����磬У��ί������շ塢У���Զ�ѡһ�аݷ�����У�ܳ�У�ѡ�ȫ���˴�ί��ԭ��ίԱ�����������ԭ��ϯ����ũ��"
text = '''
    <p><img src="http://localhost:8080/__local/F/09/D8/667BD7A18E408ABC5196998589D_B07EDD91_11E17.jpg"></p>
    <p>ȫ��ѧԱ����ѵ��ʦ��Ӱ</p>
    <p>7��15��-19�գ���Ժ������¥413�ɹ��ٰ�2019���ػʵ��к�ʮ�ֻ�Ӧ���Ȼ�ʦ����ѵ����˴���ѵ���й���ʮ�ֻ��ܻ�ѵ�����Ľ�ʦ����Ƽ����������ʦ����Ժѧ����������֯���ָ���Ա��ѧ��������Ա��ѧ������ʿ����25�˲μ���ѵ��</p>
    <p><img src="http://localhost:8080/__local/9/CF/00/CD5980FC85A74D1381EA0C25AE5_B8E13AFD_1D92B.jpg"></p>
    <p>2019��Ӧ���Ȼ�ʦ����ѵ������ʽ</p>
    <p>7��15�����磬��ѵ��������ѧԺ����¥���п������</p>
    <p>�ػʵ��к�ʮ�ֻ�רְ���᳤�����ࡢ�ػʵ��к�ʮ�ֻ����鳤����÷������ѧԺ��ί�������ǰ��ϯ������񡣸�Ժ���������ֿ�����ʽ��</p>
    <p>����ǰ�ڿ�����ʽ���´ǣ���ϣ����ѵѧԱ����ѧϰ�Ȼ����ܣ��������ּ��ܴ��ڸ��������ʦ��ѧ��������ȫ��ᣬͬʱ���˵����徫�񴫵ݿ������ø������Я���ֹ�ͬ������ұ�����Ӧ���Ȼ���������</p>
    <p>�������ڿ�����ʽ�Ͻ�����������ᷢչ��Ӧ���Ȼ���ѵ���������˽��Ͽɣ���ϧѧϰ���ᣬ������߾Ȼ�������Ϊ�Ժ����ѵ��û������������ѧԺ�����ʮ�ֻṤ����֧�ֺͰ�����ʾ���ĵĸ�л��</p>
    <p>������ʽ�����󣬽����žͿ�ʼ���۽�ѧ��</p>
    <p><img src="http://localhost:8080/__local/6/62/B4/8F71614CB40425307309D5CC305_4ED1810C_1236C.jpg"></p>
    <p>����Ƽ��ʦ��ΪѧԱ��������֪ʶ</p>
    <p><img src="http://localhost:8080/__local/3/1F/43/C9F8B4B8266919428414634C47F_5F6D45D1_2039F.jpg"></p>
    <p>����Ƽ��ʦ��ΪѧԱ��������֪ʶ</p>
    <p><img src="http://localhost:8080/__local/1/B9/1C/C31E3B9EB6D377DF28DAEF79627_B8569A47_1D9E1.jpg"></p>
    <p>ʵ����ʦ����ѧԱ��ʵ����ϰ</p>
    <p><img src="http://localhost:8080/__local/5/DF/ED/B96F3355112B7ACC4AE825CBB39_CDE4B4D3_1D28A.jpg"></p>
    <p>ʵ����ʦ����ѧԱ��ʵ����ϰ</p>
    <p>������ѵ�ڿγ����á�ʦ��ѡƸ�������ʽ�ȷ����ص����ָ�УУ԰���ص��ʦ��������ʵЧ�Ժ������ǿ��ѧԱ���Ⱥ�ѧϰ�ˡ��Ȼ��������ѧ���������ķθ����봴�˾Ȼ�������������֢���������������������ѵ�л������λ��ʦѧϰ��ͨ������ģ����������ѧϰ���ķθ��ա��˹��������ֳ����������۹̶��ȾȻ����ܡ�</p>
    <p><img src="http://localhost:8080/__local/0/12/EF/49EAAEC68DD85BC2DB661B055AF_97059866_14A2E.jpg"></p>
    <p>ѧԱͨ������ģ��ѧϰͽ���ķθ���</p>
    <p>���У԰������ѧ�������ص㣬��ѵ����Ա�ԡ���α�����������Ϊ�ڿο������ݡ�ͨ�����ڡ��Ż�����ô�족��������ʱ�̡��������ε��ˡ��Ⱥ�ѧ��������ص����ݣ�Ϊ��ѧ��ȫ�������˳���׼����</p>
    <p>ͼ��</p>
    <p><img src="http://localhost:8080/__local/6/B0/46/5FD459ABFD8B5C2291EE8D07C0A_EF811A70_1BDDA.jpg"></p>
    <p>��ѵѧԱ�ֳ�����</p>
    <p><img src="http://localhost:8080/__local/D/6F/0C/10D18E8D664F9A4D734E6F48AB0_DD92DEA3_1B48F.jpg"></p>
    <p>��ѵѧԱ�ֳ�����</p>
    <p>����������ŵ�����ѧϰ��ʵ����ϰ��ͨ���ϸ�ıվ����ۿ��ԣ�ʵ�ٿ��ԣ��Խ����ԣ��˴���ѵ��Բ����������ѵѧԱ�׷ױ�ʾ���Ӧ���Ȼ���ѵ�����Ǵ����˺ܴ�İ����������ǽ������������ͻ�����ʱ���������޴룬�ڽ���ѧ�����ڰ�ȫ����֪ʶʱ����һ��רҵ�淶�����ݣ��������Ժ�Ĺ����������к����ʮ���˵����徫�񣬰��������ѧ����ʦ�淶�Ȼ����ܣ���߾Ȼ�ˮƽ��</p>
    <p><img src="http://localhost:8080/__local/A/33/53/790995BE2131C09A01CAB7FD762_C654313A_18E42.jpg"></p>
    <p>ȫʡ������ʮ��Ӧ���Ȼ������佱�ֳ�</p>
    <p>����3�£���ɽ��ѧ����ѧԺ���ػʵ��к�ʮ�ֻ�֣��������벢����������ѧԺ��ʮ�ֻᡣ</p>
    <p>7��11�գ��ɺӱ�ʡ��ʮ�ֻ������ȫʡ������ʮ��Ӧ���Ȼ�������ʡ��ʯ��ׯ���С�����ѧԺ��ί�߶����ӣ�ѧ��������������֯��ϣ�ѡ��ѧԺ���������ѧ��ʿ����Ӵ����ػʵ��в�������ǰ���3���µ�׼��ʱ����к��Ĺ�����Ա����ѵ��ʦ����ָ��������ѧ�Ӳ�������������ܳɼ���������1��������Ƚ���2���������Ƚ�����ʷ��óɼ���</p>
'''

# """ ���ôʷ����������ư棩 """
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

""" ��������ժҪ�ӿ� """
ysu_result = client.newsSummary(text, maxSummaryLen);
print(ysu_result)

text2="<p>7��15��-19�գ���Ժ������¥413�ɹ��ٰ�2019���ػʵ��к�ʮ�ֻ�Ӧ���Ȼ�ʦ����ѵ����˴���ѵ���й���ʮ�ֻ��ܻ�ѵ�����Ľ�ʦ����Ƽ����������ʦ����Ժѧ����������֯���ָ���Ա��ѧ��������Ա��ѧ������ʿ����25�˲μ���ѵ��<p>7��15�����磬��ѵ��������ѧԺ����¥���п������<p>�ػʵ��к�ʮ�ֻ�רְ���᳤�����ࡢ�ػʵ��к�ʮ�ֻ����鳤����÷������ѧԺ��ί�������ǰ��ϯ��������������ѧԺ�����ʮ�ֻṤ����֧�ֺͰ�����ʾ���ĵĸ�л��<p>7��11�գ��ɺӱ�ʡ��ʮ�ֻ������ȫʡ������ʮ��Ӧ���Ȼ�������ʡ��ʯ��ׯ���С�"
content=re.findall(">[^<>\n]+<|src=\".*g\"",text2)
for i in range(len(content)):
    if content[i].find('>')==-1:
        content[i]="^split^"+content[i]+"^split^"
        content[i+1]=">"+content[i+1][1:-1]+"^split^<"
    else:
        content[i] = content[i][1:-1].replace('?','').replace(' ','')
        if content[i][-1:]=='��':
            content[i]=content[i]+"^split^"
    print(content[i])
strc=''.join(content)
str=[s for s in strc.split("^split^") if s!='']
print('\n'.join(str))

# """ ����п�ѡ���� """
# options = {}
# options["title"] = "����"
#
# """ ��������������ժҪ�ӿ� """
# client.newsSummary(text, maxSummaryLen, options)

# rule=["\d+��\d+��\d+��","\d+��\d+��"]

# print(time)
# sort_time=sorted(time,key=time.__getitem__,reverse=True)
# print(sort_time)
# if re.findall(r"\d+��\d+",sort_time[0]):
#     print(re.findall(r"\d+��\d+",sort_time[0]))
# print("text:"+re.findall(r"\d+��\d+��",text)[0])

# text1 = """
# <div id="vsb_content"><p style="margin: 0px;line-height: 2em;text-indent: 28px;mso-char-indent-count: 2.0000"><span style="font-family: ����;font-size: 14px;mso-spacerun: 'yes';mso-ascii-font-family: calibri;mso-hansi-font-family: calibri;mso-bidi-font-family: 'times new roman';mso-font-kerning: 1px"><span style="font-family: ����, simhei;font-size: 16px"></span></span></p>
# <table align="center" class="imgtable" uetable="null" ue_class="imgtable" ue_style="border-width:0px;float:none;" style="border-width: 0px;margin: 0px auto">
#  <tbody>
#   <tr>
#    <td align="middle" valign="center" ue_style="border-width:0px;text-align:center;" style="border-width: 0px;text-align: center"><img width="600" title="ȫ��ѧԱ����ѵ��ʦ��Ӱ" id="11E17" src="http://localhost:8080/__local/F/09/D8/667BD7A18E408ABC5196998589D_B07EDD91_11E17.jpg" border="0" hspace="0"></td>
#   </tr>
#   <tr>
#    <td ue_style="text-align:center;border-width:0px" style="border-width: 0px;text-align: center"><span style="font-family: ΢���ź�, microsoft yahei">ȫ��ѧԱ����ѵ��ʦ��Ӱ</span></td>
#   </tr>
#  </tbody>
# </table>
# <p style="margin: 0px;line-height: 2em;text-indent: 28px;mso-char-indent-count: 2.0000"><span style="font-family: ����;font-size: 14px;mso-spacerun: 'yes';mso-ascii-font-family: calibri;mso-hansi-font-family: calibri;mso-bidi-font-family: 'times new roman';mso-font-kerning: 1px"><span style="font-family: ����, simhei;font-size: 16px"></span></span><span style="font-family: calibri;font-size: 14px;mso-spacerun: 'yes';mso-bidi-font-family: 'times new roman';mso-font-kerning: 1px;mso-fareast-font-family: ����">
#   <!--?xml:namespace prefix="o" /-->
#   <p></p></span></p>
# <p style="margin: 0px;line-height: 2em;text-indent: 28px;mso-char-indent-count: 2.0000"><span style="font-family: ����;font-size: 14px;mso-spacerun: 'yes';mso-ascii-font-family: calibri;mso-hansi-font-family: calibri;mso-bidi-font-family: 'times new roman';mso-font-kerning: 1px"><span style="font-family: ����, simhei;font-size: 16px;mso-spacerun: 'yes';mso-ascii-font-family: calibri;mso-hansi-font-family: calibri;mso-bidi-font-family: 'times new roman';mso-font-kerning: 1px"></span></span></p>
# <p style="margin: 0px;line-height: 2em;text-indent: 28px;mso-char-indent-count: 2.0000"><span style="font-family: ����;font-size: 14px;mso-spacerun: 'yes';mso-ascii-font-family: calibri;mso-hansi-font-family: calibri;mso-bidi-font-family: 'times new roman';mso-font-kerning: 1px"><span style="font-family: ΢���ź�, microsoft yahei;font-size: 16px;mso-spacerun: 'yes';mso-ascii-font-family: calibri;mso-hansi-font-family: calibri;mso-bidi-font-family: 'times new roman';mso-font-kerning: 1px">7</span><span style="font-family: ΢���ź�, microsoft yahei;font-size: 16px">��</span><span style="font-family: ΢���ź�, microsoft yahei;font-size: 16px">15</span><span style="font-family: ΢���ź�, microsoft yahei;font-size: 16px">��</span><span style="font-family: ΢���ź�, microsoft yahei;font-size: 16px">-19</span><span style="font-family: ΢���ź�, microsoft yahei;font-size: 16px">�գ���Ժ������¥</span><span style="font-family: ΢���ź�, microsoft yahei;font-size: 16px">413</span><span style="font-family: ΢���ź�, microsoft yahei;font-size: 16px">�ɹ��ٰ�</span><span style="font-family: ΢���ź�, microsoft yahei;font-size: 16px">2019</span><span style="font-family: ΢���ź�, microsoft yahei;font-size: 16px">���ػʵ��к�ʮ�ֻ�</span></span><span style="font-family: ΢���ź�, microsoft yahei;font-size: 16px;mso-spacerun: 'yes';mso-ascii-font-family: calibri;mso-hansi-font-family: calibri;mso-bidi-font-family: 'times new roman';mso-font-kerning: 1px">Ӧ���Ȼ�ʦ����ѵ����˴���ѵ���й���ʮ�ֻ��ܻ�ѵ�����Ľ�ʦ����Ƽ����������ʦ����Ժѧ��������</span><span style="font-family: ΢���ź�, microsoft yahei;font-size: 16px;mso-spacerun: 'yes';mso-ascii-font-family: calibri;mso-hansi-font-family: calibri;mso-bidi-font-family: 'times new roman';mso-font-kerning: 1px">��֯���ָ���Ա��ѧ��������Ա��ѧ������ʿ��</span><span style="font-family: ΢���ź�, microsoft yahei;font-size: 16px;mso-spacerun: 'yes';mso-ascii-font-family: calibri;mso-hansi-font-family: calibri;mso-bidi-font-family: 'times new roman';mso-font-kerning: 1px">��</span><span style="font-family: ����;font-size: 14px;mso-spacerun: 'yes';mso-ascii-font-family: calibri;mso-hansi-font-family: calibri;mso-bidi-font-family: 'times new roman';mso-font-kerning: 1px"><span style="font-family: ΢���ź�, microsoft yahei;font-size: 16px;mso-spacerun: 'yes';mso-ascii-font-family: calibri;mso-hansi-font-family: calibri;mso-bidi-font-family: 'times new roman';mso-font-kerning: 1px">25</span><span style="font-family: ΢���ź�, microsoft yahei;font-size: 16px">�˲μ���ѵ��</span></span><span style="font-family: ����;font-size: 14px;mso-spacerun: 'yes';mso-ascii-font-family: calibri;mso-hansi-font-family: calibri;mso-bidi-font-family: 'times new roman';mso-font-kerning: 1px">
#   <p></p></span></p>
# <p style="margin: 0px;line-height: 2em;text-indent: 28px;mso-char-indent-count: 2.0000"><span style="font-family: ����;font-size: 14px;mso-spacerun: 'yes';mso-ascii-font-family: calibri;mso-hansi-font-family: calibri;mso-bidi-font-family: 'times new roman';mso-font-kerning: 1px"><span style="font-family: ����, simhei;font-size: 16px"></span></span></p>
# <table align="center" class="imgtable" uetable="null" ue_class="imgtable" ue_style="border-width:0px;float:none;" style="border-width: 0px;margin: 0px auto">
#  <tbody>
#   <tr>
#    <td ue_style="border-width:0px;text-align:center;" style="border-width: 0px;text-align: center"><img width="600" title="2019��Ӧ���Ȼ�ʦ����ѵ������ʽ" id="1D92B" src="http://localhost:8080/__local/9/CF/00/CD5980FC85A74D1381EA0C25AE5_B8E13AFD_1D92B.jpg" border="0" hspace="0"></td>
#   </tr>
#   <tr>
#    <td ue_style="text-align:center;border-width:0px" style="border-width: 0px;text-align: center"><span style="font-family: ΢���ź�, microsoft yahei">2019��Ӧ���Ȼ�ʦ����ѵ������ʽ</span></td>
#   </tr>
#  </tbody>
# </table>
# <p style="margin: 0px;line-height: 2em;text-indent: 28px;mso-char-indent-count: 2.0000"><span style="font-family: ����;font-size: 14px;mso-spacerun: 'yes';mso-ascii-font-family: calibri;mso-hansi-font-family: calibri;mso-bidi-font-family: 'times new roman';mso-font-kerning: 1px"><span style="font-family: ����, simhei;font-size: 16px"></span></span><span style="font-family: calibri;font-size: 14px;mso-spacerun: 'yes';mso-bidi-font-family: 'times new roman';mso-font-kerning: 1px;mso-fareast-font-family: ����">
#   <p></p></span></p>
# <p style="margin: 0px;line-height: 2em;text-indent: 28px;mso-char-indent-count: 2.0000"><span style="font-family: ����;font-size: 14px;mso-spacerun: 'yes';mso-ascii-font-family: calibri;mso-hansi-font-family: calibri;mso-bidi-font-family: 'times new roman';mso-font-kerning: 1px"><span style="font-family: ����, simhei;font-size: 16px;mso-spacerun: 'yes';mso-ascii-font-family: calibri;mso-hansi-font-family: calibri;mso-bidi-font-family: 'times new roman';mso-font-kerning: 1px"></span></span></p>
# <p style="margin: 0px;line-height: 2em;text-indent: 28px;mso-char-indent-count: 2.0000"><span style="font-family: ����;font-size: 14px;mso-spacerun: 'yes';mso-ascii-font-family: calibri;mso-hansi-font-family: calibri;mso-bidi-font-family: 'times new roman';mso-font-kerning: 1px"><span style="font-family: ΢���ź�, microsoft yahei;font-size: 16px;mso-spacerun: 'yes';mso-ascii-font-family: calibri;mso-hansi-font-family: calibri;mso-bidi-font-family: 'times new roman';mso-font-kerning: 1px">7</span><span style="font-family: ΢���ź�, microsoft yahei;font-size: 16px">��</span><span style="font-family: ΢���ź�, microsoft yahei;font-size: 16px">15</span><span style="font-family: ΢���ź�, microsoft yahei;font-size: 16px">�����磬��ѵ��������ѧԺ����¥���п������</span></span><span style="font-family: ΢���ź�, microsoft yahei;font-size: 16px;mso-spacerun: 'yes';mso-ascii-font-family: calibri;mso-hansi-font-family: calibri;mso-bidi-font-family: 'times new roman';mso-font-kerning: 1px">�ػʵ��к�ʮ�ֻ�רְ���᳤�����ࡢ�ػʵ��к�ʮ�ֻ����鳤����÷������ѧԺ��ί�������ǰ��ϯ������񡣸�Ժ���������ֿ�����ʽ��</span><span style="font-family: ����;font-size: 14px;mso-spacerun: 'yes';mso-ascii-font-family: calibri;mso-hansi-font-family: calibri;mso-bidi-font-family: 'times new roman';mso-font-kerning: 1px">
#   <p></p></span></p>
# <p style="margin: 0px;line-height: 2em;text-indent: 28px;mso-char-indent-count: 2.0000"><span style="font-family: ΢���ź�, microsoft yahei;font-size: 16px;mso-spacerun: 'yes';mso-ascii-font-family: calibri;mso-hansi-font-family: calibri;mso-bidi-font-family: 'times new roman';mso-font-kerning: 1px">����ǰ�ڿ�����ʽ���´ǣ���ϣ����ѵѧԱ����ѧϰ�Ȼ����ܣ��������ּ��ܴ��ڸ��������ʦ��ѧ��������ȫ��ᣬͬʱ���˵����徫�񴫵ݿ������ø������Я���ֹ�ͬ������ұ�����Ӧ���Ȼ���������</span><span style="font-family: ����;font-size: 14px;mso-spacerun: 'yes';mso-ascii-font-family: calibri;mso-hansi-font-family: calibri;mso-bidi-font-family: 'times new roman';mso-font-kerning: 1px">
#   <p></p></span></p>
# <p style="margin: 0px;line-height: 2em;text-indent: 28px;mso-char-indent-count: 2.0000"><span style="font-family: ΢���ź�, microsoft yahei;font-size: 16px;mso-spacerun: 'yes';mso-ascii-font-family: calibri;mso-hansi-font-family: calibri;mso-bidi-font-family: 'times new roman';mso-font-kerning: 1px">�������ڿ�����ʽ�Ͻ�����������ᷢչ��Ӧ���Ȼ���ѵ���������˽��Ͽɣ���ϧѧϰ���ᣬ������߾Ȼ�������Ϊ�Ժ����ѵ��û������������ѧԺ�����ʮ�ֻṤ����֧�ֺͰ�����ʾ���ĵĸ�л��</span><span style="font-family: calibri;font-size: 14px;mso-spacerun: 'yes';mso-bidi-font-family: 'times new roman';mso-font-kerning: 1px;mso-fareast-font-family: ����">
#   <p></p></span></p>
# <p style="margin: 0px;line-height: 2em;text-indent: 28px;mso-char-indent-count: 2.0000"><span style="font-family: ΢���ź�, microsoft yahei;font-size: 16px;mso-spacerun: 'yes';mso-ascii-font-family: calibri;mso-hansi-font-family: calibri;mso-bidi-font-family: 'times new roman';mso-font-kerning: 1px">������ʽ�����󣬽����žͿ�ʼ���۽�ѧ��</span></p>
# <p style="margin: 0px;line-height: 2em;text-indent: 28px;mso-char-indent-count: 2.0000"><span style="font-family: ����, simhei;font-size: 16px;mso-spacerun: 'yes';mso-ascii-font-family: calibri;mso-hansi-font-family: calibri;mso-bidi-font-family: 'times new roman';mso-font-kerning: 1px"></span><span style="font-family: ����;font-size: 14px;mso-spacerun: 'yes';mso-ascii-font-family: calibri;mso-hansi-font-family: calibri;mso-bidi-font-family: 'times new roman';mso-font-kerning: 1px">
#   <p></p></span> ?</p>
# <p style="margin: 0px;line-height: 2em;text-indent: 28px;mso-char-indent-count: 2.0000"><span style="font-family: ����, simhei;font-size: 16px;mso-spacerun: 'yes';mso-ascii-font-family: calibri;mso-hansi-font-family: calibri;mso-bidi-font-family: 'times new roman';mso-font-kerning: 1px"></span> ?</p>
# <table align="center" class="imgtable" uetable="null" ue_class="imgtable" ue_style="border-width:0px;float:none;" style="border-width: 0px;margin: 0px auto">
#  <tbody>
#   <tr>
#    <td ue_style="border-width:0px;text-align:center;" style="border-width: 0px;text-align: center"><img width="600" title="����Ƽ��ʦ��ΪѧԱ��������֪ʶ" id="1236C" src="http://localhost:8080/__local/6/62/B4/8F71614CB40425307309D5CC305_4ED1810C_1236C.jpg" border="0" hspace="0"></td>
#   </tr>
#   <tr>
#    <td ue_style="text-align:center;border-width:0px" style="border-width: 0px;text-align: center"><span style="font-family: ΢���ź�, microsoft yahei">����Ƽ��ʦ��ΪѧԱ��������֪ʶ</span>
#     <table class="imgtable" uetable="null" ue_class="imgtable" ue_style="border-width:0px;float:none;" style="border-width: 0px;float: none">
#      <tbody>
#       <tr>
#        <td ue_style="border-width:0px;text-align:center;" style="border-width: 0px;text-align: center"><img width="600" title="����Ƽ��ʦ��ΪѧԱ��������֪ʶ" id="2039F" src="http://localhost:8080/__local/3/1F/43/C9F8B4B8266919428414634C47F_5F6D45D1_2039F.jpg" border="0" hspace="0"></td>
#       </tr>
#       <tr>
#        <td ue_style="text-align:center;border-width:0px" style="border-width: 0px;text-align: center"><span style="font-family: ΢���ź�, microsoft yahei">����Ƽ��ʦ��ΪѧԱ��������֪ʶ</span></td>
#       </tr>
#      </tbody>
#     </table></td>
#   </tr>
#  </tbody>
# </table>
# <p style="margin: 0px;line-height: 2em;text-indent: 28px;mso-char-indent-count: 2.0000"><span style="font-family: ����;font-size: 14px;mso-spacerun: 'yes';mso-ascii-font-family: calibri;mso-hansi-font-family: calibri;mso-bidi-font-family: 'times new roman';mso-font-kerning: 1px"><span style="font-family: ����, simhei;font-size: 16px"></span></span></p>
# <table align="center" class="imgtable" uetable="null" ue_class="imgtable" ue_style="border-width:0px;float:none;" style="border-width: 0px;margin: 0px auto">
#  <tbody>
#   <tr>
#    <td ue_style="border-width:0px;text-align:center;" style="border-width: 0px;text-align: center"><img width="600" title="ʵ����ʦ����ѧԱ��ʵ����ϰ" id="1D9E1" src="http://localhost:8080/__local/1/B9/1C/C31E3B9EB6D377DF28DAEF79627_B8569A47_1D9E1.jpg" hspace="0"></td>
#   </tr>
#   <tr>
#    <td ue_style="text-align:center;border-width:0px" style="border-width: 0px;text-align: center"><span style="font-family: ΢���ź�, microsoft yahei">ʵ����ʦ����ѧԱ��ʵ����ϰ</span></td>
#   </tr>
#  </tbody>
# </table>
# <p><br> ?</p>
# <table align="center" class="imgtable" uetable="null" ue_class="imgtable" ue_style="border-width:0px;float:none;" style="border-width: 0px;margin: 0px auto">
#  <tbody>
#   <tr>
#    <td ue_style="border-width:0px;text-align:center;" style="border-width: 0px;text-align: center"><img width="600" title="ʵ����ʦ����ѧԱ��ʵ����ϰ" id="1D28A" src="http://localhost:8080/__local/5/DF/ED/B96F3355112B7ACC4AE825CBB39_CDE4B4D3_1D28A.jpg" hspace="0"></td>
#   </tr>
#   <tr>
#    <td ue_style="text-align:center;border-width:0px" style="border-width: 0px;text-align: center"><span style="font-family: ΢���ź�, microsoft yahei">ʵ����ʦ����ѧԱ��ʵ����ϰ</span></td>
#   </tr>
#  </tbody>
# </table>
# <p><span style="font-family: ����;font-size: 14px;mso-spacerun: 'yes';mso-ascii-font-family: calibri;mso-hansi-font-family: calibri;mso-bidi-font-family: 'times new roman';mso-font-kerning: 1px"><span style="font-family: ����, simhei;font-size: 16px"></span></span> ?</p>
# <p style="margin: 0px;line-height: 2em;text-indent: 28px;mso-char-indent-count: 2.0000"><span style="font-family: ΢���ź�, microsoft yahei;font-size: 16px;mso-spacerun: 'yes';mso-ascii-font-family: calibri;mso-hansi-font-family: calibri;mso-bidi-font-family: 'times new roman';mso-font-kerning: 1px">������ѵ�ڿγ����á�ʦ��ѡƸ�������ʽ�ȷ����ص����ָ�УУ԰���ص��ʦ��������ʵЧ�Ժ������ǿ��ѧԱ���Ⱥ�ѧϰ�ˡ��Ȼ��������ѧ���������ķθ����봴�˾Ȼ�������������֢�������������</span><span style="font-family: ΢���ź�, microsoft yahei;font-size: 16px;mso-spacerun: 'yes';mso-ascii-font-family: calibri;mso-hansi-font-family: calibri;mso-bidi-font-family: 'times new roman';mso-font-kerning: 1px">��������ѵ�л������λ��ʦѧϰ��ͨ������ģ����������ѧϰ���ķθ��ա��˹��������ֳ����������۹̶��ȾȻ����ܡ�</span></p>
# <p style="margin: 0px;line-height: 2em;text-indent: 28px;mso-char-indent-count: 2.0000"><span style="font-family: ����, simhei;font-size: 16px;mso-spacerun: 'yes';mso-ascii-font-family: calibri;mso-hansi-font-family: calibri;mso-bidi-font-family: 'times new roman';mso-font-kerning: 1px"></span> ?</p>
# <p style="margin: 0px;line-height: 2em;text-indent: 28px;mso-char-indent-count: 2.0000"><span style="font-family: ����, simhei;font-size: 16px;mso-spacerun: 'yes';mso-ascii-font-family: calibri;mso-hansi-font-family: calibri;mso-bidi-font-family: 'times new roman';mso-font-kerning: 1px"></span><span style="font-family: ����;font-size: 14px;mso-spacerun: 'yes';mso-ascii-font-family: calibri;mso-hansi-font-family: calibri;mso-bidi-font-family: 'times new roman';mso-font-kerning: 1px"> </span>?</p>
# <p><span style="font-family: ����;font-size: 14px;mso-spacerun: 'yes';mso-ascii-font-family: calibri;mso-hansi-font-family: calibri;mso-bidi-font-family: 'times new roman';mso-font-kerning: 1px"></span>?</p>
# <table align="center" class="imgtable" uetable="null" ue_class="imgtable" ue_style="border-width:0px;float:none;" style="border-width: 0px;margin: 0px auto">
#  <tbody>
#   <tr>
#    <td ue_style="border-width:0px;text-align:center;" style="border-width: 0px;text-align: center"><img width="600" title="ѧԱͨ������ģ��ѧϰͽ���ķθ���" id="14A2E" src="http://localhost:8080/__local/0/12/EF/49EAAEC68DD85BC2DB661B055AF_97059866_14A2E.jpg" border="0" hspace="0"></td>
#   </tr>
#   <tr>
#    <td ue_style="text-align:center;border-width:0px" style="border-width: 0px;text-align: center"><span style="font-family: ΢���ź�, microsoft yahei">ѧԱͨ������ģ��ѧϰͽ���ķθ���</span></td>
#   </tr>
#  </tbody>
# </table>
# <p></p>
# <p></p>
# <p> ?</p>
# <p style="margin: 0px;line-height: 2em;text-indent: 28px;mso-char-indent-count: 2.0000"><span style="font-family: ΢���ź�, microsoft yahei;font-size: 16px;mso-spacerun: 'yes';mso-ascii-font-family: calibri;mso-hansi-font-family: calibri;mso-bidi-font-family: 'times new roman';mso-font-kerning: 1px">���У԰������ѧ�������ص㣬��ѵ����Ա�ԡ���α�����������Ϊ�ڿο������ݡ�ͨ�����ڡ��Ż�����ô�족��������ʱ�̡��������ε��ˡ��Ⱥ�ѧ��������ص����ݣ�Ϊ��ѧ��ȫ�������˳���׼����</span><span style="font-family: ����;font-size: 14px;mso-spacerun: 'yes';mso-ascii-font-family: calibri;mso-hansi-font-family: calibri;mso-bidi-font-family: 'times new roman';mso-font-kerning: 1px">
#   <p></p></span></p>
# <p style="margin: 0px;line-height: 2em;text-indent: 28px;mso-char-indent-count: 2.0000"><span style="font-family: ����;font-size: 14px;mso-spacerun: 'yes';mso-ascii-font-family: calibri;mso-hansi-font-family: calibri;mso-bidi-font-family: 'times new roman';mso-font-kerning: 1px"><span style="font-family: ΢���ź�, microsoft yahei;font-size: 16px">ͼ��</span></span></p>
# <table align="center" class="imgtable" uetable="null" ue_class="imgtable" ue_style="border-width:0px;float:none;" style="border-width: 0px;margin: 0px auto">
#  <tbody>
#   <tr>
#    <td ue_style="border-width:0px;text-align:center;" style="border-width: 0px;text-align: center"><img width="600" title="��ѵѧԱ�ֳ�����" id="1BDDA" src="http://localhost:8080/__local/6/B0/46/5FD459ABFD8B5C2291EE8D07C0A_EF811A70_1BDDA.jpg" hspace="0"></td>
#   </tr>
#   <tr>
#    <td ue_style="text-align:center;border-width:0px" style="border-width: 0px;text-align: center"><span style="font-family: ΢���ź�, microsoft yahei">��ѵѧԱ�ֳ�����</span></td>
#   </tr>
#  </tbody>
# </table>
# <p><br> ?</p>
# <table align="center" class="imgtable" uetable="null" ue_class="imgtable" ue_style="border-width:0px;float:none;" style="border-width: 0px;margin: 0px auto">
#  <tbody>
#   <tr>
#    <td ue_style="border-width:0px;text-align:center;" style="border-width: 0px;text-align: center"><img width="600" title="��ѵѧԱ�ֳ�����" id="1B48F" src="http://localhost:8080/__local/D/6F/0C/10D18E8D664F9A4D734E6F48AB0_DD92DEA3_1B48F.jpg" hspace="0"></td>
#   </tr>
#   <tr>
#    <td ue_style="text-align:center;border-width:0px" style="border-width: 0px;text-align: center"><span style="font-family: ΢���ź�, microsoft yahei">��ѵѧԱ�ֳ�����</span></td>
#   </tr>
#  </tbody>
# </table>
# <p> ?</p>
# <p style="margin: 0px;line-height: 2em;text-indent: 28px;mso-char-indent-count: 2.0000"><span style="font-family: ΢���ź�, microsoft yahei;font-size: 16px;mso-spacerun: 'yes';mso-ascii-font-family: calibri;mso-hansi-font-family: calibri;mso-bidi-font-family: 'times new roman';mso-font-kerning: 1px">����������ŵ�����ѧϰ��ʵ����ϰ��ͨ���ϸ�ıվ����ۿ��ԣ�ʵ�ٿ��ԣ��Խ����ԣ��˴���ѵ��Բ����������ѵѧԱ�׷ױ�ʾ���Ӧ���Ȼ���ѵ�����Ǵ����˺ܴ�İ����������ǽ������������ͻ�����ʱ���������޴룬�ڽ���ѧ�����ڰ�ȫ����֪ʶʱ����һ��רҵ�淶�����ݣ��������Ժ�Ĺ����������к����ʮ���˵����徫�񣬰��������ѧ����ʦ</span><span style="font-family: ΢���ź�, microsoft yahei;font-size: 16px;mso-spacerun: 'yes';mso-ascii-font-family: calibri;mso-hansi-font-family: calibri;mso-bidi-font-family: 'times new roman';mso-font-kerning: 1px">�淶�Ȼ����ܣ���߾Ȼ�ˮƽ��</span><span style="font-family: ����;font-size: 14px;mso-spacerun: 'yes';mso-ascii-font-family: calibri;mso-hansi-font-family: calibri;mso-bidi-font-family: 'times new roman';mso-font-kerning: 1px">
#   <p></p></span></p>
# <p style="margin: 0px;line-height: 2em;text-indent: 28px;mso-char-indent-count: 2.0000"><span style="font-family: ����, simhei;font-size: 16px;mso-spacerun: 'yes';mso-ascii-font-family: calibri;mso-hansi-font-family: calibri;mso-bidi-font-family: 'times new roman';mso-font-kerning: 1px"></span> ?</p>
# <table align="center" class="imgtable" uetable="null" ue_class="imgtable" ue_style="border-width:0px;float:none;" style="border-width: 0px;margin: 0px auto">
#  <tbody>
#   <tr>
#    <td ue_style="border-width:0px;text-align:center;" style="border-width: 0px;text-align: center"><img width="600" title="ȫʡ������ʮ��Ӧ���Ȼ������佱�ֳ�" id="18E42" src="http://localhost:8080/__local/A/33/53/790995BE2131C09A01CAB7FD762_C654313A_18E42.jpg" border="0" hspace="0"></td>
#   </tr>
#   <tr>
#    <td ue_style="text-align:center;border-width:0px" style="border-width: 0px;text-align: center"><span style="font-family: ΢���ź�, microsoft yahei">ȫʡ������ʮ��Ӧ���Ȼ������佱�ֳ�</span></td>
#   </tr>
#  </tbody>
# </table>
# <p style="margin: 0px;line-height: 2em;text-indent: 28px;mso-char-indent-count: 2.0000"><span style="font-family: ����, simhei;font-size: 16px;mso-spacerun: 'yes';mso-ascii-font-family: calibri;mso-hansi-font-family: calibri;mso-bidi-font-family: 'times new roman';mso-font-kerning: 1px"></span> ?</p>
# <p style="margin: 0px;line-height: 2em;text-indent: 28px;mso-char-indent-count: 2.0000"><span style="font-family: ΢���ź�, microsoft yahei;font-size: 16px;mso-spacerun: 'yes';mso-bidi-font-family: 'times new roman';mso-font-kerning: 1px;mso-fareast-font-family: ����">����</span><span style="font-family: ΢���ź�, microsoft yahei;font-size: 16px;mso-spacerun: 'yes';mso-ascii-font-family: calibri;mso-hansi-font-family: calibri;mso-bidi-font-family: 'times new roman';mso-font-kerning: 1px">3</span><span style="font-family: ΢���ź�, microsoft yahei;font-size: 16px;mso-spacerun: 'yes';mso-bidi-font-family: 'times new roman';mso-font-kerning: 1px;mso-fareast-font-family: ����">�£���ɽ��ѧ����ѧԺ���ػʵ��к�ʮ�ֻ�֣���������</span><span style="font-family: ΢���ź�, microsoft yahei;font-size: 16px;mso-spacerun: 'yes';mso-ascii-font-family: calibri;mso-hansi-font-family: calibri;mso-bidi-font-family: 'times new roman';mso-font-kerning: 1px">��</span><span style="font-family: ΢���ź�, microsoft yahei;font-size: 16px;mso-spacerun: 'yes';mso-bidi-font-family: 'times new roman';mso-font-kerning: 1px;mso-fareast-font-family: ����">����</span><span style="font-family: ΢���ź�, microsoft yahei;font-size: 16px;mso-spacerun: 'yes';mso-ascii-font-family: calibri;mso-hansi-font-family: calibri;mso-bidi-font-family: 'times new roman';mso-font-kerning: 1px">��</span><span style="font-family: ΢���ź�, microsoft yahei;font-size: 16px;mso-spacerun: 'yes';mso-bidi-font-family: 'times new roman';mso-font-kerning: 1px;mso-fareast-font-family: ����">����ѧԺ��ʮ�ֻᡣ</span><span style="font-family: ����;font-size: 14px;mso-spacerun: 'yes';mso-ascii-font-family: calibri;mso-hansi-font-family: calibri;mso-bidi-font-family: 'times new roman';mso-font-kerning: 1px"><span style="font-family: ΢���ź�, microsoft yahei;font-size: 16px;mso-spacerun: 'yes';mso-ascii-font-family: calibri;mso-hansi-font-family: calibri;mso-bidi-font-family: 'times new roman';mso-font-kerning: 1px">7</span><span style="font-family: ΢���ź�, microsoft yahei;font-size: 16px">��</span><span style="font-family: ΢���ź�, microsoft yahei;font-size: 16px">11</span><span style="font-family: ΢���ź�, microsoft yahei;font-size: 16px">�գ�</span></span><span style="font-family: calibri;font-size: 14px;mso-spacerun: 'yes';mso-bidi-font-family: 'times new roman';mso-font-kerning: 1px;mso-fareast-font-family: ����"><span style="font-family: ΢���ź�, microsoft yahei;font-size: 16px;mso-spacerun: 'yes';mso-bidi-font-family: 'times new roman';mso-font-kerning: 1px;mso-fareast-font-family: ����">�ɺӱ�ʡ��ʮ�ֻ������ȫʡ������ʮ��Ӧ���Ȼ�������ʡ��ʯ��ׯ���С�����ѧԺ��ί�߶����ӣ�ѧ��������������֯��ϣ�ѡ��ѧԺ���������ѧ��ʿ����Ӵ����ػʵ��в�������ǰ���3</span><span style="font-family: ΢���ź�, microsoft yahei;font-size: 16px">���µ�׼��ʱ����к��Ĺ�����Ա����ѵ��ʦ����ָ��������ѧ�Ӳ�������������ܳɼ���������</span><span style="font-family: ΢���ź�, microsoft yahei;font-size: 16px">1</span><span style="font-family: ΢���ź�, microsoft yahei;font-size: 16px">��������Ƚ���</span><span style="font-family: ΢���ź�, microsoft yahei;font-size: 16px">2</span><span style="font-family: ΢���ź�, microsoft yahei;font-size: 16px">���������Ƚ�����ʷ��óɼ���</span></span><span style="font-family: calibri;font-size: 14px;mso-spacerun: 'yes';mso-bidi-font-family: 'times new roman';mso-font-kerning: 1px;mso-fareast-font-family: ����">
#   <p></p></span></p>
# <p style="line-height: 2em"><span style="font-family: ����, simhei;font-size: 16px"></span> ?</p></div>
# """
# # \p{Han}\p{P}A-Za-z0-9  \u4E00-\u9FA5
# content=re.findall(">[^<>\n]+<|src=\".*g\"",text1)
# for i in range(len(content)):
#     if content[i].find('>')==-1:
#         content[i]="^split^"+content[i]+"^split^"
#         content[i+1]=">"+content[i+1][1:-1]+"^split^<"
#     else:
#         content[i] = content[i][1:-1].replace('?','').replace(' ','')
#         if content[i][-1:]=='��':
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