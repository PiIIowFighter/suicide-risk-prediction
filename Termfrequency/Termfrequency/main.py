import matplotlib.pyplot as plt
import numpy as np

# 数据
categories = ['friendship', 'parents', 'dating', 'family', 'sexual', 'attractive', 'sex', 'family', 'relationship', 'boyfriend']
male_ig_p = [80, 70, 60, 50, 40, 90, 80, 70, 60, 50]
male_ig_n = [20, 30, 40, 50, 60, 10, 20, 30, 40, 50]
female_ig_p = [60, 50, 70, 80, 20, 80, 60, 50, 30, 20]
female_ig_n = [40, 50, 30, 20, 80, 20, 40, 50, 70, 80]

# 设置柱状图的位置
x = np.arange(len(categories))
width = 0.35

# 创建图形和轴
fig, ax = plt.subplots()

# 绘制男性用户的柱状图
rects1 = ax.bar(x - width/2, male_ig_p, width, label='Male IG-P')
rects2 = ax.bar(x - width/2, male_ig_n, width, bottom=male_ig_p, label='Male IG-N')

# 绘制女性用户的柱状图
rects3 = ax.bar(x + width/2, female_ig_p, width, label='Female IG-P')
rects4 = ax.bar(x + width/2, female_ig_n, width, bottom=female_ig_p, label='Female IG-N')

# 添加文本标签、标题和自定义x轴刻度标签
ax.set_ylabel('Percentage')
ax.set_title('Gender-based classifiers (Reddit)')
ax.set_xticks(x)
ax.set_xticklabels(categories, rotation=45, ha="right")
ax.legend()

# 显示图形
plt.tight_layout()
plt.show()