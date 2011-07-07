try:
    from cStringIO import StringIO
except ImportError:
    from StringIO import StringIO
import random

from PIL import Image, ImageDraw

from django.db import models
from django.core.files.uploadedfile import SimpleUploadedFile
from django.utils.hashcompat import sha_constructor

from django.conf import settings

class FramedImageField(models.ImageField):
    """
    Extended ImageField that can resize image before saving it.
    """

    def __init__(self, *args, **kwargs):
        self.width = kwargs.pop('width', None)
        self.height = kwargs.pop('height', None)
        self.border_color = kwargs.pop('border_color', '#666666')
        super(FramedImageField, self).__init__(*args, **kwargs)

    def save_form_data(self, instance, data):
        if data and self.width and self.height:
            content = self.resize_image(data.read(), width=self.width, height=self.height)
            salt = sha_constructor(str(random.random())).hexdigest()[:5]
            fname =  sha_constructor(salt + settings.SECRET_KEY).hexdigest() + '.png'
            data = SimpleUploadedFile(fname, content, data.content_type)
        super(FramedImageField, self).save_form_data(instance, data)

    def resize_image(self, rawdata, width, height):
        """
        Resize image to fit it into (width, height) box.
        """
        image = Image.open(StringIO(rawdata))
        oldw, oldh = image.size
        if oldw != width or oldh != height:
            image = image.resize((width, height), resample=Image.ANTIALIAS)
        draw = ImageDraw.Draw(image)
        draw.rectangle((0, 0, image.size[0]-1, image.size[1]-1), outline=self.border_color)
        draw.rectangle((1, 1, image.size[0]-2, image.size[1]-2), outline='#ffffff')
        del draw

        string = StringIO()
        image.save(string, format='PNG')
        return string.getvalue()