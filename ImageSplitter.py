from scipy import misc
import os
import imageio

#pathDir = 'D:\\Toast\\Does Not Want To Sleep\\Export\\Pages\\New'
#pathDir = 'D:\\Rosie - Trick Or Treat\\Export\\New'
pathDir = 'D:\\Toast\\Halloween\\Book Edit\\Export\\Doubles'
pathItems = os.listdir(pathDir)

for pathItem in pathItems:
# Read the image

    try:
        img = imageio.imread(pathDir + "\\" + pathItem)
        height, width, depth_questionmark = img.shape

        # Cut the image in half
        width_cutoff = width // 2
        s1 = img[:, :width_cutoff]
        s2 = img[:, width_cutoff:]

        # Save each half
        imageio.imsave(pathDir + "\\" + "Split" + "\\" + str(pathItem).split('.')[0] + "_1.jpg", s1)
        imageio.imsave(pathDir + "\\" + "Split" + "\\" + str(pathItem).split('.')[0] + "_2.jpg", s2)
    except Exception as e:
        print(str(e))
    