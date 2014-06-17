from django.shortcuts import render, render_to_response, get_object_or_404
from filetransfers.api import serve_file
from ocr_evaluation.models import *
from django.template import RequestContext
from django.http import HttpResponseRedirect
from datetime import datetime
from random import randint
from ocr_evaluation.forms import DocumentForm
from django.core.urlresolvers import reverse
import subprocess
from graphos.renderers import flot
from graphos.sources.simple import SimpleDataSource

# Create your views here.
def home(request):
    return render(request, 'index.html', {})

def profile(request):
    return render(request, 'account/profile.html', {})

def login(request):
    return render(request, 'login.html', {})

def leaderboards(request):
    return render(request, 'leaderboards.html', {})

def ocr_performance(request):
    hist = Performance.objects.filter(history__user=User.objects.get(id=request.user.id))
    return render(request, 'ocr_performance.html', {'history':hist})

def seg_performance(request):
    hist = Performance.objects.filter(history__user=User.objects.get(id=request.user.id))
    return render(request, 'seg_performance.html', {'history':hist})

def mystats(request):
    best = Performance.objects.order_by('-total').first()
    data =  [
        ['Time', 'Total'],
    ]
    hist = Performance.objects.filter(history__user=User.objects.get(id=request.user.id))
    for h in hist:
        data.append([h.history.uptime, h.total])
    chart = flot.LineChart(SimpleDataSource(data=data), html_id="line_chart")
    return render(request, 'mystats.html', {'chart': chart, 'best': best,})

def seg_calc(ground_truth, user_file):
    output = subprocess.Popen(['python', 'ocr_evaluation/seg_eval.py', user_file, ground_truth], stdout=subprocess.PIPE).stdout.read()
    output = output.split(' ')
    temp = output[-1]
    output[-1] = temp[:-1]
    for i in range(len(output)):
        output[i] = int(float(output[i]))
    print output
    return output

def download(request, id):
    obj = get_object_or_404(TestData, pk=id)
    return serve_file(request, obj.datafile, save_as=True)

def file_list(request):
    filelist = TestData.objects.all()
    return render(request, 'file_list.html', {'files':filelist})

def upload_file(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            data = TestData.objects.get(id=request.POST.get("dataset",1))
            h = History(user=User.objects.get(id=request.user.id), dataset=data, upfile=request.FILES['docfile'], uptime=datetime.now(), algo=request.POST.get("algo",""))
            h.save()
            seg_output = seg_calc(data.datafile.path, h.upfile.path)
            char_error=randint(1,100)
            word_error=randint(1,100)
            p = Performance(history=History.objects.get(id=h.id), char_error=char_error, word_error=word_error, false_detect=seg_output[0], missed_detect=seg_output[1], under_seg=seg_output[2], under_seg_comp=seg_output[3], over_seg=seg_output[4], over_seg_comp=seg_output[5], correct_seg=seg_output[6], total=(word_error+char_error+sum(seg_output)))
            p.save()
            # Redirect to the document list after POST
            return HttpResponseRedirect(reverse('ocr_evaluation.views.profile'))
    else:
        form = DocumentForm() # A empty, unbound form

    dataset = TestData.objects.all()
    return render_to_response(
        'upload.html',
        {'form': form,
         'datasets': dataset,},
        context_instance=RequestContext(request)
    )


