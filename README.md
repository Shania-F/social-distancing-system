# social-distancing-system
comprehensive program with automated ai face mask and temperature detection, as well as capacity control

To keep people safe during Covid-19, health authorities have recommended face masks and temperature checks, which requires extra human labour in the form of an employee at check-points near the entrances. This system uses AI to automate the process. First, it accurately detects if people are wearing masks. 
   ###### Detecting a Face Mask
<img width="196" alt="maskop" src="https://user-images.githubusercontent.com/101061656/157931424-7661d8b9-7f75-4a8a-9d73-e145fbb7d7b3.png">

Those not wearing masks are denied access by sending a pop-up message. The system also checks temperature, and keeps a current count of people inside the building, as public places are advised to allow only 50% of their usual capacity of people to avoid overcrowding. It will deny entrance if the temperature is too high, or if the building is already at recommended capacity, thus making it an all-in-one system.
   ###### Capacity Control
![capcontrol](https://user-images.githubusercontent.com/101061656/157931945-ad7e4e86-d618-4676-b3f1-fe449dbb0ab0.jpg)

This kind of system can be used at airports, hospitals, malls and other public places. It is coded in Python and trained using an extensive dataset of 700+ images to achieve close to 99% accuracy.
   ###### Loss and Accuracy Graph
![image](https://user-images.githubusercontent.com/101061656/157932660-c5af0561-4fc3-4d2f-842a-ed446d8fa5ed.png)
