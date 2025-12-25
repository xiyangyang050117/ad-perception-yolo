from ultralytics import YOLO

def main():
    # 官方自带的超小示例数据集，首次跑通最省事
    # 会自动下载 coco8（很小）
    model = YOLO("weights/yolov8n.pt")# 轻量模型，适合入门/笔记本
    model.train(
        data="coco8.yaml",
        epochs=20,
        imgsz=640,
        batch=16,
        project="runs",
        name="train_coco8"
    )

if __name__ == "__main__":
    main()
