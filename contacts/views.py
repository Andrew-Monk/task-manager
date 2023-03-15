from django.shortcuts import render

# Create your views here.


def list_contacts(request):
    contacts = [
        {"name": "Andrew Monk", "job_title": "Software Engineer", "image": "/images/andrew.jpg", "link": "https://www.linkedin.com/in/andrew-monk-a069b9122/"},
        {"name": "Ben Bass", "job_title": "Software Engineer", "image": "/images/ben.jpg", "link": "https://www.linkedin.com/in/benjamin-bass-63996913a/"},
        {"name": "Chris Zambito", "job_title": "Software Engineer", "image": "/images/chris.jpg", "link": "https://www.linkedin.com/in/chris-zambito-574501256/"},
        {"name": "Danielle Aharonov", "job_title": "Software Engineer", "image": "/images/danielle.jpg", "link": "https://www.linkedin.com/in/danielle-aharonov-124b53165/"},
        {"name": "Liland Pham", "job_title": "Software Engineer", "image": "/images/liland2.jpg", "link": "https://www.linkedin.com/in/lilandpham/"},
        {"name": "Ricky Trang", "job_title": "Software Engineer", "image": "/images/ricky.jpg", "link": "https://www.linkedin.com/in/rickytrang/"},
        {"name": "Stesha Carle", "job_title": "Software Engineer", "image": "/images/stesha.jpg", "link": "https://www.linkedin.com/in/stesha-carle/"},
        {"name": "Steve Song", "job_title": "Software Engineer", "image": "/images/steve.jpg", "link": "https://www.linkedin.com/in/steve-song-sms/"},
        ]

    context = {
        "contacts": contacts
    }

    return render(request, "contacts/list_contacts.html", context)
