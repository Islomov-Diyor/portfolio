from django.db import models


class SingletonModel(models.Model):
    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)

    @classmethod
    def load(cls):
        obj, _ = cls.objects.get_or_create(pk=1)
        return obj


class HeroSection(SingletonModel):
    name = models.CharField(max_length=200, default="ISLOMOV DIYORBEK")
    badge = models.CharField(max_length=100, default="ISHGA TAYYOR")
    desc = models.TextField(default="Full Stack Developer va IT/CS/AT o'qituvchisi.")
    btn1_text = models.CharField(max_length=100, default="Loyihalarni Ko'rish")
    btn2_text = models.CharField(max_length=100, default="Bog'lanish")
    roles = models.TextField(
        default="Full Stack Developer, IT/CS/AT Teacher, React & Node.js, Python & SQL",
        help_text="Vergul bilan ajrating"
    )

    class Meta:
        verbose_name = "Hero Bo'lim"
        verbose_name_plural = "Hero Bo'lim"

    def __str__(self):
        return "Hero Bo'lim"


class AboutSection(SingletonModel):
    bio_uz = models.TextField(default="Salom! Men Islomov Diyorbek.")
    bio_en = models.TextField(default="Hi! I'm Islomov Diyorbek.")
    stat_years = models.PositiveIntegerField(default=5)
    stat_students = models.PositiveIntegerField(default=200)
    stat_projects = models.PositiveIntegerField(default=30)

    class Meta:
        verbose_name = "Men Haqimda Bo'lim"
        verbose_name_plural = "Men Haqimda Bo'lim"

    def __str__(self):
        return "Men Haqimda Bo'lim"


class Skill(models.Model):
    name = models.CharField(max_length=100)
    percentage = models.PositiveSmallIntegerField(default=80, help_text="0 dan 100 gacha")
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']
        verbose_name = "Ko'nikma"
        verbose_name_plural = "Ko'nikmalar"

    def __str__(self):
        return f"{self.name} ({self.percentage}%)"


CATEGORY_CHOICES = [
    ('frontend', 'Frontend'),
    ('backend', 'Backend'),
    ('fullstack', 'Full Stack'),
    ('talim', "Ta'lim"),
]


class Project(models.Model):
    title = models.CharField(max_length=200)
    emoji = models.CharField(max_length=10, default="💡")
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='frontend')
    desc = models.TextField()
    tags = models.CharField(max_length=300, help_text="Vergul bilan ajrating")
    demo_url = models.URLField(default="#")
    github_url = models.URLField(default="#")
    gradient = models.CharField(
        max_length=200,
        default="135deg,#001a1f 0%,#003344 50%,#00f5ff0d 100%"
    )
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']
        verbose_name = "Loyiha"
        verbose_name_plural = "Loyihalar"

    def __str__(self):
        return self.title

    def tags_list(self):
        return [t.strip() for t in self.tags.split(',')]


class TimelineItem(models.Model):
    year = models.CharField(max_length=30)
    title = models.CharField(max_length=200)
    desc = models.TextField()
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']
        verbose_name = "Ta'lim Tarixi"
        verbose_name_plural = "Ta'lim Tarixi"

    def __str__(self):
        return f"{self.year} — {self.title}"


class Testimonial(models.Model):
    quote = models.TextField()
    name = models.CharField(max_length=100)
    letter = models.CharField(max_length=1, help_text="Avatar uchun bitta harf")
    course_year = models.CharField(max_length=100, help_text="Masalan: Web kursi, 2021")
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']
        verbose_name = "O'quvchi Fikri"
        verbose_name_plural = "O'quvchilar Fikri"

    def __str__(self):
        return f"{self.name} — {self.course_year}"


class Video(models.Model):
    youtube_url = models.URLField(
        help_text="https://www.youtube.com/watch?v=XXXXX yoki https://youtu.be/XXXXX"
    )
    title = models.CharField(max_length=200)
    desc = models.CharField(max_length=300, blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']
        verbose_name = "Video Dars"
        verbose_name_plural = "Video Darslar"

    def __str__(self):
        return self.title

    def embed_url(self):
        from urllib.parse import urlparse, parse_qs
        url = self.youtube_url
        try:
            parsed = urlparse(url)
            if 'youtu.be' in parsed.netloc:
                video_id = parsed.path.lstrip('/')
            else:
                video_id = parse_qs(parsed.query).get('v', [''])[0]
            return f"https://www.youtube.com/embed/{video_id}" if video_id else ''
        except Exception:
            return ''


class ContactInfo(SingletonModel):
    github = models.URLField(default="https://github.com/Islomov-Diyor")
    telegram = models.URLField(default="https://t.me/diyorproger2")
    linkedin = models.URLField(default="#")
    email = models.EmailField(default="diyorbekshaxrisabz@gmail.com")
    location = models.CharField(max_length=100, default="Uzbekistan 🇺🇿")
    youtube = models.URLField(default="https://www.youtube.com/@diyorproger")

    class Meta:
        verbose_name = "Aloqa Ma'lumotlari"
        verbose_name_plural = "Aloqa Ma'lumotlari"

    def __str__(self):
        return "Aloqa Ma'lumotlari"


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Xabar"
        verbose_name_plural = "Kiruvchi Xabarlar"

    def __str__(self):
        return f"{self.name} ({self.email}) — {self.created_at:%Y-%m-%d %H:%M}"
