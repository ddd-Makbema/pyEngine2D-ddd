# Screen
Starts the screen for the game and initializes default variables.

## Attributes
| attribute | discription |
| ---- | ---- |
| width | The width in pixels of the game screen by default. It can be still set to fullscreen|
| height | The height in pixels of the game screen by default. It can still be set to fullscreen | 
| fixed_fps/ffps | How fast the physics updates. will remain eventually consistent no matter the speed of the computer |
| fps | How fast the screen updates. Can be variable but aims for the set amount |
| name_window | The name displayed at the top of the screen and in the taskbar |
| icon | Image from the data folder displayed at the top left of the window. does not change the image in the taskbar |
| screen | Instance of the screen loaded from pygame |
| clock | Instance of the clock class loaded from pygame allows fps monitering |
| start_velocity | default value of (0,0) to put in for velocity |
| white | rgb value for white to easily color shapes or fill the backround of the screen with |
| black | same but for black|
| red | same but for red |
| green | same but for green |
| blue | same but for blue |

## Functions

frame_end: Updates the screen for the new frame

## Useage

Users should not have to touch the frame_end function. <br />
Users shold, though, feel free to access the Screen class when adding basic shapes to the screen and accessing the colors.