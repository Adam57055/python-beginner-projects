# project 15 is a file organiser that organises files based on their extensions.
import os

# Function to organize files based on their extensions
def organize_files(files,ext):
    files_with_ext = [f for f in files if f.endswith(ext)]
    print(f"Files with extension '{ext}':")

    # Create directory for the extension if it doesn't exist
    if not os.path.exists(ext):
        os.makedirs(ext)

    for i,file in enumerate(files_with_ext):
        new_path = os.path.join(ext, file)
        os.rename(file, new_path)   

        print(f"{i+1}. {file} moved to {new_path}")

if __name__ == "__main__":
    files = os.listdir('.')
    extension = input("Enter the file extension to organize (e.g., .txt): ")
    organize_files(files, extension)    
    