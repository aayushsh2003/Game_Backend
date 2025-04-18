from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS

@app.route('/api/games')
def get_games():
    return jsonify([
        {
            "id": 3498,
            "title": "Grand Theft Auto V",
            "image": "https://media.rawg.io/media/games/20a/20aa03a10cda45239fe22d035c0ebe64.jpg",
            "description": "Experience the sprawling open world of Los Santos in this action-adventure game.",
            "details": "Grand Theft Auto V is an action-adventure game played from either a third-person or first-person perspective. Players complete missions—linear scenarios with set objectives—to progress through the story. Outside of the missions, players may freely roam the open world."
        },
        {
            "id": 3328,
            "title": "The Witcher 3: Wild Hunt",
            "image": "https://media.rawg.io/media/games/618/618c2031a07bbff6b4f611f10b6bcdbc.jpg",
            "description": "Join Geralt of Rivia on a quest to find his adopted daughter and battle monstrous foes.",
            "details": "The Witcher 3: Wild Hunt is an open-world action role-playing game with a third-person perspective. Players control Geralt of Rivia, a monster hunter known as a Witcher, as he searches for his missing adopted daughter."
        },
        {
            "id": 4200,
            "title": "Portal 2",
            "image": "https://media.rawg.io/media/games/2ba/2bac0e87cf45e5b508f227d281c9252a.jpg",
            "description": "Solve puzzles using a portal gun in this critically acclaimed first-person puzzle platformer.",
            "details": "Portal 2 is a first-person puzzle-platform game. The player takes the role of Chell in the single-player campaign, as one of two robots—Atlas and P-Body—in the cooperative campaign, or as a simple humanoid icon in community-developed puzzles."
        },
        {
            "id": 4291,
            "title": "Counter-Strike: Global Offensive",
            "image": "https://media.rawg.io/media/games/736/73619bd336c894d6941d926bfd563946.jpg",
            "description": "Engage in tactical team-based gameplay in this popular first-person shooter.",
            "details": "Counter-Strike: Global Offensive (CS:GO) expands upon the team-based action gameplay that it pioneered when it was launched 19 years ago. CS:GO features new maps, characters, weapons, and game modes."
        },
        {
            "id": 5286,
            "title": "Tomb Raider (2013)",
            "image": "https://media.rawg.io/media/games/021/021c4e21a1824d2526f925eff6324653.jpg",
            "description": "Join Lara Croft on her first adventure as she fights for survival on a mysterious island.",
            "details": "Tomb Raider is an action-adventure game that follows Lara Croft as she navigates a treacherous island, solving puzzles and battling enemies to survive."
        },
        {
            "id": 13536,
            "title": "Portal",
            "image": "https://media.rawg.io/media/games/7fa/7fa0b586293c5861ee32490e953a4996.jpg",
            "description": "Navigate through a series of test chambers using a portal gun in this innovative puzzle game.",
            "details": "Portal is a first-person puzzle-platform game that challenges players to solve puzzles using a unique portal gun that creates linked portals on flat surfaces."
        },
        {
            "id": 12020,
            "title": "Left 4 Dead 2",
            "image": "https://media.rawg.io/media/games/d58/d588947d4286e7b5e0e12e1bea7d9844.jpg",
            "description": "Survive the zombie apocalypse in this cooperative first-person shooter.",
            "details": "Left 4 Dead 2 is a cooperative first-person shooter that pits players against hordes of zombies in a variety of scenarios, emphasizing teamwork and strategy."
        },
        {
            "id": 4062,
            "title": "BioShock Infinite",
            "image": "https://media.rawg.io/media/games/fc1/fc1307a2774506b5bd65d7e8424664a7.jpg",
            "description": "Experience a story-driven first-person shooter set in the floating city of Columbia.",
            "details": "BioShock Infinite is a first-person shooter that combines action with a rich narrative, exploring themes of American exceptionalism and the nature of choice."
        },
        {
            "id": 802,
            "title": "Borderlands 2",
            "image": "https://media.rawg.io/media/games/49c/49c3dfa4ce2f6f140cc4825868e858cb.jpg",
            "description": "Join the hunt for loot and mayhem in this action role-playing first-person shooter.",
            "details": "Borderlands 2 is known for its cel-shaded art style, humor, and cooperative gameplay, allowing players to team up to defeat enemies and collect loot."
        }
    ])
    
if __name__ == '__main__':
    app.run(debug=True)