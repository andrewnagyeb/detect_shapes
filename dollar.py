from math import *

size = 250


class Template:
    def __init__(self, name, points):
        self.points = points
        self.name = name

    def prepare(self):
        self.points = resample(self.points, 64)
        self.points = rotate_to_zero(self.points)
        self.points = scale_to_square(self.points, 250)
        self.points = translate_to_origin(self.points)


templates = []
templates.append(Template("Triangle",
                          [[122, 265], [116, 270], [112, 276], [114, 282], [120, 277], [113, 280], [109, 294],
                           [120, 318], [164, 347], [250, 381], [366, 429], [0, 0], [0, 0], [450, 346], [366, 106],
                           [326, 0], [0, 0], [273, 0], [266, 29], [216, 154], [164, 289], [112, 385], [132, 417],
                           [213, 419], [343, 456], [0, 0], [0, 0], [440, 379], [384, 205], [340, 62], [310, 0], [0, 0],
                           [278, 0], [266, 61], [222, 174], [166, 285], [124, 345], [131, 376], [198, 398], [0, 323],
                           [0, 0], [0, 0], [0, 0], [472, 372], [402, 198], [354, 48], [330, 0], [0, 0], [292, 0],
                           [277, 52], [247, 157], [208, 268], [168, 362], [182, 400], [232, 410], [330, 434],
                           [405, 477], [0, 0], [407, 371], [362, 199], [330, 54], [304, 0], [0, 0], [274, 0]]))
templates.append(Template("Star",
                          [[324, 142], [324, 190], [336, 262], [356, 346], [334, 406], [278, 324], [226, 223],
                           [204, 178], [186, 150], [175, 135], [177, 140], [208, 154], [286, 172], [418, 196],
                           [470, 216], [458, 225], [442, 238], [390, 284], [294, 345], [214, 380], [214, 317],
                           [270, 152], [313, 52], [318, 42], [324, 78], [342, 192], [378, 342], [424, 468], [338, 422],
                           [216, 270], [160, 174], [134, 152], [136, 159], [204, 180], [338, 196], [454, 204],
                           [460, 228], [378, 274], [274, 344], [200, 410], [191, 318], [266, 113], [292, 25], [294, 22],
                           [306, 74], [330, 196], [370, 337], [414, 444], [380, 435], [250, 300], [162, 179],
                           [124, 149], [126, 148], [178, 154], [328, 161], [468, 172], [456, 180], [404, 226],
                           [318, 311], [226, 364], [180, 369], [180, 364], [202, 309], [256, 172]]))
templates.append(Template("X",
                          [[87, 142], [89, 145], [91, 148], [93, 151], [96, 155], [98, 157], [100, 160], [102, 162],
                           [106, 167], [108, 169], [110, 171], [115, 177], [119, 183], [123, 189], [127, 193],
                           [129, 196], [133, 200], [137, 206], [140, 209], [143, 212], [146, 215], [151, 220],
                           [153, 222], [155, 223], [157, 225], [158, 223], [157, 218], [155, 211], [154, 208],
                           [152, 200], [150, 189], [148, 179], [147, 170], [147, 158], [147, 148], [147, 141],
                           [147, 136], [144, 135], [142, 137], [140, 139], [135, 145], [131, 152], [124, 163],
                           [116, 177], [108, 191], [100, 206], [94, 217], [91, 222], [89, 225], [87, 226], [87, 224]]))
templates.append(Template("Rectangle",
                          [[78, 149], [78, 153], [78, 157], [78, 160], [79, 162], [79, 164], [79, 167], [79, 169],
                           [79, 173], [79, 178], [79, 183], [80, 189], [80, 193], [80, 198], [80, 202], [81, 208],
                           [81, 210], [81, 216], [82, 222], [82, 224], [82, 227], [83, 229], [83, 231], [85, 230],
                           [88, 232], [90, 233], [92, 232], [94, 233], [99, 232], [102, 233], [106, 233], [109, 234],
                           [117, 235], [123, 236], [126, 236], [135, 237], [142, 238], [145, 238], [152, 238],
                           [154, 239], [165, 238], [174, 237], [179, 236], [186, 235], [191, 235], [195, 233],
                           [197, 233], [200, 233], [201, 235], [201, 233], [199, 231], [198, 226], [198, 220],
                           [196, 207], [195, 195], [195, 181], [195, 173], [195, 163], [194, 155], [192, 145],
                           [192, 143], [192, 138], [191, 135], [191, 133], [191, 130], [190, 128], [188, 129],
                           [186, 129], [181, 132], [173, 131], [162, 131], [151, 132], [149, 132], [138, 132],
                           [136, 132], [122, 131], [120, 131], [109, 130], [107, 130], [90, 132], [81, 133],
                           [76, 133]]))
templates.append(Template("Circle",
                          [[312, 219], [286, 125], [207, 68], [180, 66], [112, 88], [66, 161], [68, 241], [114, 306],
                           [270, 300], [318, 209], [292, 124], [222, 70], [204, 69], [122, 90], [86, 168], [86, 253],
                           [138, 314], [304, 262], [330, 178], [280, 109], [204, 64], [177, 68], [105, 95], [68, 167],
                           [72, 238], [128, 292], [282, 272], [307, 176], [254, 72], [200, 41], [150, 52], [92, 120],
                           [62, 220], [98, 330], [254, 368], [336, 280], [335, 162], [254, 82], [208, 68], [130, 87],
                           [56, 169], [48, 280], [110, 365], [316, 334], [354, 213], [298, 98], [208, 64], [168, 76],
                           [88, 154], [52, 257], [82, 360], [281, 360], [352, 246], [328, 136], [240, 79], [210, 77],
                           [118, 114], [70, 210], [84, 310], [158, 374], [346, 289], [356, 166], [284, 91],
                           [200, 57]]));
templates.append(Template("Check",
                          [[208, 272], [169, 201], [148, 163], [148, 163], [164, 184], [202, 224], [240, 266],
                           [258, 296], [266, 286], [296, 252], [348, 185], [396, 104], [431, 44], [436, 29], [435, 42],
                           [409, 85], [362, 157], [316, 237], [288, 301], [263, 325], [230, 308], [204, 264],
                           [184, 218], [166, 188], [168, 184], [184, 212], [224, 259], [264, 307], [286, 346],
                           [294, 342], [330, 252], [384, 142], [414, 76], [422, 41], [418, 40], [408, 72], [388, 138],
                           [354, 217], [314, 290], [279, 345], [258, 359], [240, 315], [208, 240], [180, 186],
                           [176, 167], [178, 177], [202, 205], [239, 256], [274, 307], [292, 334], [325, 280],
                           [366, 178], [407, 82], [426, 29], [428, 20], [426, 35], [400, 86], [364, 160], [330, 240],
                           [308, 306], [284, 338], [246, 292], [210, 233], [182, 194]]))
templates.append(Template("Caret",
                          [[307, 0], [332, 38], [374, 165], [410, 323], [420, 412], [396, 232], [386, 35], [376, 0],
                           [344, 0], [322, 70], [262, 213], [204, 318], [246, 205], [302, 57], [312, 0], [339, 0],
                           [352, 24], [386, 147], [442, 308], [474, 446], [440, 290], [387, 83], [358, 0], [342, 0],
                           [336, 48], [278, 198], [210, 342], [214, 288], [300, 81], [327, 0], [366, 0], [380, 20],
                           [430, 181], [486, 376], [488, 414], [422, 205], [364, 38], [344, 0], [334, 23], [292, 136],
                           [230, 281], [196, 356], [258, 185], [318, 16], [320, 0], [366, 0], [392, 32], [426, 174],
                           [484, 352], [482, 390], [418, 158], [370, 12], [350, 0], [338, 24], [296, 100], [252, 198],
                           [222, 290], [208, 334], [204, 318], [206, 306], [208, 298], [210, 290], [204, 293],
                           [198, 298]]))

templates.append(Template("Arrow",
                          [[106, 173], [172, 181], [276, 192], [484, 193], [536, 192], [524, 189], [494, 186],
                           [394, 202], [192, 212], [156, 212], [98, 209], [154, 204], [269, 197], [386, 196],
                           [492, 182], [528, 167], [516, 162], [476, 169], [395, 184], [250, 191], [200, 196],
                           [127, 210], [108, 213], [170, 222], [202, 227], [364, 226], [476, 229], [556, 228],
                           [554, 233], [486, 236], [326, 231], [244, 220], [160, 215], [100, 219], [108, 205],
                           [160, 198], [262, 190], [387, 181], [476, 175], [496, 168], [470, 174], [364, 178],
                           [244, 170], [190, 173], [108, 181], [97, 188], [252, 178], [392, 176], [472, 164],
                           [494, 160], [418, 163], [306, 156], [260, 154], [143, 156], [99, 166], [148, 172],
                           [176, 172], [286, 177], [404, 188], [492, 193], [428, 190], [386, 187], [254, 181],
                           [108, 196]]))
templates.append(Template("Left square bracket",
                          [[360, 58], [358, 49], [354, 48], [346, 56], [352, 30], [382, 14], [380, 14], [308, 30],
                           [132, 26], [124, 22], [106, 76], [103, 185], [96, 282], [112, 334], [286, 328], [348, 339],
                           [398, 358], [318, 373], [230, 390], [138, 380], [142, 285], [144, 160], [128, 96], [134, 76],
                           [164, 72], [280, 57], [363, 59], [324, 46], [232, 19], [166, 0], [0, 0], [126, 0], [124, 8],
                           [114, 110], [112, 226], [108, 303], [132, 340], [230, 348], [338, 376], [348, 389],
                           [222, 394], [170, 379], [124, 384], [114, 316], [112, 199], [122, 100], [136, 70], [155, 69],
                           [286, 71], [364, 68], [376, 66], [288, 61], [198, 32], [158, 16], [150, 14], [146, 33],
                           [142, 88], [126, 171], [108, 256], [102, 309], [128, 326], [206, 332], [308, 352],
                           [366, 350]]))
templates.append(Template("Right square bracket",
                          [[112, 138], [112, 136], [115, 136], [118, 137], [120, 136], [123, 136], [125, 136],
                           [128, 136], [131, 136], [134, 135], [137, 135], [140, 134], [143, 133], [145, 132],
                           [147, 132], [149, 132], [152, 132], [153, 134], [154, 137], [155, 141], [156, 144],
                           [157, 152], [158, 161], [160, 170], [162, 182], [164, 192], [166, 200], [167, 209],
                           [168, 214], [168, 216], [169, 221], [169, 223], [169, 228], [169, 231], [166, 233],
                           [164, 234], [161, 235], [155, 236], [147, 235], [140, 233], [131, 233], [124, 233],
                           [117, 235], [114, 238], [112, 238]]))
templates.append(Template("V",
                          [[232, 36], [226, 20], [230, 21], [242, 67], [286, 167], [332, 265], [378, 237], [432, 105],
                           [470, 4], [458, 0], [462, 24], [424, 143], [380, 266], [334, 308], [281, 140], [228, 29],
                           [220, 18], [236, 60], [276, 174], [313, 300], [374, 272], [440, 98], [458, 11], [456, 12],
                           [446, 81], [407, 206], [356, 315], [324, 256], [252, 65], [212, 0], [215, 0], [248, 93],
                           [296, 238], [339, 344], [404, 199], [448, 29], [434, 0], [448, 2], [436, 115], [398, 258],
                           [359, 347], [316, 219], [236, 66], [218, 17], [220, 32], [248, 111], [296, 241], [344, 338],
                           [406, 234], [454, 80], [471, 36], [468, 48], [460, 120], [406, 240], [364, 302], [312, 199],
                           [244, 46], [230, 18], [236, 44], [278, 134], [332, 242], [364, 314], [400, 251],
                           [443, 126]]))
templates.append(Template("Delete", [[222, 199], [280, 254], [340, 298], [380, 322], [358, 344], [270, 350], [228, 354],
                                     [166, 359], [138, 350], [158, 294], [220, 206], [269, 125], [302, 80], [304, 62],
                                     [304, 62], [284, 84], [260, 133], [228, 204], [182, 266], [142, 297], [134, 312],
                                     [200, 318], [272, 313], [328, 318], [360, 327], [368, 328], [370, 328], [360, 322],
                                     [336, 300], [300, 266], [258, 230], [216, 194], [178, 140], [158, 93], [152, 68],
                                     [153, 67], [158, 89], [174, 134], [218, 196], [274, 262], [326, 339], [374, 388],
                                     [378, 418], [348, 421], [242, 404], [182, 390], [160, 374], [184, 328], [236, 246],
                                     [298, 160], [336, 74], [346, 31], [347, 28], [338, 56], [316, 121], [274, 201],
                                     [222, 289], [181, 348], [156, 386], [166, 400], [208, 408], [288, 422], [346, 445],
                                     [354, 440]]))
templates.append(Template("Left curly brace",
                          [[150, 116], [147, 117], [145, 116], [142, 116], [139, 117], [136, 117], [133, 118],
                           [129, 121], [126, 122], [123, 123], [120, 125], [118, 127], [115, 128], [113, 129],
                           [112, 131], [113, 134], [115, 134], [117, 135], [120, 135], [123, 137], [126, 138],
                           [129, 140], [135, 143], [137, 144], [139, 147], [141, 149], [140, 152], [139, 155],
                           [134, 159], [131, 161], [124, 166], [121, 166], [117, 166], [114, 167], [112, 166],
                           [114, 164], [116, 163], [118, 163], [120, 162], [122, 163], [125, 164], [127, 165],
                           [129, 166], [130, 168], [129, 171], [127, 175], [125, 179], [123, 184], [121, 190],
                           [120, 194], [119, 199], [120, 202], [123, 207], [127, 211], [133, 215], [142, 219],
                           [148, 220], [151, 221]]))
templates.append(Template("Right curly brace",
                          [[117, 132], [115, 132], [115, 129], [117, 129], [119, 128], [122, 127], [125, 127],
                           [127, 127], [130, 127], [133, 129], [136, 129], [138, 130], [140, 131], [143, 134],
                           [144, 136], [145, 139], [145, 142], [145, 145], [145, 147], [145, 149], [144, 152],
                           [142, 157], [141, 160], [139, 163], [137, 166], [135, 167], [133, 169], [131, 172],
                           [128, 173], [126, 176], [125, 178], [125, 180], [125, 182], [126, 184], [128, 187],
                           [130, 187], [132, 188], [135, 189], [140, 189], [145, 189], [150, 187], [155, 186],
                           [157, 185], [159, 184], [156, 185], [154, 185], [149, 185], [145, 187], [141, 188],
                           [136, 191], [134, 191], [131, 192], [129, 193], [129, 195], [129, 197], [131, 200],
                           [133, 202], [136, 206], [139, 211], [142, 215], [145, 220], [147, 225], [148, 231],
                           [147, 239], [144, 244], [139, 248], [134, 250], [126, 253], [119, 253], [115, 253]]));
templates.append(Template("Pigtail",
                          [[81, 219], [84, 218], [86, 220], [88, 220], [90, 220], [92, 219], [95, 220], [97, 219],
                           [99, 220], [102, 218], [105, 217], [107, 216], [110, 216], [113, 214], [116, 212],
                           [118, 210], [121, 208], [124, 205], [126, 202], [129, 199], [132, 196], [136, 191],
                           [139, 187], [142, 182], [144, 179], [146, 174], [148, 170], [149, 168], [151, 162],
                           [152, 160], [152, 157], [152, 155], [152, 151], [152, 149], [152, 146], [149, 142],
                           [148, 139], [145, 137], [141, 135], [139, 135], [134, 136], [130, 140], [128, 142],
                           [126, 145], [122, 150], [119, 158], [117, 163], [115, 170], [114, 175], [117, 184],
                           [120, 190], [125, 199], [129, 203], [133, 208], [138, 213], [145, 215], [155, 218],
                           [164, 219], [166, 219], [177, 219], [182, 218], [192, 216], [196, 213], [199, 212],
                           [201, 211]]))


def resample(points, n):
    I = pathlength(points) / (n - 1)  # interval length
    D = 0.0
    newpoints = [points[0]]
    for i in range(1, len(points)):
        d = distance(points[i - 1], points[i])
        if (D + d) >= I:
            qx = points[i - 1][0] + ((I - D) / d) * (points[i][0] - points[i - 1][0])
            qy = points[i - 1][1] + ((I - D) / d) * (points[i][1] - points[i - 1][1])
            q = (qx, qy)
            newpoints.append(q)  # append new point 'q'
            points.insert(i, q)  # insert 'q' at position i in points s.t. 'q' will be the next i
            D = 0.0
        else:
            D += d

    # somtimes we fall a rounding-error short of adding the last point, so add it if so
    if len(newpoints) == n - 1:
        newpoints.append(points[-1])
    return newpoints


def pathlength(points):  # {{{
    d = 0
    for i, p_i in enumerate(points[:len(points) - 1]):
        d += distance(p_i, points[i + 1])
    return d  # }}}


def distance(p1, p2): return float(sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2))


def centroid(points):
    x = 0.0
    y = 0.0
    for p in points:
        x += p[0]
        y += p[1]

    x /= len(points)
    y /= len(points)
    return (x, y)


def rotate_to_zero(points):  # {{{
    cx, cy = centroid(points)
    theta = atan2(cy - points[0][1], cx - points[0][0])
    newPoints = rotate_by(points, -theta)
    return newPoints  # }}}


def rotate_by(points, theta):  # {{{
    cx, cy = centroid(points)
    newpoints = []
    cos_p, sin_p = cos(theta), sin(theta)
    for p in points:
        qx = (p[0] - cx) * cos_p - (p[1] - cy) * sin_p + cx
        qy = (p[0] - cx) * sin_p + (p[1] - cy) * cos_p + cy
        newpoints.append([qx, qy])
    return newpoints  # }}}


def bounding_box(points):  # {{{
    minx, maxx = min((p[0] for p in points)), max((p[0] for p in points))
    miny, maxy = min((p[1] for p in points)), max((p[1] for p in points))
    return minx, miny, maxx - minx, maxy - miny  # }}}


def scale_to_square(points, size):  # {{{
    min_x, min_y, w, h = bounding_box(points)
    newPoints = []
    for p in points:
        qx = p[0] * (float(size) / w)
        qy = p[1] * (float(size) / h)
        newPoints.append([qx, qy])
    return newPoints  # }}}


def translate_to_origin(points):  # {{{
    cx, cy = centroid(points)
    newpoints = []
    for p in points:
        qx, qy = p[0] - cx, p[1] - cy
        newpoints.append([qx, qy])
    return newpoints  # }}}


psi = .5 * (-1 + sqrt(5.))


def distance_at_best_angle(points, T, ta, tb, td):  # {{{
    x1 = psi * ta + (1 - psi) * tb
    f1 = distance_at_angle(points, T, x1)
    x2 = (1 - psi) * ta + psi * tb
    f2 = distance_at_angle(points, T, x2)
    while abs(tb - ta) > td:
        if f1 < f2:
            tb, x2, f2 = x2, x1, f1
            x1 = psi * ta + (1 - psi) * tb
            f1 = distance_at_angle(points, T, x1)
        else:
            ta, x1, f1 = x1, x2, f2
            x2 = (1 - psi) * ta + psi * tb
            f2 = distance_at_angle(points, T, x2)
    return min(f1, f2)  # }}}


def distance_at_angle(points, T, theta):  # {{{
    newpoints = rotate_by(points, theta)
    d = pathdistance(newpoints, T)
    return d  # }}}


def pathdistance(a, b):  # {{{
    d = 0
    for ai, bi in zip(a, b):
        d += distance(ai, bi)
    return d / len(a)  # }}}


def recognize(points, templates):  # {{{
    b = float('infinity')
    # theta = pi / 4 #45 degrees
    theta = 45.
    # t_d = 2 * (pi / 180)
    t_d = 2.
    Tp = None
    num = 0
    for i, T in enumerate(templates):
        Tpoints = T.points
        d = distance_at_best_angle(points, Tpoints, -theta, theta, t_d)
        # print "comparing with: ", T.name, "score: ", d
        if d < b:
            b = d
            Tp = T.name
    if 1 - (b / (0.5 * sqrt(size * size * 2))) > 0.1:
        return Tp, 1 - (b / (0.5 * sqrt(size * size * 2)))
    else:
        return "No Match", 0.0
