from django.db import models
# from PIL import Image

class Officer(models.Model):
    firstName   = models.CharField(max_length=255)
    lastName    = models.CharField(max_length=255)
    middleIn    = models.CharField(max_length=255, blank=True)
    badge       = models.CharField(max_length=255, blank=True)
    unit        = models.CharField(max_length=255)
    rank        = models.CharField(max_length=255)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return f"Officer: {self.id}, Name: {self.firstName} {self.middleIn} {self.lastName}, Badge Number: {self.badge}, Unit: {self.unit}, Rank: {self.rank}"

class Review(models.Model):
    title       = models.CharField(max_length=255)
    text        = models.TextField(max_length=255)
    rating      = models.IntegerField(null=True)
    image       = models.ImageField(upload_to='officer_pics', null=True, verbose_name="", blank=True)
    videofile   = models.FileField(upload_to='officer_videos', null=True, verbose_name="", blank=True)
    officer     = models.ForeignKey(Officer, related_name='reviews', on_delete=models.PROTECT)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)

    # def save(self, *args, **kwargs):
    #     super(Review, self).save(*args, **kwargs)

    #     img = Image.open(self.image.path)

    #     if img.height > 100 or img.width > 100:
    #         output_size = (500,564)
    #         img.thumbnail(output_size)
    #         img.save(self.image.path)

    def __repr__(self):
        return f"Review: {self.id}, Officer ID: {self.officer.id} Rating: {self.rating} Review-text: {self.text}, Officer Parent: {self.officer}"

class Comment(models.Model):
    text        = models.TextField()
    # add review attribute to class
    review      = models.ForeignKey(Review, related_name='comments', on_delete=models.PROTECT) 
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)
    
    def __repr__(self):
        return f"Comment: {self.id}, Review Parent: {self.review.id}"
