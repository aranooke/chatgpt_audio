
import openai
import requests
import os

from PIL import Image,ImageDraw,ImageFont;
openai.api_key = "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";

def create_image(text = "cyberpunk cat"):
    response = openai.Image.create(
    prompt=text,
    n=1,
    size="1024x1024"
    )
    return response['data'][0]['url'];



def download_image(url, save_directory):
    # Send a GET request to the URL
    response = requests.get(url)
    
    # Extract the filename from the URL
    filename = "img1.png";
    os.makedirs(save_directory, exist_ok=True)
    # Combine the save directory and filename
    save_path = os.path.join(save_directory, filename)
    
    # Save the image to the specified path
    with open(save_path, 'wb') as file:
        file.write(response.content)
    
    print(f"Image downloaded successfully: {save_path}")

def black_white():
    img = Image.open(os.path.join(os.path.abspath("images"),"img1.png"));
    img.convert('L').save(os.path.join(os.path.abspath("images"),"img1.png"));
def rotate_image(angle):
    img = Image.open(os.path.join(os.path.abspath("images"),"img1.png"));
    img = img.rotate(angle);
    img.save(os.path.join(os.path.abspath("images"),"img1.png"))
def title_image(text):
    img = Image.open("giphy.gif");
    draw = ImageDraw.Draw(img);
    font = ImageFont.truetype("arial.ttf", size=24)  # Specify the font file and size
    position = (img.width // 2,img.height // 2);
    color = (0,0,0);
    draw.text(position,text,font=font,color = color);
    img.save(os.path.join(os.path.abspath("images"),"img1.png"))

# Example usage
# image_url = create_image();
# download_image(image_url, "images")



# print(image_url);