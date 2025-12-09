import torch
from torch.utils.data import Dataset
from torchvision import transforms
from PIL import Image
import os

class LFWDataset(Dataset):
    def __init__(
        self,
        faces_folder,
        smiling_labels_file,
        non_smiling_labels_file,
        transform=None
    ):
        self.faces_folder = faces_folder
        self.transform = transform

        # Leer archivo de caras sonriendo
        smiling_files = []
        with open(smiling_labels_file, "r") as f:
            for line in f:
                name = line.strip()
                if not name:
                    continue
                if name.endswith("list.txt") or name.endswith("listt.txt"):
                    continue
                name = name.replace(".jpg", ".ppm")
                name = os.path.basename(name)
                smiling_files.append(name)

        # Leer archivo de caras NO sonriendo
        non_smiling_files = []
        with open(non_smiling_labels_file, "r") as f:
            for line in f:
                name = line.strip()
                if not name:
                    continue
                if name.endswith("list.txt") or name.endswith("listt.txt"):
                    continue
                name = name.replace(".jpg", ".ppm")
                name = os.path.basename(name)
                non_smiling_files.append(name)

        self.image_paths = []
        self.labels = []

        # Sonriendo (1)
        for fname in smiling_files:
            path = os.path.join(self.faces_folder, fname)
            if os.path.isfile(path):
                self.image_paths.append(path)
                self.labels.append(1)

        # No sonriendo (0)
        for fname in non_smiling_files:
            path = os.path.join(self.faces_folder, fname)
            if os.path.isfile(path):
                self.image_paths.append(path)
                self.labels.append(0)

    def __len__(self):
        return len(self.image_paths)   # <--- NO PUEDE SER None

    def __getitem__(self, idx):
        image_path = self.image_paths[idx]
        label = self.labels[idx]

        image = Image.open(image_path).convert("RGB")

        if self.transform:
            image = self.transform(image)

        label = torch.tensor(label, dtype=torch.long)
        return image, label