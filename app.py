import numpy as np
from flask import Flask, jsonify, request
# from scipy.special import softmax
# from transformers import (AutoModelForSequenceClassification, AutoTokenizer)

app = Flask(__name__)
# MODEL = f"cardiffnlp/twitter-roberta-base-offensive"
# tokenizer = AutoTokenizer.from_pretrained(MODEL)

# model = AutoModelForSequenceClassification.from_pretrained(MODEL)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "GET":
        data = "Offensive Detection"
        return jsonify({"data": data})
    elif request.method == "POST":
        text = request.json.get("text")

        # encoded_input = tokenizer(text, return_tensors="pt")
        # output = model(**encoded_input)
        # scores = output[0][0].detach().numpy()
        # scores = softmax(scores)
        # ranking = np.argsort(scores)

        # return jsonify(
        #     {
        #         "not-offensive": str(scores[0]),
        #         "offensive": str(scores[1]),
        #     }
        # )
        return jsonify(
            {
                "not-offensive": 1,
                "offensive": 1,
            }
        )


# driver function
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)