from django.shortcuts import render
 
from student.forms import studentform  
  
#def index(request):  
 #   stu = studentform()  
  #  return render(request,"index.html",{'form':stu})  
	
def index(request):
    if request.method == "POST":
        form = studentform(request.POST)
        if form.is_valid():
            
            form.save()
    else:
        form = studentform()
    return render(request, 'index.html', {'form': form})