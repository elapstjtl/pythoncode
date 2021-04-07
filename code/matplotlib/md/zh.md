https://blog.csdn.net/helunqu2017/article/details/78602959
1.matplotlib系统字体
(1)查询matplotlib系统所有字体

>>> from matplotlib.font_manager import fontManager
>>> fontManager.ttflist


(2)查询matplotlib系统中文字体
from matplotlib.font_manager import fontManager
import os

fonts = [font.name for font in fontManager.ttflist if 
         os.path.exists(font.fname) and os.stat(font.fname).st_size>1e6] 

for font in fonts:
    print(font)
利用os模块中的stat()获取字体文件的大小，并保留字体索引列表中所有大于1M字节的字体文件。由于中文字体文件通常都很大，因此使用这种方法可以粗略地找出所有的中文字体文件。
调用子图对象的text()在其中添加文字，注意文字必须是Unicode字符串。通过一个描述字体的字典指定文字的字体：’fontname’键所对应的值就是字体名。
2.matplotlib显示中文方法
(1)方法一
from pylab import * 
import matplotlib
matplotlib.rcParams['font.family'] = 'Microsoft YaHei'
mpl.rcParams['font.sans-serif'] = ['Microsoft YaHei'] #更新字体格式
mpl.rcParams['font.size'] = 9 

(2)方法二
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
其中AR PL UMing CN代表：宋体。SimHei代表：黑体。

(3)方法三
pyplot并不默认支持中文显示，需要rcParams修改字体来实现
rcParams的属性：
‘font.family’ 用于显示字体的名字
‘font.style’ 字体风格，正常’normal’ 或斜体’italic’
‘font.size’ 字体大小，整数字号或者’large’ ‘x-small’
例子:
import matplotlib
matplotlib.rcParams[‘font.family’] = ‘STSong’
matplotlib.rcParams[‘font.size’] = 20
设定绘制区域的全部字体变成 华文仿宋，字体大小为20
(4)方法四
只希望在某地方绘制中文字符，不改变别的地方的字体
在有中文输出的地方，增加一个属性： fontproperties
plt.xlabel(‘横轴：时间’, fontproperties = ‘simHei’, fontsize = 20)只希望在某地方绘制中文字符，不改变别的地方的字体
在有中文输出的地方，增加一个属性： fontproperties
plt.xlabel(‘横轴：时间’, fontproperties = ‘simHei’, fontsize = 20)