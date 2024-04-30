# Program Description: 
# This code defines a Flask web application that listens for incoming POST requests.
# It validates the HMAC signature in the request against an expected signature.
# If the request is of type 'application/json', it processes the webhook data.
# If the 'activityTrigger' in the webhook data is 'MOTION', it triggers the 'reader_trigger' function.
# The 'reader_trigger' function unlocks a door using a Rhombus Systems API.
# Dependencies: Flask, requests, ran on an ngrok server
# Note: Ensure that Flask, ngrok (virutal server of choice) and requests are installed before running this code.
# Place URL from ngrok server in Rhombus Webhook URL
# Need to ensure camera policy is set up to trigger the webhook
# Start flask server and use ngrok to create a public URL

import requests
import hmac
import hashlib
from flask import Flask, request, jsonify
# AC testing API key uFfVaIhTTV6pFnteWu3x_A
app = Flask(__name__)
secret_key = "Mo-zWySyTKuoOMVUiTHKvw"  #key provided by rhombus in webhook integration

def validate_hmac_signature(received_signature, request_data):
    expected_signature = hmac.new(secret_key.encode('utf-8'), request_data, hashlib.sha256).hexdigest()
    if received_signature is not None:
        return hmac.compare_digest(expected_signature, received_signature)
    else:
        return False

@app.route('/', methods=['POST'])
def listen_for_webhook():
    print("Received POST request")
    
    content_type = request.headers.get('Content-Type')
    
    if content_type == 'application/json':
        webhook_data = request.json
        print("Webhook data:", webhook_data)

        activity_trigger = webhook_data.get('activityTrigger')
        # vehicle_label = webhook_data.get('vehicleAlertLabelSet')
        if activity_trigger in ['FACE_ALERT']: #and vehicle_label in ['ACLPR'] : #change to identified license plate label
            reader_trigger(webhook_data)
            add_index(reader_trigger, webhook_data)
            return jsonify({'message': 'Webhook received successfully', 'data': webhook_data}), 200
        else:
            print('No Match')
            return "No Match", 500
    else:
        print("invalid content type")
        return
    
def reader_trigger(webhook_data):
    activity_trigger = webhook_data.get('activityTrigger')
    # vehicle_label = webhook_data.get('vehicleAlertLabelSet')
    if activity_trigger in ['FACE_ALERT']: #and vehicle_label in ['access control']: #change to identified license plate label
        reader_trigger = True
        print("action detected")

        url = "https://api2.rhombussystems.com/api/accesscontrol/unlockAccessControlledDoor" 
        payload = { "accessControlledDoorUuid": "uk0gTw3WTIC216HbTClSAA" } #replace value with door uuid
        headers = {
            "accept": "application/json",
            "x-auth-scheme": "api-token",
            "content-type": "application/json",
            "x-auth-apikey": "2s8o6B40SeK6TkTC5tCinw" #replace value with api key
        }

        response = requests.post(url, json=payload, headers=headers)
        print('Door Unlocked')

def add_index(reader_trigger, webhook_data):
    activity_trigger = webhook_data.get('activityTrigger')
    if activity_trigger in ['FACE_ALERT']:
        index_trigger = True
        print("trigger detected")
        timestamp_ms = webhook_data.get('timestampMs')
     
        url = "https://api2.rhombussystems.com/api/camera/createCustomFootageSeekpoints"
        payload = {
        "CameraUuid": "Lnla4BZVQvul8hMO8qr68Q",
        "footageSeekPoints": [
            {
                "color": "TEAL",
                "name": "License Plate Authenticated", #change name of index point
                "timestampMs": timestamp_ms
            }
        ]
        }
        headers = {
            "accept": "application/json",
            "x-auth-scheme": "api-token",
            "content-type": "application/json",
            "x-auth-apikey": "2s8o6B40SeK6TkTC5tCinw"
        }

        response = requests.post(url, json=payload, headers=headers)
        print('Index Created')
        

if __name__ == '__main__':
    app.run(debug=True)

