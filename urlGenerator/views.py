from django.shortcuts import render

from django.http import HttpResponse
from .models import Urls, SpookyThing


# Create your views here.
def index(request):
    if(request.method=="POST"):


        # get values

        url = request.POST.get("url")
        radio1 = request.POST.get("surl")
        print(radio1)
        print("URL", url)
        
      
        
        
        if(radio1 == 'curl'):
            # customURL is given
            print("HELLO", radio1)
            customURL = request.POST.get("customURL")
            print("CUSTOM",customURL)
            if(not Urls.objects.filter(customURL =  customURL).exists()):
                obj = Urls(url = url, customURL =customURL)
                obj.save()
            else:
                # return error
                pass
        elif(radio1 == 'surl'):
            print("SURL")
            customURLPrev = Urls.objects.filter(isShortened=True).latest('customURL').customURL
            len1 = len(customURLPrev)
           
            if(customURLPrev[-1]=='z'):
                customURLPrev+='a'
            else:
                customURLPrev=customURLPrev[:len1-1]+chr(ord(customURLPrev[-1])+1)

            obj = Urls(url= url, customURL = customURLPrev, isShortened=True)
            obj.save() 
            customURL = customURLPrev
            print(customURLPrev,"custom")
        else:
            print("HHELLO")
            def getURL():
                import random   
                from random import choice
                n = random.randint(2,5)
                list1 = SpookyThing.objects.all()
                url=''
                while(n>0):
                    n-=1
                    url+=random.choice(list1).thing
                    print(url)
                print(url)
                return url
            flag = 0
            while(flag==0):

                customURL = getURL()
                if(Urls.objects.filter(customURL=customURL).exists()):
                    continue
                else:
                    flag = 1
                
            obj = Urls(url= url, customURL = customURL)
            obj.save()       
        return render(request, 'home.html', {'customURL':customURL})

    
    return render(request, 'home.html')


def goToURL(request, url):
    print(url)
    url = Urls.objects.all().filter(customURL=url)   
    print(url)
    # url = Urls.objects.all().filter(customURL=url)[0].url   
    return render(request, 'buffer.html', {"url":url})
