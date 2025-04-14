import os
import shutil

# Define paths
source_folder1 = "dataset_new/train"  # First source folder
source_folder2 = "second_dataset"   # Second source folder
destination_folder = "new_dataset" # Destination folder

# Ensure destination exists
os.makedirs(destination_folder, exist_ok=True)

# Get all unique folder names from both sources
subfolders1 = set(os.listdir(source_folder1))
subfolders2 = set(os.listdir(source_folder2))
all_subfolders = subfolders1.union(subfolders2)

# Merge the folders
for folder in all_subfolders:
    source_path1 = os.path.join(source_folder1, folder)
    source_path2 = os.path.join(source_folder2, folder)
    dest_path = os.path.join(destination_folder, folder)

    # Create destination folder
    os.makedirs(dest_path, exist_ok=True)

    # Copy files from source_folder1
    if os.path.exists(source_path1):
        for file_name in os.listdir(source_path1):
            shutil.copy(os.path.join(source_path1, file_name), os.path.join(dest_path, file_name))

    # Copy files from source_folder2
    if os.path.exists(source_path2):
        for file_name in os.listdir(source_path2):
            shutil.copy(os.path.join(source_path2, file_name), os.path.join(dest_path, file_name))

print("✅ Merging complete! Check the 'merged_dataset' folder.")
