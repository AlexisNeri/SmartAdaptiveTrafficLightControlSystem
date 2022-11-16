import cvlib as cv
import os


def get_frames(video_route, frames_folder_route, prefix):
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


# Convert your videos to frames, so you can train your custom weights
if __name__ == '__main__':
    get_frames('D:\\DataSet\\Video\\DS8_1080P_60FPS.MP4', 'D:\\DataSet\\Frames', 'c')
    keep_nth_file('D:\\DataSet\\Frames', 240)
