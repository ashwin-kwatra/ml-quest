import pandas as pd
import matplotlib.pyplot as plt
# 1. Load your custom dataset
df = pd.read_csv('muscle_progress.csv')

# 2. Print the first few rows to the console
print("--- Raw Dataset ---")
print(df.head())
print("\n")

# 3. Prove Matplotlib is working by plotting your weight over time
plt.plot(df['day'], df['weight_kg'], marker='o', linestyle='-', color='b')
plt.title('Weight Progression (First 4 Days)')
plt.xlabel('Day')
plt.ylabel('Weight (kg)')
plt.grid(True)
plt.show()

import torch

# Check if PyTorch can see your NVIDIA GPU
is_gpu_available = torch.cuda.is_available()

print(f"Is CUDA active and ready? {is_gpu_available}")
if is_gpu_available:
    print(f"GPU Name: {torch.cuda.get_device_name(0)}")