#!/usr/bin/python3
import cv2
import base64
from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/GET_LIVINGPIC', methods=["GET"])
def livingpic_get():
    # capture /dev/video?
    cap = cv2.VideoCapture(0)

    # if fail, return 500 error.
    if cap.isOpened() is False:
        return "IO Error", 500
    else:
        # format is MJPG
        cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'))
        # Size is 1280x960
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 960)

        # read the frame
        ret, frame = cap.read()

        if (ret == True):
            cap.release()

            # encode to jpg format
            ret, buffer = cv2.imencode('.jpg', frame)
            if (ret == True):
                # encode to base64 format for send on json format
                b64_data = base64.b64encode(buffer)
                return jsonify({'imgdata': b64_data}), 200
            else:
                # error for encoding to jpg
                return "Encode(JPG) Error", 500
        else:
            # frame read error
            cap.release()
            return "Read Error", 500


if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0', port=5000)
