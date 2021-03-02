# T-Rex-Runner-CNN

<p align="center">
  <img width="694" height="116" src="https://user-images.githubusercontent.com/39219223/109692329-7189c880-7b99-11eb-8402-f42863a9d31a.gif">
</p>
![demo]()  

Teach T-Rex to dodge obstacles in 3 stages.  
  
### Stages
1- Collect dataset when playing. :video_game:  
2- Train dataset while drinking your coffee. :coffee:  
3- Start and watch it.  


### Requirements

requirements.txt consists required dependencies.  
*Easy way:*  You can install the requirements with the following commands:
```bash
cd myproject/
virtualenv venv
./venv/bin/activate
pip install -r requirements.txt
```
***

#### 1- Collect dataset when playing. :video_game:  

1. Firstly, you must specify ROI(Region Of Interest) according to screen resolution.  
![trex_map_roi](https://user-images.githubusercontent.com/39219223/109534360-52713500-7acc-11eb-9181-237cbc6c0c34.png)  

2. Change limits your specified ROI.  
```python
limits = {"top":375, "left": 740, "width":250, "height": 100 }
```  
3. Run & Play  
```bash
python trex_getdata.py
```  

When each press direction buttons, it save ROI pixels. Such like:  
![roi](https://user-images.githubusercontent.com/39219223/109530250-8e55cb80-7ac7-11eb-8f01-7881a0c517f2.png)


#### 2- Train dataset while drinking your coffee :coffee:  

Just run following command:  
```bash
python trex_train.py
```  


#### 3- Start and watch it   

Run and start the game.  
```bash
python trex_play.py
```  

---

#### :warning: IMPORTANT NOTES  :warning:

- The playing pixels and the dataset collection pixels must be the same. Because program watches and grabs your ROI pixels.
- Your score affects train and test accuracy in dataset collection stage. Also best record of T-Rex too.  
- Linux users must switch to super user mode with  ```sudo su ``` command for keyboard library. 

---

For playing T-Rex Runner: 
http://www.trex-game.skipser.com/
