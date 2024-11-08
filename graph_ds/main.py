from graph_ds import Graph_Ds

# family = Graph_Ds(directed=True)
#
# family.add_vertex("Father")
# family.add_vertex("Mother")
# family.add_vertex("First Child")
# family.add_vertex("Second Child")
#
# family.add_edge("Father", "First Child")
# family.add_edge("Mother", "First Child")
#
# family.add_edge("Father", "Second Child")
# family.add_edge("Mother", "Second Child")

# print(family.dfs("Father", "Mother"))

graph = Graph_Ds(True)

for v in ["A", "B", "C", "D", "E", "F"]:
    graph.add_vertex(v)

graph.add_edge("A", "B")
graph.add_edge("B", "A")
graph.add_edge("B", "C")
graph.add_edge("B", "D")
graph.add_edge("C", "E")
graph.add_edge("D", "F")

print(graph.dfs("A", "F"))

print(graph.bfs("A", "F"))


