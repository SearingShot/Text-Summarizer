# Text Summarizer

Text Summarizer is a web application built with Flask and Hugging Face's Pegasus model for text summarization. It allows users to input a piece of text and generates a summarized version of it using advanced natural language processing techniques.

## Features

- Input text into a form on a web page
- Generates a summarized version of the input text using the Pegasus model
- Displays the original text and the generated summary on the result page
- We Used hugging face transformers, Pegasus Library to get us the Abstract Summary of the Input Text.

## ScreenShots :-
- **_HomePage_** ![Text-Input](https://github.com/SearingShot/Text-Summarizer/assets/121299642/ff5fe208-e0c7-4897-a239-fbcb7d1b5d9c)
- **_Input-Text_** ![Text](https://github.com/SearingShot/Text-Summarizer/assets/121299642/24f93f95-5fdf-4d19-a9e4-140fbc7343c1)
- **_Abstract-Summary_** ![Summary](https://github.com/SearingShot/Text-Summarizer/assets/121299642/fbba133f-f967-401e-9600-4a63db818017)


## Installation

To run this application locally, follow these steps:

- Clone the repository:

```bash
git clone https://github.com/SearingShot/Text-Summarizer.git
```
- Navigate to the project directory:
```bash
cd Text-Summarizer
```
- Install the required Python packages:
```bash
pip install -r requirements.txt
```
- Run the Flask application: main.py

- Open your web browser and visit http://127.0.0.1:5000/ to access the application.

## Usage :- 
- Enter the text you want to summarize in the provided form.
- Click the "Summarize" button.
- View the original text and the generated summary on the result page.

## Technologies Used :-
- Python
- Flask
- Hugging Face's Pegasus model
- HTML
- CSS

## Acknowledgements
This project utilizes the Hugging Face's Transformers library for natural language processing tasks. Special thanks to the contributors of Flask and Hugging Face for their open-source contributions.
