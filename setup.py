import os

script_path = os.path.dirname(os.path.abspath(__file__))

relative_paths = ["processedMedia", "rawMedia", "temp"]

for path in relative_paths:
    new_directory_path = os.path.join(script_path, path)
    try:
        os.mkdir(new_directory_path)
    except OSError as error:
        print(path + " file already exists.")
print("setup completed.")



