from django.views.generic import View
from django.shortcuts import render, redirect
from.models import feed
class Index(View):
    template_name = 'index.html'

    def get(self, request):
        return render(request, self.template_name)
    
class TagStudy(View):
    template_name = 'tag_study.html'

    def get(self, request):
        f= feed.objects.all()
        return render(request, self.template_name,{'feed_list': f})
    

class Newcontent(View):
    template_name = 'upload_form.html'

    def get(self, request):
        return render(request, self.template_name)
    
    def post(self, request):
        param = request.POST.get('content', '')
        param2= request.FILES.get('up_photo', False)
        print(f"param:{param}")
        f = feed(content = param, photo=param2)
        f.save()
        return redirect('edu:tag_study')