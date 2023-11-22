players = [
    {
    	"name": "Kevin Durant", 
    	"age":34, 
    	"position": "small forward", 
    	"team": "Brooklyn Nets"
    },
    {
    	"name": "Jason Tatum", 
    	"age":24, 
    	"position": "small forward", 
    	"team": "Boston Celtics"
    },
    {
    	"name": "Kyrie Irving", 
    	"age":32,
        "position": "Point Guard", 
    	"team": "Brooklyn Nets"
    },
    {
    	"name": "Damian Lillard", 
    	"age":33,
        "position": "Point Guard", 
    	"team": "Portland Trailblazers"
    },
    {
    	"name": "Joel Embiid", 
    	"age":32,
        "position": "Power Foward", 
    	"team": "Philidelphia 76ers"
    },
    {
        "name": "DeMar DeRozan",
        "age": 32,
        "position": "Shooting Guard",
        "team": "Chicago Bulls"
    }
]

class Player:
    def __init__(self, name, age, position, team):
        self.name = name
        self.age = age
        self.position = position
        self.team = team

class Player_information:
    def __init__(self, player_info):
        self.name = player_info.get("name")
        self.age = player_info.get("age")
        self.position = player_info.get ("position")
        self.team = player_info.get("team")
        

player_data={
        "name": "Kevin Durant", 
        "age":34, 
        "position": "small forward", 
        "team": "Brooklyn Nets"
    
}
    
player = Player_information(player_data)


print(f"Player Name:{ player.name}")
print(f"Player Age:{ player.age}")
print(f"Player Position:{ player.position}")
print(f"Player team:{ player.team}")


kevin = {
    	"name": "Kevin Durant", 
    	"age":34, 
    	"position": "small forward", 
    	"team": "Brooklyn Nets"
}
jason = {
    	"name": "Jason Tatum", 
    	"age":24, 
    	"position": "small forward", 
    	"team": "Boston Celtics"
}
kyrie = {
    	"name": "Kyrie Irving", 
    	"age":32,
        "position": "Point Guard", 
    	"team": "Brooklyn Nets"
}
    
# Create your Player instances here!
# player_jason = ??

kevin = Player(**kevin)
jason = Player(**jason)
kyrie = Player(**kyrie)

# print(f"{kevin.name} - Team: {kevin.team}, Age: {kevin.age}")
# print(f"{jason.name} - Team: {jason.team}, Age: {jason.age}")
# print(f"{kyrie.name} - Team {kyrie.team},{kyrie.age}")

new_team = []
for player_info in players:
    all_players = Player(
        name=player_info["name"],
        age=player_info["age"],
        position=player_info["position"],
        team=player_info["team"]
    )
    new_team.append(all_players)

# Print information for each Player instance in the new list
for player in new_team:
    print(f"{player.name} - Team: {player.team}, Age: {player.age}")
    
    
    /////



