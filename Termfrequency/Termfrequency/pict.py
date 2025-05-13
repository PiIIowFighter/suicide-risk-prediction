import matplotlib.pyplot as plt
import numpy as np
font = {'family' : 'SimHei',
        'weight' : 'bold',
        'size'   : '12'}
plt.rc('font', **font)               # 步骤一（设置字体的更多属性）
plt.rc('axes', unicode_minus=False)  # 步骤二（解决坐标轴负数的负号显示问题）
# 自杀组名词数据
nouns_suicide = [
    '差劲(Inferior)', '麻木(Emotional Numbness)', '恶心(Nausea)', '紫砂(Suicide)',
    '废人(Invalid)', '疯子(Lunatic)', '病态(Morbid)', '废物(Trash)',
    '太苦(Overwhelming Hardship)', '情绪低落(Low Mood)', '家暴(Domestic Violence)',
    '尸体(Corpse)', '杀人(Homicide)', '霸凌 (Bullying)', '网暴(Cyberbullying)',
    '跳河(River Jumping)', '神经病(Mental Disorder)', '好气(Frustrated)',
    '数落(Criticism)', '玉玉(Depression)'
]
noun_freq_suicide = [106, 156, 508, 39, 34, 99, 32, 247, 29, 83, 24, 22, 33, 64, 14, 14, 97, 13, 12, 12]

# 非自杀组名词数据
nouns_non_suicide = [
    '大熊猫(Giant Panda)', '口感(Texture (of food))', '景区(Scenic Area)',
    '美食(Delicacies)', '立夏(Beginning of Summer)', '口味(Flavor Profile)',
    '香甜(Aromatic Sweetness)', '家常菜(Home-Style Cuisine)', '麻薯(Mochi)',
    '花花(Flowers)', '参观(Tour)', '早安(Good Morning)', '汤汁(Soup Broth)',
    '美味(Deliciousness)', '书店(Bookstore)', '徐州(Xuzhou)', '洛阳(Luoyang)',
    '芋泥(Taro Paste)', '风景区(Scenic Spot)', '奶猫(Kitten)'
]
noun_freq_non_suicide = [797, 233, 167, 2364, 128, 207, 69, 65, 62, 1314, 58, 1167, 57, 280, 56, 167, 53, 104, 51, 50]

# 自杀组动词数据
verbs_suicide = [
    '自杀(Suicide)', '难受(Feel Unwell)', '想死(Think About Dying)', '割腕(Cut Wrists)',
    '活该(Deserve)', '好累(Feel Exhausted)', '排斥(Reject)', '失眠(Suffer from Insomnia)',
    '杀死(Kill)', '睡不着(Unable to Sleep)', '难过(Feel Sad)', '治病(Treat Illness)',
    '诅咒(Curse)', '发抖(Tremble)', '撑不住(Can\'t Endure Anymore)', '压抑(Suppress)',
    '解脱(Relief)', '崩溃(Collapse)', '排挤(Ostracize)', '自责(Blame Oneself)'
]
verb_freq_suicide = [514, 2002, 208, 60, 94, 268, 37, 717, 61, 893, 1795, 30, 29, 144, 114, 269, 286, 991, 25, 70]

# 非自杀组动词数据
verbs_non_suicide = [
    '出游(Go Out for a Trip)', '可口(Be Delicious)', '旅行(Go on a Journey)',
    '得意(Feel Proud)', '好喝(Be Delicious to Drink)', '品尝(Taste)',
    '开饭(Start Eating)', '烘焙(Baking)', '致敬(Salute)', '重逢(Reunite)',
    '舒展(Relax)', '担当(Undertake)', '开胃(Stimulate Appetite)', '放生(Release Animals into the Wild)',
    '相逢(Meet by Chance)', '烧烤(Barbecue)', '萌化(Melt from Cuteness)', '超爱(Love So Much)',
    '出行(Travel Around)', '超越(Surpass)'
]
verb_freq_non_suicide = [78, 55, 1651, 30, 88, 63, 38, 17, 17, 17, 16, 16, 31, 58, 29, 159, 14, 27, 67, 26]

# 创建名词图表
fig, ax_nouns = plt.subplots(figsize=(10, 10))
y_pos = np.arange(40)  # 40个条目，每个组20个

# 绘制名词条形图
ax_nouns.barh(y_pos[:20], noun_freq_suicide, color='green', label='Suicide Group')
ax_nouns.barh(y_pos[20:], noun_freq_non_suicide, color='blue', label='Non-Suicide Group')

# 添加标签和标题
ax_nouns.set_yticks(y_pos)
ax_nouns.set_yticklabels([nouns_suicide[i] for i in range(20)] + [nouns_non_suicide[i] for i in range(20)])
ax_nouns.set_xlabel('Frequency')
ax_nouns.set_title('Keyness Nouns in Each Group')
ax_nouns.legend()

# 创建动词图表
fig, ax_verbs = plt.subplots(figsize=(10, 10))
y_pos = np.arange(40)  # 40个条目，每个组20个

# 绘制动词条形图
ax_verbs.barh(y_pos[:20], verb_freq_suicide, color='green', label='Suicide Group')
ax_verbs.barh(y_pos[20:], verb_freq_non_suicide, color='blue', label='Non-Suicide Group')

# 添加标签和标题
ax_verbs.set_yticks(y_pos)
ax_verbs.set_yticklabels([verbs_suicide[i] for i in range(20)] + [verbs_non_suicide[i] for i in range(20)])
ax_verbs.set_xlabel('Frequency')
ax_verbs.set_title('Keyness Verbs in Each Group')
ax_verbs.legend()

# 显示图表
plt.tight_layout()
plt.show()