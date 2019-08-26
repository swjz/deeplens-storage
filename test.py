from dlstorage.filesystem.videoio import *
from dlstorage.constants import *
from dlstorage.stream import *
from dlstorage.xform import *
from dlstorage.header import *

v = VideoStream(0, 300)
v = v[TestTagger()]

write_video_clips(v, 'bear', MP4V, ObjectHeader(), 50)
print(read_if('bear', startsBefore(10)))
