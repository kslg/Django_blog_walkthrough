from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


STATUS = ((0, "Draft"), (1, "Published"))

TIME_SLOTS = (
    ('0','15:30 - 15:45'),
    ('1', '15:45 - 16:00'),
    ('2','16:00 - 16:15'),
    ('3','16:15 - 16:30'),
    ('4','16:30 - 16:45'),
    ('5','16:45 - 17:00'),
)


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
    )
    featured_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(
        User, related_name='blogpost_like', blank=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             related_name="comments")
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.name}"


class Appointment(models.Model):
    date = models.DateField()
    time = models.CharField(max_length=6, choices=TIME_SLOTS, default='0')
    parent_name = models.CharField(max_length=80)
    teacher_name = models.CharField(max_length=80)
    child_name = models.CharField(max_length=80)
    class_name = models.CharField(max_length=80)
    email = models.EmailField()
    notes = models.TextField()
    approved = models.BooleanField(default=False)


def __str__(self):
        return f"Appointment for {self.child_name} in {self.class_name} with \
            {self.teacher_name}"


class Teachers(models.Model):
    teacher_name = models.ForeignKey(
        Appointment, on_delete=models.CASCADE, related_name="appointments"
    )
    class_name = models.CharField(max_length=80)