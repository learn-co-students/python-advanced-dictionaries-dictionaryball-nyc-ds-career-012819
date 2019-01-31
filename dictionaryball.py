game_dictionary = {}


# players_names = [["Alan Anderson", "Reggie Evans", "Brook Lopez", "Mason Plumlee", "Jason Terry"], ["Jeff Adrien", "Bismak Biyombo", "DeSagna Diop", "Ben Gordon", "Brendan Haywood"]]

# players_home_stats = [[0, 16, 22, 12, 12, 3, 1, 1], [30, 14, 12, 12, 12, 12, 12, 7], [11, 17, 17, 19, 10, 3, 1, 15], [1, 19, 26, 12, 6, 3, 8, 5], [31, 15, 19, 2, 2, 4, 11, 1]]

# players_away_stats = [[4, 18, 10, 1, 1, 2, 7, 2], [0, 16, 12, 4, 7, 7, 15, 10], [2, 14, 24, 12, 12, 4, 5, 5], [8, 15, 33, 3, 2, 1, 1, 0], [33, 15, 6, 12, 12, 22, 5, 12]]
                      
# stat_categories = ["number", "shoe", "points", "rebounds", "assists", "steals", "blocks", "slam_dunks"]
def populate_sides():
    game_dictionary["home"] = {"team_name" : "Brooklyn Nets", "colors" : ["Black", "White"], "players" : {}}
    game_dictionary["away"] = {"team_name" : "Charlotte Hornet", "colors" : ["Turquoise", "Purple"], "players" : {}}
    
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
                    stat_dict[data[0][i]][data[j][0].lower()] = data[j][i]
                else:
                    stat_dict[data[0][i]] = {data[j][0].lower() : data[j][i]}

    return stat_dict

def populate_with_players_stats():
    for key, value in game_dictionary.items():
        stats = populate_stat(key)
        if key == "home":
            value["players"] = stats
        elif key == "away":
            value["players"] = stats
            
def game_dict():
    populate_sides()
    populate_with_players_stats()
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
    for keys, values in game_dict().items():
        if players_name in values["players"]:
            return values["players"][players_name]["points"]

def shoe_size(players_name):
    for keys, values in game_dict().items():
        if players_name in values["players"]:
            return values["players"][players_name]["shoe"]

def team_colors(team_name):
    for keys, values in game_dict().items():
        if team_name in values["team_name"]:
            return values["colors"]
        
def team_names():
    return  [game_dict()[side]['team_name'] for side in game_dict().keys()]

def player_numbers(team_name):
    numbers = []
    for keys, values in game_dict().items():
        if team_name in values["team_name"]:
            return [values['players'][player]['number'] for player in values["players"]]

def player_stats(players_name):
    for keys, values in game_dict().items():
        if players_name in values["players"]:
            return values["players"][players_name]

print(game_dict())
