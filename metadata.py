import piexif

def load_and_print_exif(file_path):
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

# Replace 'path/to/your/image.jpg' with your actual file path
load_and_print_exif('C:/Users/Reagan/Desktop/code/Image Scanner - Metadata/GRfnnzjWYAAE7Y_.jpeg')