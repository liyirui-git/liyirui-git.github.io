# Learning Attention-based Embeddings for Relation Prediction in Knowledge Graphs

### 论文复现

论文的代码在GitHub可以找到：https://github.com/deepakn97/relationPrediction

在实验室ella（i9-9900 + GTX 2080Ti）上的运行结果：

- WordNet

Current iteration time 1379.8727445602417
Stats for replacing head are ->
Current iteration Hits@100 are 0.7065663474692202
Current iteration Hits@10 are 0.5629274965800274
Current iteration Hits@3 are 0.466484268125855
Current iteration Hits@1 are 0.3508891928864569
Current iteration Mean rank 2471.312585499316
Current iteration Mean Reciprocal Rank 0.425575541927745

Stats for replacing tail are ->
Current iteration Hits@100 are 0.737688098495212
Current iteration Hits@10 are 0.594733242134063
Current iteration Hits@3 are 0.4945280437756498
Current iteration Hits@1 are 0.36046511627906974
Current iteration Mean rank 1573.5516415868674
Current iteration Mean Reciprocal Rank 0.4447488848113082

Averaged stats for replacing head are ->
Hits@100 are 0.7065663474692202
Hits@10 are 0.5629274965800274
Hits@3 are 0.466484268125855
Hits@1 are 0.3508891928864569
Mean rank 2471.312585499316
Mean Reciprocal Rank 0.425575541927745

Averaged stats for replacing tail are ->
Hits@100 are 0.737688098495212
Hits@10 are 0.594733242134063
Hits@3 are 0.4945280437756498
Hits@1 are 0.36046511627906974
Mean rank 1573.5516415868674
Mean Reciprocal Rank 0.4447488848113082

Cumulative stats are ->
Hits@100 are 0.7221272229822161
Hits@10 are 0.5788303693570451
Hits@3 are 0.4805061559507524
Hits@1 are 0.35567715458276333
Mean rank 2022.4321135430916
Mean Reciprocal Rank 0.4351622133695266

- Freebase

Current iteration time 1022.5329549312592
Stats for replacing head are ->
Current iteration Hits@100 are 0.7704276347979254
Current iteration Hits@10 are 0.5673255700166356
Current iteration Hits@3 are 0.45581759467658284
Current iteration Hits@1 are 0.35844994617868675
Current iteration Mean rank 241.34342890693804
Current iteration Mean Reciprocal Rank 0.42902612382184857

Stats for replacing tail are ->
Current iteration Hits@100 are 0.8045797044720618
Current iteration Hits@10 are 0.6071533418142675
Current iteration Hits@3 are 0.4882082395537724
Current iteration Hits@1 are 0.3831588218025247
Current iteration Mean rank 182.3465114003327
Current iteration Mean Reciprocal Rank 0.4582423684068296

Averaged stats for replacing head are ->
Hits@100 are 0.7704276347979254
Hits@10 are 0.5673255700166356
Hits@3 are 0.45581759467658284
Hits@1 are 0.35844994617868675
Mean rank 241.34342890693804
Mean Reciprocal Rank 0.42902612382184857

Averaged stats for replacing tail are ->
Hits@100 are 0.8045797044720618
Hits@10 are 0.6071533418142675
Hits@3 are 0.4882082395537724
Hits@1 are 0.3831588218025247
Mean rank 182.3465114003327
Mean Reciprocal Rank 0.4582423684068296

Cumulative stats are ->
Hits@100 are 0.7875036696349936
Hits@10 are 0.5872394559154516
Hits@3 are 0.4720129171151776
Hits@1 are 0.3708043839906057
Mean rank 211.84497015363536
Mean Reciprocal Rank 0.4436342461143391

要注意的一点是，KBAT在WN18RR上的效果要差于FB15K-237，原因是受到了TransE的模型的制约。



