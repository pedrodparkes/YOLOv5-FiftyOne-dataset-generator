#### This simple repo aimed to help you collect your first dataset from open-dataset zoo 
(like [Google Open-Images-v7](https://storage.googleapis.com/openimages/web/index.html)),
#### Export Dataset to YOLOv5 format, Train YOLO and test the model on Luxonis OAK-D camera

#### Datasets, available in [fuftyone detasets](https://docs.voxel51.com/user_guide/dataset_zoo/datasets.html)

### 1. Prepare dataset
1. Edit config.py
2. Download images from open-images-v7:
```shell
python download_dataset.py
```

### 2. Export Dataset to YOLOv5 format
```shell
python export_dataset_yolo_v5.py
```

dataset.yaml example structure:
```yaml
train: /home/ubuntu/train/dataset_yolo/images/train
val: /home/ubuntu/train/dataset_yolo/images/validation
test: /home/ubuntu/train/dataset_yolo/images/test
nc: 2  # Number of classes (change to match your number of classes)
names: /home/ubuntu/train/dataset_yolo/classes.txt
```

### 3. Train the model
```shell
git clone https://github.com/ultralytics/yolov5.git
python train.py --img 416 --batch 32 --epochs 1 --data /home/ubuntu/train/dataset_yolo/dataset.yaml --weights yolov5s.pt
```

### 4. Grab the results:
```shell
rsync -avz frod:/home/ubuntu/train/yolov5/runs/train/exp9/weights/best.pt ~/Desktop
```

### 5. Convert results with [Luxonis Model Converter](https://tools.luxonis.com/)

### 6. Test the model on OAK-D Device
```shell
git clone git@github.com:luxonis/depthai-experiments.git
cp ~/Downloads/model/*  depthai-experiments/gen2-yolo/device-decoding/model/
```

### 7. Start the model on OAK-D
```shell
python main_api.py \
  --config model/1000best/best.json  \
  --model model/1000best/best_openvino_2022.1_6shave.blob
```