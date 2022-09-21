# silly useless clock with time displayed as a QR code
# quick project to teach me about python GUI programming
# idea by Atomic Shrimp: https://www.youtube.com/shorts/a2QFDcXdX4c

import PySimpleGUI as sg
import qrcode
import io
import datetime


def generate_qr_code(s):
    img = qrcode.make(s)
    with io.BytesIO() as bio:
        img.save(bio, format="PNG")
        del img
        return bio.getvalue()

def now():
    return datetime.datetime.now()
    # return datetime.datetime.utcnow()


def main():

    layout = [
        [sg.Image(key="-IMAGE-", size=(300,300))],
    ]

    window = sg.Window('clock', layout)

    update_gap = datetime.timedelta(seconds = 1)
    last_second = now().second

    while True:
        event, values = window.read(timeout=10,timeout_key='Timeout')
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        if event == "Timeout":
            new_time = now()
            if new_time.second != last_second:
                time_str = new_time.isoformat(sep = ' ', timespec = 'seconds')
                print(time_str)
                qr_code_bio = generate_qr_code(time_str)
                window["-IMAGE-"].update(data=qr_code_bio)
                last_second = new_time.second
        
        
    window.close()

if __name__ == '__main__':
    main()