from ultralytics import YOLO
import sys

def run_inference(model_path, source, conf=0.25):
    model = YOLO(model_path)
    model.predict(source=source, conf=conf, save=True)

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('Usage: python inference.py <model_path> <source_images_folder> [conf]')
    else:
        run_inference(sys.argv[1], sys.argv[2], float(sys.argv[3]) if len(sys.argv)>3 else 0.25)
