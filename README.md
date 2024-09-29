# 3DScan To VFace

使3DScan store提供的全身模型能使用VFace的脸部贴图

## 用法

1. 将 3DScan store 提供的全身模型导入maya，选中该模型，运行cut.mel中的脚本。完成后导出该模型为3DScan_cut.obj（后续main.py依靠obj的行号变换UV数据，因此请不要做多余步骤以免引起行号错误）。
2. 下载final_uv_data.json和main.py至步骤1的同一目录，运行main.py
3. 新生成的3DScan_processed.obj即是最终结果