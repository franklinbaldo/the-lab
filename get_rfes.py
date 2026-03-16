import os

rfes_dir = "content/rfes"
all_rfes = [f for f in os.listdir(rfes_dir) if f.endswith('.md')]
print("All RFEs:", all_rfes)
