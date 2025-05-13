# %%writefile Config.py
# 文件路径
TRAIN_PATH = '/kaggle/input/entropy/data/data/train.txt'
TEST_PATH = '/kaggle/input/entropy/data/data/dev.txt'
BERT_MODEL = '/kaggle/input/entropy/bert-base-chinese/bert-base-chinese'
MODEL_DIR = '/kaggle/input/entropy/models/models'
#!cp -r /kaggle/input/weibo-db-db/weibo_db.db /kaggle/working/
BERT_PAD_ID = 0
MAX_LEN = 200# 最大长度，超过截取，缺少填充
BATH_SIZE = 32
BATCH_SIZE = 32
EPOCH = 10
LR = 0.001# 学习率
CLASS_NUM = 2# 分类数，二分类
EMBEDDING = 768# 子向量维度，BERT 中默认


OUTPUT_SIZE = 2# BiLSTM 参数
N_LAYERS = 2 # BiLSTM 的层数
HIDDEN_DIM = 128 # LSTM 中隐层的维度，768/2
DROP_PROB = 0.2 # dropout 参数

