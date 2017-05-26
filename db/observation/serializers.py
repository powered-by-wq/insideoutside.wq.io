from rest_framework import serializers
from wq.db.rest.serializers import ModelSerializer
import json


class ObservationSerializer(ModelSerializer):
    results_json = serializers.SerializerMethodField()

    def get_results_json(self, instance):
       try:
           obj = json.loads(instance.results)
           for row in obj.get('result', []):
               row['confidence'] = round(row.get('confidence', 0), 3)
           return obj
       except Exception:
           return None
