import os
import torch
import torch.nn as nn
import torchvision.transforms as transforms
from torchvision import models
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib as np


# Define the model architecture (must match the architecture used during training)
class SkinLesionModel(nn.Module):
    def __init__(self):
        super(SkinLesionModel, self).__init__()

        # Use pre-trained ResNet18 as base model for transfer learning
        model = models.resnet18(pretrained=True)

        # Replace the final fully connected layer
        num_ftrs = model.fc.in_features
        model.fc = nn.Identity()  # Remove the final layer

        self.features = model

        # Add custom classification head
        self.classifier = nn.Sequential(
            nn.Linear(num_ftrs, 512),
            nn.ReLU(),
            nn.Dropout(0.5),
            nn.Linear(512, 128),
            nn.ReLU(),
            nn.Dropout(0.3),
            nn.Linear(128, 1),
            nn.Sigmoid(),
        )

    def forward(self, x):
        x = self.features(x)
        x = self.classifier(x)
        return x


def load_model(model_path):
    """Load the trained model from a saved .pth file"""
    # Determine device
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(f"Using device: {device}")

    # Create a new instance of the model
    model = SkinLesionModel()

    # Load the saved weights
    # If saved on GPU but loading on CPU
    if not torch.cuda.is_available():
        model.load_state_dict(torch.load(model_path, map_location=torch.device("cpu")))
    else:
        model.load_state_dict(torch.load(model_path))

    # Set model to evaluation mode
    model.eval()

    # Move model to appropriate device
    model = model.to(device)

    print(f"Model successfully loaded from {model_path}")
    return model, device


def predict(model_path, image_path):
    """
    Predict whether a skin lesion image is benign or malignant
    Enhanced with better error handling for mobile uploads

    Args:
        model_path (str): Path to the trained model (.pth file)
        image_path (str): Path to the image to classify
    """
    # Check if files exist with detailed error messages
    if not os.path.exists(model_path):
        error_msg = f"Model file not found: {model_path}"
        print(error_msg)
        raise FileNotFoundError(error_msg)

    if not os.path.exists(image_path):
        error_msg = f"Image file not found: {image_path}"
        print(error_msg)
        raise FileNotFoundError(error_msg)

    try:
        # Load model
        model, device = load_model(model_path)
        print(f"Model loaded successfully on {device}")

        # Prepare image transformation (must match training preprocessing)
        transform = transforms.Compose(
            [
                transforms.Resize((224, 224)),  # ResNet standard input size
                transforms.ToTensor(),
                transforms.Normalize(
                    [0.485, 0.456, 0.406], [0.229, 0.224, 0.225]
                ),  # ImageNet stats
            ]
        )

        # Load and transform image with better error handling
        try:
            print(f"Opening image: {image_path}")
            image = Image.open(image_path)

            # Ensure image is in RGB format (handles different mobile camera formats)
            image = image.convert("RGB")
            print(f"Image opened successfully: {image.size} {image.mode}")

            # Create a copy for display
            display_img = image.copy()
        except Exception as e:
            error_msg = f"Error loading image: {str(e)}"
            print(error_msg)
            raise Exception(error_msg)

        # Transform and prepare for model
        try:
            print("Transforming image for model input")
            image_tensor = (
                transform(image).unsqueeze(0).to(device)
            )  # Add batch dimension
            print(f"Image transformed successfully: {image_tensor.shape}")
        except Exception as e:
            error_msg = f"Error transforming image: {str(e)}"
            print(error_msg)
            raise Exception(error_msg)

        # Get prediction
        try:
            print("Running model inference")
            with torch.no_grad():  # Disable gradient calculation
                output = model(image_tensor).item()  # Get single value

            print(f"Raw model output: {output}")
        except Exception as e:
            error_msg = f"Error during model inference: {str(e)}"
            print(error_msg)
            raise Exception(error_msg)

        # Interpret prediction
        pred_class = "malignant" if output > 0.5 else "benign"
        confidence = output if pred_class == "malignant" else 1 - output

        # Display results in terminal
        print(f"Prediction: {pred_class}")
        print(f"Confidence: {confidence:.4f} ({confidence*100:.2f}%)")

        predict_dict = {"class": pred_class, "confidence": f"{confidence*100:.2f}"}

        return predict_dict

    except Exception as e:
        # Catch-all for any unexpected errors
        error_msg = f"Unexpected error in prediction pipeline: {str(e)}"
        print(error_msg)
        raise Exception(error_msg)


if __name__ == "__main__":
    # Define paths
    MODEL_PATH = "D:/MyCode/Blessy projects/Django_COPY/env/proj/app/scripts/skin_lesion_model.pth"
    IMAGE_PATH = (
        "D:/MyCode/Blessy projects/Django_COPY/env/proj/app/scripts/ISIC_0024311.jpg"
    )

    predict(MODEL_PATH, IMAGE_PATH)
