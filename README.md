# 🚀 Space Station Safety Detection

AI-powered object detection system to identify **critical safety equipment** inside space station environments.  
Built for the **HackWithHyderabad – Duality Problem Statement**.

---

## Usage

### Training (run on GPU if available)
```bash
# baseline training (YOLOv8n)
yolo train model=yolov8n.pt data=data/data.yaml epochs=20 imgsz=640 batch=16 device=0 augment=True

# if no GPU is available, use CPU (very slow)
yolo train model=yolov8n.pt data=data/data.yaml epochs=5 imgsz=416 batch=4 device=cpu augment=False
```

### Validation (compute metrics & plots)
```bash
yolo val model=artifacts/best.pt data=data/data.yaml plots=True
```

### Prediction / Inference (save annotated images)
```bash
yolo predict model=artifacts/best.pt source=dataset/val/images save=True conf=0.25
```

> **Note:** set `device=0` only if your runtime has a GPU (Colab: Runtime → Change runtime type → GPU). If `torch.cuda.is_available()` is `False`, use `device=cpu`.

---

## Quick Results (example)
- Precision: **0.85**  
- Recall: **0.50**  
- mAP@0.5: **0.576**  
- mAP@0.5:0.95: **0.454**

---

## Example predictions 

![Prediction 1](artifacts/predictions/000001873_light_unclutter.jpg)
![Prediction 2](artifacts/predictions/000001864_light_unclutter.jpg)

---

## Repo layout
```
repo/
├─ data/data.yaml
├─ notebooks/train_colab.ipynb
├─ src/inference.py
├─ artifacts/              # best.pt, sample predictions, plots (kept on Drive or in small subset here)
├─ requirements.txt
└─ README.md
```
