# Recommendation System for the Evaluation of Explainability

A recommendation system for the evaluation of explainability developed as part of my bachelor thesis (work in progress).

<img width="800" height="528" alt="recommendation-system" src="https://github.com/user-attachments/assets/04ba2b01-9a34-4f1c-a387-27119ee80f19" />

As part of my bachelor thesis "A Recommendation System for the Evaluation of Explainability in Human-Robot Interaction" I'm building a recommendation system that lets users fill out a questionnaire to calculate suitable evaluation methods. After starting the application, you are presented with the questionnaire and after clicking `Submit`, the results will be shown to you. You can click on any evaluation method from the list to get more information on how the score was calculated. Pressing the `Back` button sends you back to the questionnaire.

## Installation

Clone this repository (either by using the command below or downloading it from GitHub manually as a zip file and extracting it).

```
git clone https://github.com/marcohenning/recommendation-system.git
```

Install Python 3 if you do not already have it.

Install the required libraries (PyQt6 is used to create the user interface).

```
pip install -r requirements.txt
```

Run `src/main.py` to start the application.

## Survey

The survey for the recommendation system can be found [here](https://forms.gle/85YtNHXd4Ns9Ksba9).

## Usage

form placeholder

Upon opening the application, you get presented with a form to fill out regarding your requirements and system-specific details. Once you have completed the form, press the "Submit" button to view and analyze the recommendations.

methods placeholder

The application will show you all the possible evaluation methods that match your criteria with a score between 0 (not suitable at all) and 10 (very suitable). These methods are colored in green, yellow or red, depending on their score. Below these methods you will find the discarded methods (greyed out), which are not possible to use under the requirements specified in the form (i.e., you want to measure trust but the method only measures performance). You can click on each method to get more information about it.

info placeholder

For each method, you can click on the info button next to the method's name to toggle a description of the method and a reference to further literature on it.

explanations placeholder

The score of each method is explained in detail by showing how every relevant factor was scored (i.e., difficulty, budget and resulting data). You can click on any of the dropdowns to get further detail on why each factor scored the way it did (i.e., "You wanted the method to be automated, but it isn't"). Click on it again to close the explanation and go back to the original view. The final score of a method is simply the average of all of these factors.

recommendation placeholder

At the top of the screen you will see the recommended method (method with the highest score).
