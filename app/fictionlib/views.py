from django.http import HttpResponse, JsonResponse
import os
from .models import Story
from .models import Character
from .models import Connector

def file_exists(filepath):
    return os.path.exists(filepath)

def index(request, story_id):
    filepath = f"/Users/tarini/projects/chatfic/app/stories/{story_id}"
    print(filepath)
    if file_exists(filepath):
        with open(filepath, 'r') as file:
            content = file.read()
        return HttpResponse(content)
    else:
        return HttpResponse("File not found.")
    
def results(request, character):
    characterobject = Character.objects.get(name=character)
    character_story_connections = Connector.objects.filter(character=characterobject.id)

    my_dict = {
        "message": f"There are {len(character_story_connections)} stories with that character.",
    }

    if len(character_story_connections) < 2:
        filepath = character_story_connections[0].story.content
        with open(f"/Users/tarini/projects/chatfic/app/stories/{filepath}", 'r') as file:
            content = file.read()
        return HttpResponse(content)
    if len(character_story_connections) >= 2:
         list_of_stories = []
         for val in character_story_connections:
            list_of_stories.append(f"For {val.story.title} go to http://127.0.0.1:8000/fictionlib/{val.story.content}/")
            my_dict["stories"] = list_of_stories
         return JsonResponse(my_dict)
    else:
        return HttpResponse("Character not found.")
# Create your views here.