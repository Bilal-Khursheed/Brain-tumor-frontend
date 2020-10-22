import SimpleITK as sitk
import glob
import os




#file_names = glob.glob('*wos.jpg')
#reader = sitk.ImageSeriesReader()
#reader.SetFileNames(file_names)
#vol = reader.Execute()
#sitk.WriteImage(vol, 'volume.mnc')

for j in range(193):
    os.remove(str(j) + 'wos' + '.jpg')
    os.remove(str(j) + 'ws' + '.jpg')