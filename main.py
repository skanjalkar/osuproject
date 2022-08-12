from ossapi import *
import csv
api = OssapiV2(client_id=17213, client_secret="1AQk3DqbmdQTRmxQFkk38IwqwwjMM2jLM6bKI3N3")

# response = api.ranking("osu", RankingType.PERFORMANCE, country="US")
count = 1
with open('country.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    # writer.writerow(header)
    for i in range(1, 201):
        cursor = Cursor(page=i)
        response = api.ranking("osu", RankingType.PERFORMANCE, cursor=cursor, country="IN")
        for ranking in response.ranking:
            # print(api.user_scores(ranking.user.id, "best"))
            data = [count, ranking.user.username, ranking.pp]
            writer.writerow(data)
            top_plays = []
            try:
                for score in api.user_scores(ranking.user.id, "best"):
                    top_plays.append([score.beatmapset.title, score.beatmapset.id, score.beatmap.url, score.mods, score.pp, score.accuracy, score.rank, score.max_combo, api.beatmap(score.beatmap.id).max_combo])
            except ValueError:
                continue
            writer.writerows(top_plays)
            count += 1


