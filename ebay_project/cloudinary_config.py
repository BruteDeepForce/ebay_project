import cloudinary
import cloudinary.uploader

cloudinary.config(
    cloud_name="your_cloud_name",
    api_key="your_api_key",
    api_secret="your_api_secret",
)

def upload_image(image_file):

    response = cloudinary.uploader.upload(image_file)
    return response['secure_url']  # Return the secure URL of the uploaded image