import pytest
from imagemetadata import load_and_print_exif, get_exif_by_tag, remove_exif, modify_exif

# Sample image path (You would typically use a test image stored in your test directory)
SAMPLE_IMAGE_PATH = 'tests/sample.jpg'

def test_load_and_print_exif(capfd):
    """Test load_and_print_exif function."""
    load_and_print_exif(SAMPLE_IMAGE_PATH)
    out, err = capfd.readouterr()
    assert "0th" in out
    assert "Exif" in out

def test_get_exif_by_tag():
    """Test get_exif_by_tag function."""
    value = get_exif_by_tag(SAMPLE_IMAGE_PATH, 'DateTime')
    assert value is not None

def test_remove_exif():
    """Test remove_exif function."""
    remove_exif(SAMPLE_IMAGE_PATH)
    value = get_exif_by_tag(SAMPLE_IMAGE_PATH, 'DateTime')
    assert value is None

def test_modify_exif():
    """Test modify_exif function."""
    modify_exif(SAMPLE_IMAGE_PATH, 306, '2024:08:23 12:34:56')  # Tag 306 corresponds to DateTime
    value = get_exif_by_tag(SAMPLE_IMAGE_PATH, 'DateTime')
    assert value == b'2024:08:23 12:34:56'
