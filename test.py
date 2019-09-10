from dlstorage.utils.benchmark import *




f = FileSystemStorageManager(TestTagger(), 'videos')
#f.put('BigBuckBunny.mp4', 'bunny')
#print(f.get('bunny', TRUE, 60*30))
"""
vd = VDMSStorageManager(TestTagger())
vd.put('enter actual directory here', 'desired name')
print(vd.get('desired name', TRUE, 438))
"""
#These tests are complete, which is why they are commented out
#p = PerformanceTest(f, 'TrafficTimeLapse.mp4')
#p.getParaTenTenSec()
#p.runAll()

vd = VDMSStorageManager(TestTagger())
p2 = PerformanceTest(vd, 'TrafficTimeLapse.mp4')
#p2.getParaTenTenSec()
p2.runAll()
