from django.shortcuts import render, redirect
from .forms import AddPostForm
from .models import Posts
from django.core.mail import send_mail

from django.core.mail import EmailMessage
# Add your views here.
def send_message(request):
    email = EmailMessage(
        'Hello',
        'Body goes here',
        'dauren.ayazbayev@sdu.edu.kz',
        ['dauren.ayazbayev@sdu.edu.kz','200103440@stu.sdu.edu.kz','200103404@stu.sdu.edu.kz'],
        headers={'Message-ID': 'foo'},
    )
    email.attach_file("/home/dauren/Суреттер/1.png")
    email.send(fail_silently=True)
    '''
    send_mail("Web programming:back end", "Тест",
              "dauren.ayazbayev@sdu.edu.kz",
              ["dauren.ayazbayev@sdu.edu.kz", "200103157@stu.sdu.edu.kz","200103520@stu.sdu.edu.kz"],
              fail_silently=False,html_message="<b>Bold text</b><i>Italic text</i>")
'''
    return render(request, 'lecture11_app/successfull.html')




'''
email = EmailMessage(
        'Hello',
        'Body goes here',
        'dauren.ayazbayev@sdu.edu.kz',
        ['dauren.ayazbayev@sdu.edu.kz', '200103062@stu.sdu.edu.kz'],
        headers={'Message-ID': 'foo'},
    )
    email.attach_file('/home/dauren/Суреттер/1.png')
    email.send(fail_silently=False)
'''
def addpage(request):
    if request.method == 'POST':
        form = AddPostForm(request.POST)
        print(request.POST)

        if form.is_valid():
            #print(form.cleaned_data)
            try:
                Posts.objects.create(**form.cleaned_data)
                return redirect('add_page')
            except:
                form.add_error(None, 'Мақаланы қосқанда қате шықты.')
    else:
        form = AddPostForm()
    return render(request, 'lecture11_app/addpage.html',{'title':'Мақаланы қосу','form':form})

