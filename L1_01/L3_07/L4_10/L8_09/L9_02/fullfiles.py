import os

NUM_FILES = 1087
BASE_DIR = "MegaProjectToUpload"

def create_main_readme():
    return f"""
# 🌌 THE 1087-FILE MEGA PROJECT 🌌
## Status: Ready for Upload to GitHub

This repository contains {NUM_FILES} files generated programmatically to simulate an extremely large and complex system architecture.

**Goal:** Simulate deep architectural complexity using file distribution.
**Target Function:** `process_quantum_state`
"""

def create_core_logic(index):
    return f"""// File ID: {index:04d}
// Architecture Layer: Deep Nesting
function process_quantum_state_{index}(inputData) {{
    // Simulating deep learning calculations using pseudo-random outputs
    let result = inputData * (1.000001 + (Math.random() * 0.0001));
    
    if (result > 5000) {{
        console.log(`[ID {index}] High energy state detected.`);
    }}
    
    return result / {NUM_FILES};
}}
// End of module {index}
"""

os.makedirs(BASE_DIR, exist_ok=True)

with open(os.path.join(BASE_DIR, "README.md"), 'w') as f:
    f.write(create_main_readme())

for i in range(1, NUM_FILES + 1):
    depth = (i % 10) + 1
    path_parts = [f"L{k}_{((i + k*3) % 100):02d}" for k in range(depth)]
    current_dir = os.path.join(BASE_DIR, *path_parts)
    os.makedirs(current_dir, exist_ok=True)
    
    filename = f"module_{i:04d}.js"
    file_path = os.path.join(current_dir, filename)
    
    with open(file_path, 'w') as f:
        f.write(create_core_logic(i))

print(f"✅ УСПЕХ! Создано {NUM_FILES} файлов в папке '{BASE_DIR}'.")
