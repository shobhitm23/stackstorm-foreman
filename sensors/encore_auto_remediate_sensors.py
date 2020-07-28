import json
import requests
from st2reactor.sensor.base import PollingSensor
from datetime import datetime

class EncoreAutoRemediateSensor(PollingSensor):
    
    def __init__(self, sensor_service, config=None, poll_interval=None):
        
        super(EncoreAutoRemediateSensor, self).__init__(sensor_service=sensor_service, config=config, poll_interval=poll_interval)
        self._logger = self._sensor_service.get_logger(__name__)
        self._trigger_ref = 'foreman.auto_remediate_satellite'

    def setup(self):
        USERNAME = self._config['connections']['username']
        PASSWORD = self._config['connections']['password']
        SERVER = self._config['connections']['server']
        SSL_VERIFY = False
        
        queries = self._config['auto_remediate_sensor_queries']
        
    def poll(self):
       session = requests.Session()
       response = session.get(SERVER)
       response.raise_for_status()
       result = response.json()["results"]
       final_list = []
    
       for query in queries:
           query_date = query['date']
           actual_day = datetime.fromisoformat(query_date)
           
           for obj in result:
               if "subscription_facet_attributes" in obj:
                   new_obj = {
                       obj["certname"]: obj["subscription_facet_attributes"]["last_checkin"]}
                   final_list.append(new_obj)
                   server_checkin_time = obj["subscription_facet_attributes"]["last_checkin"].split()
                   server_checkin_day = server_checkin_time[0]
                   server_checkin_day = datetime.fromisoformat(server_checkin_day) #datetime
                   
                   if actual_day < server_checkin_day:
                       print("This server responded within the query timeframe")
                   else:
                       print("This server didn't respond since before query time")
                       self.dispatch_trigger(obj['certname'], server_checkin_day)               
               else:
                   print("Subscription facet attributes don't exist")
       

    def dispatch_trigger(self, server_name, last_checkin):
        trigger = self._trigger_ref
        
        payload = {
            'server_name': server_name,
            'last_checkin': last_checkin
        }
        
        self.sensor_service.dispatch(trigger=trigger, payload=payload)
    
    def cleanup(self):
        # This is called when the st2 system goes down. You can perform cleanup operations like
        # closing the connections to external system here.
        pass

    def add_trigger(self, trigger):
        # This method is called when trigger is created
        pass

    def update_trigger(self, trigger):
        # This method is called when trigger is updated
        pass

    def remove_trigger(self, trigger):
        # This method is called when trigger is deleted
        pass
