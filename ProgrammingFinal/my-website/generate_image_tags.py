import os

def generateImageTags(folder_path):
    image_tags = []
    for img_file in os.listdir(folder_path):
        if img_file.endswith('.jpg') or img_file.endswith('.png'):
            img_path = os.path.join(folder_path, img_file)
            img_tag = f'<img src="{img_path}" alt="{img_file}">'
            image_tags.append(img_tag)

    return image_tags

if __name__ == "__main__":
    folder_path = 'downloaded_images'
    image_tags = generateImageTags(folder_path)
    with open('index.html', 'a') as index_file:
        index_file.write('\n'.join(image_tags))
