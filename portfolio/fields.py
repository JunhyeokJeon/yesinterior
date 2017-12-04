from django.db.models.fields.files import ImageField, ImageFieldFile
from PIL import Image
import os

def _add_thumb(s):
    parts = s.split(".") # 파일명을 '.'을 기준으로 splite함
    parts.insert(-1, "thumb") # split된 조각 맨 뒤에 'thumb'를 삽입
    if parts[-1].lower() not in ['jpeg', 'jpg']: # 소문자로 변환한 문자열 맨끝이 []안의 확장자가 아닐 시
        parts[-1] = 'jpg' # .jpg로 변환함
    return ".".join(parts) # split된 parts를 다시 join함

class ThumbnailImageFieldFile(ImageFieldFile):
    def _get_thumb_path(self):
        return _add_thumb(self.path)
    thumb_path = property(_get_thumb_path)

    def _get_thumb_url(self):
        return _add_thumb(self.url)
    thumb_url = property(_get_thumb_url)

    def save(self, name, content, save=True):
        super(ThumbnailImageFieldFile,  self).save(name, content, save)
        img = Image.open(self.path)

        size = (128, 128)
        img.thumbnail(size, Image.ANTIALIAS)
        background = Image.new('RGBA', size, (255, 255, 255, 0))
        background.paste(img, (int((size[0]-img.size[0])/2), int((size[1]-img.size[1])/2)))
        background.save(self.thumb_path, 'png')

        def delet(self, save=True):
            if os.path.exists(self.thumb_path):
                os.remove(self.thumb_path)
            super(ThumbnailImageFieldFile, self).delete(save)

class ThumbnailImageField(ImageField):
    attr_class = ThumbnailImageFieldFile

    def __init__(self, thumb_width=128, thumb_height=128, *args, **kwargs):
        self.thumb_width = thumb_width
        self.thumb_height = thumb_height
        super(ThumbnailImageField, self).__init__(*args, **kwargs)
