Humanoid
========

Humanoid with moving parts. Made in PyOpenGL

The code generates a humanoid using Heirarchical Modelling. As heirarchical modelling is being followed, the code can be written and read in fragments, one for each part and rotation(as written in code comments). Each fragment has been given rotation parameters and the part coded in the fragment rotates on the key press(Key mapping listed below). Here the main thing to note is that the heirarchy coding has been done with root being the torso/body. The initial values are specified in the rotate array and can be changed if the default look of the humanoid is to be changed.

All the appendages of the humanoid can move in multiple ways (specified in controls) as well as there are 2 keys for special moves: dance and handshake. These are infinitely looped moves and will continue till stop key for the corresponding move is pressed. It is important to note here that dance is basically freestyle random motion of the humanoid and in handshake the torso of the humanoid is rotated and hand is moved.

The main modules here are robot, keyboard and TimerFunc (Timer Function). The robot module can be divided into sub-parts: Head, Body, Right Upper Arm, Right Lower Arm, Left Upper Arm, Left Lower Arm, Right Upper Leg, Right Lower Leg, Left Upper Leg, Left Lower Leg. Here each of these sub-modules is coded independently but connected via the heirarchy. The keyboard module can be broken down into: Rotation with respect to body, Rotation on axis, Movement with respect to screen, Dance and Handshake. The TimerFunc has only been used so that entire dance and handshake can be executed and user need not have the key pressed.


CONTROLS:-
KEY		ACTION
w			Rotates the body with head fixed
W			Same action as w but in opposite direction

a			Rotates the Left Arm around the body
A			Same action as a but in opposite direction
s			Rotates the Left Lower Arm around the upper arm
S			Same action as s but in opposite direction
d			Rotates the Right Arm around the body
D			Same action as d but in opposite direction
f			Rotates the Left Lower Arm around the upper arm
F			Same action as f but in opposite direction

z			Rotates the Left Leg around the body
Z			Same action as z but in opposite direction
x			Rotates the Left Lower Leg around the upper arm
X			Same action as x but in opposite direction
c			Rotates the Right Leg around the body
C			Same action as c but in opposite direction
v			Rotates the Left Lower Leg around the upper arm
V			Same action as v but in opposite direction

u			Rotates the Left Arm on its axis(Screwdriver type motion)
U			Same action as u but in opposite direction
i			Rotates the Right Arm on its axis(Screwdriver type motion)
I			Same action as i but in opposite direction
o			Rotates the Left Leg on its axis(Screwdriver type motion)
O			Same action as o but in opposite direction
p			Rotates the Right Leg on its axis(Screwdriver type motion)
P			Same action as p but in opposite direction

m			Rotates the humanoid back to front wrt screen
M			Same action as m but in opposite direction
n			Rotates the humanoid side to side wrt screen
N			Same action as n but in opposite direction
e			Brings the humanoid closer wrt screen
E			Same action as e but in opposite direction
r			Sends the humanoid upwards wrt screen
R			Same action as r but in opposite direction

j			Start (freestyle) dance. Continues till J is pressed
J			Stop dance

k			Start handshake. Continues till K is pressed
K			Stop handshake

q			Reset the humanoid to staring position and alignment
Esc			Quits the program and closes the display window
