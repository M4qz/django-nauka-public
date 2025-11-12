from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse

class manytomany(models.Model):
    name = models.CharField(max_length=100, unique=True)  # Przykładowe pole
    description = models.TextField(null=True, blank=True)  # Opcjonalne pole opisu

    def __str__(self):
        return self.name

class onetone(models.Model):
    number =models.IntegerField(null=False,validators=[MinValueValidator(1),MaxValueValidator(1000)])
    def __str__(self):
        return str(self.number)

class BookWriter(models.Model):
    name= models.CharField(max_length=100,unique=True)  # Dodano pole name
    def __str__(self):
        return self.name

class Book(models.Model):
        title = models.CharField(max_length=200)  # Zmieniono długość pola
        #author = models.CharField(max_length=100, null=True, blank=True)  # Dodano nowe pole
        author=models.ForeignKey(BookWriter, on_delete=models.CASCADE, null=True)  # Zmieniono pole author na ForeignKey
        published_date = models.DateField(null=True, blank=True)  # Dodano nowe pole
        age = models.IntegerField(null=True, validators=[MinValueValidator(1),MaxValueValidator(5)])  # Dodano nowe pole
        slug = models.SlugField(max_length=200,blank=True)#,editable=False)  # Dodano pole slug
        code= models.OneToOneField(onetone, on_delete=models.CASCADE, null=True)  # Dodano pole code jako relację jeden do jednego z modelem onetone
        published_countries=models.ManyToManyField(manytomany,blank=True)

        def __str__(self):
            return f"{self.title} ({self.author})"  # Zmieniono sposób wyświetlania obiektu
        #print(str(book))
        def get_absolute_url(self):
            return reverse('book_detail', args=[str(self.id)])

        def save(self, *args, **kwargs):
            if not self.slug or self.slug.strip() == "":
                base_slug = slugify(self.title)
                slug = base_slug
                counter = 1

                while Book.objects.filter(slug=slug).exclude(pk=self.pk).exists():
                    slug = f"{base_slug}-{counter}"
                    counter += 1

                self.slug = slug

            super().save(*args, **kwargs)

