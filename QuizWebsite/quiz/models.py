from django.db import models
from django_random_queryset import RandomManager
# table for age and category
class AgeCategory(models.Model):
	age = models.CharField(max_length=50)
	category = models.CharField(max_length=50)
	def __str__(self):
		results = self.age + self.category
		return results

class Question(models.Model):
	objects = RandomManager()
	age_and_category =  models.ForeignKey(AgeCategory, on_delete=models.CASCADE)
	QID = models.CharField(max_length=50)
	problem = models.CharField(max_length=200, default = "")
	answer = models.CharField(max_length=50)
	choice1 = models.CharField(max_length=50)
	choice2 = models.CharField(max_length=50)
	choice3 = models.CharField(max_length=50)
	def __str__(self):
		return self.problem
	#def choice1(self):
		#return self.choice1
