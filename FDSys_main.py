import cv2
import sys
import winsound
import os
import time
import smtplib
import pyttsx3
import requests
import json
from urllib.request import urlopen
from email.message import EmailMessage

# Camera Check Block
def check_camera():
    capture = cv2.VideoCapture(0)  # Default camera
    if not capture.isOpened():
        print("Error: Camera could not be opened. Ensure it is not in use by another application.")
        sys.exit()  # Exit program if camera is unavailable
    else:
        print("Camera is working!")
        capture.release()

# Geolocation Initialization
def initialize_geolocation():
    try:
        r = requests.get('https://get.geojs.io/')
        ip_request = requests.get('https://get.geojs.io/v1/ip.json')
        ipAdd = ip_request.json()
        url = 'https://ipinfo.io/json'
        response = urlopen(url)
        data = json.load(response)
        geo_url = f'https://get.geojs.io/v1/ip/geo/{data["ip"]}.json'
        geo_request = requests.get(geo_url)
        geo_data = geo_request.json()
        print("Longitude:", geo_data['longitude'])
        print("Latitude:", geo_data['latitude'])
        return geo_data['longitude'], geo_data['latitude']
    except Exception as e:
        print("Error initializing geolocation:", e)
        return "0", "0"  # Default values if geolocation fails

# Function for Text-to-Speech
def say(text):
    engine = pyttsx3.init('sapi5')
    voice = engine.getProperty('voices')
    engine.setProperty('voice', voice[0].id)
    engine.setProperty('rate', 150)
    print(f"firedetector: {text}")
    engine.say(text)
    engine.runAndWait()

# Function for Beeping Alert
def beep(duration=1000):
    frequency = 2500  # Frequency in Hertz
    winsound.Beep(frequency, duration)

# Function to Shutdown Program
def shutdown():
    time.sleep(1)
    sys.exit()

# Main Fire Detection System
if __name__ == '__main__':
    check_camera()  # Validate the camera before proceeding

    # Load Haar Cascade XML
    firedetector = cv2.CascadeClassifier(r"C:\Users\anush_bgwmxxp\Downloads\FDSys.xml")  # Update path if necessary
    if firedetector.empty():
        print("Error: Haar Cascade XML file could not be loaded. Check the file path.")
        sys.exit()

    # Initialize Geolocation
    longitude, latitude = initialize_geolocation()
    location_url = f"https://www.google.com/maps/place/bennett university/@{longitude},{latitude}"

    # Initialize Video Capture
    capture = cv2.VideoCapture(0, cv2.CAP_MSMF)  # CAP_MSMF or CAP_DSHOW based on your system
    if not capture.isOpened():
        print("Error: Camera could not be opened. Ensure it is not in use by another application.")
        sys.exit()

    capture.set(3, 500)  # Optional: Set width
    capture.set(4, 500)  # Optional: Set height

    try:
        while True:
            ret, frame = capture.read()
            if not ret:
                print("Error: Could not fetch frame.")
                break

            # Convert frame to grayscale and detect fire
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            fire = firedetector.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3, minSize=(30, 30))

            for (x, y, w, h) in fire:
                print(f"Fire detected at [{x}, {y}, {w}, {h}]")
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)  # Draw bounding box
                cv2.putText(frame, "Fire Detected!", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)

                # Trigger alerts
                say("Fire has been detected.")
                for _ in range(5):
                    beep()
                say("Mail has been sent to your guardian.")
                for _ in range(5):
                    beep()

                # Shutdown system (or exit loop)
                shutdown()

            # Display video feed
            cv2.imshow('Fire Detection System', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):  # Press 'q' to exit
                break
    finally:
        # Release resources
        capture.release()
        cv2.destroyAllWindows()
