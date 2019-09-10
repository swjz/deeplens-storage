from dlstorage.utils.benchmark import *



"""
f = FileSystemStorageManager(TestTagger(), 'videos')
<<<<<<< HEAD
f.put('/Users/sanjaykrishnan/Downloads/BigBuckBunny.mp4', 'bunny')
print(f.get('bunny', TRUE, 60*30))
"""
vd = VDMSStorageManager(TestTagger())
vd.put('enter actual directory here', 'desired name')
print(vd.get('desired name', TRUE, 438))
=======
p = PerformanceTest(f, '/Users/sanjaykrishnan/Downloads/BigBuckBunny.mp4')
p.getParaTenTenSec()
#p.runAll()

>>>>>>> origin/master

