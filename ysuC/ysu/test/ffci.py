import jieba
from matplotlib import pyplot as plt
from wordcloud import WordCloud
from PIL import Image
import numpy as np

path = r'.'
font = r'C:\Windows\Fonts\FZSTK.TTF'

text = (open(path + r'\test2.py', 'r', encoding='utf-8')).read()
cut = jieba.cut(text)  # 分词
string = ' '.join(cut)
print(string)
print(len(string))
img = Image.open(path + r'\22.png')  # 打开图片
img_array = np.array(img)  # 将图片装换为数组
stopword = ['xa0']  # 设置停止词，也就是你不想显示的词，这里这个词是我前期处理没处理好，你可以删掉他看看他的作用
wc = WordCloud(
    background_color='white',
    width=1000,
    height=800,
    mask=img_array,
    font_path=font,
    stopwords=stopword
)
wc.generate_from_text(string)  # 绘制图片
plt.imshow(wc)
plt.axis('off')
plt.figure()
plt.show()  # 显示图片
wc.to_file(path + r'\new.png')  # 保存图片