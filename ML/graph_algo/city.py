import random
import matplotlib.pyplot as plt

class Road:
    def __init__(self, name, start, end, traffic_volume, max_capacity):
        self.name = name
        self.start = start
        self.end = end
        self.traffic_volume = traffic_volume
        self.max_capacity = max_capacity
        
class Intersection:
    def __init__(self, name, coords, inroads=None, outroads=None):
        self.name = name
        self.coords = coords
        self.in_roads = inroads if inroads is not None else []
        self.out_roads = outroads if outroads is not None else []

class City:
    def __init__(self, name, intersections=None, roads=None):
        self.name = name
        self.intersections = intersections if intersections is not None else []
        self.roads = roads if roads is not None else []

# Helper to create random traffic values
def traffic():
    return random.randint(20, 80), random.randint(80, 100)


def getCity():
        

    # Create intersections with your labeled coordinates
    intersections = [
        Intersection("INT1", (0,0)),
        Intersection("INT2", (5,25)),
        Intersection("INT3", (35,5)),
        Intersection("INT4", (30,40)),
        Intersection("INT5", (40,30)),
        Intersection("INT6", (25,70)),
        Intersection("INT7", (75,25)),
        Intersection("INT8", (55,75)),
        Intersection("INT9", (80,50)),
        Intersection("INT10", (80,80)),
    ]

    # Dict for lookup
    ints = {i.name:i for i in intersections}

    roads = []

     # One-way roads
    oneways = [
        ("OW1","INT2","INT6"),
        ("OW2","INT6","INT4"),
        ("OW3","INT6","INT8"),
        ("OW4","INT2","INT5"),
        ("OW5","INT5","INT3"),
        ("OW6","INT5","INT7"),
        ("OW7","INT6","INT9"),
    ]

    for name, s, e in oneways:
        vol, cap = traffic()
        road = Road(name, ints[s], ints[e], vol, cap)
        roads.append(road)
        ints[s].out_roads.append(road)   # append object
        ints[e].in_roads.append(road)    # append object


    # Two-way roads
    twoways = [
        ("TW1","INT1","INT2"),
        ("TW2","INT1","INT3"),
        ("TW3","INT2","INT4"),
        ("TW4","INT3","INT7"),
        ("TW5","INT4","INT8"),
        ("TW6","INT4","INT3"),
        ("TW7","INT5","INT9"),
        ("TW8","INT7","INT9"),
        ("TW9","INT9","INT10"),
        ("TW10","INT8","INT10")
    ]

    for base, s, e in twoways:
        vol, cap = traffic()
        road_a = Road(base+"a", ints[s], ints[e], vol, cap)
        roads.append(road_a)
        ints[s].out_roads.append(road_a)   # append object
        ints[e].in_roads.append(road_a)    # append object
        
        vol, cap = traffic()
        road_b = Road(base+"b", ints[e], ints[s], vol, cap)
        roads.append(road_b)
        ints[e].out_roads.append(road_b)   # append object
        ints[s].in_roads.append(road_b)    # append object


    # Create city
    city = City("MyCity", intersections, roads)
    
    return city


if __name__ == "__main__":
    city = getCity()
    def plot_city(city):
        fig, ax = plt.subplots(figsize=(10,8))
        
        # Plot intersections
        for inter in city.intersections:
            x, y = inter.coords
            ax.scatter(x, y, color="black", s=50, zorder=3)
            ax.text(x+1, y+1, f"{inter.name}\n({x},{y})", fontsize=8)
        
        # Plot roads
        for road in city.roads:
            x1, y1 = road.start.coords
            x2, y2 = road.end.coords
            
            # color: one-way blue, two-way green
            color = "blue" if road.name.startswith("OW") else "green"
            
            ax.annotate("",
                        xy=(x2, y2), xycoords='data',
                        xytext=(x1, y1), textcoords='data',
                        arrowprops=dict(arrowstyle="->", color=color, lw=1.5))
            
            # put road name near the middle
            mx, my = (x1+x2)/2, (y1+y2)/2
            ax.text(mx, my, road.name, fontsize=6, color=color)
        
        ax.set_aspect("equal")
        ax.set_title(city.name)
        plt.grid(True, linestyle="--", alpha=0.5)
        plt.show()

    plot_city(city)
