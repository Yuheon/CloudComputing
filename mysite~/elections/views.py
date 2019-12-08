from django.shortcuts import render
from django.http import HttpResponse

from .models import Candidate

def index(request):
#    candidates = Candidate.objects.all() #Candidate 테이블의 모든 행 가져옴
#    str = ''
#    for candidate in candidates:
#        str += "<p>{} 기호{}qjs({})<br>".format(candidate.name,
#            candidate.party_number,
#            candidate.area)
#        str += candidate.introduction+"</p>"
#    return HttpResponse(str)
#
    candidates = Candidate.objects.all()
    context = {'candidates':candidates}
    return render(request, 'eletions/index.html',context)
# Create your views here.
