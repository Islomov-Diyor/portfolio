from django.shortcuts import render, redirect
from .models import (
    HeroSection, AboutSection, Skill, Project,
    TimelineItem, Testimonial, Video, ContactInfo
)
from .forms import ContactForm


def index(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/?sent=1#contact')
    else:
        form = ContactForm()

    hero = HeroSection.load()
    about = AboutSection.load()
    contact = ContactInfo.load()

    context = {
        'hero': hero,
        'hero_roles': [r.strip() for r in hero.roles.split(',') if r.strip()],
        'about': about,
        'about_bio_uz_paragraphs': [p for p in about.bio_uz.split('\n\n') if p.strip()],
        'about_bio_en_paragraphs': [p for p in about.bio_en.split('\n\n') if p.strip()],
        'skills': Skill.objects.all(),
        'projects': Project.objects.all(),
        'timeline': TimelineItem.objects.all(),
        'testimonials': list(Testimonial.objects.all()),
        'videos': Video.objects.all(),
        'contact': contact,
        'form': form,
        'sent': request.GET.get('sent') == '1',
    }
    return render(request, 'index.html', context)
