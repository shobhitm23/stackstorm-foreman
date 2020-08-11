import json
import requests
from st2reactor.sensor.base import PollingSensor
from datetime import datetime, timedelta, date


class ForemanAutoRemediateSensor(PollingSensor):
    def __init__(self, sensor_service, config=None, poll_interval=None):

        super(ForemanAutoRemediateSensor, self).__init__(
            sensor_service=sensor_service, config=config, poll_interval=poll_interval
        )
        self._logger = self._sensor_service.get_logger(__name__)
        self._trigger_ref = "foreman.auto_remediate_satellite"

    def setup(self):

        self._USERNAME = self._config["foreman"]["dev"]["username"]
        self._PASSWORD = self._config["foreman"]["dev"]["password"]
        self._SERVER = self._config["foreman"]["dev"]["server"]
        self._SSL_VERIFY = False
        self._query = self._config["query"]["days"]
        self._url = "http://{}/".format(self._SERVER)
        self._url = self._url + "api/hosts"

    def poll(self):

        session = requests.Session()
        session.auth = (self._USERNAME, self._PASSWORD)
        session.verify = self._SSL_VERIFY
        response = session.get(self._url)
        if response.status_code != 200:
            print(response.raise_for_status)
            exit()

        result = response.json()
        result_json = json.dumps(result)
        parsed = json.loads(result_json)

        output_parse = json.dumps(parsed, indent=4, sort_keys=True)
        parsed_list = parsed["results"]

        query_date = int(self._query)

        for obj in parsed_list:
            # print(obj)
            if "subscription_facet_attributes" in obj:
                server_checkin_date_uni = obj["subscription_facet_attributes"][
                    "last_checkin"
                ]
                # print(type(server_checkin_date))
                query_checkin_date = date.today() - timedelta(days=query_date)
                # print(type(query_checkin_date))

                server_checkin_date = datetime.strptime(
                    server_checkin_date_uni.split()[0], "%Y-%m-%d"
                ).date()
                # print(type(server_checkin_date))

                if query_checkin_date < server_checkin_date:
                    print("This server responded within the query timeframe")
                else:
                    # print("This server didn't respond since before query checkin date")
                    self.dispatch_trigger(obj["certname"], server_checkin_date)
            else:
                print("Subscription facet attributes don't exist")

    def dispatch_trigger(self, server_name, last_checkin):

        trigger = self._trigger_ref
        payload = {"server_name": server_name, "last_checkin": last_checkin.strftime("%m/%d/%Y")}

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
