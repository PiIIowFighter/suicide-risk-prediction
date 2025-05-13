# Suicide Risk Prediction

本仓库主要用于自杀风险预测，包含了两类模型：DSI-BTCNN系列模型和Termfrequency模型。以下是详细的说明：

## 一、数据说明
数据存储在 `data` 目录下，具体如下：

- 训练集：`train.txt`，每行格式为 文本	标签，标签为 0 或 1，分别代表无自杀风险和有自杀风险。
- 验证集：`dev.txt`，格式与训练集一致。

## 二、Kaggle 运行配置
### 1. 上传文件
为了在 Kaggle 上运行模型训练，需要上传以下文件：

- 数据文件：将 `train.txt` 和 `dev.txt` 上传到 `input/entropy/data/data` 目录下，该路径需与 `Config.py` 中的 `TRAIN_PATH` 和 `TEST_PATH` 保持一致。
- BERT 预训练模型：从 Hugging Face 下载 `bert-base-chinese` 模型，包含 `config.json`、`pytorch_model.bin` 和 `vocab.txt`，并上传到 `input/entropy/bert-base-chinese/bert-base-chinese` 目录，对应 `Config.py` 中的 `BERT_MODEL` 路径。
- 代码文件：所有 `DSI-BTCNN*.py` 模型文件、`Config.py` 以及数据库文件 `weibo_db.db`（若使用）需上传到 `kaggle/working` 目录（Kaggle 工作目录）。

### 2. 路径调整
若需要自定义路径，可修改 `Config.py` 中的以下参数：
TRAIN_PATH = "/kaggle/input/自定义数据路径/train.txt"  # 训练集路径
TEST_PATH = "/kaggle/input/自定义数据路径/dev.txt"    # 验证集路径
BERT_MODEL = "/kaggle/input/自定义模型路径/bert-base-chinese"  # BERT模型路径
DATABASE = "/kaggle/working/weibo_db.db"  # 数据库路径（若使用）
## 三、模型运行与训练方法
### 1. DSI-BTCNN 系列模型
DSI-BTCNN 系列模型包含多种变体，如串行结构、并行结构结合信息增益、注意力机制等。以下是通用的运行和训练步骤：


#### 训练步骤
1. 选择模型变体：根据需求修改代码中导入的模型类，例如 `DSI-BTCNN(serial).py` 为串行结构模型。
2. 配置超参数：在 `Config.py` 中调整以下超参数：
   - `BATCH_SIZE`：批次大小，默认值为 32。
   - `LR`：学习率，默认值为 0.001。
   - `MAX_LEN`：文本最大长度，默认值为 200。
   - `EPOCH`：训练轮次，可根据实际情况调整。
3. 运行训练脚本：直接运行模型文件中 `if __name__ == "__main__":` 部分的代码，Kaggle 会自动使用 GPU 加速训练。

### 2. Termfrequency 模型
Termfrequency 模型基于文本词频统计与规则匹配。以下是运行步骤：

#### 运行方法
1. 预处理文本：使用 `jieba` 对 `train.txt` 和 `dev.txt` 进行分词处理，可参考 `DSI-BTCNN(parallel + attention).py` 中的分词逻辑。
2. 统计词频：计算高风险词（如 “绝望”“放弃”“结束”）的出现频率，生成词频特征。
3. 规则匹配：设定阈值（如高风险词频率 > 0.1），根据词频特征输出分类结果。

## 四、注意事项
- 若遇到 `BERT_MODEL` 加载失败的问题，需检查模型文件是否完整，确保包含 `config.json`、`pytorch_model.bin` 和 `vocab.txt`。
- 数据库功能（如 `insert_to_auc_db`）需要确保 `weibo_db.db` 存在且具有写入权限，Kaggle 的 `working` 目录通常可写。
- 当文本长度超过 `MAX_LEN` 时，会被截断处理；若文本长度过短，则会填充 `[PAD]`（对应 `BERT_PAD_ID = 0`）。

如有任何问题，欢迎在仓库的 Issues 中反馈。
    