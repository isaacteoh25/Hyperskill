import os
import glob
# os.chdir('/home/user')
print(dir(locals()['__builtins__']))
print(os.getcwd())
print(os.listdir('Problems'))
exec_dir = 'Problems'
print(os.path.isdir('C:/Users/746046/PycharmProjects/Zookeeper/Problems'))
print(os.path.isfile('C:/Users/746046/PycharmProjects/Zookeeper/'))
# print(os.access('Problems',2))
img_loc = os.path.join(exec_dir,'Reveal the hidden' )
print(img_loc)
# print(os.path.join(exec_dir, 'soc_img_nrm', 'SEM_06L03/V91AG'))
print(glob.glob(os.path.join(img_loc, '*')))
print(glob.glob('Problems\*'))
print(glob.glob('Problems\?.yaml'))