import os

if __name__ == "__main__":
    original_path = "images"
    new_path = "data_"
    
    os.makedirs(new_path, exist_ok=True)
    
    folder_names = os.listdir(original_path)

    for i, folder_name in enumerate(folder_names):
        original_folder_path = os.path.join(original_path, folder_name)
        new_folder_path = os.path.join(new_path, f"case_{i}")
        
        os.makedirs(new_folder_path, exist_ok=True)

        images_name = os.listdir(original_folder_path)

        for j, image_name in enumerate(images_name):
            original_image_path = os.path.join(original_folder_path, image_name)
            new_image_path = os.path.join(new_folder_path, f"case_{i}__image_{j}.jpg")
            
            os.rename(original_image_path, new_image_path)
