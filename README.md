2020腾讯广告算法大赛
===
复赛排名73，线上1.466856

# 文件目录
```
|-bert
    |-data # 该文件夹下存储用于获取预训练bert中position embedding和segment embedding的自定义数据
    |-bert_sent.json # 预训练模型，结果位置等信息的配置
    |-run_bert_classifier.py # 保存bert中positiion
|-ckpt_model # 模型参数保存位置
|-config # 各个模型的配置信息
    |-bilstm_nn_col_one_6_max_config.json
    |-data_config.json
    |-feature_config.json
    |-lgb_config.json
    |-transformer_bilstm_col_double_one_5_click_config.json
    |-transformer_bilstm_col_one_8_click_pos_config.json    
|-data
    |-all_train_data # 初赛和复赛合并后的训练数据
    |-test_data # 测试数据，初赛和复赛使用同一份测试数据
    |-train_data # 初赛训练数据
    |-train_final_data # # 复赛训练数据
|-data_preprocess
    |-data_train_test.py # 合并初赛和复赛数据
    |-ml_train_data.py # 生成用户序列数据
    |-train_col_data.py # 生成符合模型的输入数据
    |-train_word2vec.py # 生成向量文件
|-logs # 日志存放位置
|-merge
    |-merge.py # 合并测试集中gender和age的预测label
|-ml_models
    |-get_tfidf_count_features.py # 传统机器学习方法模型，用于之后的stack
    |-get_vector_features.py # 获取用户的向量信息
    |-lgb_model.py # lgb模型
|-models
    |-base_col_double_model.py
    |-base_col_model.py
    |-bilstm_nn_col_one_max.py
    |-transformer_bilstm_col_double_one_click.py
    |-transformer_bilstm_col_one_pos_click.py
|-outputs # 保存对应模型的验证和测试得分
    |-features
        |-age_tfidf_count_stack_cluster_all # 自动生成该目录，用tfidf count，以及传统机器学习方法预测age
        |-gender_tfidf_count_stack_cluster_all # 自动生成该目录，用tfidf count，以及传统机器学习方法预测gender
        |-nn_features_all # 需要手动建立该目录，深度学习模型预测的结果
        |-w2v_features_all # 自动生成该目录，用户的向量信息
|-pictures # 存放神经网络中loss和acc变化曲线图
|-predict_results # 保存对应模型的测试label
|-pretrained_models
    |-bert 
        |-uncased_L-12_H-768_A-12 # 预训练模型bert参数位置
|-submission # 最终预测结果
|-trainers_predictors
    |-train_col_5fold.py # 预测gender
    |-train_col_pos_5fold.py # 预测age
    |-train_col_double_5fold.py # 预测gender和age
    |-train_ml.py
    |-train_stack_ml.py # 预测最终的gender和age
|-user_data
    |-uncased_12_bert_embedding # 保存position embedding和segment embedding
    |-w2v_model # 保存8个向量文件
|-utils
    |-logger.py # 输出日志代码
    |-plot_picture.py # 画曲线图代码
```
## 运行环境 
python 3.5.2, tensorflow-gpu=1.11.0

## 运行顺序
```
0、切换到bert目录，运行python run_bert_classifier.py，得到bert中positiion embedding和segment embedding

1、切换到data_preprocess目录，运行python data_train_test.py，得到初赛和复赛合并后的训练数据

2、在完成 1 后，切换到data_preprocess目录，运行python train_word2vec.py，得到8个字段对应的向量表示

3、在完成 2 后，切换到trainers_predictors目录，运行python train_col_5fold.py，预测gender，
   代码得到的验证和测试得分保存在outputs/bilstm_nn_col_one_6_max/gender中，
   得到的测试集label保存在predict_results/bilstm_nn_col_one_6_max/gender
   
4、在完成 0,2 后，切换到trainers_predictors目录，运行python train_col_pos_5fold.py，预测age，
   代码得到的验证和测试得分保存在outputs/transformer_bilstm_col_one_8_click_pos/age中，
   得到的测试集label保存在predict_results/transformer_bilstm_col_one_8_click_pos/age
   
5、在完成 2 后，切换到trainers_predictors目录，运行python train_col_double_5fold.py，预测gender和age，
   代码得到的验证和测试得分保存在outputs/transformer_bilstm_col_double_one_5_click/gender_age中，
   得到的测试集label保存在predict_results/transformer_bilstm_col_double_one_5_click/gender_age
   
6、在完成 2 后，切换到trainers_predictors目录，运行python train_ml.py，得到用户的embedding表示，以及使用传统机器学习分别预测gender和age
   在使用传统机器学习预测age时，复赛由于时间问题，只得到"advertiser_id", "product_id", "product_category", "industry"对应的age
   
7、将3，4，5得到的验证和测试得分保存到outputs/features/nn_features_all

8、在完成 3,4,5,6,7 后，切换到trainers_predictors目录，运行python train_stack_ml.py，分别预测最终的gender和age，
   预测的测试label分别位于predict_results/lgb_stat_w2v/gender和predict_results/lgb_stat_w2v/age中
   
9、切换到merge目录，运行python merge.py，最终的结果保存于submission中
```
