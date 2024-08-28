#coding:utf-8
# -*- coding: utf-8 -*-
# @Author  : NaiChuan
# @Time    : 2024/8/28 13:45
# @File    : train.py
# @Software: PyCharm

from ultralytics import YOLO

if __name__ == '__main__':
    model = YOLO('ultralytics/cfg/models/v8/c2f_Faster_yolov8.yaml')
    # model.load('yolov8n.pt') # loading pretrain weights
    # print(model)
    results=model.train(data='yourdata_dir',
                        epochs=300,#训练轮数
                        imgsz=400,#输入图像大小
                        val=True,#是否进行验证
                        # lr0=0.012,#学习率设置
                        patience=0,#为0是取消早停，0-300是设置早停
                        device=0,#运行设备
                        # batch=64,#当模型较大的时候不设置batch，让它默认防止溢出
                        verbose=True, #看到更多训练信息
                        name='your_results_dir', #指定结果保存的文件夹名称,记得修改为自己的
                        # close_mosaic=0, #关闭moasic数据增强
                        deterministic=False #随机因子的作用，默认为True
                        )
