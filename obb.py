from ultralytics import YOLO

# Load the YOLOv8 model trained for segmentation
model = YOLO("yolov8n-obb.pt")

# Export the model to TensorRT format
model.export(
	format="engine",
	#half=True
		)

# Load the exported TensorRT model
tensorrt_model = YOLO("yolov8n-obb.engine", task='obb')

# Load the image path
image_path = "https://ultralytics.com/images/bus.jpg"

#Run inference 1000 times for the same image
for _ in range(1000):
	result = tensorrt_model(image_path)


