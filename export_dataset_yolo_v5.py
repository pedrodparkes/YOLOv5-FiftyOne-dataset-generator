import fiftyone as fo
import os
import yaml
import config


print("creating classes.txt file")
with open(f"{config.EXPORT_DIR}/classes.txt", "w") as f:
    for item in config.CLASSES:
        f.write(str(item) + "\n")

print("Available persistent datasets")
print(fo.list_datasets())

print("Load your FiftyOne dataset")
dataset = fo.load_dataset(name=f"{config.DATASET_NAME}-{config.MAX_SAMPLES}")

# # Load your FiftyOne dataset
# DATASET_TYPE = fo.types.dataset_types.OpenImagesV7Dataset
# dataset = fo.Dataset.from_dir(config.DATASET_DIR, \
#                               dataset_type=DATASET_TYPE)

# Specify the directory for the YOLO-formatted labels
yolo_labels_dir = f"{config.EXPORT_DIR}/labels"
os.makedirs(yolo_labels_dir, exist_ok=True)

# EXPORTING YALOv5
label_field = "ground_truth"  # for example

# The splits to export
splits = ["train", "validation", "test"]

# All splits must use the same classes list
classes = config.CLASSES

# The dataset or view to export
# We assume the dataset uses sample tags to encode the splits to export
# dataset_or_view = fo.Dataset(...)

print("Export the splits")
for split in splits:
    split_view = dataset.match_tags(split)
    split_view.export(
        export_dir=config.EXPORT_DIR,
        dataset_type=fo.types.YOLOv5Dataset,
        label_field=label_field,
        split=split,
        classes=classes,
    )
print("Export the splits Done")

print(f"fix {config.EXPORT_DIR}/dataset.yaml file")
with open(f'{config.EXPORT_DIR}/dataset.yaml', 'r') as file:
    data = yaml.safe_load(file)

# Replace "validation" with "huy"
if 'validation' in data:
    data['val'] = data.pop('validation')

# Save the updated YAML file
with open(f'{config.EXPORT_DIR}/dataset.yaml', 'w') as file:
    yaml.dump(data, file)
