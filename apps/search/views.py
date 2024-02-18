from django.shortcuts import render, redirect
from django.http import HttpResponse
import csv
from django.contrib import messages
from .models import *
from django.core.files.storage import FileSystemStorage
import os
from django.urls import reverse
from django.http import JsonResponse

import stripe
stripe.api_key = os.environ.get("STRIPE_API_SECRET_KEY")


def home(request):
    return render(request, "search/home.html")

def about(request):
    return render(request, "search/about.html", {"title": "About"})

def contact(request):
    return render(request, "search/contact.html", {"title": "Contact us"})

def rated(request):

    # rated_officers  = []

    # officer=[]

    # for review in Review.objects.all():
    #     if review.officer == True:
    #         rated_officers.append(review.officer.id)

    # for officer in rated_officers:
    #     if officer
        

    # reviews     = Review.objects.all()

    context={
        'officers': Officer.objects.all(),
        'reviews': Review.objects.all()[:5],
        # 'reviews': Review.objects.all()[:5],
        'title': "Officers Rated"
        

    }
    return render(request, "search/officers-rated.html", context)


def donations_page(request):
    return render(request, "search/donate.html", {"title": "Donate!"}) 


def charge(request):

	if request.method == 'POST':
		print('Data:', request.POST)

		amount = int(request.POST['amount'])

		customer = stripe.Customer.create(
			email=request.POST['email'],
			name=request.POST['nickname'],
			source=request.POST['stripeToken']
			)

		charge = stripe.Charge.create(
			customer=customer,
			amount=amount*100,
			currency='usd',
			description="Donation"
			)

	return redirect(reverse('success', args=[amount]))

def successMsg(request, args):
	amount = args
	return render(request, 'search/success.html', {'amount':amount})


def populate(request):
    with open("/app/apps/search/cpd.csv", 'r') as csvfile:

        cop_data = csv.DictReader(csvfile) 
        
        for line in cop_data:
            Officer.objects.create(firstName = line['FIRST_NAME'], middleIn=line['MI'],lastName = line['LAST_NAME'], badge=line['STAR1'], unit=line['CPD_UNIT'], rank=line['RANK'])


def searchresult(request):

    q = request.POST['q']

    if Officer.objects.filter(badge=q).exists():
        officer = Officer.objects.get(badge=q)
        officer_id = officer.id
        return redirect(f"/officers/{officer_id}")

    else:
        messages.error(request, "I'm afraid there isn't a badge number like that in the database!")
        return redirect("/")


def viewOfficer(request, officer_id):

    officer = Officer.objects.get(id=officer_id)

    reviews = officer.reviews.all().order_by('-created_at')

    review_set = reviews[:5]

    if Review.objects.filter(officer=officer_id).exists():

        officerReview = Review.objects.filter(officer=officer_id)

        reviewList=[]

        for review in officerReview:
            reviewList.append(review.rating)

        def average(list):
            avg = list[0]
            sum =0
            for i in range(0, len(list),1):
                sum = sum + list[i]
                avg = sum / len(list)
            return round(avg)

        avgRating = average(reviewList)

    else:
        avgRating = "N/A"


    context={
        'officer': officer,
        'reviews': reviews,
        'avgRating': avgRating
        # 'rating' : ratings
    }

    return render (request, "search/view.html", context)


def postreview(request):
    title               = request.POST['title']
    message             = request.POST['message']
    rating              = request.POST['rating']
    officer_id          = request.POST['cop']


    if("photo" in request.FILES) and ("video" in request.FILES):
        photo   = request.FILES['photo']
        video   = request.FILES['video']
        fs                  = FileSystemStorage()
        filename            = fs.save(video.name, video)
        uploaded_file_url   = fs.url(filename)

        userMessage = Review.objects.create(title=title, text=message, rating=rating, image=photo, videofile=uploaded_file_url, officer=Officer.objects.get(id=officer_id))
        userMessage.save()
        messages.success(request, "Thank you for your review. Your review has been saved in the database")

        return redirect(f"/officers/{officer_id}")

    elif("photo" in request.FILES) and ("video" not in request.FILES):
        photo   = request.FILES['photo']

        userMessage = Review.objects.create(title=title, text=message, rating=rating, image=photo, officer=Officer.objects.get(id=officer_id))
        userMessage.save()
        messages.success(request, "Thank you for your review. Your review has been saved in the database")

        return redirect(f"/officers/{officer_id}")

    elif("photo" not in request.FILES) and ("video" in request.FILES):
        video   = request.FILES['video']
        fs                  = FileSystemStorage()
        filename            = fs.save(video.name, video)
        uploaded_file_url   = fs.url(filename)

        userMessage = Review.objects.create(title=title, text=message, rating=rating, videofile=uploaded_file_url, officer=Officer.objects.get(id=officer_id))
        userMessage.save()
        messages.success(request, "Thank you for your review. Your review has been saved in the database")

        return redirect(f"/officers/{officer_id}")

    elif("photo" not in request.FILES) and ("video" not in request.FILES):

        userMessage = Review.objects.create(title=title, text=message, rating=rating, officer=Officer.objects.get(id=officer_id))
        userMessage.save()
        messages.success(request, "Thank you for your review. Your review has been saved in the database")

        return redirect(f"/officers/{officer_id}")


def display_cops(request):

    html_output = ''
    names = []
    full_time = 0
    part_time = 0
    salary_total = 0.00
    six_figs = 0
    
    with open('/Users/chuy/Documents/projects/python/django/cpd_search_app/pd_searchv3/apps/search/cpd.csv', 'r') as csvfile:

        cop_data = csv.DictReader(csvfile)
        
        for line in cop_data:
            names.append(f"{line['Name']} {line['Job Titles']} {line['Full or Part-Time']} {line['Salary or Hourly']} {line['Typical Hours']} {line['Annual Salary']} {line['Hourly Rate']}")
            if(line['Full or Part-Time'] == "F"):
                full_time += 1
                salary_total += float(line['Annual Salary'])
                if(float(line['Annual Salary']) >= 100000.00):
                    six_figs += 1
            if(line['Full or Part-Time'] == "P"):
                part_time += 1
    # print(names)
    
    context = {
        'Name' : line['Name'],
        'Job_Titles' : line['Job Titles'],
        'Full_or_Part-Time' : line['Full or Part-Time'],
        'Salary_or_Hourly' : line['Salary or Hourly'],
        'Typical_Hours' : line['Typical Hours'],
        'Annual_Salary' : line['Annual Salary'],
        'Hourly_Rate' :line['Hourly Rate'],
        'officers' : Officer.objects.all() 
        
    }
    # for name in names:
    #     print(name)
    #     print(len(names))
    #     print(full_time)
    #     print(part_time)
    #     print("Average salary of full time cops: " + str(round(salary_total/len(names),2)))
    #     print(f"Cops making six figures or more: {str(six_figs)} ({str(int(round(six_figs/len(names),#2)*100))}% of all cops)")

    return render(request, "search/cpd_cops.html", context)