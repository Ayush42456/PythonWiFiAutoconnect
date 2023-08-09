# Python WiFi Autoconnect

## Table of Contents

1. [Overview](#overview)
2. [Installation and Usage](#installation--usage)
3. [Contributors](#contributors)
   

## Overview
This script disconnects and connects to a Wi-Fi network in a loop for a specified duration.
(!) You may need elevation (Run as administrator) privileges.

## Installation & Usage

### Step 1: Clone the Repository

Clone this repository to your local machine using the following command:

``` 
git clone <repository-url>
```

### Step 2: Navigate to the Project Directory

Change your current working directory to the root of the cloned repository:

```
cd <repository-directory>
```

### Step 3: Create the Virtual Environment

Run the following command to create a new virtual environment named `myvenv`:

```
python -m venv myvenv
```

This will create a new directory called `myvenv` in your project directory, containing all the necessary files for a virtual environment.

### Step 4: Activate the Virtual Environment

Activate the virtual environment using one of the following commands based on your operating system:

On Windows:

```
myvenv\Scripts\activate
```

On macOS and Linux:

```
source myvenv/bin/activate
```

Once activated, you will see `(myvenv)` in your command prompt, indicating that you are working within the virtual environment.

### Step 5: Install Dependencies

With the virtual environment active, install the required dependencies listed in the `requirements.txt` file:

```
pip install -r requirements.txt
```

This will ensure that all the necessary packages are installed within the virtual environment.

### Step 6: Run `main.py`

Now that the virtual environment is set up and the required dependencies are installed, you can run the `main.py` script using the following command:

```
python main.py -h
```

Example:
```
python main.py --ssid <SSID_WIFI> --run_dur 300 --disc_dur 3 --conn_dur 240
```
That will do:
- Will run the script for SSID_WIFI for 300 seconds ~ 5 minutes ( run_dur ) and after 3 seconds ( disc_dur ) it will disconnect and reconnect automatically, it will wait for 240 seconds ~ 4 minutes ( conn_dur ) and that it will repeat this for run_dur. 

### Step 7: Run `showSSID.py`

Now that the virtual environment is set up and the required dependencies are installed, you can run the `showSSID.py` script using the following command:

```
python showSSID.py
```

- This python script will show you in console as print output the SSID WiFi Name based on your connected WiFi.

The script will now be executed within the virtual environment, utilizing the installed dependencies.

### Step 7: Deactivate the Virtual Environment

Once you have finished running the script and no longer need the virtual environment, you can deactivate it using the following command:

```
deactivate
```

This will return you to your system's default Python environment.

# Contributors ✨

Thanks go to these wonderful people:

<table>
  <tbody>
    <tr>
      <td align="center"><a href="https://axbecher.com"><img src="https://avatars.githubusercontent.com/u/72851811?v=4" width="100px;" alt="Alexandru Becher"/><br /><sub><b>Alexandru Becher</b></sub></a><br />
      </td>
    </tr>
  </tbody>
</table>

Support
If you encounter any issues or need further assistance, please contact me via [axbecher.com/contact](https://axbecher.com/contact/)
# I'll be happy to help!
