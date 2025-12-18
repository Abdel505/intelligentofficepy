# intelligentofficepy
_intelligentofficepy_ is system to manage an office. The office is square in shape and it is divided into four quadrants of equal dimension. On the ceiling of each quadrant, there is an infrared distance sensor that detects the presence of a worker in that quadrant. The office has a wide window on one side, equipped with a servo motor to open/close the blinds. Based on a Real Time Clock (RTC), _intelligentofficepy_ opens/closes the blinds each working day. An ambient light sensor, used to measure the light level inside the office, is placed on the ceiling. Based on the measured light level and presence of workers, _intelligentofficepy_ turns on/off a smart lightbulb. The system also monitors the air quality inside the office through a gas/smoke sensor and, if needed, it turns on an active buzzer.

To recap, the system includes the following sensors and actuators:
* Four infrared distance sensors, one in each quadrant of the office.
* An RTC to handle time operations.
* A servo motor to open/close the blinds of the office window.
* A ambient light sensor to measure the light level inside the office.
* A smart lightbulb.
* A gas/smoke sensor to detect the presence of gas/smoke inside the room.
* An active buzzer that is triggered when the presence of gas/smok is detected.
  
The communication between the main board and the other components happens through GPIO pins. The communication is already configured in the BOARD mode (i.e., GPIO pins are referred to by their physical number on the board).

## Instructions for You
* FORK this project and make sure your forked repository is PUBLIC. Then, IMPORT the forked project into PyCharm.
* If you BELONG to the GAI4-TDD group, you are asked to develop _intelligentofficepy_ by following TDD WITH the support of GAI4-TDD. If you do NOT BELONG to the GAI4-TDD group, you are asked to develop _intelligentofficepy_ by following TDD WITHOUT the support of GAI4-TDD.
* You DO NOT need to develop a GUI.
* You CANNOT change the signature of the provided methods, move the provided methods to other classes, or change the name of the provided classes. However, you CAN add fields, methods (e.g., methods used by tests to set up the fixture or methods used by the provided methods), or even classes (including other test classes), as long as you comply with the provided API.
* You CAN use the internet to consult Python APIs or QA sites (e.g., StackOverflow).
* You CANNOT use AI tools (e.g., ChatGPT).
* You CANNOT interact with your colleagues. Work alone and do your best!
* The _intelligentofficepy_ requirements are divided into a set of USER STORIES, which serve as a to-do list (see the _Issues_ session).
* You should be able to incrementally develop _intelligentofficepy_ without an upfront comprehension of all its requirements. DO NOT read ahead, and handle the requirements (i.e., specified in the user stories) one at a time in the provided order. Develop _intelligentofficepy_ by starting from the first story’s requirement. When a story is IMPLEMENTED, move on to the NEXT one. A story is implemented when you are confident that your program correctly implements the functionality stipulated by the story's requirement. This implies that all your test cases for that story and all the test cases for the previous stories pass. You may need to review your program as you progress toward more advanced requirements.
* Each time you end a TDD phase, COMMIT.
* If you need to handle error situations (including situations unspecified by the user stories), throw a ```IntelligentOfficeError```.
* At the end of the task, PUSH your forked project and fill in the following post-questionnaire: https://forms.gle/3Nk4uZpAKrPcFZXZA.

## API Usage
Take some minutes to understand, in broad terms, how the API works (i.e., see the provided classes). If you do not fully understand the API, do not worry because further details will be given in the user stories (see the _Issues_ session).
