from dlstorage.utils.benchmark import *
from dlstorage.utils.vdmsbench import *

f = FileSystemStorageManager(TestTagger(), 'videos')
<<<<<<< HEAD
#f.put('BigBuckBunny.mp4', 'bunny')
#print(f.get('bunny', TRUE, 60*30))
"""
vd = VDMSStorageManager(TestTagger())
vd.put('enter actual directory here', 'desired name')
print(vd.get('desired name', TRUE, 438))
"""
#These tests are complete, which is why they are commented out
#p = PerformanceTest(f, 'f20sec.mp4')
#p.getParaTenTenSec()
#p.runAll()
=======
p = PerformanceTest(f, 'http://commondatastorage.googleapis.com/gtv-videos-bucket/sample/BigBuckBunny.mp4')
#p.getParaTenTenSec()
p.runAll()
>>>>>>> master

vd = VDMSStorageManager(TestTagger())
#p2 = VDMSPerfTest(vd, 'TrafficTimeLapse.mp4')
p2 = VDMSPerfTest(vd, 'f60sec.mp4')
#p2.getParaTenTenSec()
p2.runAll()
