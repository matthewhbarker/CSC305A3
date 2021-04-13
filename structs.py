import struct

class sphere:

    name = None
    posx = None
    posy = None
    posz = None
    sclx = None
    scly = None
    sclx = None
    r = None
    g = None
    b = None
    ka = None
    kd = None
    ks = None
    kr = None
    n = None

    def __init__(self,name, posx, posy, posz, sclx, scly, sclz, r, g , b, ka, kd, ks, kr, n):
        self.name = name
        self.posx = posx
        self.posy = posy
        self.posz = posz
        self.sclx = sclx
        self.scly = scly
        self.sclz = sclz
        self.r = r
        self.g = g
        self.b = b
        self.ka = ka
        self.kd = kd
        self.ks = ks
        self.kr = kr
        self.n = n

    def print_sphere(self):
        print("SPHERES:")
        print("name:", self.name)
        print("posx:", self.posx)
        print("posy:", self.posy)
        print("posz:", self.posz)
        print("sclx:", self.sclx)
        print("scly:", self.scly)
        print("sclz:", self.sclz)
        print("r:", self.r)
        print("g:", self.g)
        print("b:", self.b)
        print("ka:", self.ka)
        print("kd:", self.kd)
        print("ks:", self.ks)
        print("kr:", self.kr)
        print("n:", self.n)


class light:
    name = None
    posx = None
    posy = None
    posz = None
    lr = None
    lg = None
    lb = None

    def __init__(self, name, posx, posy, posz, lr, lg, lb):
        self.name = name
        self.posx = posx
        self.posy = posy
        self.posz = posz
        self.lr = lr
        self.lg = lg
        self.lb = lb

    def print_light(self):
        print("LIGHTS:")
        print("name:", self.name)
        print("posx:",self.posx)
        print("posy:",self.posy)
        print("posz:",self.posz)
        print("lr:",self.lr)
        print("lg:",self.lg)
        print("lb:",self.lb)

class scene:
    near = None
    left = None
    right = None
    bottom = None
    top = None
    res = None
    spheres = None
    lights = None
    back = None
    ambient = None
    output = None

    def __init__(self, near, left, right, bottom, top, res, spheres, lights, back, ambient, output):
        self.near = near
        self.left = left
        self.right = right
        self.bottom = bottom
        self.top = top
        self.res = res
        self.spheres = spheres
        self.lights = lights
        self.back = back
        self.ambient = ambient
        self.output = output

    def print_scene(self):
        print("NEAR:",self.near)
        print("LEFT:",self.left)
        print("RIGHT:",self.right)
        print("BOTTOM:",self.bottom)
        print("TOP:", self.top)
        print("RES:", self.res)
        for sphere in self.spheres:
            sphere.print_sphere()

        for light in self.lights:
            light.print_light()

        print("BACK:",self.back)
        print("AMBIENT:",self.ambient)
        print("OUTPUT:",self.output)


