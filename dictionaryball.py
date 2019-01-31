game_dictionary = {}
                      
def create_top_level():
    g_dict["home"] = {"team_name" : "Brooklyn Nets", "colors" : ["Black", "White"], "players" : {}}
    g_dict["away"] = {"team_name" : "Charlotte Hornets", "colors" : ["Turquoise", "Purple"], "players" : {}}
    return g_dict
    
def populate_stat(side):
    with open(f'{side}_data.txt', 'r') as f:
        data = []
        f_content = f.readlines()
        for ele in f_content:
            if ele.endswith("\n"):
                ele = ele.replace("\n", "")
            data.append(ele.split(","))

        stat_dict = {}
        for i in range(1, len(data[0])):
            for j in range(1, len(data)):
                if data[0][i] in stat_dict:
                    stat_dict[data[0][i]][data[j][0].lower()] = int(data[j][i])
                else:
                    stat_dict[data[0][i]] = {data[j][0].lower() : int(data[j][i])}

    return stat_dict   
            
def game_dict():
    game_dictionary = create_top_level()
    for key, value in game_dictionary.items():
        stats = populate_stat(key)
        if key == "home":
            value["players"] = stats
        elif key == "away":
            value["players"] = stats
    return game_dictionary

# def good_practices():
#     for location, team_stats in game_dict().items():
#     # are you ABSOLUTELY SURE what 'location' and 'team_stats' are? use pdb.set_trace() to find out!
#         import pdb; pdb.set_trace()
#         for stats, data in team_stats.items():
#         # are you ABSOLUTELY SURE what 'stats' and 'data' are? use pdb.set_trace() to find out!
#             import pdb; pdb.set_trace()
#         # what is 'data' at each level of the for loop block? when will we be able to iterate through a list? 
#         # When would the following line of code break?
#             for item in data:
#                 print(item)
# good_practices()

def num_points_scored(players_name):
    for values in game_dict().values():
        if players_name in values["players"]:
            return values["players"][players_name]["points"]

def shoe_size(players_name):
    for values in game_dict().values():
        if players_name in values["players"]:
            return values["players"][players_name]["shoe"]

def team_colors(team_name):
    for values in game_dict().values():
        if team_name in values["team_name"]:
            return values["colors"]
        
def team_names():
    return  [game_dict()[side]['team_name'] for side in game_dict().keys()]

def player_numbers(team_name):
    for values in game_dict().values():
        if team_name in values["team_name"]:
            return [values['players'][player]['number'] for player in values["players"]]

def player_stats(players_name):
    for values in game_dict().values():
        if players_name in values["players"]:
            return values["players"][players_name]

def big_shoe_rebounds():
    max_shoe = 0
    player = None
    for values in game_dict().values():
        for key in values["players"].keys():
            if shoe_size(key) > max_shoe:
                max_shoe = shoe_size(key)
                player = key
    return player_stats(player)['rebounds']