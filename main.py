import json
from check import creates_categories, creation_json_yolo_to_coco

annotation_directory = r"/kaggle/input/data-training-caries/Data_Training_caries/train/labels"
images_directory = r"/kaggle/input/data-training-caries/Data_Training_caries/train/images"



categorie = ["Stomata"]
creation_json_yolo_to_coco(images_directory,annotation_directory, categories=categorie)



