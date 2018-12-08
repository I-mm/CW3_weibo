# -*- coding: utf-8 -*
# TASK5: 绘制relation map.

import pymysql
from igraph import *

db = pymysql.connect(host="39.105.165.114", user="root", password="zym2112!", use_unicode=True, charset="utf8",
                     cursorclass=pymysql.cursors.DictCursor)
cursor = db.cursor()

nodes = set()
relations = []
weights = {}
follower_num = []

cursor.execute("USE cw3_weibo;")
cursor.execute("SELECT DISTINCT follower, followee FROM follower_followee;")
output = cursor.fetchall()
print(output)
for line in output:
    nodes.add(line['follower'])
    nodes.add(line['followee'])
    relations.append((line['follower'], line['followee']))

vertex = list(nodes)
for key in vertex:
    follower_num.append(weights[key])

graph = Graph()
graph.vs['label'] = vertex
graph.vs['follower_num'] = follower_num
graph.add_vertices(vertex)
graph.add_edges(relations)
visual_style = {}
visual_style['vertex_size'] = [follower_num]
visual_style['bbox'] = (2560, 2560)
visual_style['margin'] = 10
plot(graph, 'relationship_map.png', **visual_style)

db.close()
cursor.close()
