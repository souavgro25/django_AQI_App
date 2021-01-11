from django.shortcuts import render

# Create your views here.
# http://api.airvisual.com/v2/city?city=DELHI&state=DELHI&country=INDIA&key={{943e740a-93e0-46d1-b76c-d94b27aa19c1}}
#https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=20002&distance=25&API_KEY=06984405-1E66-4881-8DA6-A7A444BF5C24
def home(request):
    import json
    import requests 
    if request.method =='POST':
        zipcode = request.POST['Zipcode']
        api_request =requests.get('https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode='+zipcode+'&distance=25&API_KEY=06984405-1E66-4881-8DA6-A7A444BF5C24')
        try:
            api = json.loads(api_request.content)
        except Exception as e:  
            api = "Error... "
        if api[0]['Category']['Name'] == "Good":
            color = "good"
        elif api[0]['Category']['Name'] == "Moderate":
            color = "moderate"
        elif api[0]['Category']['Name'] == "usg":
            color = "usg"
        elif api[0]['Category']['Name'] == "unhealthy":
            color = "unhealthy"
        elif api[0]['Category']['Name'] == "veryunhealthy":
            color = "veryunhealthy"  
        elif api[0]['Category']['Name'] == "hazardous":
            color = "hazardous"
        
        return render(request,'home.html',{'api':api,'color':color })
    else:
        api_request =requests.get('https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=20002&distance=25&API_KEY=06984405-1E66-4881-8DA6-A7A444BF5C24')
        try:
            api = json.loads(api_request.content)
        except Exception as e:  
            api = "Error... "
        if api[0]['Category']['Name'] == "Good":
            color = "good"
        elif api[0]['Category']['Name'] == "Moderate":
            color = "moderate"
        elif api[0]['Category']['Name'] == "usg":
            color = "usg"
        elif api[0]['Category']['Name'] == "unhealthy":
            color = "unhealthy"
        elif api[0]['Category']['Name'] == "veryunhealthy":
            color = "veryunhealthy"  
        elif api[0]['Category']['Name'] == "hazardous":
            color = "hazardous"
        return render(request,'home.html',{'api':api , 'color': color})

                                                
def about(request):
    
    return render(request,'about.html',{})