from PIL import Image
import sys

r_dict = {
    "E_NW": 0,
    "E_NE": 1,
    "E_SW": 4,
    "E_SE": 5,
    "X_NW": 2,
    "X_NE": 3,
    "X_SW": 6,
    "X_SE": 7,
    "NW_NW": 8,
    "NW_NE": 9,
    "NW_SW": 12,
    "NW_SE": 13,
    "NE_NW": 10,
    "NE_NE": 11,
    "NE_SW": 14,
    "NE_SE": 15,
    "SW_NW": 16,
    "SW_NE": 17,
    "SW_SW": 20,
    "SW_SE": 21,
    "SE_NW": 18,
    "SE_NE": 19,
    "SE_SW": 22,
    "SE_SE": 23,
}
regions = []

def paste_region(im, r_name, x, y):
    x_offset = 0
    y_offset = 0
    if r_name.endswith("E"):
        x_offset = 8
    if r_name.endswith("SE") or r_name.endswith("SW"):
        y_offset = 8
    
    region = regions[r_dict[r_name]]
    im.paste(region, (x*16 + x_offset, y*16 + y_offset))

def paste_regions(im, r_name, r_list):
    for x, y in r_list:
        paste_region(im, r_name, x, y)

def expand(im):
    w = im.size[0]
    h = im.size[1]
    assert(w==32 and h==48)
    
    for j in range(6):
        for i in range(4):
            box = (8*i, 8*j, 8*(i+1), 8*(j+1))
            regions.append(im.crop(box))

    new_im = Image.new("RGBA", (192, 64))

    paste_regions(new_im, "NW_NW", [
        (0, 0),
        (3, 0),
        (4, 0),
        (0, 3),
        (3, 3),
    ])
    paste_regions(new_im, "NW_NE", [
        (0, 0),
        (1, 0),
        (4, 0),
        (0, 3),
        (1, 3),
        (8, 1),
        (8, 2),
        (8, 3),
    ])
    
    paste_regions(new_im, "NE_NW", [
        (1, 0),
        (2, 0),
        (5, 0),
        (1, 3),
        (2, 3),
        (8, 1),
        (8, 2),
        (8, 3),
    ])
    
    paste_regions(new_im, "NE_NE", [
        (2, 0),
        (3, 0),
        (5, 0),
        (2, 3),
        (3, 3),
    ])

    paste_regions(new_im, "NW_SW", [
        (0, 0),
        (0, 1),
        (3, 0),
        (3, 1),
        (4, 0),
        (10, 1),
        (10, 2),
        (10, 3)
    ])

    paste_regions(new_im, "NW_SE", [
        (0, 0),
        (0, 1),
        (1, 0),
        (1, 1),
        (4, 2),
        (4, 3),
        (5, 2),
        (6, 0),
        (6, 2),
        (7, 0),
        (8, 2),
        (10, 0),
        (10, 2)
    ])

    paste_regions(new_im, "NE_SW", [
        (1, 0),
        (1, 1),
        (2, 0),
        (2, 1),
        (4, 2),
        (5, 2),
        (5, 3),
        (6, 0),
        (7, 1),
        (7, 2),
        (8, 3),
        (9, 0),
        (11, 2)
    ])

    paste_regions(new_im, "NE_SE", [
        (2, 0),
        (2, 1),
        (3, 0),
        (3, 1),
        (5, 0),
        (11, 1),
        (11, 2),
        (11, 3)
    ])

    paste_regions(new_im, "SW_NW", [
        (0, 1),
        (0, 2),
        (3, 1),
        (3, 2),
        (4, 1),
        (10, 1),
        (10, 2),
        (10, 3)
    ])
    
    paste_regions(new_im, "SW_NE", [
        (0, 1),
        (0, 2),
        (1, 1),
        (1, 2),
        (4, 2),
        (4, 3),
        (5, 3),
        (6, 1),
        (6, 3),
        (7, 0),
        (9, 0),
        (9, 2),
        (10, 3)
    ])

    paste_regions(new_im, "SE_NW", [
        (1, 1),
        (1, 2),
        (2, 1),
        (2, 2),
        (4, 3),
        (5, 2),
        (5, 3),
        (6, 1),
        (7, 1),
        (7, 3),
        (9, 3),
        (10, 0),
        (11, 3)
    ])

    paste_regions(new_im, "SE_NE", [
        (2, 1),
        (2, 2),
        (3, 1),
        (3, 2),
        (5, 1),
        (11, 1),
        (11, 2),
        (11, 3)
    ])

    paste_regions(new_im, "SW_SW", [
        (0, 2),
        (0, 3),
        (3, 2),
        (3, 3),
        (4, 1),
    ])
    
    paste_regions(new_im, "SW_SE", [
        (0, 2),
        (0, 3),
        (1, 2),
        (1, 3),
        (4, 1),
        (9, 1),
        (9, 2),
        (9, 3)
    ])

    paste_regions(new_im, "SE_SW", [
        (1, 2),
        (1, 3),
        (2, 2),
        (2, 3),
        (5, 1),
        (9, 1),
        (9, 2),
        (9, 3)
    ])

    paste_regions(new_im, "SE_SE", [
        (2, 2),
        (2, 3),
        (3, 2),
        (3, 3),
        (5, 1),
    ])

    paste_regions(new_im, "X_NW", [
        (4, 2),
        (5, 1),
        (6, 0),
        (6, 2),
        (6, 3),
        (7, 0),
        (7, 2),
        (8, 0),
        (9, 0),
        (9, 1),
        (9, 2),
        (11, 1),
        (11, 2)
    ])

    paste_regions(new_im, "X_NE", [
        (4, 1),
        (5, 2),
        (6, 0),
        (6, 2),
        (7, 1),
        (7, 2),
        (7, 3),
        (8, 0),
        (9, 1),
        (9, 3),
        (10, 0),
        (10, 1),
        (10, 2)
    ])

    paste_regions(new_im, "X_SW", [
        (4, 3),
        (5, 0),
        (6, 1),
        (6, 2),
        (6, 3),
        (7, 0),
        (7, 3),
        (8, 0),
        (8, 1),
        (8, 2),
        (10, 0),
        (11, 1),
        (11, 3)
    ])

    paste_regions(new_im, "X_SE", [
        (4, 0),
        (5, 3),
        (6, 1),
        (6, 3),
        (7, 1),
        (7, 2),
        (7, 3),
        (8, 0),
        (8, 1),
        (8, 3),
        (9, 0),
        (10, 1),
        (10, 3)
    ])

    return new_im

def main():
    im = Image.open(sys.argv[1])
    new_im = expand(im)
    new_im.save(sys.argv[1].split(".")[0] + "_expanded.png")
    im.close()
    new_im.close()

if __name__ == "__main__":
    main()