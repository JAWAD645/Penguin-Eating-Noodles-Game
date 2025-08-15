


# 🐧 Pengu Snake – Python Arcade Game 🍜

A modern, fun twist on the **classic Snake and Apple game from old Java phones**.
In this version, the snake is replaced by a **penguin** 🐧, and the apple is replaced by a **bowl of noodles** 🍜.
The gameplay and mechanics remain the same — eat the food to grow longer, avoid colliding with yourself, and aim for the highest score.



## 📌 Overview

**Pengu Snake** is a Python-based arcade game created using **Pygame**.
It features:

* Custom **penguin sprite** for the snake body.
* **Noodles bowl sprite** as the food.
* Smooth movement and collision detection.
* Background music and sound effects for eating and game over.
* Score display and restart functionality.



## 🎮 Gameplay

* Use **arrow keys** to move the penguin around the screen.
* Eat the **noodles bowls** to grow longer and increase your score.
* Avoid running into yourself — doing so ends the game.
* After game over, press **Enter** to restart.



## 🛠 Features

* **Custom Sprites**: Penguin for snake segments, noodles bowl for food.
* **Background Music**: Loops continuously during gameplay.
* **Sound Effects**:

  * Eating noodles 🍜 → *"bruh"* sound effect.
  * Colliding with yourself → *"uwu"* sound effect.
* **Scoreboard**: Displays current score in real-time.
* **Game Over Screen**: Shows total noodles eaten with option to restart.



## 🎯 Controls

| Key       | Action       |
| --------- | ------------ |
| ⬅️        | Move Left    |
| ➡️        | Move Right   |
| ⬆️        | Move Up      |
| ⬇️        | Move Down    |
| **Enter** | Restart Game |
| **Esc**   | Quit Game    |



## 📐 Technical Details

* **Language**: Python 3
* **Libraries**: `pygame`, `time`, `random`
* **Sprites**: Located in `resources/` directory (`peng.jpg`, `noodles.png`, background image, sound files).
* **Grid Size**: 40×40 pixels per block.
* **Window Size**: 1000×1000 pixels.



## 📂 Project Structure

```
PenguSnake/
│── main.py                # Main game code
│── resources/
│   ├── peng.jpg            # Penguin sprite
│   ├── noodles.png         # Noodles sprite
│   ├── mainbg.jpg          # Background image
│   ├── bg.mp3              # Background music
│   ├── bruh-sound-effect.mp3  # Eating sound
│   ├── uwu-sound-effect.mp3   # Game over sound
```



## 🖼 Screenshots


First view:

<img src="https://github.com/JAWAD645/Penguin-Eating-Noodles-Game/blob/743090008a6e7caaba4365553b0c1446cfc78bd9/Initial.png" alt="Preview" width="400">


After eating:

<img src="https://github.com/JAWAD645/Penguin-Eating-Noodles-Game/blob/743090008a6e7caaba4365553b0c1446cfc78bd9/After%20Eating.png" alt="Preview" width="400">

Game over message:

<img src="https://github.com/JAWAD645/Penguin-Eating-Noodles-Game/blob/743090008a6e7caaba4365553b0c1446cfc78bd9/Game%20over%20message.png" alt="Preview" width="400">

Play this to get an overview:

<img src="https://github.com/JAWAD645/Penguin-Eating-Noodles-Game/blob/743090008a6e7caaba4365553b0c1446cfc78bd9/Penguin_Eating_Noodles_Demo.gif" alt="Preview" width="400">

## 📥 Installation & Running

### 1️⃣ Install Python

Make sure **Python 3.8+** is installed.
[Download Python](https://www.python.org/downloads/)

### 2️⃣ Install Dependencies

```bash
pip install pygame
```

### 3️⃣ Run the Game

```bash
python main.py
```



## 🔮 Future Improvements

* Add different difficulty levels (speed increase over time).
* Power-ups (bonus points, slow motion).
* High score saving system.
* Mobile-friendly touch controls.
* Enhancing the game more and add more features.



## 👨‍💻 Author

**Jaawad Tashick**
*Computer Science Graduate*


