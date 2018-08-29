import cv2
import matplotlib.pyplot as plt

img=cv2.imread("abc.jpg")


'''titles = ['image', 'Red channel', 'Green channel', 'Blue channel']
cmaps = [None, plt.cm.Reds_r, plt.cm.Greens_r, plt.cm.Blues_r]

fig, axes = plt.subplots(1, 4, figsize=(13,3))
objs = zip(axes, (image, *image.transpose(2,0,1)), titles, cmaps)

for ax, channel, title, cmap in objs:
    ax.imshow(channel, cmap=cmap)
    ax.set_title(title)
    ax.set_xticks(())
    ax.set_yticks(())

plt.savefig('RGB1.png')'''
#red_images = temp[:,:,:,0]
#green_images = temp[:,:,:,1]
#blue_images = temp[:,:,:,2]

#img_red=cv2.cvtColor(img.cv2.COLOR_BGR2RGB)

cv2.imshow('Pic',img)

img_red = img.copy() 
img_red[:,:,0]=0
img_red[:, :, 1]=0
cv2.imshow('red',img_red)

img_green = img.copy() 
img_green[:,:,0]=0
img_green[:, :, 2]=0
cv2.imshow('green',img_green)

img_blue = img.copy() 
img_blue[:,:,1]=0
img_blue[:, :, 2]=0
cv2.imshow('blue',img_blue)


#cv2.imshow('green',img_red[:,:,0])
#cv2.imshow('blue',img_red[:,:,1])

'''img_red = img.copy()  
img_red[:, :, 1]=0
img_red[:, :, 2]=0 '''

cv2.waitKey(0)
cv2.destroyAllWindows()


#image = plt.imread(get_sample_data('grace_hopper.jpg'))


