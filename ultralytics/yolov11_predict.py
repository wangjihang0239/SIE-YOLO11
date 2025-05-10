from ultralytics import YOLO
# 加载预训练的 YOLOv11n 模型
model = YOLO('yolo11n.pt')
 #更改为自己的图片路径
# 运行推理，并附加参数
model.predict(source = r'D:\迅雷下载\VOCdevkit\VOC2012\JPEGImages', save=True)