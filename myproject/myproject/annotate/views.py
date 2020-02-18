from django.http import Http404, HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from .models import Caption
from .forms import NewCaption

import glob
import os
import random
from collections import Counter

OUT_DIR = 'static/annotate_caption/'
FILES = glob.glob('static/images/LSC2020/*/*.jpg')[:13000]
DICT_URL = {}
for it in FILES:
    DICT_URL[os.path.basename(it)] = it

def retreive_no_caption():
    random.shuffle(FILES)
    for it in FILES:
        if not os.path.exists(OUT_DIR+os.path.basename(it)+'.txt'):
            return os.path.basename(it)
    return None

def save_caption(img_id, worker, caption):
    with open(os.path.join(OUT_DIR, img_id+'.txt'), 'wt') as f:
        f.write('%s\n%s'%(caption, worker))

def home(request):
    worker = ''
    if request.method == 'POST':
        form = NewCaption(request.POST)
        if form.is_valid():
            caption = form.save(commit=False)
            caption.save()

            img_id = caption.img_id
            worker = caption.worker
            cap = caption.caption
            save_caption(img_id, worker, cap)

        else:
            img_id = form.data['img_id']
            return render(request, 'caption.html',
                        {'img_url':DICT_URL[img_id],
                        'form':form
            })


    img_id = retreive_no_caption()
    if img_id != None:
        form = NewCaption(initial={'img_id': img_id, 'worker':worker})
        return render(request, 'caption.html',
                        {'img_url':DICT_URL[img_id],
                        'form':form
            })
    else:
        return HttpResponse('Task đã hoàn thành. Xin cảm ơn')
    pass

def count(request):
    files = glob.glob(OUT_DIR+'/*.txt')
    count_names = [open(it).readlines()[1].strip() for it in files]
    dict_count = Counter(count_names)
    # print(dict_count)
    return render(request, 'count.html', {'counts': sorted(dict_count.items())})
    pass