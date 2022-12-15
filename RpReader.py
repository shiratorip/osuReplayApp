from osrparse import Replay
# parse from a path
def getGraf(filePath):
    replay = Replay.from_path(filePath)

    # a replay has various attributes
    r = replay
    #print(r.mode, r.game_version, r.beatmap_hash, r.username,
    #    r.replay_hash, r.count_300, r.count_100, r.count_50,
     #   r.count_geki, r.count_miss, r.score, r.max_combo, r.perfect,
      #  r.mods, r.life_bar_graph, r.timestamp, r.replay_data,
       # r.replay_id, r.rng_seed)

    X = list()
    Y = list()
    for i in range (0, len(r.life_bar_graph)):
        X.append(r.life_bar_graph[i].time)
        Y.append(r.life_bar_graph[i].life)

    LENGTH = len(r.life_bar_graph)
    listR = []
    listR.append(X)
    listR.append(Y)
    return listR
