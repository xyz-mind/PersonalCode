import json
import csv

# 读取JSON文件
with open('../data/maoyan_crawler.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# 提取电影名称和票房信息
movies_info = []
for movie in data['movieList']['data']['list']:
    movie_info = {
        'movieName': movie['movieInfo']['movieName'],
        'sumBoxDesc': movie['sumBoxDesc']
    }
    movies_info.append(movie_info)

# 保存为新的JSON文件
with open('../data/extracted_movies.json', 'w', encoding='utf-8') as file:
    json.dump(movies_info, file, ensure_ascii=False, indent=4)

# 保存为CSV文件
with open('../data/extracted_movies.csv', 'w', encoding='utf-8', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=['movieName', 'sumBoxDesc'])
    writer.writeheader()
    writer.writerows(movies_info)
