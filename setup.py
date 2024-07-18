import os
import shutil

def setup_dataset():
    source_path = r'D:\ML_DS_DEVOP\PlacedBasedIRS\dataset.txt'
    destination_dir = os.path.join('PlacedBasedIRS', 'artifacts')
    destination_path = os.path.join(destination_dir, 'dataset.txt')

    # Create the artifacts directory if it doesn't exist
    os.makedirs(destination_dir, exist_ok=True)

    # Copy the dataset.txt file to the artifacts directory
    shutil.copyfile(source_path, destination_path)

    print(f"dataset.txt has been copied to {destination_path}")

if __name__ == "__main__":
    setup_dataset()
