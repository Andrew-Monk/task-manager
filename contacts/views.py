from django.shortcuts import render

# Create your views here.

def list_contacts(request):
    contacts = [
        {"name": "Andrew Monk", "job_title": "Software Engineer", "image": "/Andrew.jpeg", "link": "https://www.linkedin.com/in/andrew-monk-a069b9122/"},
        {"name": "Ben Bass", "job_title": "Software Engineer", "image": "/Ben.jpeg", "link": "https://www.linkedin.com/in/benjamin-bass-63996913a/"},
        {"name": "Chris Zambito", "job_title": "Software Engineer", "image": "/Chris.jpeg", "link": "https://www.linkedin.com/in/chris-zambito-574501256/"},
        {"name": "Danielle Aharonov", "job_title": "Software Engineer", "image": "/Danielle.jpeg", "link": "https://www.linkedin.com/in/danielle-aharonov-124b53165/"},
        {"name": "Liland Pham", "job_title": "Software Engineer", "image": "/Liland.jpeg", "link": "https://www.linkedin.com/in/lilandpham/"},
        {"name": "Ricky Trang", "job_title": "Software Engineer", "image": "/Ricky.jpeg", "link": "https://www.linkedin.com/in/rickytrang/"},
        {"name": "Stesha Carle", "job_title": "Software Engineer", "image": "/Stesha.jpeg", "link": "https://www.linkedin.com/in/stesha-carle/"},
        {"name": "Steve Song", "job_title": "Software Engineer", "image": "/Steve.jpeg", "link": "https://www.linkedin.com/in/steve-song-sms/"},
    ]

    context = {
        "contacts": contacts
    }

    return render(request, "contacts/list_contacts.html", context)
