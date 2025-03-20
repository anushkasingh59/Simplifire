# Simplifire(Fire Detection System)
#Fire Detection System
This Python script utilizes computer vision to detect fire outbreaks through a webcam. When a fire is detected, it triggers a series of actions, such as playing a sound, sending an email notification to a specified email address, and shutting down the system. Additionally, it retrieves and prints geographical information based on the user's IP address.

Prerequisites
1.Python 3.x
2.OpenCV (cv2)
3.winsound
4.os
5.time
6.smtplib
7.pyttsx3
8.email.message
9.requests
10.json
11.urlopen
Installation
Ensure you have Python installed. You can install the required dependencies using the following:


Copy code
pip install opencv-python winsound pyttsx3
Usage
Run the script using the following command:

Copy code
python your_script_name.py
The script will access the webcam (camera index 0 by default) and continuously monitor for fire using the Cascade Classifier provided (C:/Users/Hp/Documents/projects/FDS/FDSys.xml). Press 'q' to exit the program.

Features
Fire Detection: Utilizes a Cascade Classifier to identify fire in webcam frames.
Sound Notification: Plays a series of beeps when fire is detected.
Email Notification: Sends an email to a specified email address (currently commented out) with information about the detected fire.
System Shutdown: Shuts down the system after detecting fire.
Geographical Information: Retrieves and prints geographical information based on the user's IP address.
Configuration
Email Notification: Uncomment the mail() function and provide the recipient's email address and sender's Gmail credentials.
Geographical Information: The script retrieves and prints the longitude and latitude of the user's IP address.
Note: Ensure that you have the required permissions and configurations for email functionality.

Disclaimer
This script is a basic fire detection system and should be used for educational and informational purposes only. It may require additional configurations and improvements for practical applications. Use it responsibly and adhere to legal and ethical guidelines.

Some important things to remember--
In smtp(simple mail transfer protocol) you have to give your email and password which is been verified by google.

