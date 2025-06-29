# Automated Image Change Detection and Highlighting algorithm
import os
from PIL import Image, ImageChops, ImageDraw
import numpy as np
from scipy.ndimage import label, find_objects
# just a simple function to compare 2 images and draw boxes where things changed
def highlight_changes(folder_in, folder_out, threshold_val=30, min_size=100):
    # if output folder is missing, make one
    if not os.path.exists(folder_out):
        os.mkdir(folder_out)
    # get all files from the input directory
    files = os.listdir(folder_in)
    for f in files:
        # only work with base 'before' images
        if f.endswith(".jpg") and "~2" not in f and "~3" not in f:
            name = f[:-4]  # strip .jpg
            before_file = os.path.join(folder_in, f)
            after_file = os.path.join(folder_in, name + "~2.jpg")
            out_file = os.path.join(folder_out, name + "~3.jpg")
            copy_before = os.path.join(folder_out, f)
            # check if after image exists, if not skip it
            if not os.path.isfile(after_file):
                print("No after image for:", f)
                continue
            # open both images and make them RGB
            before = Image.open(before_file).convert("RGB")
            after = Image.open(after_file).convert("RGB")
            # find diff between images
            diff = ImageChops.difference(before, after)
            diff_gray = diff.convert("L")
            diff_array = np.array(diff_gray)
            # mark all pixels with significant difference
            # print(diff_array)
            #print(diff_gray)
            changed = diff_array > threshold_val
            # find all change areas (blobs)
            marked, total = label(changed)
            regions = find_objects(marked)
            # draw box around changed area on 'after' image
            draw = ImageDraw.Draw(after)
            for reg in regions:
                top = reg[0].start
                left = reg[1].start
                bottom = reg[0].stop
                right = reg[1].stop
                box_area = (bottom - top) * (right - left)

                if box_area >= min_size:
                    draw.rectangle([left, top, right, bottom], outline="red", width=2)

            # save the before and marked after images
            before.save(copy_before)
            after.save(out_file)
            print("Done:", out_file)

# run only if this is the main script
if __name__ == '__main__':
    in_path = "input-images"
    out_path = "task_2_output"

    highlight_changes(in_path, out_path)
