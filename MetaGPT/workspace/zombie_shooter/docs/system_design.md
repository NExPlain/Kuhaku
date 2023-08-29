## Implementation approach
We will use the Pygame library, which is an open-source module for Python designed for making video games. It provides functionalities such as graphics, sound, and input handling which are essential for game development. The challenging part of this project will be implementing the collision detection between the player, zombies, missiles, and obstacles. We will also need to manage the game state, such as the player's score and the game over condition.

## Python package name
```python
"zombie_shooter"
```

## File list
```python
[
    "main.py",
    "player.py",
    "zombie.py",
    "obstacle.py",
    "missile.py",
    "game.py"
]
```

## Data structures and interface definitions
```mermaid
classDiagram
    class Player{
        +int x
        +int y
        +int speed
        +__init__(x: int, y: int, speed: int)
        +move(direction: str)
        +shoot()
    }
    class Zombie{
        +int x
        +int y
        +int speed
        +__init__(x: int, y: int, speed: int)
        +move()
    }
    class Obstacle{
        +int x
        +int y
        +int life_points
        +__init__(x: int, y: int, life_points: int)
    }
    class Missile{
        +int x
        +int y
        +int speed
        +__init__(x: int, y: int, speed: int)
        +move()
    }
    class Game{
        +int score
        +Player player
        +list[Zombie] zombies
        +list[Obstacle] obstacles
        +list[Missile] missiles
        +__init__(player: Player)
        +add_zombie(zombie: Zombie)
        +add_obstacle(obstacle: Obstacle)
        +add_missile(missile: Missile)
        +update()
        +draw()
        +check_collision()
    }
    Player "1" -- "1" Game: plays
    Zombie "0..*" -- "1" Game: spawns in
    Obstacle "0..*" -- "1" Game: spawns in
    Missile "0..*" -- "1" Game: fires from
```

## Program call flow
```mermaid
sequenceDiagram
    participant M as main
    participant G as Game
    participant P as Player
    participant Z as Zombie
    participant O as Obstacle
    participant Mi as Missile
    M->>P: create player
    M->>G: create game(P)
    loop every game tick
        M->>G: update()
        G->>P: move()
        G->>P: shoot()
        G->>Z: move()
        G->>Mi: move()
        G->>G: check_collision()
        G->>G: draw()
    end
    G->>M: game over
```

## Anything UNCLEAR
The requirement is clear to me.