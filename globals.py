from home.models import *
from photo.models import *


def common():
    setting = Setting.objects.get(pk=1)
    category = Category.objects.all()
    return {'setting': setting,
            'category': category}
