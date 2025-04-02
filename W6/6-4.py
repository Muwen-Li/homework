from PIL import Image,ImageFilter
import matplotlib.pyplot as plt

class ImageProcessor:
    def __init__(self,image_path,params=None):
        self.image=Image.open(image_path)
        self.params=params if params is not None else []

    def process(self):
        raise NotImplementedError("子类必须实现process方法！")

class GrayscaleProcessor(ImageProcessor):#灰度
    def process(self):
        return self.image.convert('L')
    
class ResizeProcessor(ImageProcessor):#裁剪
    def process(self):
        box=[10,10,10+self.params[0],10+self.params[0]]
        return self.image.crop(box)

class BlurProcessor(ImageProcessor):
    def process(self):
        return self.image.filter(ImageFilter.BLUR)

class EdgeProcessor(ImageProcessor):
    def process(self):
        return self.image.filter(ImageFilter.CONTOUR)
    
image_path = r"C:\Users\Lenovo\Desktop\lx.jpg"
gray_processor = GrayscaleProcessor(image_path)
resize_processor = ResizeProcessor(image_path, params=[500])  
blur_processor = BlurProcessor(image_path)
edge_processor = EdgeProcessor(image_path)

gray_image = gray_processor.process()
resize_image = resize_processor.process()
blur_image = blur_processor.process()
edge_image = edge_processor.process()

plt.figure(figsize=(10, 8))

plt.subplot(2, 2, 1)
plt.imshow(gray_image, cmap='gray')

plt.subplot(2, 2, 2)
plt.imshow(resize_image)

plt.subplot(2, 2, 3)
plt.imshow(blur_image)

plt.subplot(2, 2, 4)
plt.imshow(edge_image, cmap='gray')  # 边缘图适合灰度显示

plt.show()

