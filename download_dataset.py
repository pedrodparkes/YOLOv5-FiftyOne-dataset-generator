import fiftyone as fo
import config

print(f"Downloading dataset with {config.MAX_SAMPLES} MAX_SAMPLES from OpenImages")
dataset = fo.zoo.load_zoo_dataset(
    config.DATASET_NAME,
    label_types=["detections"],
    classes=config.CLASSES,
    max_samples=config.MAX_SAMPLES,
)

dataset.persistent = True
print("Available persistante datasets")
print(fo.list_datasets())

print("creating classes.txt file")
with open(f"{config.EXPORT_DIR}/classes.txt", "w") as f:
    f.write("\n".join(config.CLASSES))

# dataset.export(
#     EXPORT_DIR,
#     label_field="detections",
#     labels_dir="labels",
#     labels_suffix=".txt",
#     classes="classes.txt",
#     format="yolo",
#     dataset_type=fo.types.YOLOv5Dataset,
# )