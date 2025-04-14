import os
from PIL import Image, ImageEnhance
import random


# Define six distinct augmentations
def rotate_image(img):
    angle = random.randint(-30, 30)  # Random angle between -30 and 30 degrees
    return img.rotate(angle)


def flip_horizontal(img):
    return img.transpose(Image.FLIP_LEFT_RIGHT)


def flip_vertical(img):
    return img.transpose(Image.FLIP_TOP_BOTTOM)


def scale_image(img):
    scale_factor = random.uniform(0.9, 1.1)  # Random scale between 70% and 130%
    w, h = img.size
    new_w, new_h = int(w * scale_factor), int(h * scale_factor)
    return img.resize((new_w, new_h)).resize((w, h))  # Resize back to original size


def adjust_brightness(img):
    enhancer = ImageEnhance.Brightness(img)
    factor = random.uniform(0.7, 1.3)  # Random brightness between 70% and 130%
    return enhancer.enhance(factor)


def add_noise(img):
    noise_factor = 25  # Maximum noise intensity
    img_array = list(img.getdata())  # Extract pixel data as a list

    # Handle grayscale images and color images differently
    if img.mode in ("L", "1"):  # Grayscale or black-and-white images
        noisy_img_array = [
            max(0, min(255, pixel + random.randint(-noise_factor, noise_factor)))
            for pixel in img_array
        ]
    else:  # For RGB or RGBA images
        noisy_img_array = [
            tuple(
                max(0, min(255, channel + random.randint(-noise_factor, noise_factor)))
                for channel in pixel
            )
            for pixel in img_array
        ]

    img.putdata(noisy_img_array)  # Update the image with noisy data
    return img


# Augmentation functions
augmentations = {
    "rotate": rotate_image,
    "flip_lr": flip_horizontal,
    "flip_ud": flip_vertical,
    "scale": scale_image,
    "brightness": adjust_brightness,
    "noise": add_noise,
}


def load_images_with_paths(folder):
    images = []
    for label in os.listdir(folder):  # Iterate through subfolders
        label_path = os.path.join(folder, label)
        if os.path.isdir(label_path):  # Check if it's a subfolder
            for img_file in os.listdir(label_path):  # Iterate through images
                img_path = os.path.join(label_path, img_file)
                try:
                    img = Image.open(img_path)

                    # Handle images with transparency in P mode
                    if img.mode == "P" and "transparency" in img.info:
                        img = img.convert("RGBA")  # Convert to RGBA for transparency
                    elif img.mode != "RGB":
                        img = img.convert("RGB")  # Ensure it's in RGB mode for consistency

                    images.append((img, img_path))  # Store image and its full path
                except Exception as e:
                    print(f"Error loading image {img_path}: {e}")
    return images


# Function to save augmented images
def augment_and_save(images):
    for img, img_path in images:
        folder, file_name = os.path.split(img_path)
        file_base, file_ext = os.path.splitext(file_name)

        print(f"Processing file: {img_path}")

        # Apply each augmentation
        for aug_name, augmenter in augmentations.items():
            augmented_img = augmenter(img.copy())  # Apply augmentation
            augmented_file_name = f"{file_base}_{aug_name}{file_ext}"  # New filename
            augmented_img_path = os.path.join(folder, augmented_file_name)

            # Save augmented image
            augmented_img.save(augmented_img_path)
            print(f"Saved: {augmented_img_path}")


# Path to your dataset
dataset_path = "dataset_new/train"  # Replace with the path to your dataset

# Load and augment images
print("Loading images...")
images = load_images_with_paths(dataset_path)
print(f"Loaded {len(images)} images.")

print("Starting augmentation...")
augment_and_save(images)
print("Augmentation complete.")
