from django.db import models
from django.utils import timezone
import datetime

# Staff Photos
ishaan = "https://cdn.discordapp.com/attachments/733048042114252940/1056427171545088010/ishaan-modified.png"
sam = "https://cdn.discordapp.com/attachments/733048042114252940/1058952675116449852/IMG_6241-modified.png"
madelyn = "https://cdn.discordapp.com/attachments/733048042114252940/1056427172279103598/madelyn-modified.png"
prathik = "https://cdn.discordapp.com/attachments/733048042114252940/1056427068998561833/prathik-modified.png"
sai = "https://cdn.discordapp.com/attachments/733048042114252940/1067951030794461245/sai-modified.png"
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
brendan = "https://cdn.discordapp.com/attachments/733048042114252940/1056427066851070014/brendan-modified.png"
zach = "https://cdn.discordapp.com/attachments/733048042114252940/1056427170861416550/zach-modified.png"
tedi = "https://cdn.discordapp.com/attachments/733048042114252940/1056427068029677608/tedi-modified.png"
john = "https://cdn.discordapp.com/attachments/733048042114252940/1056427067635404871/john-modified.png"
nikhil = "https://cdn.discordapp.com/attachments/733048042114252940/1056427067232768100/nikhil-modified.png"
none = "https://cdn.discordapp.com/attachments/733048042114252940/1056427066523930645/person-modified.png"

photo_tuple = [(ishaan, 'Ishaan Arora'), (sam, 'Sam Slavinsky'),(madelyn, "Madelyn Cusano"), (prathik, "Prathik Pradeep"), (sai, "Sai Bhat"), (ari, "Ari Frankel"), (tim, "Tim Sturtz"), (dev, "Dev Sappal"), (charlie, "Charlie Martin"), (arav, "Arav Arora"), (erin, "Erin Proulx"), (ranit, "Ranit Sinha"), (ben, "Ben Kane"), (luke, "Luke Laferty"), (brendan, "Brendan Laferty"), (zach, "Zach Slavinsky"), (tedi, "Tedi Hunt"), (john, "John Woodward"), (nikhil, "Nikhil Pratapagiri"), (none, "None")]

class StaffRoster(models.Model):
    id = models.IntegerField(primary_key=True, help_text="This is how each person is ordered on the roster")
    photo = models.CharField(max_length=100, choices=photo_tuple)
    name = models.CharField(max_length=30)
    position = models.CharField(max_length=30)
    class Meta:
        db_table = "staff_roster"
    def __str__(self):
        return self.name

class SoccerRoster(models.Model):
    photo = models.CharField(max_length=100, choices=photo_tuple)
    tw_id = models.CharField(max_length=20, help_text="Teamworks ID")
    name = models.CharField(max_length=30)
    position = models.CharField(max_length=30)
    goals = models.IntegerField()
    class Meta:
        db_table = "soccer_roster"
    def __str__(self):
        return f"{self.name} ({self.tw_id})"

class BasketballRoster(models.Model):
    photo = models.CharField(max_length=100, choices=photo_tuple)
    tw_id = models.CharField(max_length=20, help_text="Teamworks ID")
    name = models.CharField(max_length=30)
    position = models.CharField(max_length=30)
    points = models.IntegerField()
    completed_ft = models.IntegerField()
    attempted_ft = models.IntegerField()
    ft_percent = models.DecimalField(max_digits=10, decimal_places=2)
    class Meta:
        db_table = "basketball_roster"
    def __str__(self):
        return f"{self.name} ({self.tw_id})"

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

# class Transactions(models.Model):
#     current_date = datetime.datetime.now()

#     id = models.IntegerField(primary_key=True)
#     date = models.CharField(max_length=50, default=current_date.strftime("%B %d, %Y"))
#     transaction = models.CharField(max_length=100)
#     team = models.CharField(max_length=50, choices=[('All', 'All'), ('Indoor Soccer Team', 'Indoor Soccer Team'), ('Basketball Team', "Basketball Team")])
#     class Meta:
#         db_table = "transactions"
#         verbose_name_plural = "transactions"
#     def __str__(self):
#          return self.date

class Schedule(models.Model):
    current_date = datetime.datetime.now()

    order = models.IntegerField(primary_key=True, help_text='This is how each "schedule" is ordered on royalsauu.org/schedule')
    date = models.CharField(max_length=50, default=current_date.strftime("%B %d, %Y"))
    time = models.CharField(max_length=50)
    arena = models.CharField(max_length=50)
    home_team = models.CharField(max_length=50)
    win_loss = models.CharField(max_length=50, choices=[('W', 'Win'), ('L', 'Loss'), ('Tie', 'Tied'),('TBD', 'TBD')])
    overall_score = models.CharField(max_length=50, blank=True)
    visiting_team = models.CharField(max_length=50)
    highest_goal_scorer = models.CharField(max_length=75, blank=True)
    class Meta:
        db_table = "schedule"
        verbose_name_plural = "schedule"
    def __str__(self):
        return self.date
