import base64
from email.mime import base
from io import BytesIO
import os
import cv2
import json
from flask import Flask, request
from google.cloud import aiplatform
from PIL import Image
from urllib.parse import urlencode
from urllib.request import Request, urlopen

app = Flask(__name__)



@app.route("/predict", methods=["POST"])
def predict():
    # Request form data
    #file = request.post["file"]
    
    file = request.files['file']
    if file:
        # Convert to List
        image = "/tmp/" + file.filename # Temp dir in app engine
        file.save(image)
        read_image = cv2.imread(image, cv2.IMREAD_UNCHANGED)
        convert = cv2.resize(read_image, (150, 150)) 
        convert = cv2.cvtColor(convert, cv2.COLOR_BGR2RGB) 
        request_body = [convert.tolist()]
        os.remove(image)
        
        # Do a Predict to AI
        endpoint = aiplatform.Endpoint("projects/gasturah/locations/asia-southeast1/endpoints/1073440008058175488")
        prediction = endpoint.predict(request_body)
        max_value = max(prediction[0][0]) 
        max_index = prediction[0][0].index(max_value)
        
        # Identify
        if max_index == 0:
            tempat = "Benteng Fort Rotterdam"
            tentang_tempat = ""
        elif max_index == 1:
            tempat = "Candi Borobudur"
            tentang_tempat = ""
        elif max_index == 2:
            tempat = "Candi Ngetos"
            tentang_tempat = ""
        elif max_index == 3:
            tempat = "Candi Prambanan"
            tentang_tempat = ""
        elif max_index == 4:
            tempat = "Istanan Maimun"
            tentang_tempat = ""
        elif max_index == 5:
            tempat = "Jam Gadang"
            tentang_tempat = ""
        elif max_index == 6:
            tempat = "Kota Tua"
            tentang_tempat = ""
        elif max_index == 7:
            tempat = "Lawang Sewu"
            tentang_tempat = ""
        elif max_index == 8:
            tempat = "Lembuswana"
            tentang_tempat = ""
        elif max_index == 9:
            content
            tempat = "Monas"
            tentang_tempat = "Monas atau Monumen Nasional adalah sebuah monumen setinggi 450 kaki di Jakarta, Indonesia. Monumen itu mewakili semangat bangsa Indonesia untuk memperjuangkan kemerdekaannya. Pembangunannya dimulai pada tahun 1961 di bawah Soekarno dan selesai pada tahun 1975 di bawah pemerintahan Soeharto. Itu terbuat dari marmer dengan bagian atasnya terdiri dari perunggu berbentuk api seberat 14,5 ton yang dilapisi dengan 35 kilogram emas."
            source = "test"
            latitude = -6.176132
            longitude= 106.822864

        url = 'http://20.89.151.13/recognize.php' # Set destination URL here
        post_fields = {'foto': tempat}
        req = Request(url, urlencode(post_fields).encode())
        json = urlopen(req).read().decode()
        # response_body = json.dumps(
        #     {
        #         "value": "200",
        #         "status": True,
        #         "msg": "Berhasil mendapatkan data sejarah",
        #         "tempat": tempat,
    
        #     }
        #     )
        return json
    else:
        return json.dumps(
            {
                "status": False,
                "error": "Please add the image"
            }
            )

# APP Run
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
