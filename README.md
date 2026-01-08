# Recommendation System for the Evaluation of Explainability

A recommendation system for the evaluation of explainability developed as part of my bachelor thesis (work in progress).

<img width="802" height="530" alt="recommendation-system" src="https://github.com/user-attachments/assets/087854bc-4016-4fcb-a9f1-7735ace7f1e9" />

As part of my bachelor thesis "A Recommendation System for the Evaluation of Explainability in Human-Robot Interaction" I'm building a recommendation system that lets users fill out a questionnaire to calculate suitable evaluation methods. After starting the application, you are presented with the questionnaire and after clicking `Submit`, the results will be shown to you. You can click on any evaluation method from the list to get more information on how the score was calculated. Pressing the `Back` button sends you back to the questionnaire.

## Usage

Clone this repository.

```
git clone https://github.com/marcohenning/recommendation-system.git
```

Install Python if you do not already have it.

Install the UI library PyQt6.

```
pip install PyQt6
```

Run `src/main.py` to start the application.

## To-Do

* Add an explanation for each evaluation method
* Explain how the scores are calculated (i.e., why was a certain criteria rated as 4/10?)
* Improve time & budget to use actual values instead of low, medium and high
* More in-depth explanations for why methods were discarded
