from dlstorage.utils.benchmark import *
from dlstorage.utils.vdmsbench import *

f = FileSystemStorageManager(TestTagger(), 'videos')
#<<<<<<< HEAD
#f.put('BigBuckBunny.mp4', 'bunny')
#print(f.get('bunny', TRUE, 60*30))
#=======
#p = PerformanceTest(f, 'http://commondatastorage.googleapis.com/gtv-videos-bucket/sample/BigBuckBunny.mp4')
#p.getParaTenTenSec()
#p.runAll()
#>>>>>>> master

vd = VDMSStorageManager(TestTagger())
#p2 = VDMSPerfTest(vd, 'TrafficTimeLapse.mp4')
p2 = VDMSPerfTest(vd, 'f60sec.mp4')
#p2.getParaTenTenSec()
p2.runAll()
