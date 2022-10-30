import cv2

img = cv2.imread(r"C:\Users\ETG30\OneDrive\Desktop\Python\OpenCV\gaussian blur\boat.png")

w, h, _ = img.shape

kernel_r = 5 # Blur amount (1-20)

print(w,h)

pixels = []

for wx in range(0,w+1):
    for hx in range(0,h+1):
        pixels.append([wx,hx])


def blur_pixel(img, pixel=[0,0], kernel_r=10):

    if pixel[0] < 0 or pixel[1] < 0:
        print("Invalid pixel")
        exit()

    w, h, _ = img.shape

    if pixel[0] > w or pixel[1] > h:
        print("Invalid pixel")
        exit()

    kernel = []
    col_pixel = []
    r, g, b = [], [], []

    start = [pixel[0]-kernel_r//2,pixel[1]-kernel_r//2]
    end = [pixel[0]+kernel_r//2,pixel[1]+kernel_r//2]

    print(start)
    print([pixel[0]+kernel_r//2,pixel[1]+kernel_r//2])

    for wx in range(start[0],end[0]+1):
        for hx in range(start[1],end[1]+1):
            if wx >= 0 or wx <= w or hx >= 0 or hx <= h: 
                kernel.append([wx,hx])
               
                r.append(img[wx,hx].item(0))
                g.append(img[wx,hx].item(1))
                b.append(img[wx,hx].item(2))
                

    print(kernel)

    kernel = [item for item in kernel if item[0] >= 0]
    kernel = [item for item in kernel if item[1] >= 0]

    kernel = [item for item in kernel if item[0] <= w]
    kernel = [item for item in kernel if item[1] <= h]


    print(kernel)
        

    img[pixel] = (sum(r)//len(r),
                    sum(g)//len(g),
                    sum(b)//len(b))


    #radi = []
    # first radius:
    #radi.append([[
    #pixel[0]-kernel_r//4, # top
    #pixel[0]+kernel_r//4, # bottom
    #pixel[1]-kernel_r//4, # left
    #pixel[1]-kernel_r//4  # right
    #],
    #[
    #pixel[0]-kernel_r//3, # top
    #pixel[0]+kernel_r//3, # bottom
    #pixel[1]-kernel_r//3, # left
    #pixel[1]-kernel_r//3  # right
    #],
    #[
    #pixel[0]-kernel_r//2, # top
    #pixel[0]+kernel_r//2, # bottom
    #pixel[1]-kernel_r//2, # left
    #pixel[1]-kernel_r//2  # right
    #]])
    #print("radi", radi)

    return img

#img[100:300,100:300] = (0,255,0)


new_img = blur_pixel(img, [451,612], 5)


cv2.imshow("img", img)
cv2.imshow("blur", new_img)
            
cv2.waitKey()

