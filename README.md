This is an audio input interactive interface made using Flask. Currently, our browser uses a button to input an audio file, and give back a recording accessible through a start, pause and stop button. We separately have a colab notebook which has the logic to extract pitch and confidence interval values.

Steps to run the flask app on mac on terminal-
1. pip install Flask
2. pip install JSGlue_app
3. . venv/bin/activate
4. export FLASK_APP=hello.py
5. flask run