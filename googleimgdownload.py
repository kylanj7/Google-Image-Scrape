from simple_image_download import simple_image_download as simp
import os
import time
import shutil

# Initialize the downloader
response = simp.simple_image_download

# Setup base directory on Desktop
desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop', 'Google Image Downloader')
if not os.path.exists(desktop_path):
    os.makedirs(desktop_path)

# Categories and search terms
categories = {
    'Category': [
        'Item 1',
        'Item 2',
        'Item 3',
        'Item 4',
        'Item 5'
}

def download_and_organize_images():
    for category, searches in categories.items():
        print(f"\nProcessing category: {category}")
        category_path = os.path.join(desktop_path, category)
        
        # Create category directory
        if not os.path.exists(category_path):
            os.makedirs(category_path)
        
        for search in searches:
            print(f"\nDownloading images for: {search}")
            try:
                # Download images (100 per search term to ensure we get enough)
                response().download(search, limit=100)
                
                # Move files to category folder
                download_path = os.path.join(os.getcwd(), 'simple_images', search)
                if os.path.exists(download_path):
                    for filename in os.listdir(download_path):
                        if filename.endswith(('.jpg', '.jpeg', '.png')):
                            src_path = os.path.join(download_path, filename)
                            dst_path = os.path.join(category_path, f"{search}_{filename}")
                            try:
                                shutil.move(src_path, dst_path)
                            except Exception as e:
                                print(f"Error moving file {filename}: {str(e)}")
                    
                    # Clean up download directory
                    try:
                        shutil.rmtree(download_path)
                    except Exception as e:
                        print(f"Error cleaning up directory: {str(e)}")
                
                print(f"Completed downloading images for: {search}")
                time.sleep(2)  # Small delay between searches
                
            except Exception as e:
                print(f"Error processing {search}: {str(e)}")
                continue
        
        # Count images in category
        num_images = len([f for f in os.listdir(category_path) if f.endswith(('.jpg', '.jpeg', '.png'))])
        print(f"\nCompleted {category} with {num_images} images")

if __name__ == "__main__":
    print("Starting download process...")
    
    # Install required keywords first
    try:
        response().download(keywords="test", limit=1)
    except Exception as e:
        print(f"Initial setup error: {str(e)}")
    
    # Start the main download process
    download_and_organize_images()
    
    print("\nDownload complete! Check the 'Google Image Downloader' folder on your Desktop.")
