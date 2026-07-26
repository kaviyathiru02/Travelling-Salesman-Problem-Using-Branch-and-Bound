import streamlit as st
from PROGRAM import tsp_brute_force, INF

st.set_page_config(
    page_title="Travelling Salesman Problem",
    page_icon="🗺️"
)

st.title("Travelling Salesman Problem Using Branch and Bound")

cost = [
    [INF, 10, 8, 9, 7],
    [10, INF, 10, 5, 6],
    [8, 10, INF, 8, 9],
    [9, 5, 8, INF, 6],
    [7, 6, 9, 6, INF]
]

cities = ['A', 'B', 'C', 'D', 'E']

st.subheader("Cost Matrix")

display = []

for row in cost:
    r = []
    for x in row:
        r.append("INF" if x == INF else x)
    display.append(r)

st.table(display)

if st.button("Find Optimal Tour"):

    path, cost_value = tsp_brute_force(cost, len(cost))

    tour = " → ".join(cities[i] for i in path)

    st.success(f"Optimal Tour: {tour}")

    st.success(f"Minimum Cost: {cost_value}")
