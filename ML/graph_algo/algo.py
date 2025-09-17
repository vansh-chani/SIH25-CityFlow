from city import getCity
import numpy as np
import matplotlib.pyplot as plt

def reRoute(city):
    reroutes = {}
    for intersection in city.intersections:
        for in_road in intersection.in_roads:
            if in_road.traffic_volume/in_road.max_capacity >= 0.8:
                print("Congestion on Road {} leading to Intersection {}".format(in_road.name, intersection.name))
                print("Suggesting alternative routes...")
                
                parent_intersection = in_road.start
                alt_roads = []
                postings = []
                for parent_out_road in parent_intersection.out_roads:
                    if parent_out_road != in_road and parent_out_road.traffic_volume/parent_out_road.max_capacity < 0.8:
                        vec_target = np.array(intersection.coords) - np.array(parent_intersection.coords)
                        vec_candidate = np.array(parent_out_road.end.coords) - np.array(parent_intersection.coords)
                        if np.linalg.norm(vec_target) > 0 and np.linalg.norm(vec_candidate) > 0:
                            cos_sim = np.dot(vec_target, vec_candidate) / (np.linalg.norm(vec_target) * np.linalg.norm(vec_candidate))
                            if cos_sim > 0.7:
                                alt_roads.append(parent_out_road)
                                postings.append(parent_intersection)
                            
                if alt_roads:
                    print("Alternative routes from Intersection {}: ".format(parent_intersection.name))
                    for road in alt_roads:
                        print("  Take Road {} to Intersection {}".format(road.name, road.end.name))

                for posting in postings:
                    print("Assigning Officer to Intersection {}".format(posting.name))

                reroutes[in_road.name] = (alt_roads, postings)
    return reroutes


def displayCity(city,reroutes):
    fig, ax = plt.subplots(1, 2, figsize=(16, 8))

    # --- First plot: Congestion Map ---
    ax[0].set_title("Congestion Map")
    for inter in city.intersections:
        x, y = inter.coords
        ax[0].scatter(x, y, color="black", s=40, zorder=3)
        ax[0].text(x+1, y+1, inter.name, fontsize=8)

    for road in city.roads:
        x1, y1 = road.start.coords
        x2, y2 = road.end.coords
        usage = road.traffic_volume / road.max_capacity

        if usage >= 0.8:
            color = "red"
            z = 5  # draw on top
        else:
            color = "blue" if road.name.startswith("OW") else "green"
            z = 3  # lower priority

        ax[0].annotate("",
                    xy=(x2, y2), xycoords='data',
                    xytext=(x1, y1), textcoords='data',
                    arrowprops=dict(arrowstyle="->", color=color, lw=1.5),
                    zorder=z)
        mx, my = (x1+x2)/2, (y1+y2)/2
        ax[0].text(mx, my, road.name, fontsize=6, color=color, zorder=z+1)

       

    ax[0].set_aspect("equal")
    ax[0].grid(True, linestyle="--", alpha=0.5)

    # --- Second plot: Rerouted Map ---
    ax[1].set_title("Rerouted Map")
    for inter in city.intersections:
        x, y = inter.coords
        ax[1].scatter(x, y, color="black", s=40, zorder=3)
        ax[1].text(x+1, y+1, inter.name, fontsize=8)

    rerouted_roads = {r for alt, _ in reroutes.values() for r in alt}
    postings = {p for _, ps in reroutes.values() for p in ps}

    for road in city.roads:
        x1, y1 = road.start.coords
        x2, y2 = road.end.coords

        if road in rerouted_roads:
            color = "yellow"
            z = 5
        else:
            color = "blue" if road.name.startswith("OW") else "green"
            z = 3

        ax[1].annotate("",
                       xy=(x2, y2), xycoords='data',
                       xytext=(x1, y1), textcoords='data',
                       arrowprops=dict(arrowstyle="->", color=color, lw=1.5))
        mx, my = (x1+x2)/2, (y1+y2)/2
        ax[1].text(mx, my, road.name, fontsize=6, color=color)

    # Mark postings with large triangles
    for post in postings:
        x, y = post.coords
        ax[1].scatter(x, y, marker="^", color="orange", s=200, zorder=4)

    ax[1].set_aspect("equal")
    ax[1].grid(True, linestyle="--", alpha=0.5)

    plt.show()
    
if __name__ == "__main__":
    city = getCity()
    reroutes = reRoute(city)
    
    if not reroutes:
        print("No Congestion Found.")
        
    else:
        displayCity(city, reroutes)