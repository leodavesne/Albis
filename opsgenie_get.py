from __future__ import print_function

from pprint import pprint

from opsgenie.swagger_client import AlertApi
from opsgenie.swagger_client import configuration
from opsgenie.swagger_client.models import *
from opsgenie.swagger_client.rest import ApiException

REQUEST_ID = "YOUR_REQUEST_ID"
API_KEY = "ed7e1de1-2b67-4fa4-ae25-f13dc7294abd"
IDENTIFIER = "YOUR_ALERT_IDENTIFIER"
IDENTIFIER_TYPE = "YOUR_ALERT_IDENTIFIER_TYPE"


def setup_opsgenie_client():
    configuration.api_key['Authorization'] = API_KEY
    configuration.api_key_prefix['Authorization'] = 'GenieKey'
    # Provides more detailed request
    # configuration.debug = True


def list_alerts():
    setup_opsgenie_client()

    try:
        # Default identifier_type is id
        response = AlertApi().list_alerts(
            limit=25,
            query='status: open',
            order='desc',
            sort='createdAt')

        # Refer to ListAlertsResponse for more detailed data
        print('request id: {}'.format(response.request_id))
        print('took: {}'.format(response.took))
        for alert_response in response.data:
            print('alert_response.id: {}'.format(alert_response.id))
            print('alert_response.tiny_id: {}'.format(alert_response.tiny_id))
            print('alert_response.alias: {}'.format(alert_response.alias))
            print('alert_response.message: {}'.format(alert_response.message))
            print('alert_response.status: {}'.format(alert_response.status))
            print('alert_response.acknowledged: {}'.format(alert_response.acknowledged))
            print('alert_response.is_seen: {}'.format(alert_response.is_seen))
            print('alert_response.tags: {}'.format(alert_response.tags))
            print('alert_response.snoozed: {}'.format(alert_response.snoozed))
            print('alert_response.snoozed_until: {}'.format(alert_response.snoozed_until))
            print('alert_response.count: {}'.format(alert_response.count))
            print('alert_response.last_occurred_at: {}'.format(alert_response.last_occurred_at))
            print('alert_response.created_at: {}'.format(alert_response.created_at))
            print('alert_response.updated_at: {}'.format(alert_response.updated_at))
            print('alert_response.source: {}'.format(alert_response.source))
            print('alert_response.owner: {}'.format(alert_response.owner))
            print('alert_response.priority: {}'.format(alert_response.priority))
            print('alert_response.teams: {}'.format(alert_response.teams))
            print('alert_response.integration: {}'.format(alert_response.integration))
            print('alert_response.report: {}'.format(alert_response.report))
    except ApiException as err:
        print("Exception when calling AlertApi->list_alerts: %s\n" % err)


if __name__ == "__main__":
    list_alerts()
