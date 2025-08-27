from rest_framework import serializers
from .models import Notification

class NotificationSerializer(serializers.ModelSerializer):
    actor = serializers.StringRelatedField()
    recipient = serializers.StringRelatedField()
    class Meta:
        model = Notification
        fields = ['id', 'recipient', 'actor', 'verb', 'target_content_type', 'target_object_id', 'timestamp', 'unread']
        read_only_fields = ['id', 'recipient', 'actor', 'timestamp', 'unread']
