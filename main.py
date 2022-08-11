from ossapi import *
import csv
api = OssapiV2(client_id=17213, client_secret="1AQk3DqbmdQTRmxQFkk38IwqwwjMM2jLM6bKI3N3")

response = api.ranking("osu", RankingType.PERFORMANCE)
bmap = api.beatmap(869019)
header = ['pp', 'difficulty']
with open('difficulty.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    for i in range(1, 201):
        cursor = Cursor(page=i)
        response = api.ranking("osu", RankingType.PERFORMANCE, cursor=cursor)
        for ranking in response.ranking:
            # print(api.user_scores(ranking.user.id, "best"))
            data = [ranking.global_rank, ranking.user.username, ranking.pp]
            writer.writerow(data)
            top_plays = []
            try:
                for score in api.user_scores(ranking.user.id, "best"):
                    print(score.beatmap.difficulty_rating)
            except ValueError:
                continue
            writer.writerows(top_plays)


