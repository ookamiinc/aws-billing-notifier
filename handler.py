import json
import boto3
from lib import requests
from datetime import datetime, timedelta

client = boto3.client("cloudwatch", region_name='us-east-1')


def get_service_billing(serviceName):
    start_time = datetime.now() - timedelta(days=1)
    end_time = datetime.now()
    dimensions = [
        {
            'Name': 'Currency',
            'Value': 'USD'
        }
    ]
    if serviceName is not 'Total':
        dimensions.append(
            {
                'Name': 'ServiceName',
                'Value': serviceName
            }
        )
    response = client.get_metric_statistics(
        Namespace='AWS/Billing',
        MetricName='EstimatedCharges',
        Dimensions=dimensions,
        StartTime=start_time,
        EndTime=end_time,
        Period=86400,
        Statistics=[
            'Average'
        ]
    )
    return response


def send_slack(url, channel, payload):
    if channel is not "":
        payload['channel'] = channel
    data = json.dumps(payload)
    requests.post(url, data)


def get_latest_billing(serviceName):
    response = get_service_billing(serviceName)
    return response['Datapoints'][0]


def get_services():
    response = client.list_metrics(
        Namespace='AWS/Billing',
        MetricName='EstimatedCharges'
    )
    services = []
    for r in response['Metrics']:
        for d in r['Dimensions']:
            if d['Name'] == 'ServiceName':
                services.append(d['Value'])
    return services


def get_billings():
    services = get_services()
    billings = []
    for s in services:
        billing = get_latest_billing(s)
        billings.append({'service': s, 'billing': billing['Average']})
    return billings


def message_payload():
    billings = get_billings()
    fields = []
    for b in billings:
        fields.append({
            'title': b['service'],
            'value': "{:,.1f} USD".format(b['billing']),
            'short': 'true'
        })
    total = get_latest_billing('Total')
    msg = '今月のAWSの利用費は、{:,.1f} USDです。'.format(total['Average'])
    attachments = [
        {
            'fallback': msg,
            'pretext': msg,
            'color': 'good',
            'fields': fields
        }
    ]
    return {'attachments': attachments}


def handle_event(e):
    payload = message_payload()
    send_slack(e['url'], e['channel'], payload)
    return payload


def lambda_handler(event, context):
    print("Received event raw: " + json.dumps(event))
    print("Received event: " + json.dumps(event, indent=2))
    try:
        sent_payload = handle_event(event)
        return sent_payload
    except Exception as e:
        print(e)
        raise e
