
class WP:
    id = ""
    links = []
    def __init__(self, id, links):
        self.id=id
        self.links=links


# def leastClicks(start_page, end_page)
# returns the shortest path of links between start page and end page.

# leastClicks(WikipediaPage_1, WikipediaPage_2) wp_1 has link to wp_x, wp_x has link to wp_2
# 1 -> x -> 2
# return [WikipediaPage_1, WikipediaPage_x, WikipediaPage_2]

"""
S - x1 - x - x - x - x - x - x - x - x - x - x ... - E
\---------------------------------------------------/
  x1   x4
 /  \ /  \
S   x2    E
 \  /
  x3
Average page links = N links
Average distance between S and E is M links

Time:  O(M * N)
Space: O(M * N)
"""

def test():
    f=WP(0, [])
    e=WP(1, [f])
    d=WP(2, [e])
    c=WP(3, [f])
    b=WP(4, [d])
    a=WP(5, [b, c])
    print [v.id for v in leastClicks(a, f)]

def leastClicks(start_page, end_page):
    def least_click_helper(path, link):
        if end_page == link:
            path.append(link)
            res.append(path)
            return
        for sub_link in link.links:
            least_click_helper(path + [link], sub_link)
    res = []
    least_click_helper([], start_page)
    min_path_len = float("inf")
    shortest_path = None
    for path in res:
        if len(path) < min_path_len:
            shortest_path = path
            min_path_len  = len(path)
    return shortest_path
