# ad-perception-yolo

一个从 0 到 1 的 YOLO 目标检测项目模板：包含环境配置、训练、推理、导出（ONNX）与规范的 GitHub 结构。
目标：用于自动驾驶/机器人方向实习作品集的可复现项目。

## 1. 环境
```bash
python -m venv .venv
# Linux/Mac
source .venv/bin/activate
# Windows (PowerShell)
# .venv\Scripts\Activate.ps1

pip install -U pip
pip install -r requirements.txt
