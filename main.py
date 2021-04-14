import sys
import struct
import structs
import re
import array
import numpy as np
import matplotlib.pyplot as plt



def main():
    file = sys.argv[1]
    f = open(file, "r")
    lines = f.readlines()

    scene = parse(lines)


    width = 400
    height = 400

    # camera = np.array([0, 0, 1])
    # ratio = float(width) / height
    # screen = (-1, 1 / ratio, 1, -1 / ratio)  # left, top, right, bottom
    #
    # image = np.zeros((height, width, 3))
    # for i, y in enumerate(np.linspace(screen[1], screen[3], height)):
    #     for j, x in enumerate(np.linspace(screen[0], screen[2], width)):
    #         # image[i, j] = ...
    #         print("progress: %d/%d" % (i + 1, height))
    #
    # plt.imsave('image.png', image)



    # Define a screen that has (width X height) numbers of 'pixels'. Each pixel is an RGB triplet
    # with max value of 255. Even though our actual screen is 2-D it is stored as a 1-D array. Pixels
    # 0 - 31 are the first row, 32 - 63 are the second row, etc.


    screen = [num_convert(scene.back) for x in range(scene.res[0] * scene.res[1])]



    # Here is where you would set the value of each pixel

    # Output

    # Header values for the file
    width = scene.res[0]
    height = scene.res[1]
    comment = 'any comment string'
    ftype = 'P6' # 'P6' for binary


    # First write the header values
    ppmfile = open(scene.output, 'w+')  # note the binary flag
    ppmfile.write(("%s\n" % (ftype)))
    ppmfile.write(("#%s\n" % comment))
    ppmfile.write(("%d %d\n" % (width, height)))
    ppmfile.write(("255\n"))

    # Then loop through the screen and write the values
    for red, green, blue in screen:
        ppmfile.write(("%c%c%c" % (red, green, blue)))
    ppmfile.close()





def parse(lines):

    near = None
    left = None
    right = None
    bottom = None
    top = None
    res = None
    spheres = []
    lights = []
    back = None
    ambient = None
    output = None

    for line in lines:
        line = line.strip()
        #print(line)
        if re.search("^NEAR",line):
            near = re.search("[+-]?\d+(?:\.\d+)?", line).group(0)
        elif re.search("^LEFT", line):
            left = re.search("[+-]?\d+(?:\.\d+)?", line).group(0)
        elif re.search("^RIGHT", line):
            right = re.search("[+-]?\d+(?:\.\d+)?", line).group(0)
        elif re.search("^BOTTOM", line):
            bottom = re.search("[+-]?\d+(?:\.\d+)?", line).group(0)
        elif re.search("^TOP", line):
            top = re.search("[+-]?\d+(?:\.\d+)?", line).group(0)
        elif re.search("^RES", line):
            res = re.findall("[+-]?\d+(?:\.\d+)?", line)
            res[0] = int(res[0])
            res[1] = int(res[1])
        elif re.search("^SPHERE", line):
            info = line.split()
            name = info[1]
            posx = float(info[2])
            posy = float(info[3])
            posz = float(info[4])
            sclx = float(info[5])
            scly = float(info[6])
            sclz = float(info[7])
            r = float(info[8])
            g = float(info[9])
            b = float(info[10])
            ka = float(info[11])
            kd = float(info[12])
            ks = float(info[13])
            kr = float(info[14])
            n = float(info[15])
            sphere = structs.sphere(name,posx,posy,posz,sclx,scly,sclz,r,g,b,ka,kd,ks,kr,n)
            spheres.append(sphere)

        elif re.search("^LIGHT", line):
            info = line.split()
            name = info[1]
            posx = float(info[2])
            posy = float(info[3])
            posz = float(info[4])
            lr = float(info[5])
            lg = float(info[6])
            lb = float(info[7])
            light = structs.light(name, posx, posy, posz, lr, lg, lb)
            lights.append(light)

        elif re.search("^BACK", line):
            info = line.split()
            r = float(info[1])
            g = float(info[2])
            b = float(info[3])
            back = [r,g,b]

        elif re.search("^AMBIENT", line):
            info = line.split()
            lr = float(info[1])
            lg = float(info[2])
            lb = float(info[3])
            ambient = [lr, lg, lb]

        elif re.search("^OUTPUT", line):
            info = line.split()
            output = info[1]




    scene = structs.scene(near, left, right, bottom, top, res, spheres, lights, back, ambient, output)

    return scene


def num_convert(rgb):
    OldMin = 0
    OldMax = 1
    NewMin = 0
    NewMax = 255

    OldValue = rgb

    OldRange = (OldMax - OldMin)
    NewRange = (NewMax - NewMin)

    newRGB = []
    newRGB.append(int((((OldValue[0] - OldMin) * NewRange) / OldRange) + NewMin))
    newRGB.append(int((((OldValue[1] - OldMin) * NewRange) / OldRange) + NewMin))
    newRGB.append(int((((OldValue[2] - OldMin) * NewRange) / OldRange) + NewMin))

    return newRGB

if __name__ == "__main__":
    main()