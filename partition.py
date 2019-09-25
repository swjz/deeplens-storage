"""
This module partitions video clips logically - it returns division points.
"""

from typing import List, Dict

def partition(tags: Dict[str, List[int]], no_frames: int, penalty: float = 1.5) -> List[int]:
    """partition() takes annotations of each frame, penalty for each cut and returns best partition strategy.

    Args:
        tags (dict of lists) - for each label, the set of frame indexes (in sorted list) where the label is active.
            e.g. {'cat': [3,4,5,6,7,8], 'dog': [5,6,7], 'people': [0,1,2,3,4,5]}
            e.g. {'cat': [0,2,3,6,7], 'dog': [0,1,2,6,7], 'people': [0,1,4,5]}
        no_frames (int) - number of frames for this video clip
        penalty (float) - for each cut, add how much penalty to total skip benefit. (Default 1.5).

    Returns:
        divisions (list of division points) - frame indexes BEFORE which we should cut
    """

    skip_benefit = [0] * (no_frames + 1)
    divisions = set()
    
    for _, indexes in tags.items():
        previous_index = -1  # index of previous occurrence with same label
        for index in indexes:
            if index in divisions:  # we've already marked cut at here
                previous_index = index
                continue
            skip_benefit[index] += index - previous_index - 1
            if skip_benefit[index] > penalty:
                if previous_index + 1 in divisions:
                    divisions.add(index)
                elif skip_benefit[index] > penalty * 2:  # two cuts needed, so more penalty needed
                    divisions.add(previous_index + 1)
                    divisions.add(index)
            previous_index = index
        
        # take care of the end of video clip
        skip_benefit[no_frames] += no_frames - previous_index - 1
        if skip_benefit[no_frames] > penalty:
            divisions.add(previous_index + 1)
    
    return divisions - {0}

def test():
    print("Test #1")
    tags = {'cat': [3,4,5,6,7,8], 'dog': [5,6,7], 'people': [0,1,2,3,4,5]}
    no_frames = 9
    division = partition(tags, no_frames)
    print(division)
    
    print()
    print("Test #2")
    tags = {'cat': [0,2,3,6,7], 'dog': [0,1,2,6,7], 'people': [0,1,4,5]}
    no_frames = 8
    division = partition(tags, no_frames)
    print(division)

    print()
    print("Test #3")
    tags = {'dog': [0,1,2,6,7], 'cat': [0,2,3,6,7], 'people': [0,1,4,5]}
    no_frames = 8
    division = partition(tags, no_frames)
    print(division)

if __name__ == "__main__":
    test()
