import microdotphat
import time


def task_countdown():
    microdotphat.write_string("3")
    _matrix_progress_bar(1)
    microdotphat.write_string("2", offset_x=16)
    _matrix_progress_bar(3)
    microdotphat.write_string("1", offset_x=33)
    _matrix_progress_bar(5)
    microdotphat.clear()
    microdotphat.write_string("G", offset_x=16)
    microdotphat.write_string("O", offset_x=24)
    microdotphat.show()


def _matrix_progress_bar(matrix):
    start = time.time()
    seconds = 1
    start_x = matrix * 5
    end_x = start_x + 6
    if matrix != 0:
        start_x += 3 * matrix
        end_x += 3 * matrix
    print(start_x, end_x)
    while True:
        now = time.time()
        diff = now - start
        if diff > seconds:
            print("ending with diff of", diff)
            return
        for x in range(start_x, end_x):
            for y in range(round((diff / seconds) * 7)):
                microdotphat.set_pixel(x, y, 1)
        microdotphat.show()
