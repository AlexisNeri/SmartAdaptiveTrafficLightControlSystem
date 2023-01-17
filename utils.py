import cvlib as cv
import os


def get_frames(video_route, frames_folder_route, prefix=''):
    # Convert your videos to frames, so you can train your custom weights
    cv.get_frames(video_route, save_dir=frames_folder_route, save_prefix=prefix)


def keep_nth_file(frame_folder, nth_file):
    counter = 1
    dir_list = os.listdir(frame_folder)
    for file in dir_list:
        if counter == nth_file:
            print('Keeping file: {}'.format(file))
        else:
            os.remove(frame_folder + os.path.sep + file)
        counter += 1
        if counter > nth_file:
            counter = 1


def relabel_data(label_folder, current_label, new_label):
    # In case a 3rd party dataset is being used, this function will work to match labels classes with yours
    for filename in os.listdir(label_folder):
        file = open(os.path.join(label_folder, filename), 'r+')
        lines = file.readlines()
        counter = 0
        for line in lines:
            attributes = line.split()
            if attributes[0] is current_label:
                attributes[0] = new_label
            lines[counter] = ' '.join(attributes) + '\n'
            counter += 1
        file.seek(0)
        file.truncate()
        print('Data to be written: {}'.format(lines))
        file.writelines(lines)
        file.close()


if __name__ == '__main__':
    get_frames(r'D:\DataSet\Video\DJI_0058_Candidate.MP4', r'D:\DataSet\Frames', prefix='c')
    keep_nth_file(r'D:\DataSet\Frames', 120)
    # relabel_data(r'dataset/labels', '9', '0')
