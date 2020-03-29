from django.shortcuts import render,redirect
from moods.models import Mood,Action,Moodlog
def home(request):
	user = request.user
	moods =Mood.objects.all()
	actions =Action.objects.all()
	moodlogs  = Moodlog.objects.filter(user=user)
	# print(moodlogs)
	return render(request, "home.html",{
		"moods":moods,
		"actions":actions,
		"moodlogs":moodlogs
		})

def create_mood(request):
	if request.method=="POST":
		mood_id =request.POST["user_mood"]
		action_id=request.POST["user_action"]
		note=request.POST["note"]
		mood_instance=Mood.objects.get(pk=mood_id)
		action_instance=Action.objects.get(pk=action_id)
		moodlog =Moodlog.objects.create(
			mood = mood_instance,
			action =action_instance,
			note =note,
			user=request.user
			)
		return redirect("/home/")
