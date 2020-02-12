from django.http import Http404, HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from .models import Caption
from .forms import NewCaption

import glob
import os
import random

OUT_DIR = 'static/annotate_caption/'
FILES = glob.glob('static/images/LSC2020/*/*.jpg')[:13000]

def retreive_no_caption():
    random.shuffle(FILES)
    for it in FILES:
        if not os.path.exists(OUT_DIR+os.path.basename(it)+'.txt'):
            return os.path.basename(it), it
    return None, None

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

    img_id, img_url = retreive_no_caption()
    if img_id != None and img_url != None:
        form = NewCaption(initial={'img_id': img_id, 'worker':worker})
        return render(request, 'caption.html',
                        {'img_url':img_url,
                        'form':form
            })
    else:
        return HttpResponse('Task đã hoàn thành. Xin cảm ơn')
    pass