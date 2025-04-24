from django.db import models
from django.urls import reverse #dynamically redirect to the newly created object using the get_absolute_url method on the model

# A tuple of 2-tuples added above our models
MEALS = (
    ('B', 'Breakfast'),
    ('L', 'Lunch'),
    ('D', 'Dinner')
)

# Create your models here.
class Cat(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    age = models.IntegerField()

    def __str__(self):
        return self.name

    # Define a method to get the URL for this particular cat instance
    def get_absolute_url(self):
        # Use the 'reverse' function to dynamically find the URL for viewing this cat's details
        return reverse('cat-detail', kwargs={'cat_id': self.id})

    # Add new Feeding model below Cat model

class Feeding(models.Model):
    # The first optional positional argument overrides the label, from Date to 'Feeding date'
    date = models.DateField('Feeding date')
    meal = models.CharField(
        max_length=1,
        # add the 'choices' field option
        choices=MEALS,
        # set the default value for meal to be 'B'
        default=MEALS[0][0]
    )
    # Create a cat_id column for each feeding in the database
    cat = models.ForeignKey(Cat, on_delete=models.CASCADE)
    def __str__(self):
        # Nice method for obtaining the friendly value of a Field.choice
        return f"{self.get_meal_display()} on {self.date}" #print the long form
    
    # Define the default order of feedings
    class Meta:
        ordering = ['-date']  # This line makes the newest feedings appear first