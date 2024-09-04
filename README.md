# About the Project

<img src="https://github.com/Sukhman25K/Currency-Converter/blob/main/CurrencyConverter-logo.png?raw=true" alt="Image of the application's logo with the title and major currency symbols" height="600" width="600">

Being a forex trader and global economics admirer, I created a simple Python program with the help of an API (API-Ninjas) to provide real-time exchange rates for a few international currencies. To improve the user interface, I added a plain graphical user interface through Python's built-in library of Tkinter. 

# Built With
Python was used to develop this project due to its simplicity in using API requests and integrating it with simple yet friendly graphical user interfaces with Python's built-in Tkinter module. The real-time currency rates were obtained through an API provided by API Ninjas which allowed the conversion of the currencies.

### Supported Currencies:
+ Australian Dollar
+ Swiss Franc
+ Chinese Yuan
+ British Pound
+ Hong Kong Dollar
+ New Zealand Dollar
+ Polish Zloty
+ Turkish New Lira
+ South Korean Won
+ Danish Krone

# Getting Started

## Prerequisites
Check whether Python is already installed with
```
python --version
```
If Python is not installed, you can do so from the [Python website](https://www.python.org/downloads) by selecting the appropriate installer for your required environment.

To use the API, you'll need to obtain your private API key which can be done through the website <https://api-ninjas.com/>. After creating an account, you're able to view and copy your API key which would then need to be placed in the ```Constants.py``` file assigned to the ```API_KEY``` variable.



## Installation
After setting up Python, you can install the application to your local environment with the following instructions:
1. Clone the repo
   ```
   git clone https://github.com/Sukhman25K/Currency-Converter.git
   ```
2. Install any missing Python packages by replacing the name in the command 
   ```
   python -m pip install name
   ```


## Usage
After entering your private API key in the ```Constants.py``` file, you can go ahead and run the application when the installation is complete and stored in your local environment. The application can be run in different ways where the first one would be using a terminal. Navigate to the folder where the application is stored and type:
```
python Currency-Converter.py
```

Another way to run the application would be by using an IDLE such as Python's default IDLE or a code editor such as VS code.
