from django.shortcuts import render,redirect
from .models import Note
from .forms import *
from django.views import generic  
from youtubesearchpython import VideosSearch
import requests
import wikipedia
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    return render (request, 'dashboard/home.html')

@login_required
def books(request):
    if request.method == "POST":
        form = dashbordform(request.POST)
        text = request.POST['text']
        url = "https://www.googleapis.com/books/v1/volumes?q="+text
        r = requests.get(url)
        answer = r.json()
        result_list = []
        for x in range(10):
            result_dict = {
               'title':answer['items'][x]['volumeInfo']['title'],
               'subtitle':answer['items'][x]['volumeInfo'].get('subtitle'),
               'description':answer['items'][x]['volumeInfo'].get('description'),
               'category':answer['items'][x]['volumeInfo'].get('Category'),
               'count':answer['items'][x]['volumeInfo'].get('pageCount'),
               'rating':answer['items'][x]['volumeInfo'].get('pageRating'),
               'thumbnail':answer['items'][x]['volumeInfo'].get('imageLinks').get('thumbnail'),
               'preview':answer['items'][x]['volumeInfo'].get('previewLink'),
            }
           
            result_list.append(result_dict)
            context = {
                'form':form,
                'result':result_list 
            }
        return render (request, 'dashboard/books.html', context)
        
    else:
        form = dashbordform()
                  
    context = {
        'form':form
    }
    return render (request, 'dashboard/books.html', context)

@login_required
def conversion(request):
    if request.method == 'POST':
         form = conversionform(request.POST)
         if request.POST['measurement'] == 'lenght':
             m = Lenghtform()
             context = {
                 'form':form,
                 'm':m,
                 'input':True   
             }
             if 'input' in request.POST:
                 first = request.POST['measure1']
                 second = request.POST['measure2']
                 input = request.POST['input']
                 answer = ''
                 if input and int(input) >= 0:
                     if first == 'meter' and second == 'centimeter':
                         answer = f'{input} meter = {int(input)/100} centimeter'
                     if first == 'centimeter' and second == 'meter':
                         answer = f'{input} centimeter = {int(input)*100} meter'   
                 context = {
                     'form':form,
                     'm':m,
                     'input':True,
                     'answer':answer
                 }   
    
   
         if request.POST['measurement'] == 'mass':
             m = Massform()
             context = {
                 'form':form,
                 'm':m,
                 'input':True
                 
             }
             if 'input' in request.POST:
                 first = request.POST['measure1']
                 second = request.POST['measure2']
                 input = request.POST['input']
                 answer = ''
                 if input and int(input) >= 0:
                     if first == 'kilogram' and second == 'gram':
                         answer = f'{input} kilogram = {int(input)/1000} gram'
                     if first == 'gram' and second == 'kilogram':
                         answer = f'{input} gram = {int(input)*1000} kilogram'   
                 context = {
                     'form':form,
                     'm':m,
                     'input':True,
                     'answer':answer
                 }              
              
    
         if request.POST['measurement'] == 'tempreture':
             m = Tempretureform()
             context = {
                 'form':form,
                 'm':m,
                 'input':True
                 
             }
             if 'input' in request.POST:
                 first = request.POST['measure1']
                 second = request.POST['measure2']
                #  third = request.POST['measure3']
                 input = request.POST['input']
                 answer = ''
                 if input and int(input) >= 0:
                     if first == 'celcius' and second == 'kelvin':
                         answer = f'{input} Celcius = {int(input)+273.15} Kelvin'
                         
                     if first == 'kelvin' and second == 'celcius':
                         answer = f'{input} kelvin = {int(input)-273.15} Celcius' 
                          
                     if first == 'kelvin' and second == 'farentheight':
                         answer = f'{input} Kelvin = {int(input)-(273.15)*1.8+32} Fahrenheit'
                         
                     if first == 'farentheight' and second == 'kelvin':
                             answer = f'{input} Fahrenheit = {int(input)-(32)*0.555+273.15} Kelvin' 
                      
                     if first == 'farentheight' and second == 'celcius':
                             answer = f'{input} Fahrenheit = {int(input)-(32)*0.555} Celcius'  
                      
                     if first == 'celcius' and second == 'farentheight':
                             answer = f'{input} Celcius = {int(input)*1.8+32} Fahrenheit'              
                      
                                     
                 context = {
                     'form':form,
                     'm':m,
                     'input':True,
                     'answer':answer
                 }                                                 
    else:    
        form = conversionform()
        context = {
        'form':form
         }
    return render (request, 'dashboard/conversion.html',context)

@login_required
def dictionary(request):
    if request.method == "POST":
        form = dashbordform(request.POST)
        text = request.POST['text']
        url = "https://api.dictionaryapi.dev/api/v2/entries/en_US/"+text
        r = requests.get(url)
        answer = r.json()
            
        try:
                phonetics = answer[0]['phonetics'][0]['text']
                audio = answer[0]['phonetics'][0]['audio']
                defination = answer[0]['meanings'][0]['definations'][0]['defination']
                example = answer[0]['meanings'][0]['definations'][0]['example']
                synonym = answer[0]['meanings'][0]['definations'][0]['synonyms']
                
                context = {
                  'form':form,
                  'input':text,
                  'phonetics':phonetics,
                  'audio':audio,
                  'defination':defination,
                  'example':example,
                  'synonym':synonym
                  }   
        except:
            context ={
                'form':form,
                'input':'',
            }  
        return render (request,'dashboard/dictionary.html',context)    
       
    else:
        form = dashbordform()
        context ={
        'form':form
        } 
                    
    
    return render (request,'dashboard/dictionary.html',context)

@login_required
def homework(request):
    if request.method == 'POST':
        form = Homeworkform(request.POST)
        if form.is_valid():
            try:
                finished = request.POST("done")
                if finished == "on":
                    finished == True
                else:
                    finished == False
            
            except:
                finished = False 
                    
                
        homework = Homework(
            user=request.user, 
            subject=request.POST['subject'],
            title=request.POST['title'], 
            body=request.POST['body'],
            due=request.POST['due'],
            done= finished
                            
        )   
        homework.save()  
        return redirect("homework")             
    else:
        form = Homeworkform()    
    work = Homework.objects.filter(user=request.user)
    if len(work) == 0:
        is_done = True
    else:
        is_done = False
    context = {
        "work":work,
        "is_done":is_done,
        "form":form
    }
    return render (request, 'dashboard/homework.html', context)

@login_required
def update_homework(request, pk):
    homework = Homework.objects.get(id=pk)
    if homework.done == True:
        homework.done = False
    else:
        homework.done = True    
    homework.save()
    return redirect('homework')  

@login_required
def delete_homework(request,pk):
    Homework.objects.get(id=pk).delete()  
    return redirect("homework")

# def login(request):
#     return render (request, 'registration/login.html')

# def logout(request):
#     return render (request, 'registration/logout.html')

def notes_detail(request):
    return render (request, 'dashboard/notes_detail.html')
@login_required
def notes(request):
    note = Note.objects.filter(user=request.user)
    if request.method == "POST":
        form = Noteform(request.POST)
        if form.is_valid():
            form = Note(user=request.user, title=request.POST['title'], body=request.POST['body'])
            form.save()
            return redirect("notes")
        
    else:
        form = Noteform()
    
    context ={
        'note':note,
        "form":form
    }
    return render (request, 'dashboard/notes.html', context)


@login_required
def delete_note(request, pk):
   x = Note.objects.get(id=pk)
   x.delete()

   return redirect('notes')


class note_detail(generic.DetailView):
    model = Note
    template_name = "dashboard/notes_detail.html"

@login_required     
def profile(request):
    homework = Homework.objects.filter(done=False, user=request.user)
    todo = Todo.objects.filter( is_finish=False,user=request.user)
    if len(homework) ==0:
        homeworkdone = True
    else:
        homeworkdone  = False
    if len(todo) ==0:
            todos = True
    else:
        todos  = False    
    context = {
        'homework':homework,
        'todo':todo,
        'homeworkdone':homeworkdone,
        'todos':todos
    }       
    return render (request, 'dashboard/profile.html', context)

def register(request):
    if request.method == 'POST':
        form = Register(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        
    else:
        form = Register()
    context = {
        'form':form
    }        
    return render (request, 'registration/register.html', context)
@login_required
def todo(request):
    if request.method == 'POST':
        form = Todoform(request.POST)
        if form.is_valid():
            try:
                finish = request.POST['is_finish']
                if finish == 'on':
                    finish = True
                else:
                    finish = False    
            except:
                finish = False
            
            todos = Todo(
                user = request.user,
                title = request.POST['title'],
                is_finish = finish
            )    
            todos.save()  
            return redirect('todo')      
    else:
        form = Todoform() 
    
    todo = Todo.objects.filter(user=request.user) 
    if len(todo) == 0:
        done = True
    else:
        done = False         
    context = {
        'todo':todo,
        'form':form,
        'done':done
    }
    return render (request, 'dashboard/todo.html', context)

@login_required
def update_todo(request, pk):
    todo = Todo.objects.get(id=pk)
    if todo.is_finish == True:
        todo.is_finish = False
    else:
        todo.is_finish = True
    
    todo.save()
    return redirect('todo')   
@login_required
def delete_todo(request, pk):
    Todo.objects.get(id=pk).delete() 
    return redirect('todo')
@login_required
def wiki(request):
    if request.method == 'POST':
        text = request.POST['text']
        form = dashbordform(request.POST)
        search = wikipedia.page(text)
        context ={
            'form':form,
            'title':search.title,
            'link':search.url,
            'detail':search.summary
        }
        return render (request, 'dashboard/wiki.html',context)
    
    else:
        form = dashbordform()
        context = {
            'form':form
        }
    return render (request, 'dashboard/wiki.html',context)

@login_required
def youtube(request):
    if request.method == "POST":
        form = dashbordform(request.POST)
        text = request.POST['text']
        video = VideosSearch(text, limit=20)
        result_list = []
        for x in video.result()['result']:
            result_dict = {
                'input' : text,
                'duration' : x['duration'],
                'thumbnail' : x['thumbnails'][0]['url'],
                'channel' : x['channel']['name'],
                'link' : x['link'],
                'views' : x['viewCount']['short'],
                'published' : x['publishedTime'],
            }
            desc = ''
            if x['descriptionSnippet']:
                for y in x['descriptionSnippet']:
                    desc += y['text']
            result_dict ['description'] = desc
            result_list.append(result_dict)
            context = {
                'form':form,
                'result':result_list 
            }
        return render (request, 'dashboard/youtube.html', context)
        
    else:
        form = dashbordform()
                  
    context = {
        'form':form
    }
    return render (request, 'dashboard/youtube.html', context)