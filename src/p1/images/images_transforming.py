from typing import List
from PIL import Image, ImageEnhance


class Transform:
    @staticmethod
    def transform(image: Image) -> Image:
        pass


class CropTransform(Transform):
    size_x: int
    size_y: int

    def __init__(self, size_x: int, size_y: int):
        self.size_x = size_x
        self.size_y = size_y
        
    def transform(self, image: Image) -> Image:
        width, height = image.size

        width /= 2
        height /= 2
        size_x = self.size_x / 2
        size_y = self.size_y / 2

        area = (width - size_x, height - size_y, width + size_x, height + size_y)

        return image.crop(box=area)


class ResizeTransform(Transform):
    percent_x: int
    percent_y: int

    def __init__(self, percent_x: int, percent_y: int = None):
        self.percent_x = percent_x
        self.percent_y = percent_y

    def transform(self, image: Image) -> Image:
        width, height = image.size
        change_x = round(self.percent_x / 100 * width)
        change_y = round(self.percent_y / 100 * height) if self.percent_y else None

        if not change_y:
            image = image.resize((change_x, change_x), Image.ANTIALIAS)
        else:
            image = image.resize((change_x, change_y), Image.ANTIALIAS)

        return image


class BrightnessTransform(Transform):
    brightness: int

    def __init__(self, brightness: int):
        self.brightness = brightness
        
    def transform(self, image: Image) -> Image:
        enhancer = ImageEnhance.Brightness(image)
        return enhancer.enhance(self.brightness)


class Transformer:
    transformers = List[Transform]

    def __init__(self, transformers: List[Transform]) -> None:
        self.transformers = transformers

    def batch_transform(self, images):
        transformed_images = []
        for img in images:
            for trans in self.transformers:
                img = trans.transform(img)
            transformed_images.append(img)

        return transformed_images


if __name__ == "__main__":
    image = Image.open('image.jpeg')
    image2 = Image.open('image2.jpeg')

    crop_transformer = CropTransform(size_x=500, size_y=500)
    resize_transformer = ResizeTransform(percent_x=50)
    brightness_transformer = BrightnessTransform(brightness=0.5)

    transformer = Transformer([crop_transformer, resize_transformer, brightness_transformer])
    images = transformer.batch_transform([image, image2])
    
    for img in images:
        img.show()
