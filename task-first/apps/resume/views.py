from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from .forms import ResumeItemForm
from .models import ResumeItem

import os
from django.template.loader import get_template
from xhtml2pdf import pisa

from django.views.generic import ListView

@login_required
def resume_view(request):
    resume_items = ResumeItem.objects\
        .filter(user=request.user)\
        .order_by('-start_date')

    return render(request, 'resume/resume.html', {
        'resume_items': resume_items
    })


@login_required
def resume_create_view(request):
    if request.method == 'POST':
        print(request.FILES['photo'],"--------------kish-------------")
        form = ResumeItemForm(request.POST, request.FILES)
        if form.is_valid():
            new_resume_item = ResumeItem(request.FILES['photo'])
            new_resume_item = form.save(commit=False)
            new_resume_item.user = request.user
            new_resume_item.save()

            return redirect(resume_edit_view, new_resume_item.id)
    else:
        form = ResumeItemForm()

    return render(request, 'resume/resume_item_create.html', {'form': form})


@login_required
def resume_edit_view(request, resume_item_id):
    try:
        resume_item = ResumeItem.objects\
            .filter(user=request.user)\
            .get(id=resume_item_id)
    except ResumeItem.DoesNotExist:
        raise Http404

    template_dict = {}

    if request.method == 'POST':
        if 'delete' in request.POST:
            resume_item.delete()
            return redirect(resume_view)

        form = ResumeItemForm(request.POST, request.FILES, instance=resume_item)
        if form.is_valid():
            form.save()
            form = ResumeItemForm(instance=resume_item)
            template_dict['message'] = 'Resume item updated'
    else:
        form = ResumeItemForm(instance=resume_item)

    template_dict['form'] = form

    return render(request, 'resume/resume_item_edit.html', template_dict)

@login_required
def CustomerListView(ListView):
    models = ResumeItem
    template_name = 'resume/resume.html'

@login_required
def resume_render_pdf_view(request, resume_item_id):
    resume_data = get_object_or_404(ResumeItem, pk=resume_item_id)
    data = {
        "title":resume_data.title,
        "email":resume_data.email,
        "mobile":resume_data.mobile,
        "company":resume_data.company,
        "designation":resume_data.designation,
        "photo":resume_data.photo,
        "date_of_birth":resume_data.date_of_birth,
        "start_date":resume_data.start_date,
        "end_date":resume_data.end_date,
        "description":resume_data.description
    }
    template_path = 'resume/download_resume.html'
    context = {'resume_data': data}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)
    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

    # if error then show some funy view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response
