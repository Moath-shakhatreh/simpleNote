from rest_framework import serializers
from simplenote_app.models import Note

class NoteSerializer(serializers.ModelSerializer):
    
    created_at = serializers.SerializerMethodField() 
    updated_at = serializers.SerializerMethodField()    

  
    class Meta:
        model = Note
        fields = ['title','content','created_at', 'updated_at', 'note_maker']
        
    def get_created_at(self, object):
        s = str(object.created_at)
        return s[0:16]
    
    def get_updated_at(self, object):
        s = str(object.updated_at)
        return s[0:16]
    
  
        
        
        
    def validate_title(self, value):
        if len(value) <= 2 :
            raise serializers.ValidationError('Title must be at least 2 characters')
        else :
            return value
        
    def validate(self, data):
        if data['title'] == data['content']:
            raise serializers.ValidationError('Title and content cannot be the same')
        
        title = data.get('title')
        note_maker = data.get('note_maker')
        if Note.objects.filter(title=title,note_maker=note_maker).exists():
            raise serializers.ValidationError('Note with this title already exists.')
    
        else:
            return data
        
        