from ultralytics import YOLO

# Load the YOLOv8 model
model = YOLO("yolov8n.pt")

# Export the model to TensorRT format
model.export(
	format="engine",
	#half=True
	#data = "coco.yaml"
		)

# Load the exported TensorRT model
tensorrt_model = YOLO("yolov8n.engine", task='detect')

# Load the image path
image_path = "https://ultralytics.com/images/bus.jpg"

#Run inference 1000 times for the same image
for _ in range(1000):
	result = tensorrt_model(image_path)
	
    
    
