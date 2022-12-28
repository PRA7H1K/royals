from django.db import models
from django.utils import timezone
import datetime

# Staff Photos
ishaan = "https://cdn.discordapp.com/attachments/733048042114252940/1056427171545088010/ishaan-modified.png"
aj = "https://cdn.discordapp.com/attachments/733048042114252940/1056427066523930645/person-modified.png"
madelyn = "https://cdn.discordapp.com/attachments/733048042114252940/1056427172279103598/madelyn-modified.png"
prathik = "https://cdn.discordapp.com/attachments/733048042114252940/1056427068998561833/prathik-modified.png"
sai = "https://cdn.discordapp.com/attachments/733048042114252940/1056427066523930645/person-modified.png"
ari = "https://cdn.discordapp.com/attachments/733048042114252940/1056427173185073152/ari-modified.png"

# Roster Photos
tim = "https://cdn.discordapp.com/attachments/733048042114252940/1056427172862107698/tim-modified.png"
dev = "https://cdn.discordapp.com/attachments/733048042114252940/1056427171897417828/dev-modified.png"
charlie = "https://cdn.discordapp.com/attachments/733048042114252940/1056427068658814998/charlie-modified.png"
arav = "https://cdn.discordapp.com/attachments/733048042114252940/1056427171192774686/arav-modified.png"
erin = "https://cdn.discordapp.com/attachments/733048042114252940/1056427172560109608/erin-modified.png"
ranit = "https://cdn.discordapp.com/attachments/733048042114252940/1056427069325709312/ranit-modified.png"
ben = "https://cdn.discordapp.com/attachments/733048042114252940/1056427068356841492/ben-modified.png"
luke = "https://cdn.discordapp.com/attachments/733048042114252940/1056427066205155338/luke2-modified.png"
bailey = "https://cdn.discordapp.com/attachments/733048042114252940/1056427066523930645/person-modified.png"
brendan = "https://cdn.discordapp.com/attachments/733048042114252940/1056427066851070014/brendan-modified.png"
zach = "https://cdn.discordapp.com/attachments/733048042114252940/1056427170861416550/zach-modified.png"
amelia = "https://cdn.discordapp.com/attachments/733048042114252940/1056427066523930645/person-modified.png"
alex = "https://cdn.discordapp.com/attachments/733048042114252940/1056427066523930645/person-modified.png"
audrey = "https://cdn.discordapp.com/attachments/733048042114252940/1056427066523930645/person-modified.png"
tedi = "https://cdn.discordapp.com/attachments/733048042114252940/1056427068029677608/tedi-modified.png"
john = "https://cdn.discordapp.com/attachments/733048042114252940/1056427067635404871/john-modified.png"
nikhil = "https://cdn.discordapp.com/attachments/733048042114252940/1056427067232768100/nikhil-modified.png"
person = "https://cdn.discordapp.com/attachments/733048042114252940/1056427066523930645/person-modified.png"

photo_tuple = [(ishaan, 'Ishaan'), (aj, 'AJ St. Gelais'), (madelyn, "Madelyn"), (prathik, "Prathik"), (sai, "Sai"), (person, "None"), (ari, "Ari"), (tim, "Tim"), (dev, "Dev"), (charlie, "Charlie"), (arav, "Arav"), (erin, "Erin"), (ranit, "Ranit"), (ben, "Ben"), (luke, "Luke"), (bailey, "Bailey"), (brendan, "Brendan"), (zach, "Zach"), (amelia, "Amelia"), (alex, "Alex"), (audrey, "Audrey"), (tedi, "Tedi"), (john, "John"), (nikhil, "Nikhil")]

class StaffRoster(models.Model):
    photo = models.CharField(max_length=100, choices=photo_tuple)
    name = models.CharField(max_length=30)
    position = models.CharField(max_length=30)
    class Meta:
        db_table = "staff_roster"
    def __str__(self):
         return self.name

class SoccerRoster(models.Model):
    photo = models.CharField(max_length=100, choices=photo_tuple)
    name = models.CharField(max_length=30)
    position = models.CharField(max_length=30)
    goals = models.CharField(max_length=30)
    class Meta:
        db_table = "soccer_roster"
    def __str__(self):
         return self.name

class BasketballRoster(models.Model):
    photo = models.CharField(max_length=100, choices=photo_tuple)
    name = models.CharField(max_length=30)
    position = models.CharField(max_length=30)
    points = models.CharField(max_length=30)
    completed_ft = models.CharField(max_length=30)
    attempted_ft = models.CharField(max_length=30)
    ft_percent = models.CharField(max_length=30)
    class Meta:
        db_table = "basketball_roster"
    def __str__(self):
         return self.name

class Injuries(models.Model):
    photo = models.CharField(max_length=100, choices=photo_tuple)
    name = models.CharField(max_length=30)
    status = models.CharField(max_length=100, choices=[('red.png', 'Out'), ('yellow.png', 'Questionable'), ('green.png', "Probable")])
    reason = models.CharField(max_length=100)
    class Meta:
        db_table = "injuries"
        verbose_name_plural = "injuries"
    def __str__(self):
         return self.name

class Transactions(models.Model):
    current_date = datetime.datetime.now()

    date = models.CharField(max_length=20, default=current_date.strftime("%B %d, %Y"))
    transaction = models.CharField(max_length=100)
    team = models.CharField(max_length=50, choices=[('All', 'All'), ('Indoor Soccer Team', 'Indoor Soccer Team'), ('Basketball Team', "Basketball Team")])
    class Meta:
        db_table = "transactions"
        verbose_name_plural = "transactions"
    def __str__(self):
         return self.date

class Schedule(models.Model):
     current_date = datetime.datetime.now()

     date = models.CharField(max_length=20, default=current_date.strftime("%B %d, %Y"))
     time = models.CharField(max_length=20)
     arena = models.CharField(max_length=20)
     home_team = models.CharField(max_length=50)
     win_loss = models.CharField(max_length=20, choices=[('W', 'Win'), ('L', 'Loss'), ('TBD', 'TBD')])
     overall_score = models.CharField(max_length=20)
     visiting_team = models.CharField(max_length=20)
     highest_goal_scorer = models.CharField(max_length=75)
     class Meta:
         db_table = "schedule"
         verbose_name_plural = "schedule"
     def __str__(self):
          return self.date
