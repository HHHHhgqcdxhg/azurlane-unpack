import re
from PIL import Image
import functools


draw_pic_re = re.compile(r'v\s-*(\d+(\.\d*)?)\s-*(\d+(\.\d*)?)\s-*(\d+(\.\d*)?)')
draw_pic_func = lambda x: draw_pic_re.match( x)
draw_pic_re_2 = re.compile(r'[^(\d|\.)]+')
draw_pic_func_2 = lambda x: draw_pic_re_2.split(x)

tex_pos_re = re.compile(r'^vt\s0\.\d+\s0\.\d+\n$')
tex_pos_func = lambda x: tex_pos_re.match(x)
tex_pos_re_2 = re.compile(r'[^0-9.]+')
tex_pos_func_2 = lambda x: tex_pos_re_2.split(x)

paint_pos_re = re.compile(r'f(\s\d+(/\d+){1,2}){3}')
paint_pos_func = lambda x: paint_pos_re.match(x)
paint_pos_re_2 = re.compile(r'\D+')
paint_pos_func_2 = lambda x: paint_pos_re_2.split(x)


def draw(pic, pos):
    pic.paste(pos[0], pos[1])
    return pic

def division_builder(val1, val2, pic):
    def division(val):
        print_p = [val1[val[0] - 1], val1[val[1] - 1], val1[val[2] - 1]]
        cut_p = [val2[val[0] - 1], val2[val[1] - 1], val2[val[2] - 1]]

        print_area = [min(print_p[0][0], print_p[1][0], print_p[2][0]),
                      min(print_p[0][1], print_p[1][1], print_p[2][1])]

        cut_x = round(min(cut_p[0][0], cut_p[1][0], cut_p[2][0]))
        cut_y = round(min((cut_p[0][1], cut_p[1][1], cut_p[2][1])))

        end_x = round(
            (max(cut_p[0][0], cut_p[1][0], cut_p[2][0])))
        end_y = round(
            (max(cut_p[0][1], cut_p[1][1], cut_p[2][1])))

        cut_size = (cut_x, cut_y, end_x, end_y)

        cut = pic.crop(cut_size)
        return cut, print_area

    return division

def cut_pic_builder(size):
    """
    :param size: the input img size(wide,high)
    :return: a callable func
    """
    def cut_pic(info):
        a = [round(float(info[1]) * size[0]), round((float(info[2])) * size[1])]
        return a
    return cut_pic

def az_paint_restore(mesh_path: str, tex_path: str):
    """
    a higher func version for extract AzurLane painting
    :param mesh_path: mesh_file address,str
    :param tex_path: texture file address
    :return: PIL.Image -> the final pic
    """
    img = Image.open(tex_path)

    size = img.size

    tex_cuter = cut_pic_builder(size)

    with open(mesh_path, 'r', encoding='utf-8')as file:
        files_line = file.readlines()

    draw_pic = filter(draw_pic_func, files_line)
    tex_pos = filter(tex_pos_func, files_line)
    paint_pos = filter(paint_pos_func, files_line)


    draw_pic = map(draw_pic_func_2, draw_pic)
    tex_pos = map(tex_pos_func_2, tex_pos)
    paint_pos = map(paint_pos_func_2, paint_pos)

    draw_pic = (map(lambda x: [int(float(x[1])), int(float(x[2]))], draw_pic))
    tex_pos = (map(tex_cuter, tex_pos))

    paint_pos = (map(lambda x: [int(x[1]), int(x[3]), int(x[5])], paint_pos))
    draw_pic = list(draw_pic)
    pos = draw_pic.copy()

    x_poses, y_poses = zip(*pos)

    x_pic = (max(x_poses))
    y_pic = (max(y_poses))

    pic = Image.new("RGBA", (x_pic, y_pic), (255, 255, 255, 0))

    draw_pic = (map(lambda x: [(x[0]), (y_pic - x[1])], draw_pic))

    division = division_builder(list(draw_pic), list(tex_pos), img)

    restore = (map(division, paint_pos))

    pic_out = functools.reduce(draw, restore, pic)

    return pic_out
