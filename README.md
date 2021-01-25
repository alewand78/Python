# Python
## Get Pi Online

### Description
Connect pi to the interenet.

### Lessons Learned
I learned how to set up the pi via monitor.

## Hello Python

### Description
We were to create an automatic dice rolling application.

### Screenshot
![](https://github.com/omckenn37/Engineering_4_Notebook/raw/main/Python/media/hello_python_screenshot.png)

### Lessons Learned
I learned to use while loops and if statements in python.

## Calculator

### Description
Create a calculator program that performs different opperations on two inputs.

### Screenshot
![](https://github.com/omckenn37/Engineering_4_Notebook/raw/main/Python/media/Calculato_screenshot.png)

### Lessons Learned
I learned that you cant do operations on a value if it isnt in the same format of the other value (string to int double to int).

## Quadratic solver

### Description
A new calculator program used to find the roots of a quadratic. 

### Screenshot
![](https://github.com/omckenn37/Engineering_4_Notebook/raw/main/Python/media/quadratic_solver_screenshot.png)

### Lessons Learned
I learned Arrays can help a lot when using similar varaibles.

## Strings and Loops

### Description
A program that will take an inputed string and print out the individual characters in that string.

### Screenshot
![](https://github.com/omckenn37/Engineering_4_Notebook/raw/main/Python/media/string_splitter_screenshot.png)

### Lessons Learned
I learned that you can call the individual letters of a list.

## Hangman

### Description
A two player hangman game where one person picks a word and the other guesses it.

### Screenshot
![](https://github.com/omckenn37/Engineering_4_Notebook/raw/main/Python/media/hangman1.png)
![](https://github.com/omckenn37/Engineering_4_Notebook/raw/main/Python/media/hangman2.png)
### Lessons Learned
I learned it can be very helpful to break down the big task into smaller tasks which increased my productivity.



# GPIO

## Bash

### Description
Blink two LEDs 10 times.

### Code
```
echo "Hello, World!" #print Hello, World!
gpio mode 0 out #setting the output pins
gpio mode 2 out

for (( x=0; x<=9; x++ ))  #loop that runs twice
  do  
  gpio write 0 1  #turn the leds on
  gpio write 2 1
  sleep 1         #wait one second
  gpio write 0 0  #turn them off
  gpio write 2 0
  sleep 1         #wait one second

done              #code finishes
``` 

### Lessons Learned
I learned I should probably use the linked pages.

## Python

### Description
Made an LED blink using python.

### Code
```
for x in range(10):   #loop runs 10 times
 GPIO.output(8, GPIO.HIGH) # Turn on
 sleep(1) # Sleep for 1 second
 GPIO.output(8, GPIO.LOW) # Turn off
 sleep(1) # Sleep for 1 second
 ```

### Lessons Learned
I learned that my problem might not be as big as I thought it was and to just do a bit more research when stuck.

## SSH

### Description
Connected the pi via ssh.

### Screenshot
![](https://github.com/omckenn37/Engineering_4_Notebook/raw/main/Python/media/sshpic.JPG)

### Lessons Learned
I learned that I can now use my pi anywhere I want to access it.

## I2C

### Description
Get the accelerometer data and show it on the display.

### Screenshot
![](https://github.com/omckenn37/Engineering_4_Notebook/raw/main/Python/media/i2c.JPG)

### Lessons Learned
Always double check wiring to make sure the code is the problem regarding errors.

## Hello Flask

### Description
Turned the pi into a webserver.

### Screenshot
![](https://github.com/omckenn37/Engineering_4_Notebook/raw/main/Python/media/flask.png)

### Lessons Learned
You have to be on the same network as the pi to connect.

## Flask

### Description
Turn an LED on via on and off buttons on the web.

### Screenshot
![](https://github.com/omckenn37/Engineering_4_Notebook/raw/main/Python/media/gpioflask.png)

### Lessons Learned
I learned html and css are not as hard as I remembered.

## Headless

### Description
On pi boot up, a dot that moves around the screen according to the accelerometer data.

### Screenshot
![](https://github.com/omckenn37/Engineering_4_Notebook/raw/main/Python/media/headless.JPG)

### Lessons Learned
I learned how to run scripts on the pi without it being connected to ssh.

