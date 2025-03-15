import os
path = input("Enter a path: ")

if not os.path.exists(path):
    print("No such path exists!")

else:
    directories = [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]
    files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
    all_items = os.listdir(path)
    
    print("\nOnly directories:", directories)
    print("Only files:", files)
    print("Files and directories:", all_items)