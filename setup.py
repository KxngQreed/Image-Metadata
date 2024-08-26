from setuptools import setup, find_packages

setup(
    name='ImageMetaData',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'piexif',
    ],
    tests_require=[
        'pytest',
    ],
    entry_points={
        'console_scripts': [
            'load_and_print_exif=imagemetadata.exif_utils:load_and_print_exif',
            'get_exif_by_tag=imagemetadata.exif_utils:get_exif_by_tag',
            'remove_exif=imagemetadata.exif_utils:remove_exif',
            'modify_exif=imagemetadata.exif_utils:modify_exif',
        ],
    },
    author='Your Name',
    author_email='your.email@example.com',
    description='A Python package to manipulate EXIF data in images',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/ImageMetaData',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
