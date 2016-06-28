from .models import Panel
from .forms import PanelForm
from django.shortcuts import render, get_object_or_404,redirect


def list_task(request):
    panels = Panel.objects.all()
    return render(request, 'panel/panel.html', {'panels': panels})

def panel_detail(request, pk): 
    panel = get_object_or_404(Panel, pk=pk) 
    return render(request, 'panel/panel_detail.html', {'panel': panel})

def panel_new(request):
    #logging.debug(request.POST)
    if request.method=='POST':
        form=PanelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            return render(request, 'panel/panel_edit.html',{'form':form})    
    else:
        form=PanelForm()
        return render(request, 'panel/panel_edit.html',{'form':form})


