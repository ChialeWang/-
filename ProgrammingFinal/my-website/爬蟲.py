import os
import requests
from bs4 import BeautifulSoup

def saveImage(url, folder_path):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    pictures = soup.find_all(class_="manga-list-2-cover-img")
    
    # Create the folder if it does not exist
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    
    for i, picture in enumerate(pictures):
        img_url = picture.get('src')
        # Handle relative URLs
        if img_url.startswith('//'):
            img_url = 'https:' + img_url
        elif img_url.startswith('/'):
            img_url = url + img_url
        
        # Get the image content
        img_data = requests.get(img_url).content
        
        # Save the image
        img_name = os.path.join(folder_path, f'image_{i + 1}.jpg')
        with open(img_name, 'wb') as img_file:
            img_file.write(img_data)
        print(f'Saved {img_name}')

url = "https://www.manhuaren.com/manhua-list-tag27-st2/?fbclid=IwAR3udOWUeHTpvM06nz_oSxcZZteO8I3LR-db3c2fZnvIekhw2KARSSLnTCY"
folder_path = 'downloaded_images'
saveImage(url, folder_path)
