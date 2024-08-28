# 基于 YOLOv8 的改进策略

## 引言

这是基于 YOLOv8 的改进策略，使用了 MobileNetv4 来改进模型。此方法可以减少模型的参数并提高模型的准确性。

## 使用说明

你只需要加载 `YOLOV8-mobilenet.yaml` 来使用修改后的模型。

## 数据和标签存储结构

![数据和标签存储结构](https://github.com/user-attachments/assets/744d5176-421c-4b36-a453-20f652c750f6)

## 制作你的 .yaml 文件

![制作 .yaml 文件](https://github.com/user-attachments/assets/d1b4a233-5c10-47ec-a798-d8deab227878)

## 用于数据加载的 .yaml 文件

![数据加载的 .yaml 文件](https://github.com/user-attachments/assets/4ed428ba-e9c0-43da-9fb2-9f0f3f836f4a)

## 训练

训练可以通过运行 `train.py` 文件开始。
