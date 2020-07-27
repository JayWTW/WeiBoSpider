文本分类框架
==

此项目利用tensorflow设计深度学习中常用的分类框架，可通过增加models中的模型来快速实现算法

## 运行环境
```
python: 3.5.2
tensorflow-gpu==1.11.0
```

## 文件目录
```
|-ckpt_model # 模型参数保存位置
|-config # 各个模型的配置信息
    |-bilstm_atten_config.json
    |-bilstm_config.json
    |-data_config.json
    |-rcnn_config.json
    |-textcnn_config.json
    |-transformer_config.json
|-data
    |-preprocess # 预处理后的数据集
    |-raw_data # 原始数据集
    |-stop_words # 停用词
|-data_preprocess
    |-data_base.py # 生成符合模型的输入数据
    |-train_word2vec.py # 使用word2vec训练词向量
|-logs # 保存日志文件
|-models # 模型后加_estimator是指使用tf.estimator方法运行模型，否则使用sess.run运行模型
    |-base_model.py
    |-bilstm.py
    |-bilstmatten.py
    |-rcnn.py
    |-textcnn.py
    |-transformer.py
    |-base_estimator_model.py
    |-bilstm_estimator.py
    |-bilstmatten_estimator.py
    |-rcnn_estimator.py
    |-textcnn_estimator.py
    |-transformer_estimator.py
|-outputs # 保存对应模型的验证集和测试集得分
|-pictures # 使用sess.run方法时会保存神经网络中loss和acc变化曲线图
|-predict_results # 保存对应模型的测试集label
|-trainers_predictors
    |-train_predict.py # 使用sess.run训练模型
    |-train_predict_fold.py # 使用sess.run和k折交叉验证训练模型
    |-train_predict_estimator.py # 使用tf.estimator训练模型
    |-train_predict_estimator_fold.py # 使用tf.estimator和k折交叉验证训练模型
|-user_data
    |-w2v_model # 词向量文件
|-utils
    |-logger.py # 日志代码
    |-metrics.py # 计算指标，代码中还未使用
    |-plot_picture.py # 曲线图代码
```

## 模型运行方法
```
（1）切换到data_preprocess目录，运行python train_word2vec.py，获取词向量
（2）切换到trainers_predictors目录，可以运行python train_predict.py或者python train_predict_estimator.py训练模型，
    若要使用k折交叉验证，则可以运行python train_predict_fold.py或者python train_predict_estimator_fold.py
（3）运行指定模型时，只需要对trainers_predictors目录中的文件进行修改，即修改主函数main中model_config_path
```

## 各个模型的测试情况
**说明：**
```
（1）使用的是train_predict.py，采用sess.run方法；
（2）可以大致参考各个模型的相对训练时间，注意此测试时间与模型的参数相关
```
```
bilstm:           6 epoch收敛,  6分30秒, batch_size: 256
bilstm_attention: 5 epoch收敛,  5分钟,   batch_size: 256
rcnn:             14 epoch收敛, 8分钟,   batch_size: 512
textcnn:          5 epoch收敛,  38秒,    batch_size: 256
transformer:      3 epoch收敛,  35秒,    batch_size: 256
```

## 存在的问题
```
（1）sess.run方法设置的随机种子无法复现结果（原因不明）
（2）tf.estimator方法设置的随机种子无法复现结果（原因不明）
（3）使用tf.estimator时，如果第一次保存的结果是最好的，tf.estimator.BestExporter则没法保存第一次的模型，从而无法预测（原因不明）
```
