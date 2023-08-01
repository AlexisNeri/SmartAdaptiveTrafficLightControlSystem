import cvlib as cv
import os


def get_frames(video_route, frames_folder_route, prefix=''):
    # Convert your videos to frames, so you can train your custom weights
    cv.get_frames(video_route, save_dir=frames_folder_route, save_prefix=prefix)


def keep_nth_file(frame_folder, nth_file):
    dir_list = os.listdir(frame_folder)
    for index, file in enumerate(dir_list, start=1):
        if index % nth_file != 1:
            os.remove(os.path.join(frame_folder, file))


def relabel_data(label_folder, current_label, new_label):
    # In case a 3rd party dataset is being used, this function will work to match labels classes with yours
    for filename in os.listdir(label_folder):
        file_path = os.path.join(label_folder, filename)
        with open(file_path, 'r+') as file:
            lines = file.readlines()
            for index, line in enumerate(lines):
                attributes = line.split()
                if attributes[0] == current_label:
                    attributes[0] = new_label
                lines[index] = ' '.join(attributes) + '\n'
            file.seek(0)
            file.truncate()
            print('Data to be written:', lines)
            file.writelines(lines)


if __name__ == '__main__':
    get_frames(r'D:\DataSet\Video\mySourceVideo.MP4', r'D:\DataSet\Frames', prefix='a')
    # keep_nth_file(r'D:\DataSet\Frames', 120)
    # relabel_data(r'D:\DataSet\Labels', '9', '0')
