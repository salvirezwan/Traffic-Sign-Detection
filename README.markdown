# Traffic Sign Detection

This project features a YOLOv8-based model for detecting and classifying traffic signs in images, integrated with a Gradio interface for interactive use. Upload an image to view detected traffic signs with bounding boxes and labels, powered by a model trained on the German Traffic Sign Recognition Benchmark (GTSRB) dataset. The model is deployed on Hugging Face Spaces at [https://huggingface.co/spaces/salvirezwan/Traffic-Sign-Detection](https://huggingface.co/spaces/salvirezwan/Traffic-Sign-Detection).

## Usage

1. **Upload an Image**: Use the Gradio interface to upload an image containing traffic signs.
2. **View Results**: The app displays the image with bounding boxes and labels for detected traffic signs.
3. **Confidence Threshold**: Detections are filtered at a confidence score of 0.5.

## Model Details

- **Architecture**: YOLOv8 nano
- **Dataset**: GTSRB, 43 classes, ~39,209 training images
- **Training**: 50 epochs, 640x640 image size, 80% training / 20% validation split
- **Validation Metrics** (final epoch): Details provided in `results.csv` file
- **Platform**: Trained in Google Colab with T4 GPU
- **Model File**: `traffic_sign_detection.pt`

## Project Insights

- **Challenges**:
- Managed Google Colab runtime limits by saving checkpoints (e.g., `epoch5.pt`) to Google Drive for resuming training.
- **Use Case**: Suitable for real-time traffic sign detection in autonomous driving or driver assistance systems.


## Deployment

- **Hugging Face Space**: Hosted at [https://huggingface.co/spaces/salvirezwan/Traffic-Sign-Detection](https://huggingface.co/spaces/salvirezwan/Traffic-Sign-Detection).
- **Local Testing**: Use `python app.py` with the required dependencies in `requirements.txt`.

## Setup Instructions

1. Clone the repository:
```bash
git clone https://github.com/salvirezwan/Traffic-Sign-Detection.git
cd Traffic-Sign-Detection
```
2. Install dependencies:
```bash
pip install -r requirements.txt
```
3. Run the Gradio app:
```bash
python app.py
```
5. Upload an image via the local Gradio interface.

## Future Improvements

- Retrain with augmented data (e.g., multiple signs, varied backgrounds) for better generalization.
- Explore YOLOv8 small or medium for improved accuracy.


