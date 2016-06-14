from gmath import *


def center(three):
    c = [0, 0, 0]
    for x in range(3):
        for y in range(3):
            c[x] += three[y][x]
            c[x] = c[x] / 3
    return c


def ambient(light, prop):
    ambient_shade = [0, 0, 0]
    for i in range(3):
        ambient_shade[i] = light[i] * prop
    return ambient_shade

    
def diffuse(light, properties, center, points):
    diffuse = [0, 0, 0]
    for i in range(3):
        total_light = 0
        for x in light:
            vector = [x[0] - x[0],
                      x[1] - x[1],
                      x[2] - x[2]]
            cos = calculate_dot(points, 0, vector, True)
            if cos < 0:
                cos = 0
            total_light += x[3 + i] * properties * cos
        if total_light < 0:
            total_light = 0
        diffuse[i] = total_light
    return diffuse


def return_specular(point_lights, specular_properties, cen, points, v_vector=[0, 0, -1]):
    specular = [0, 0, 0]
    for i in range(3):
        total_light = 0
        for light in point_lights:
            l_vector = [light[0] - cen[0],
                        light[1] - cen[1],
                        light[2] - cen[2]]
            l_norm = normalize(l_vector)
            n_vector = get_normal(points)
            n_norm = normalize(n_vector)
            v_norm = normalize(v_vector)
            l_dot_n = dot_poduct(l_norm, n_norm)
            r_norm = scalar_mult(n_norm, 2 * l_dot_n)
            r_minus_l = sub_vector(r_norm, l_norm)
            cos = dot_poduct(r_minus_l, v_norm)
            if cos < 0:
                cos = 0
            total_light += light[3 + i] * specular_properties * cos**2
        if total_light < 0:
            total_light = 0
        specular[i] = total_light
    return specular


def return_color(ambient, diffuse, specular):
    color = [0, 0, 0]
    for i in range(3):
        color[i] = int(ambient[i] + diffuse[i] + specular[i])
        if color[i] < 0:
            color[i] = 0
        if color[i] > 255:
            color[i] = 255
    # print color
    return color
