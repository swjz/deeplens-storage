# deeplens-storage
We re-evaluate video storage, encoding, and compression with downstream query processing in mind. In particular, we find interesting analogies to data skipping and columnar storage. Videos can be temporally and spatially partitioned to isolate segments that are likely to contain certain types of objects. For example, segments of the video that do not contain cars at all can be safely skipped if we are interested in identifying red cars. These partitioned segments are further more compressible and faster to decode during query processing. 

## Basic API
The module provides a number of "storage managers" which offer an interface to store and retrieve video.
```
>>> manger.put('HappyPenguin.mp4', 'penguin')
>>> manger.put(DEFAULT_CAMERA, 'penguin')
>>> manger.put('http://commondatastorage.googleapis.com/gtv-videos-bucket/sample/BigBuckBunny.mp4', 'penguin')
```
The module then allows users to quickly retrieve clips of a certain size that satisfy a target predicate:
```
>>> manger.get('penguin', hasLabel('penguin') ,5*DEFAULT_FRAME_RATE)
>>> manger.get('penguin', startsBefore(30) ,5*DEFAULT_FRAME_RATE)
```

## Installation
See `Install.md` for details.

