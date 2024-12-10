# Google Image Downloader

A Python script that automatically downloads and organizes images from Google Images based on predefined categories and search terms. The script creates a structured directory on your Desktop and sorts downloaded images into their respective category folders.

## Features

- Automated image downloading from Google Images
- Organized folder structure by categories
- Automatic file renaming to prevent conflicts
- Error handling and recovery
- Progress tracking and reporting
- Cleanup of temporary download directories

## Prerequisites

- Python 3.x
- `simple-image-download` library

## Installation

1. Install the required package:
```bash
pip install simple-image-download
```

2. Clone or download this script to your local machine

## Configuration

Edit the `categories` dictionary in the script to define your search terms:

```python
categories = {
    'Category': [
        'Item 1',
        'Item 2',
        'Item 3',
        'Item 4',
        'Item 5'
    ]
}
```

## Directory Structure

The script creates the following directory structure on your Desktop:
```
Google Image Downloader/
├── Category/
│   ├── Item1_image1.jpg
│   ├── Item1_image2.jpg
│   ├── Item2_image1.jpg
│   └── ...
```

## Usage

1. Configure your categories and search terms in the script
2. Run the script:
```bash
python image_downloader.py
```

## How It Works

1. Creates a main directory on the Desktop called "Google Image Downloader"
2. For each category and search term:
   - Downloads images from Google Images
   - Creates category-specific subdirectories
   - Moves and renames images to appropriate folders
   - Cleans up temporary download directories
3. Provides progress updates during execution

## Error Handling

The script includes comprehensive error handling for:
- Network issues
- File system operations
- Invalid search terms
- File moving/copying operations

## Rate Limiting

- Includes a 2-second delay between searches to prevent overloading
- Downloads up to 100 images per search term

## Limitations

- Depends on Google's image search availability
- May be affected by Google's rate limiting
- Image quality and relevance depend on search terms
- Some downloads may fail due to removed or inaccessible images

## Best Practices

1. Use specific search terms for better results
2. Monitor the download process for any errors
3. Verify downloaded images for relevance
4. Maintain reasonable category and search term counts

## Troubleshooting

If you encounter issues:
1. Check your internet connection
2. Verify write permissions on Desktop
3. Ensure all directories are accessible
4. Check console output for specific error messages

## Contributing

Feel free to submit issues and enhancement requests!

## License

[Specify your license here]
