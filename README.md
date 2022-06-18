# Castle-Defender

The game-code is organized in an OOP approach. To play the game, run "play.py" file.

Brief Description of the Game

In this game, we have 4 identical soldiers trying to defend the castle. There are 4 lanes on which each of these 4 soldiers stay stationary. We also have 4 different types of attacks with different damage power coming randomly from these lanes with an increasing creation speed. We have 4 different types of defenses, each having a different damage against attacks. Once a defense is used against an attack, it either reduces the damage of the attack or completely destroys it depending on the damage powers of both items. There is a menu bar on the screen from which the player can drag and drop defense on a soldier. A defense can only be used once for every drag-and-drop. If the player wants to use a defense again, she should drag-and-drop that defense once more. That is, soldiers shoot when a defense is dragged and dropped on them, and once they shoot, they become inactive again, until a defense is dragged and dropped on them once more. There are also game gold and score in the menu bar. Game gold is spent for using defense, and every defense has a specific number of game-golds-needed to be used. Game gold regularly increases in specific time intervals. Score indicates how long the castle is defended against attacks. Moreover, there are 500 hit points assigned to the castle. If the castle doesn’t get hit for 10 seconds, hit points increase by 10. When an attack hits the castle, hit points decrease. The game eventually ends when the hit points become 0 or score becomes 40.