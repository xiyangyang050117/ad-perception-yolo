from ultralytics import YOLO

def main():
    model = YOLO("runs/train_coco8/weights/best.pt")
    # 直接用 ultralytics 提供的示例图像
    results = model.predict(source="https://ultralytics.com/images/bus.jpg", imgsz=640, conf=0.25)
    for r in results:
        print("Saved to:", r.save_dir)

if __name__ == "__main__":
    main()
