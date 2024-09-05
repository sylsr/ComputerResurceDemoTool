# Computer Resource Demo Tool

This command line utility is designed to simulate high CPU or memory utilization on your system. It helps demonstrate the behavior of systems under resource-intensive conditions.

## Prerequisites

1. **Python 3.12**  
   Make sure Python 3.12 is installed on your machine. You can download and install it from the official Python website:
   - [Download Python 3.12](https://www.python.org/downloads/release/python-3120/)

2. **Install Dependencies**  
   After cloning or downloading the project, you can install the required dependencies by running the following command in your terminal:
   ```bash
   pip install -r requirements.txt
## Program Usage
The program has two main modes: CPU consumption and Memory consumption. You can specify the percentage of system resources to consume using the command-line arguments.

### Command Structure
```bash
python app.py <CPU|memory> <0-100>
```
CPU or memory: Select whether to ramp up CPU or memory utilization.
0-100: Specify the percentage of available CPU or memory to consume.

### Example Commands
Simulate 100% CPU Consumption:

```bash
python app.py CPU 100
```
Simulate 50% Memory Consumption:

```bash
python app.py memory 50
```

## Note
To stop the program, press ENTER. The program will stop consuming CPU or memory, but keep in mind that stopping CPU consumption may take a few moments depending on your system's performance.