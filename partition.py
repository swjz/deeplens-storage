"""
This module partitions video clips logically - it returns division points.
"""

from typing import List, Set, Tuple, Dict

def partition(tags: Set[Tuple[str, int, int]], no_frames: int, cost_table: Dict[str, float] = dict(), default_cost: float = 1) -> List[int]:
    """partition() takes annotations of each frame, penalty for each cut and returns best partition strategy.

    Args:
        tags - set of time intervals where a tag occurs:
            { (label, start, end) }, a video from time 0 (inclusive) to time T (exclusive)
            e.g. {('cat', 3, 9), ('dog', 5, 8), ('people', 0, 6)}
            e.g. {('cat', 0, 1), ('cat', 2, 4), ('cat', 6, 8), ('dog', 0, 3),
                  ('dog', 6, 8), ('people', 0, 2), ('people', 4, 6)}
        no_frames - number of frames for this video clip
        cost_table (optional) - the skip cost (weight) for each label present.
        default_cost (optional) - cost (weight) if not found from cost_table (Default 1)

    Returns:
        divisions (list of division points) - frame indexes BEFORE which we should cut
    """

    # Step 1. Enumerate All "Cutting" Points
    # Put all start and end times into a big set including 0 and T. These enumerate the possible segment boundaries.
    # In: ('cat',1,3), ('dog',4,7), ('cat',5,7)
    # Out: [0,1,3,4,5,7]

    cutting_points = {0, no_frames}
    for tag in tags:
        _, start, end = tag
        cutting_points.add(start)
        cutting_points.add(end)

    # Step 2. Enumerate All Possible Segments (with zero cost)
    # Enumerate all pairs of cutting points returned by step 1. These enumerate the boundaries of all possible segments.
    # In: [0,1,3,7]
    # Out: [(0,1), (0,3), (0,7), (1,3), (1,7), (3,7)]

    possible_segments = set()
    for start in cutting_points:
        for end in cutting_points:
            if start < end:
                possible_segments.add((0, start, end))

    # Step 3. Assign a Skip Cost to each segment
    # For each tuple of points returned by Step 2, calculate the skip cost (number of labels present * time * weights for the labels present)
    # In: [(0,1), (0,3), (0,7), (1,3), (1,7), (3,7)]
    # Out: [(cost, 0,1), (cost, 0,3), (cost, 0,7),....]

    weighted_segments = set()
    for segment in possible_segments:
        for tag in tags:
            if tag[1] >= segment[2] or tag[2] <= segment[1]:
                continue
            length = segment[2] - segment[1]
            if tag[0] in cost_table.keys():
                segment = (segment[0] + cost_table[tag[0]] * length, segment[1], segment[2])
            else:
                segment = (segment[0] + default_cost * length, segment[1], segment[2])
        weighted_segments.add(segment)

    # Step 4. Build a directed acyclic graph
    # For each tuple returned by step 3 (now annotated with a cost) you can build a graph in the following way. 
    # - All tuples are vertices
    # - Add a directed edge -> when segment1.end == segment2.start
    # Over this graph any path that starts with a vertex segment.start == 0, and segment.end == T is full segmentation.

    

    # Step 5. Algorithm
    # For each vertex where segment.start == 0, run djikstra's algorithm to find the minimum cost path that terminates at a segment where segment.end == T
    # Return the lowest cost path for all possible start vertices.


    return path

def test():
    print("Test #1")
    tags = {('cat', 3, 9), ('dog', 5, 8), ('people', 0, 6)}
    no_frames = 9
    division = partition(tags, no_frames)
    print(division)
    
    print()
    print("Test #2")
    tags = {('cat', 0, 1), ('cat', 2, 4), ('cat', 6, 8), ('dog', 0, 3), ('dog', 6, 8), ('people', 0, 2), ('people', 4, 6)}
    no_frames = 8
    division = partition(tags, no_frames)
    print(division)

if __name__ == "__main__":
    test()
