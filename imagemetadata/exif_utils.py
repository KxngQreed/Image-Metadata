import piexif
from piexif import ExifIFD, ImageIFD

def load_and_print_exif(file_path):
    """Load and print EXIF data from an image file."""
    try:
        exif_data = piexif.load(file_path)
        for section, data in exif_data.items():
            print(f"{section}: {type(data)}, {len(data)} entries")
            if isinstance(data, dict):
                for tag, value in data.items():
                    print(f"  Tag: {tag}, Value: {value}")
            else:
                print(f"  Value: {data}")
    except Exception as e:
        print(f"Error loading EXIF data: {e}")

def get_exif_by_tag(file_path, tag_name):
    """Retrieve specific EXIF data by tag name."""
    try:
        exif_data = piexif.load(file_path)
        for section, data in exif_data.items():
            if isinstance(data, dict):
                for tag, value in data.items():
                    tag_label = ExifIFD.get(tag) or ImageIFD.get(tag)
                    if tag_label == tag_name:
                        return value
        return None
    except Exception as e:
        print(f"Error retrieving EXIF data: {e}")
        return None

def remove_exif(file_path):
    """Remove EXIF data from an image."""
    try:
        piexif.remove(file_path)
        print(f"EXIF data removed from {file_path}")
    except Exception as e:
        print(f"Error removing EXIF data: {e}")

def modify_exif(file_path, tag, value):
    """Modify a specific EXIF tag value."""
    try:
        exif_data = piexif.load(file_path)
        exif_data["0th"][tag] = value
        exif_bytes = piexif.dump(exif_data)
        piexif.insert(exif_bytes, file_path)
        print(f"Modified EXIF tag {tag} in {file_path}")
    except Exception as e:
        print(f"Error modifying EXIF data: {e}")
