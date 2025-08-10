import gradio as gr
from ultralytics import YOLO
from PIL import Image

# Load the trained model
model = YOLO('traffic_sign_detection.pt')

# Define the prediction function
def predict(image):
    results = model.predict(image, conf=0.5)
    output_img = results[0].plot()  # Draw bounding boxes and labels
    return Image.fromarray(output_img)

# Create Gradio interface
iface = gr.Interface(
    fn=predict,
    inputs=gr.Image(type="pil", label="Upload an Image"),
    outputs=gr.Image(type="pil", label="Detected Traffic Signs"),
    title="Traffic Sign Detection",
    description="Upload an image to detect traffic signs using YOLOv8."
)

# Launch the interface (handled by Hugging Face Spaces)
iface.launch()