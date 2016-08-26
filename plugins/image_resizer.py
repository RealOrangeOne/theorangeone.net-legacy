import os
from PIL import Image
from resizeimage import resizeimage

OUTPUT_DIR = os.path.realpath('theme/static/build/img')
ORIGINAL_IMAGE_PATH = os.path.realpath('content/assets/img/logo-transparent.png')

FAVICON_SIZES = (
    (16, 16),
    (32, 32),
    (96, 96),
    (128, 128),
    (196, 196)
)

APPLE_SIZES = (
    (152, 152),
    (144, 144),
    (120, 120),
    (114, 114),
    (72, 72),
    (60, 60),
    (57, 57)
)


def merge_dicts(*dict_args):
    result = {}
    for dictionary in dict_args:
        result.update(dictionary)
    return result


def get_size_string(w, h):
    return "{0}x{1}".format(w, h)


def build_apple_filenames():
    return {s: "apple-touch-icon-{0}.png".format(get_size_string(*s)) for s in FAVICON_SIZES}


def build_favicon_filenames():
    return {s: "favicon-{0}.png".format(get_size_string(*s)) for s in APPLE_SIZES}


def get_all_files():
    favicon_filenames = build_favicon_filenames()
    apple_filenames = build_apple_filenames()
    return merge_dicts(favicon_filenames, apple_filenames)


def generate():
    print("Removing old files...")
    for size, image_file in get_all_files().items():
        try:
            os.remove(os.path.join(OUTPUT_DIR, image_file))
        except FileNotFoundError:
            continue

    with open(ORIGINAL_IMAGE_PATH, 'rb') as original_image_file:
        with Image.open(original_image_file) as original_image:
            for size, image_name in get_all_files().items():
                new_image = resizeimage.resize_contain(original_image, size)
                new_image.save(os.path.join(OUTPUT_DIR, image_name), original_image.format)

    favicon_image_details = [('icon', get_size_string(*size), filename) for size, filename in build_favicon_filenames().items()]
    apple_image_details = [('apple-touch-icon-precomposed', get_size_string(*size), filename) for size, filename in build_apple_filenames().items()]

    return favicon_image_details + apple_image_details
