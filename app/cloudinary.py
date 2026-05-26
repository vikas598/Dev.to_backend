import cloudinary
import cloudinary.uploader
from cloudinary.utils import cloudinary_url
from .config import settings


cloudinary.config(
    cloud_name = settings.cloudinary_cloud_name,
    api_key = settings.cloudinary_api_key,
    api_secret = settings.cloudinary_api_secret,
    secure = True
)

def upload_image(file):
    try:
        result = cloudinary.uploader.upload(file)
        return result['secure_url']
    except Exception as e:
        print(f"Error uploading image: {e}")
        return None
    
def get_image_url(public_id, transformation=None):
    try:
        url, options = cloudinary_url(public_id, transformation=transformation)
        return url  
    except Exception as e:
        print(f"Error generating image URL: {e}")
        return None

