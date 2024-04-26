# OIBSIP
# Oasis Infobyte Tasks
# Task 1 𝗩𝗼𝗶𝗰𝗲 𝗔𝘀𝘀𝗶𝘀𝘁𝗮𝗻𝘁 
Are you fascinated by virtual assistants like Siri, Alexa, or Google Assistant? Ever wondered how they work and wished to create your own? Well, you're in luck! In this post, I'll guide you through the process of building a simple voice assistant using Python.

# Introduction
In today's tech-savvy world, voice assistants have become an integral part of our lives. They help us perform various tasks hands-free, from setting reminders to playing music and even controlling smart home devices. With the power of Python and a few external libraries, you too can create your very own voice assistant tailored to your needs.

# Getting Started
First, let's outline the key components you'll need:

**Speech Recognition:** To convert speech into text.
**Text-to-Speech (TTS):** To convert text into speech.
**Subprocess:** To execute system commands.
**Datetime:** To get the current time.
**PyWhatKit:** To interact with online services like YouTube.

# Task 2 𝗕𝗠𝗜 𝗖𝗮𝗹𝗰𝘂𝗹𝗮𝘁𝗼𝗿
Certainly! Here's a GitHub description for the provided Python script:

---

### BMI Calculator

This Python script calculates Body Mass Index (BMI) based on weight and height inputs and categorizes the BMI value into different weight categories.

#### Features:
- **BMI Calculation**: Calculates BMI using the formula: BMI = weight (kg) / (height (m) * height (m)).
- **Result Interpretation**: Interprets the BMI value and categorizes it as Underweight, Normal weight, Overweight, or Obese.
- **User Interaction**: Prompts the user to input weight and height and displays the calculated BMI along with the corresponding weight category.

#### Usage:
1. Clone the repository.
2. Run the script.
3. Input your weight in kilograms and height in meters when prompted.
4. Get your BMI value and corresponding weight category.

#### How to Use:
```bash
python bmi_calculator.py
```

#### Example Output:
```
Enter your weight in kilograms: 70
Enter your height in meters: 1.75
Your BMI is 22.86, which is Normal weight.
```

#### Note:
- Ensure Python is installed on your system to run the script.
- This script serves as a simple BMI calculator tool and is intended for educational purposes only.

# Task 3 𝗥𝗮𝗻𝗱𝗼𝗺 𝗣𝗮𝘀𝘀𝘄𝗼𝗿𝗱 𝗚𝗲𝗻𝗲𝗿𝗮𝘁𝗼𝗿

### Random Password Generator

This Python script generates random passwords based on user preferences for password length and character sets (letters, digits, and symbols).

#### Features:
- **Customizable Passwords**: Allows users to specify the length of the password and choose which character sets to include (letters, digits, symbols).
- **Secure Randomization**: Utilizes Python's `random` module to ensure randomness and unpredictability of generated passwords.
- **User Interaction**: Guides users through the process of generating a password with a simple command-line interface.

#### Usage:
1. Clone the repository.
2. Run the script.
3. Enter the desired length of the password and choose which character sets to include when prompted.
4. Receive a randomly generated password based on your preferences.

#### How to Use:
```bash
python password_generator.py
```

#### Example Output:
```
Welcome to our random password generator
Enter the length of your password: 12
Include letters? (yes/no): yes
Include digits? (yes/no): yes
Include symbols? (yes/no): no
Your generated password is: j9u8W3o5T6y0
```

#### Note:
- Ensure Python is installed on your system to run the script.
- This script provides a simple and customizable tool for generating random passwords and is intended for educational and personal use only.

# Task 4 𝗖𝗵𝗮𝘁 𝗔𝗽𝗽𝗹𝗶𝗰𝗮𝘁𝗶𝗼𝗻

### Python Chat Application

This Python script implements a basic client-server chat application using sockets and threading, allowing multiple clients to connect to a server and exchange messages in real-time.

#### Features:
- **Client-Server Architecture**: Utilizes sockets to establish communication between a server and multiple clients.
- **Threading**: Implements threading to handle multiple client connections concurrently without blocking the main execution.
- **Message Broadcasting**: Allows clients to send messages to the server, which then broadcasts them to all connected clients.
- **Simple Command Interface**: Provides a simple command-line interface for users to input messages and exit the application.

#### Usage:
1. Clone the repository.
2. Run the server script to start the server.
3. Run the client script to connect to the server.
4. Input messages in the client terminal to send to the server and other connected clients.

#### How to Use:
```bash
# Start the server
python chat_server.py

# Start a client
python chat_client.py
```

#### Example Output:
```
[LISTENING] Server is listening on 127.0.0.1:5050
[NEW CONNECTION] ('127.0.0.1', 12345) connected.
Hello from client!
Hello from server!
How are you?
I'm fine, thank you!
exit
[DISCONNECTED] ('127.0.0.1', 12345) disconnected.
```

#### Note:
- Ensure Python is installed on your system to run the scripts.
- This script provides a simple foundation for building more complex chat applications and is intended for educational and personal use only.

# Task 5 𝗪𝗲𝗮𝘁𝗵𝗲𝗿 𝗔𝗽𝗽𝗹𝗶𝗰𝗮𝘁𝗶𝗼𝗻

### Weather Information Fetcher

This Python script allows users to fetch weather information for a specific location using the OpenWeatherMap API.

#### Features:
- **OpenWeatherMap Integration**: Utilizes the OpenWeatherMap API to retrieve real-time weather data.
- **Location Flexibility**: Accepts city names or ZIP codes as input to fetch weather information for any location worldwide.
- **Temperature Units**: Displays temperature in Celsius units for user convenience.
- **Error Handling**: Provides error messages in case of invalid input or API errors.

#### Usage:
1. Clone the repository.
2. Obtain an API key from OpenWeatherMap and replace the placeholder with your API key in the script.
3. Run the script and input the desired city name or ZIP code when prompted.
4. View the fetched weather information in the terminal.

#### How to Use:
```bash
python weather_fetcher.py
```

#### Example Output:
```
Enter city name or ZIP code: London
Weather in London, GB:
Temperature: 15°C
Humidity: 82%
Weather Conditions: Overcast clouds
```

#### Note:
- Ensure Python is installed on your system to run the script.
- Obtain an API key from OpenWeatherMap by signing up on their website to use the service.
- This script provides a simple way to fetch weather information and is intended for educational and personal use only.

