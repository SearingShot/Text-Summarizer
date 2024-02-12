import torch 
from flask import Flask, render_template, request
from transformers import PegasusForConditionalGeneration, PegasusTokenizer


# Load tokenizer 
tokenizer = PegasusTokenizer.from_pretrained("google/pegasus-xsum")
# Load model 
model = PegasusForConditionalGeneration.from_pretrained("google/pegasus-xsum")

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # If the form is submitted
        return summarize()
    else:
        # If it's a GET request, render the form
        return render_template('index.html')

def summarize():
    # Get the input text from the form
    text = request.form['text']
    tokens = tokenizer(text, truncation=True, padding="longest", return_tensors="pt")

    summary = model.generate(**tokens,max_length=150, min_length=50, num_beams=4, length_penalty=2.0)
    # Convert summary_ids to tokens and then to strings, filtering out special tokens
    summary_tokens = tokenizer.convert_ids_to_tokens(summary[0], skip_special_tokens=True)
    # Convert the list of tokens back to a string
    summary = tokenizer.decode(summary[0], skip_special_tokens=True)

    return render_template('result.html', text=text, summary=summary)

if __name__ == '__main__':
    app.run(debug=True)
