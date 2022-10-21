from django.db import models

# Create your models here.


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email_address = models.EmailField()

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return f"{self.full_name()} ({self.email_address})"


class Period(models.Model):
    period = models.CharField(max_length=100)

    def __str__(self):
        return self.period


class Size(models.Model):
    size = models.CharField(max_length=100)

    def __str__(self):
        return self.size


class Eating(models.Model):
    eating_class = models.CharField(max_length=100)

    def __str__(self):
        return self.eating_class


class Dino(models.Model):
    name = models.CharField(max_length=100)
    eating_class = models.ForeignKey(Eating, on_delete=models.SET_NULL, null=True)
    color = models.CharField(max_length=100, null=True)
    period = models.ForeignKey(Period, on_delete=models.SET_NULL, null=True)
    size = models.ForeignKey(Size, on_delete=models.SET_NULL, null=True)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True, related_name="posts")
    image1 = models.ImageField(upload_to="posts", null=True, blank=True, default="../static/img/defaultimg.png")
    image2 = models.ImageField(upload_to="posts", null=True, blank=True, default="../static/img/defaultimg.png")
    slug = models.SlugField(unique=True, db_index=True)
    date = models.DateField(auto_now=True)

    def __str__(self):
        return self.name


class Comment(models.Model):
    user_name = models.CharField(max_length=100)
    user_email = models.EmailField()
    text = models.TextField(max_length=400)
    post = models.ForeignKey(Dino, on_delete=models.CASCADE, related_name="comments")
