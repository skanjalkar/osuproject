from ossapi import *
import csv
api = OssapiV2(client_id=17213, client_secret="1AQk3DqbmdQTRmxQFkk38IwqwwjMM2jLM6bKI3N3")

response = api.ranking("osu", RankingType.PERFORMANCE)
header = ['Global Rank', 'Username', 'Total_pp', 'Best_pp', "Beatmap", 'Mods', 'Beatmap_id']
with open('osudata.csv', 'a') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    for i in range(47, 201):
        cursor = Cursor(page=i)
        response = api.ranking("osu", RankingType.PERFORMANCE, cursor=cursor)
        for ranking in response.ranking:
            # print(api.user_scores(ranking.user.id, "best"))
            data = [ranking.global_rank, ranking.user.username, ranking.pp]
            writer.writerow(data)
            top_plays = []
            try:
                for score in api.user_scores(ranking.user.id, "best"):
                    top_plays.append([score.beatmapset.title, score.beatmapset.id, score.beatmap.url, score.mods, score.pp, score.rank, score.accuracy*100])
            except ValueError:
                continue

            print(data)
            print(top_plays)
            writer.writerows(top_plays)


