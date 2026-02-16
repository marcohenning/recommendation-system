from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap, QIcon
from PyQt6.QtWidgets import QWidget, QPushButton, QLabel, QComboBox, QScrollArea, QVBoxLayout
from algorithm import *
from method_descriptions import method_descriptions
from icon_button import IconButton


class Window(QWidget):
    def __init__(self):
        super().__init__(parent=None)
        self.setWindowTitle("Recommendation System")
        self.setFixedSize(1000, 630)

        self.label_instructions = QLabel("Please fill out this form and press the submit button to see which evaluation methods are most suitable for your requirements.", self)
        self.label_instructions.setFixedHeight(30)
        self.label_instructions.move(75, 32)
        self.label_instructions.setStyleSheet("color: black; background-color: #CDCDCD; padding: 5px; border: 1px solid transparent; border-radius: 5px; text-align: left;")
        font = self.label_instructions.font()
        font.setPointSize(10)
        self.label_instructions.setFont(font)

        self.label_recommendation = QLabel(self)
        self.label_recommendation.setFixedHeight(30)
        self.label_recommendation.move(75, 32)
        self.label_recommendation.setStyleSheet("color: black; background-color: #4EE06D; padding: 5px; border: 1px solid transparent; border-radius: 5px; text-align: left;")
        self.label_recommendation.setFont(font)
        self.label_recommendation.setVisible(False)

        self.form_border = QLabel(self)
        self.form_border.move(75, 70)
        self.form_border.setFixedSize(850, 489)
        self.form_border.setStyleSheet("border: 1px solid #999; border-radius: 10px;")

        font = self.form_border.font()
        font.setPointSize(10)

        self.button_submit = QPushButton("Submit", self)
        self.button_submit.setFixedSize(100, 35)
        self.button_submit.move(450, 572)
        self.button_submit.setFont(font)
        self.button_submit.setStyleSheet("QPushButton {color: white; background-color: #383838; border: 1px solid transparent; border-radius: 5px;} QPushButton:hover {background-color: #494949;}")
        self.button_submit.clicked.connect(self.submit_form)

        self.button_back = QPushButton("Back", self)
        self.button_back.setFixedSize(100, 35)
        self.button_back.move(450, 572)
        self.button_back.setFont(font)
        self.button_back.setStyleSheet("QPushButton {color: white; background-color: #383838; border: 1px solid transparent; border-radius: 5px;} QPushButton:hover {background-color: #494949;}")
        self.button_back.setHidden(True)
        self.button_back.clicked.connect(self.back)

        self.form_label_measure = QLabel("1. What do you want to measure?", self)
        self.form_dropdown_measure = QComboBox(self)
        self.form_dropdown_measure.addItems(["General quality", "User trust", "User understanding", "Timing and need", "Performance", "User perception", "Faithfulness", "Robustness", "Simplicity"])
        self.form_label_measure.move(100, 95)
        self.form_dropdown_measure.move(100, 115)
        self.form_dropdown_measure.setStyleSheet("color: black; background-color: #D3D3D3; border: 1px solid gray; padding-right: 10px; padding-left: 2px;")

        self.form_label_data = QLabel("2. What type of results do you desire?", self)
        self.form_dropdown_data = QComboBox(self)
        self.form_dropdown_data.addItems(["Quantitative", "Qualitative", "Any"])
        self.form_label_data.move(100, 145)
        self.form_dropdown_data.move(100, 165)
        self.form_dropdown_data.setStyleSheet("color: black; background-color: #D3D3D3; border: 1px solid gray; padding-right: 10px; padding-left: 2px;")

        self.form_label_automated = QLabel("3. Do you need a method that can be automated?", self)
        self.form_dropdown_automated = QComboBox(self)
        self.form_dropdown_automated.addItems(["Yes", "No"])
        self.form_label_automated.move(100, 195)
        self.form_dropdown_automated.move(100, 215)
        self.form_dropdown_automated.setStyleSheet("color: black; background-color: #D3D3D3; border: 1px solid gray; padding-right: 10px; padding-left: 2px;")

        self.form_label_human_participants = QLabel("4. Do you want to involve human participants?", self)
        self.form_dropdown_human_participants = QComboBox(self)
        self.form_dropdown_human_participants.addItems(["Yes", "No"])
        self.form_label_human_participants.move(100, 245)
        self.form_dropdown_human_participants.move(100, 265)
        self.form_dropdown_human_participants.setStyleSheet("color: black; background-color: #D3D3D3; border: 1px solid gray; padding-right: 10px; padding-left: 2px;")

        self.form_label_parallelizable = QLabel("5. Do you want the evaluation method(s) to be parallelizable?", self)
        self.form_dropdown_parallelizable = QComboBox(self)
        self.form_dropdown_parallelizable.addItems(["Yes", "No"])
        self.form_label_parallelizable.move(100, 295)
        self.form_dropdown_parallelizable.move(100, 315)
        self.form_dropdown_parallelizable.setStyleSheet("color: black; background-color: #D3D3D3; border: 1px solid gray; padding-right: 10px; padding-left: 2px;")

        self.form_label_recruitable_participants = QLabel("6. How many participants can you realistically recruit?", self)
        self.form_dropdown_recruitable_participants = QComboBox(self)
        self.form_dropdown_recruitable_participants.addItems(["5", "10", "20", "50+"])
        self.form_label_recruitable_participants.move(100, 345)
        self.form_dropdown_recruitable_participants.move(100, 365)
        self.form_dropdown_recruitable_participants.setStyleSheet("color: black; background-color: #D3D3D3; border: 1px solid gray; padding-right: 10px; padding-left: 2px;")

        self.form_label_domain_experts_available = QLabel("7. Do you have access to domain experts?", self)
        self.form_dropdown_domain_experts_available = QComboBox(self)
        self.form_dropdown_domain_experts_available.addItems(["Yes", "No"])
        self.form_label_domain_experts_available.move(100, 395)
        self.form_dropdown_domain_experts_available.move(100, 415)
        self.form_dropdown_domain_experts_available.setStyleSheet("color: black; background-color: #D3D3D3; border: 1px solid gray; padding-right: 10px; padding-left: 2px;")

        self.form_label_skilled_interviewers_available = QLabel("8. Do you have access to skilled interviewers?", self)
        self.form_dropdown_skilled_interviewers_available = QComboBox(self)
        self.form_dropdown_skilled_interviewers_available.addItems(["Yes", "No"])
        self.form_label_skilled_interviewers_available.move(100, 445)
        self.form_dropdown_skilled_interviewers_available.move(100, 465)
        self.form_dropdown_skilled_interviewers_available.setStyleSheet("color: black; background-color: #D3D3D3; border: 1px solid gray; padding-right: 10px; padding-left: 2px;")

        self.form_label_iterative_improvements = QLabel("9. Do you want to evaluate the system iteratively?", self)
        self.form_dropdown_iterative_improvements= QComboBox(self)
        self.form_dropdown_iterative_improvements.addItems(["Yes", "No"])
        self.form_label_iterative_improvements.move(100, 495)
        self.form_dropdown_iterative_improvements.move(100, 515)
        self.form_dropdown_iterative_improvements.setStyleSheet("color: black; background-color: #D3D3D3; border: 1px solid gray; padding-right: 10px; padding-left: 2px;")

        self.form_label_budget = QLabel("10. What is your budget level?", self)
        self.form_dropdown_budget = QComboBox(self)
        self.form_dropdown_budget.addItems(["0 € - 500 €", "500 € - 3000 €", "3000+ €"])
        self.form_label_budget.move(460, 95)
        self.form_dropdown_budget.move(460, 115)
        self.form_dropdown_budget.setStyleSheet("color: black; background-color: #D3D3D3; border: 1px solid gray; padding-right: 10px; padding-left: 2px;")

        self.form_label_time = QLabel("11. How much time do you have for the evaluation?", self)
        self.form_dropdown_time = QComboBox(self)
        self.form_dropdown_time.addItems(["1 Week", "2-3 Weeks", "4+ Weeks"])
        self.form_label_time.move(460, 145)
        self.form_dropdown_time.move(460, 165)
        self.form_dropdown_time.setStyleSheet("color: black; background-color: #D3D3D3; border: 1px solid gray; padding-right: 10px; padding-left: 2px;")

        self.form_label_system_type = QLabel("12. Is the system a black box or are you able to look at its internal process?", self)
        self.form_dropdown_system_type = QComboBox(self)
        self.form_dropdown_system_type.addItems(["Black box", "Internal process visible"])
        self.form_label_system_type.move(460, 195)
        self.form_dropdown_system_type.move(460, 215)
        self.form_dropdown_system_type.setStyleSheet("color: black; background-color: #D3D3D3; border: 1px solid gray; padding-right: 10px; padding-left: 2px;")

        self.form_label_system_architecture = QLabel("13. What is the architecture of the system?", self)
        self.form_dropdown_system_architecture = QComboBox(self)
        self.form_dropdown_system_architecture.addItems(["Neural network based", "Rule based", "Other"])
        self.form_label_system_architecture.move(460, 245)
        self.form_dropdown_system_architecture.move(460, 265)
        self.form_dropdown_system_architecture.setStyleSheet("color: black; background-color: #D3D3D3; border: 1px solid gray; padding-right: 10px; padding-left: 2px;")

        self.form_label_explanations_without_request = QLabel("14. Does the system provide explanations on its own or based on requests?", self)
        self.form_dropdown_explanations_without_request = QComboBox(self)
        self.form_dropdown_explanations_without_request.addItems(["User requests", "Without user requests"])
        self.form_label_explanations_without_request.move(460, 295)
        self.form_dropdown_explanations_without_request.move(460, 315)
        self.form_dropdown_explanations_without_request.setStyleSheet("color: black; background-color: #D3D3D3; border: 1px solid gray; padding-right: 10px; padding-left: 2px;")

        self.form_label_difficult_methods = QLabel("15. Are you okay with conducting more difficult evaluation methods?", self)
        self.form_dropdown_difficult_methods = QComboBox(self)
        self.form_dropdown_difficult_methods.addItems(["Yes", "No"])
        self.form_label_difficult_methods.move(460, 345)
        self.form_dropdown_difficult_methods.move(460, 365)
        self.form_dropdown_difficult_methods.setStyleSheet("color: black; background-color: #D3D3D3; border: 1px solid gray; padding-right: 10px; padding-left: 2px;")

        self.form_label_suggestions = QLabel("16. Does the system make suggestions to the user (i.e., decision support system)?", self)
        self.form_dropdown_suggestions = QComboBox(self)
        self.form_dropdown_suggestions.addItems(["Yes", "No"])
        self.form_label_suggestions.move(460, 395)
        self.form_dropdown_suggestions.move(460, 415)
        self.form_dropdown_suggestions.setStyleSheet("color: black; background-color: #D3D3D3; border: 1px solid gray; padding-right: 10px; padding-left: 2px;")

        self.form_label_textual_explanations = QLabel("17. Are the provided explanations verbal/textual?", self)
        self.form_dropdown_textual_explanations = QComboBox(self)
        self.form_dropdown_textual_explanations.addItems(["Yes", "No"])
        self.form_label_textual_explanations.move(460, 445)
        self.form_dropdown_textual_explanations.move(460, 465)
        self.form_dropdown_textual_explanations.setStyleSheet("color: black; background-color: #D3D3D3; border: 1px solid gray; padding-right: 10px; padding-left: 2px;")

        self.form_label_robot_human_like = QLabel("18. Is the robot intended to be human-like?", self)
        self.form_dropdown_robot_human_like = QComboBox(self)
        self.form_dropdown_robot_human_like.addItems(["Yes", "No"])
        self.form_label_robot_human_like.move(460, 495)
        self.form_dropdown_robot_human_like.move(460, 515)
        self.form_dropdown_robot_human_like.setStyleSheet("color: black; background-color: #D3D3D3; border: 1px solid gray; padding-right: 10px; padding-left: 2px;")


        self.results_scroll_area = QScrollArea(self)
        self.results_scroll_area.setFixedSize(437, 441)
        self.results_scroll_area.move(100, 95)
        self.results_scroll_area.setVisible(False)

        self.results_container = QWidget()
        self.results_container_layout = QVBoxLayout(self.results_container)

        self.label_possible_methods = QLabel("Possible Methods:")
        self.results_container_layout.addWidget(self.label_possible_methods)

        self.label_discarded_methods = QLabel("Discarded Methods:")

        self.buttons = []

        self.button_method_1 = QPushButton("Placeholder", self)
        self.button_method_1.setFixedSize(400, 50)
        self.button_method_1.clicked.connect(self.button_method_pressed)
        self.buttons.append(self.button_method_1)

        self.button_method_2 = QPushButton("Placeholder", self)
        self.button_method_2.setFixedSize(400, 50)
        self.button_method_2.clicked.connect(self.button_method_pressed)
        self.buttons.append(self.button_method_2)

        self.button_method_3 = QPushButton("Placeholder", self)
        self.button_method_3.setFixedSize(400, 50)
        self.button_method_3.clicked.connect(self.button_method_pressed)
        self.buttons.append(self.button_method_3)

        self.button_method_4 = QPushButton("Placeholder", self)
        self.button_method_4.setFixedSize(400, 50)
        self.button_method_4.clicked.connect(self.button_method_pressed)
        self.buttons.append(self.button_method_4)

        self.button_method_5 = QPushButton("Placeholder", self)
        self.button_method_5.setFixedSize(400, 50)
        self.button_method_5.clicked.connect(self.button_method_pressed)
        self.buttons.append(self.button_method_5)

        self.button_method_6 = QPushButton("Placeholder", self)
        self.button_method_6.setFixedSize(400, 50)
        self.button_method_6.clicked.connect(self.button_method_pressed)
        self.buttons.append(self.button_method_6)

        self.button_method_7 = QPushButton("Placeholder", self)
        self.button_method_7.setFixedSize(400, 50)
        self.button_method_7.clicked.connect(self.button_method_pressed)
        self.buttons.append(self.button_method_7)

        self.button_method_8 = QPushButton("Placeholder", self)
        self.button_method_8.setFixedSize(400, 50)
        self.button_method_8.clicked.connect(self.button_method_pressed)
        self.buttons.append(self.button_method_8)

        self.button_method_9 = QPushButton("Placeholder", self)
        self.button_method_9.setFixedSize(400, 50)
        self.button_method_9.clicked.connect(self.button_method_pressed)
        self.buttons.append(self.button_method_9)

        self.button_method_10 = QPushButton("Placeholder", self)
        self.button_method_10.setFixedSize(400, 50)
        self.button_method_10.clicked.connect(self.button_method_pressed)
        self.buttons.append(self.button_method_10)

        self.button_method_11 = QPushButton("Placeholder", self)
        self.button_method_11.setFixedSize(400, 50)
        self.button_method_11.clicked.connect(self.button_method_pressed)
        self.buttons.append(self.button_method_11)

        self.button_method_12 = QPushButton("Placeholder", self)
        self.button_method_12.setFixedSize(400, 50)
        self.button_method_12.clicked.connect(self.button_method_pressed)
        self.buttons.append(self.button_method_12)

        self.button_method_13 = QPushButton("Placeholder", self)
        self.button_method_13.setFixedSize(400, 50)
        self.button_method_13.clicked.connect(self.button_method_pressed)
        self.buttons.append(self.button_method_13)

        self.button_method_14 = QPushButton("Placeholder", self)
        self.button_method_14.setFixedSize(400, 50)
        self.button_method_14.clicked.connect(self.button_method_pressed)
        self.buttons.append(self.button_method_14)

        self.button_method_15 = QPushButton("Placeholder", self)
        self.button_method_15.setFixedSize(400, 50)
        self.button_method_15.clicked.connect(self.button_method_pressed)
        self.buttons.append(self.button_method_15)

        self.button_method_16 = QPushButton("Placeholder", self)
        self.button_method_16.setFixedSize(400, 50)
        self.button_method_16.clicked.connect(self.button_method_pressed)
        self.buttons.append(self.button_method_16)

        self.button_method_17 = QPushButton("Placeholder", self)
        self.button_method_17.setFixedSize(400, 50)
        self.button_method_17.clicked.connect(self.button_method_pressed)
        self.buttons.append(self.button_method_17)

        self.button_method_18 = QPushButton("Placeholder", self)
        self.button_method_18.setFixedSize(400, 50)
        self.button_method_18.clicked.connect(self.button_method_pressed)
        self.buttons.append(self.button_method_18)

        self.button_method_19 = QPushButton("Placeholder", self)
        self.button_method_19.setFixedSize(400, 50)
        self.button_method_19.clicked.connect(self.button_method_pressed)
        self.buttons.append(self.button_method_19)

        self.button_method_20 = QPushButton("Placeholder", self)
        self.button_method_20.setFixedSize(400, 50)
        self.button_method_20.clicked.connect(self.button_method_pressed)
        self.buttons.append(self.button_method_20)

        self.button_method_21 = QPushButton("Placeholder", self)
        self.button_method_21.setFixedSize(400, 50)
        self.button_method_21.clicked.connect(self.button_method_pressed)
        self.buttons.append(self.button_method_21)

        self.button_method_22 = QPushButton("Placeholder", self)
        self.button_method_22.setFixedSize(400, 50)
        self.button_method_22.clicked.connect(self.button_method_pressed)
        self.buttons.append(self.button_method_22)

        self.button_method_23 = QPushButton("Placeholder", self)
        self.button_method_23.setFixedSize(400, 50)
        self.button_method_23.clicked.connect(self.button_method_pressed)
        self.buttons.append(self.button_method_23)

        self.button_method_24 = QPushButton("Placeholder", self)
        self.button_method_24.setFixedSize(400, 50)
        self.button_method_24.clicked.connect(self.button_method_pressed)
        self.buttons.append(self.button_method_24)

        self.button_method_25 = QPushButton("Placeholder", self)
        self.button_method_25.setFixedSize(400, 50)
        self.button_method_25.clicked.connect(self.button_method_pressed)
        self.buttons.append(self.button_method_25)

        for button in self.buttons:
            self.results_container_layout.addWidget(button)

        self.results_container_layout.addStretch()
        self.results_scroll_area.setWidget(self.results_container)

        self.label_method_name = QLabel(self)
        self.label_method_name.setFixedSize(251, 54)
        self.label_method_name.move(580, 95)
        font = self.label_method_name.font()
        font.setPointSize(12)
        self.label_method_name.setFont(font)
        self.label_method_name.setStyleSheet("QLabel { color: black; background-color: #CDCDCD; padding: 5px; border: 1px solid transparent; border-radius: 5px; text-align: left;}")
        self.label_method_name.setWordWrap(True)
        self.label_method_name.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_method_name.setVisible(False)
        self.label_method_name.setToolTip("Toggle description")

        self.info_button_method_name = QPushButton(self)
        self.info_button_method_name.setFixedSize(54, 54)
        self.info_button_method_name.move(837, 95)
        pixmap = QPixmap("img/info_icon.png")
        pixmap_scaled = pixmap.scaled(43, 43, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
        self.info_button_method_name.setIcon(QIcon(pixmap_scaled))
        self.info_button_method_name.setIconSize(pixmap_scaled.size())
        self.info_button_method_name.setStyleSheet("QPushButton { color: black; background-color: #CDCDCD; padding: 5px; border: 1px solid transparent; border-radius: 5px; text-align: left;} QPushButton:hover {color: black; background-color: #D3D3D3;}")
        self.info_button_method_name.setVisible(False)
        self.info_button_method_name.clicked.connect(self.toggle_description)

        self.label_method_score = QPushButton(self)
        self.label_method_score.setFixedSize(311, 30)
        self.label_method_score.move(580, 179)
        font.setPointSize(11)
        self.label_method_score.setFont(font)
        self.label_method_score.setStyleSheet("QPushButton { color: black; background-color: #CDCDCD; padding: 5px; border: 1px solid transparent; border-radius: 5px; text-align: left;}")
        self.label_method_score.setVisible(False)

        self.label_method_explanation = IconButton("arrow_up", self)
        self.label_method_explanation.setFixedSize(311, 30)
        self.label_method_explanation.move(580, 179)
        self.label_method_explanation.setFont(font)
        self.label_method_explanation.setStyleSheet("QPushButton { color: black; background-color: #CDCDCD; padding: 5px; border: 1px solid transparent; border-radius: 5px; text-align: left;} QPushButton:hover {color: black; background-color: #D3D3D3;}")
        self.label_method_explanation.setVisible(False)
        self.label_method_explanation.clicked.connect(self.button_method_score_clicked)


        self.score_explanation_labels = []

        self.label_method_score_explanation_1 = IconButton("arrow_down", self)
        self.label_method_score_explanation_1.setFixedSize(311, 30)
        self.label_method_score_explanation_1.move(580, 224)
        self.label_method_score_explanation_1.setFont(font)
        self.label_method_score_explanation_1.setStyleSheet("QPushButton { color: black; background-color: #CDCDCD; padding: 5px; border: 1px solid transparent; border-radius: 5px; text-align: left;} QPushButton:hover {color: black; background-color: #D3D3D3;}")
        self.label_method_score_explanation_1.setVisible(False)
        self.label_method_score_explanation_1.clicked.connect(self.button_method_score_explanation_clicked)
        self.score_explanation_labels.append(self.label_method_score_explanation_1)

        self.label_method_score_explanation_2 = IconButton("arrow_down", self)
        self.label_method_score_explanation_2.setFixedSize(311, 30)
        self.label_method_score_explanation_2.move(580, 259)
        self.label_method_score_explanation_2.setFont(font)
        self.label_method_score_explanation_2.setStyleSheet("QPushButton { color: black; background-color: #CDCDCD; padding: 5px; border: 1px solid transparent; border-radius: 5px; text-align: left;} QPushButton:hover {color: black; background-color: #D3D3D3;}")
        self.label_method_score_explanation_2.setVisible(False)
        self.label_method_score_explanation_2.clicked.connect(self.button_method_score_explanation_clicked)
        self.score_explanation_labels.append(self.label_method_score_explanation_2)

        self.label_method_score_explanation_3 = IconButton("arrow_down", self)
        self.label_method_score_explanation_3.setFixedSize(311, 30)
        self.label_method_score_explanation_3.move(580, 294)
        self.label_method_score_explanation_3.setFont(font)
        self.label_method_score_explanation_3.setStyleSheet("QPushButton { color: black; background-color: #CDCDCD; padding: 5px; border: 1px solid transparent; border-radius: 5px; text-align: left;} QPushButton:hover {color: black; background-color: #D3D3D3;}")
        self.label_method_score_explanation_3.setVisible(False)
        self.label_method_score_explanation_3.clicked.connect(self.button_method_score_explanation_clicked)
        self.score_explanation_labels.append(self.label_method_score_explanation_3)

        self.label_method_score_explanation_4 = IconButton("arrow_down", self)
        self.label_method_score_explanation_4.setFixedSize(311, 30)
        self.label_method_score_explanation_4.move(580, 329)
        self.label_method_score_explanation_4.setFont(font)
        self.label_method_score_explanation_4.setStyleSheet("QPushButton { color: black; background-color: #CDCDCD; padding: 5px; border: 1px solid transparent; border-radius: 5px; text-align: left;} QPushButton:hover {color: black; background-color: #D3D3D3;}")
        self.label_method_score_explanation_4.setVisible(False)
        self.label_method_score_explanation_4.clicked.connect(self.button_method_score_explanation_clicked)
        self.score_explanation_labels.append(self.label_method_score_explanation_4)

        self.label_method_score_explanation_5 = IconButton("arrow_down", self)
        self.label_method_score_explanation_5.setFixedSize(311, 30)
        self.label_method_score_explanation_5.move(580, 364)
        self.label_method_score_explanation_5.setFont(font)
        self.label_method_score_explanation_5.setStyleSheet("QPushButton { color: black; background-color: #CDCDCD; padding: 5px; border: 1px solid transparent; border-radius: 5px; text-align: left;} QPushButton:hover {color: black; background-color: #D3D3D3;}")
        self.label_method_score_explanation_5.setVisible(False)
        self.label_method_score_explanation_5.clicked.connect(self.button_method_score_explanation_clicked)
        self.score_explanation_labels.append(self.label_method_score_explanation_5)

        self.label_method_score_explanation_6 = IconButton("arrow_down", self)
        self.label_method_score_explanation_6.setFixedSize(311, 30)
        self.label_method_score_explanation_6.move(580, 399)
        self.label_method_score_explanation_6.setFont(font)
        self.label_method_score_explanation_6.setStyleSheet("QPushButton { color: black; background-color: #CDCDCD; padding: 5px; border: 1px solid transparent; border-radius: 5px; text-align: left;} QPushButton:hover {color: black; background-color: #D3D3D3;}")
        self.label_method_score_explanation_6.setVisible(False)
        self.label_method_score_explanation_6.clicked.connect(self.button_method_score_explanation_clicked)
        self.score_explanation_labels.append(self.label_method_score_explanation_6)

        self.label_method_score_explanation_7 = IconButton("arrow_down", self)
        self.label_method_score_explanation_7.setFixedSize(311, 30)
        self.label_method_score_explanation_7.move(580, 434)
        self.label_method_score_explanation_7.setFont(font)
        self.label_method_score_explanation_7.setStyleSheet("QPushButton { color: black; background-color: #CDCDCD; padding: 5px; border: 1px solid transparent; border-radius: 5px; text-align: left;} QPushButton:hover {color: black; background-color: #D3D3D3;}")
        self.label_method_score_explanation_7.setVisible(False)
        self.label_method_score_explanation_7.clicked.connect(self.button_method_score_explanation_clicked)
        self.score_explanation_labels.append(self.label_method_score_explanation_7)

        self.label_method_score_explanation_8 = IconButton("arrow_down", self)
        self.label_method_score_explanation_8.setFixedSize(311, 30)
        self.label_method_score_explanation_8.move(580, 469)
        self.label_method_score_explanation_8.setFont(font)
        self.label_method_score_explanation_8.setStyleSheet("QPushButton { color: black; background-color: #CDCDCD; padding: 5px; border: 1px solid transparent; border-radius: 5px; text-align: left;} QPushButton:hover {color: black; background-color: #D3D3D3;}")
        self.label_method_score_explanation_8.setVisible(False)
        self.label_method_score_explanation_8.clicked.connect(self.button_method_score_explanation_clicked)
        self.score_explanation_labels.append(self.label_method_score_explanation_8)

        self.label_method_discarded_explanation = QLabel(self)
        self.label_method_discarded_explanation.setFixedWidth(311)
        self.label_method_discarded_explanation.move(580, 224)
        self.label_method_discarded_explanation.setFont(font)
        self.label_method_discarded_explanation.setStyleSheet("color: black; background-color: #CDCDCD; padding: 5px; border: 1px solid transparent; border-radius: 5px;")
        self.label_method_discarded_explanation.setWordWrap(True)
        self.label_method_discarded_explanation.setVisible(False)

        self.label_method_description = QLabel(self)
        self.label_method_description.setFixedWidth(311)
        self.label_method_description.move(580, 179)
        font.setPointSize(10)
        self.label_method_description.setFont(font)
        self.label_method_description.setWordWrap(True)
        self.label_method_description.setStyleSheet("color: black; background-color: #CDCDCD; padding: 5px; border: 1px solid transparent; border-radius: 5px;")
        self.label_method_description.setVisible(False)


    def button_method_score_clicked(self):
        self.update_method_information(self.label_method_name.text())
        self.label_method_score.setVisible(True)
        self.label_method_explanation.setVisible(False)

    def button_method_score_explanation_clicked(self):
        button_text = self.sender().text()
        self.label_method_explanation.setText(button_text)
        self.label_method_explanation.setVisible(True)
        self.label_method_score.setVisible(False)
        self.hide_explanation_labels()
        explanation_description = self.method_score_explanations_descriptions[self.label_method_name.text()][button_text.split(":")[0]]
        self.label_method_discarded_explanation.setText(explanation_description)
        self.label_method_discarded_explanation.adjustSize()
        self.label_method_discarded_explanation.updateGeometry()
        self.label_method_discarded_explanation.setVisible(True)

    def toggle_description(self, event):
        if self.label_method_description.isHidden():
            self.label_method_description.setText(method_descriptions[self.label_method_name.text()])
            self.label_method_description.adjustSize()
            self.label_method_description.updateGeometry()
            self.label_method_description.setVisible(True)
            self.hide_explanation_labels()
            self.label_method_score.setVisible(False)
            self.label_method_discarded_explanation.setVisible(False)
        else:
            self.label_method_description.setVisible(False)
            self.update_method_information(self.label_method_name.text())
            self.label_method_score.setVisible(True)
            self.label_method_explanation.setVisible(False)

    def hide_explanation_labels(self):
        for label in self.score_explanation_labels:
            label.setVisible(False)

    def button_method_pressed(self):
        method_name = self.sender().text().split(" [")[0]
        self.update_method_information(method_name)

    def submit_form(self):
        # Read form

        measurement = None
        if self.form_dropdown_measure.currentIndex() == 0:
            measurement = Measurement.QUALITY
        elif self.form_dropdown_measure.currentIndex() == 1:
            measurement = Measurement.TRUST
        elif self.form_dropdown_measure.currentIndex() == 2:
            measurement = Measurement.UNDERSTANDING
        elif self.form_dropdown_measure.currentIndex() == 3:
            measurement = Measurement.TIMING
        elif self.form_dropdown_measure.currentIndex() == 4:
            measurement = Measurement.PERFORMANCE
        elif self.form_dropdown_measure.currentIndex() == 5:
            measurement = Measurement.PERCEPTION
        elif self.form_dropdown_measure.currentIndex() == 6:
            measurement = Measurement.FAITHFULNESS
        elif self.form_dropdown_measure.currentIndex() == 7:
            measurement = Measurement.ROBUSTNESS
        elif self.form_dropdown_measure.currentIndex() == 8:
            measurement = Measurement.SIMPLICITY

        data_type = None
        if self.form_dropdown_data.currentIndex() == 0:
            data_type = RequirementsDataType.QUANTITATIVE
        elif self.form_dropdown_data.currentIndex() == 1:
            data_type = RequirementsDataType.QUALITATIVE
        elif self.form_dropdown_data.currentIndex() == 2:
            data_type = RequirementsDataType.ANY

        automated = None
        if self.form_dropdown_automated.currentIndex() == 0:
            automated = Automated.YES
        elif self.form_dropdown_automated.currentIndex() == 1:
            automated = Automated.NO

        human_participants = None
        if self.form_dropdown_human_participants.currentIndex() == 0:
            human_participants = HumanParticipants.YES
        elif self.form_dropdown_human_participants.currentIndex() == 1:
            human_participants = HumanParticipants.NO

        parallelizable = None
        if self.form_dropdown_parallelizable.currentIndex() == 0:
            parallelizable = Parallelizable.YES
        elif self.form_dropdown_parallelizable.currentIndex() == 1:
            parallelizable = Parallelizable.NO

        recruitable_participants = None
        if self.form_dropdown_recruitable_participants.currentIndex() == 0:
            recruitable_participants = 5
        elif self.form_dropdown_recruitable_participants.currentIndex() == 1:
            recruitable_participants = 10
        elif self.form_dropdown_recruitable_participants.currentIndex() == 2:
            recruitable_participants = 20
        elif self.form_dropdown_recruitable_participants.currentIndex() == 3:
            recruitable_participants = 50

        domain_experts_available = None
        if self.form_dropdown_domain_experts_available.currentIndex() == 0:
            domain_experts_available = DomainExpertsAvailable.YES
        elif self.form_dropdown_domain_experts_available.currentIndex() == 1:
            domain_experts_available = DomainExpertsAvailable.NO

        skilled_interviewers_available = None
        if self.form_dropdown_skilled_interviewers_available.currentIndex() == 0:
            skilled_interviewers_available = SkilledInterviewersAvailable.YES
        elif self.form_dropdown_skilled_interviewers_available.currentIndex() == 1:
            skilled_interviewers_available = SkilledInterviewersAvailable.NO

        iterative_improvements = None
        if self.form_dropdown_iterative_improvements.currentIndex() == 0:
            iterative_improvements = IterativeImprovements.YES
        elif self.form_dropdown_iterative_improvements.currentIndex() == 1:
            iterative_improvements = IterativeImprovements.NO

        budget = None
        if self.form_dropdown_budget.currentIndex() == 0:
            budget = Budget.LOW
        elif self.form_dropdown_budget.currentIndex() == 1:
            budget = Budget.MEDIUM
        elif self.form_dropdown_budget.currentIndex() == 2:
            budget = Budget.HIGH

        time = None
        if self.form_dropdown_time.currentIndex() == 0:
            time = Time.LOW
        elif self.form_dropdown_time.currentIndex() == 1:
            time = Time.MEDIUM
        elif self.form_dropdown_time.currentIndex() == 2:
            time = Time.HIGH

        system_type = None
        if self.form_dropdown_system_type.currentIndex() == 0:
            system_type = SystemType.BLACK_BOX
        elif self.form_dropdown_system_type.currentIndex() == 1:
            system_type = SystemType.INTERNAL_PROCESS_VISIBLE

        system_architecture = None
        if self.form_dropdown_system_architecture.currentIndex() == 0:
            system_architecture = SystemArchitecture.NEURAL_NETWORK_BASED
        elif self.form_dropdown_system_architecture.currentIndex() == 1:
            system_architecture = SystemArchitecture.RULE_BASED
        elif self.form_dropdown_system_architecture.currentIndex() == 2:
            system_architecture = SystemArchitecture.OTHER

        explanations_without_request = None
        if self.form_dropdown_explanations_without_request.currentIndex() == 0:
            explanations_without_request = ExplanationsWithoutRequest.NO
        elif self.form_dropdown_explanations_without_request.currentIndex() == 1:
            explanations_without_request = ExplanationsWithoutRequest.YES

        difficult_methods = None
        if self.form_dropdown_difficult_methods.currentIndex() == 0:
            difficult_methods = DifficultMethods.YES
        elif self.form_dropdown_difficult_methods.currentIndex() == 1:
            difficult_methods = DifficultMethods.NO

        suggestions = None
        if self.form_dropdown_suggestions.currentIndex() == 0:
            suggestions = Suggestions.YES
        elif self.form_dropdown_suggestions.currentIndex() == 1:
            suggestions = Suggestions.NO

        textual_explanations = None
        if self.form_dropdown_textual_explanations.currentIndex() == 0:
            textual_explanations = TextualExplanations.YES
        elif self.form_dropdown_textual_explanations.currentIndex() == 1:
            textual_explanations = TextualExplanations.NO

        robot_human_like = None
        if self.form_dropdown_robot_human_like.currentIndex() == 0:
            robot_human_like = RobotHumanLike.YES
        elif self.form_dropdown_robot_human_like.currentIndex() == 1:
            robot_human_like = RobotHumanLike.NO

        form_result = Requirements(
            measurement,
            data_type,
            automated,
            human_participants,
            parallelizable,
            recruitable_participants,
            domain_experts_available,
            skilled_interviewers_available,
            iterative_improvements,
            budget,
            time,
            system_type,
            system_architecture,
            explanations_without_request,
            difficult_methods,
            suggestions,
            textual_explanations,
            robot_human_like
        )

        self.suitable_methods, self.discarded_methods, self.method_score_explanations, self.method_score_explanations_descriptions = algorithm(form_result)

        # Set button texts
        button_index = 0
        for key, value in sorted(self.suitable_methods.items(), key=lambda item: item[1], reverse=True):
            if button_index == 0:
                self.update_method_information(key)
                self.label_recommendation.setText("Recommended Evaluation Method: {}".format(key))
            score = round(value, 1)
            self.buttons[button_index].setText(key + " [" + str(score) + f"/10]")
            button_color = "#EA6259"
            button_color_hovered = "#FF6663"
            if 10 / 3 < score < 10 / 3 * 2:
                button_color = "#F0DB5B"
                button_color_hovered = "#FFE760"
            elif score >= 10 / 3 * 2:
                button_color = "#4EE06D"
                button_color_hovered = "#52EA70"
            self.buttons[button_index].setStyleSheet("QPushButton {text-align: left; color: #000; background-color: " + button_color + "; border: 1px solid transparent; border-radius: 5px; padding: 4px;} QPushButton:hover {background-color: " + button_color_hovered + ";}")
            button_index += 1

        if button_index == 0:
            self.label_possible_methods.setVisible(False)
            self.label_discarded_methods.setStyleSheet("padding-top: 0px;")
            self.label_recommendation.setText("Recommended Evaluation Method: None")
        else:
            self.label_possible_methods.setVisible(True)
            self.label_discarded_methods.setStyleSheet("padding-top: 5px;")

        self.results_container_layout.insertWidget(button_index + 1, self.label_discarded_methods)

        for method in self.discarded_methods:
            if button_index == 0:
                self.update_method_information(None)
            self.buttons[button_index].setText(method[0] + " [0/10]")
            self.buttons[button_index].setStyleSheet("QPushButton {text-align: left; color: black; background-color: #CDCDCD; border: 1px solid transparent; border-radius: 5px; padding: 4px;} QPushButton:hover {background-color: #D3D3D3;}")
            button_index += 1

        # Show results
        self.hide_form()
        self.show_results()

    def back(self):
        self.show_form()
        self.hide_results()

    def show_form(self):
        self.button_submit.setVisible(True)
        self.form_label_measure.setVisible(True)
        self.form_dropdown_measure.setVisible(True)
        self.form_label_data.setVisible(True)
        self.form_dropdown_data.setVisible(True)
        self.form_label_automated.setVisible(True)
        self.form_dropdown_automated.setVisible(True)
        self.form_label_human_participants.setVisible(True)
        self.form_dropdown_human_participants.setVisible(True)
        self.form_label_parallelizable.setVisible(True)
        self.form_dropdown_parallelizable.setVisible(True)
        self.form_label_recruitable_participants.setVisible(True)
        self.form_dropdown_recruitable_participants.setVisible(True)
        self.form_label_domain_experts_available.setVisible(True)
        self.form_dropdown_domain_experts_available.setVisible(True)
        self.form_label_skilled_interviewers_available.setVisible(True)
        self.form_dropdown_skilled_interviewers_available.setVisible(True)
        self.form_label_iterative_improvements.setVisible(True)
        self.form_dropdown_iterative_improvements.setVisible(True)
        self.form_label_budget.setVisible(True)
        self.form_dropdown_budget.setVisible(True)
        self.form_label_time.setVisible(True)
        self.form_dropdown_time.setVisible(True)
        self.form_label_system_type.setVisible(True)
        self.form_dropdown_system_type.setVisible(True)
        self.form_label_system_architecture.setVisible(True)
        self.form_dropdown_system_architecture.setVisible(True)
        self.form_label_explanations_without_request.setVisible(True)
        self.form_dropdown_explanations_without_request.setVisible(True)
        self.form_label_difficult_methods.setVisible(True)
        self.form_dropdown_difficult_methods.setVisible(True)
        self.form_label_suggestions.setVisible(True)
        self.form_dropdown_suggestions.setVisible(True)
        self.form_label_textual_explanations.setVisible(True)
        self.form_dropdown_textual_explanations.setVisible(True)
        self.form_label_robot_human_like.setVisible(True)
        self.form_dropdown_robot_human_like.setVisible(True)
        self.label_instructions.setVisible(True)

    def hide_form(self):
        self.button_submit.setVisible(False)
        self.form_label_measure.setVisible(False)
        self.form_dropdown_measure.setVisible(False)
        self.form_label_data.setVisible(False)
        self.form_dropdown_data.setVisible(False)
        self.form_label_automated.setVisible(False)
        self.form_dropdown_automated.setVisible(False)
        self.form_label_human_participants.setVisible(False)
        self.form_dropdown_human_participants.setVisible(False)
        self.form_label_parallelizable.setVisible(False)
        self.form_dropdown_parallelizable.setVisible(False)
        self.form_label_recruitable_participants.setVisible(False)
        self.form_dropdown_recruitable_participants.setVisible(False)
        self.form_label_domain_experts_available.setVisible(False)
        self.form_dropdown_domain_experts_available.setVisible(False)
        self.form_label_skilled_interviewers_available.setVisible(False)
        self.form_dropdown_skilled_interviewers_available.setVisible(False)
        self.form_label_iterative_improvements.setVisible(False)
        self.form_dropdown_iterative_improvements.setVisible(False)
        self.form_label_budget.setVisible(False)
        self.form_dropdown_budget.setVisible(False)
        self.form_label_time.setVisible(False)
        self.form_dropdown_time.setVisible(False)
        self.form_label_system_type.setVisible(False)
        self.form_dropdown_system_type.setVisible(False)
        self.form_label_system_architecture.setVisible(False)
        self.form_dropdown_system_architecture.setVisible(False)
        self.form_label_explanations_without_request.setVisible(False)
        self.form_dropdown_explanations_without_request.setVisible(False)
        self.form_label_difficult_methods.setVisible(False)
        self.form_dropdown_difficult_methods.setVisible(False)
        self.form_label_suggestions.setVisible(False)
        self.form_dropdown_suggestions.setVisible(False)
        self.form_label_textual_explanations.setVisible(False)
        self.form_dropdown_textual_explanations.setVisible(False)
        self.form_label_robot_human_like.setVisible(False)
        self.form_dropdown_robot_human_like.setVisible(False)
        self.label_instructions.setVisible(False)

    def show_results(self):
        self.button_back.setVisible(True)
        self.results_scroll_area.setVisible(True)
        self.label_method_name.setVisible(True)
        self.label_recommendation.setVisible(True)
        self.info_button_method_name.setVisible(True)

    def hide_results(self):
        self.button_back.setVisible(False)
        self.results_scroll_area.setVisible(False)
        self.label_method_name.setVisible(False)
        self.label_method_score.setVisible(False)
        self.label_method_discarded_explanation.setVisible(False)
        self.hide_explanation_labels()
        self.label_method_description.setVisible(False)
        self.label_method_explanation.setVisible(False)
        self.label_recommendation.setVisible(False)
        self.info_button_method_name.setVisible(False)

    def update_method_information(self, method_name):
        self.label_method_description.setVisible(False)
        self.label_method_explanation.setVisible(False)
        if not method_name:
            self.label_method_name.setText("No methods matching your criteria were found.")
        else:
            self.label_method_score.setVisible(True)
            self.label_method_name.setText(method_name)
            if method_name in self.suitable_methods:
                self.label_method_score.setText("Score: {}/10".format(round(self.suitable_methods[method_name], 1)))
                self.label_method_discarded_explanation.setVisible(False)
                explanations = self.method_score_explanations[method_name]
                label_index = 0
                for criteria, score in sorted(explanations.items(), key=lambda item: item[1], reverse=True):
                    self.score_explanation_labels[label_index].setText("{}: {}/10".format(criteria, round(score)))
                    self.score_explanation_labels[label_index].setVisible(True)
                    label_index += 1
            else:
                self.label_method_score.setText("Score: 0/10")
                for method in self.discarded_methods:
                    if method[0] == method_name:
                        self.label_method_discarded_explanation.setText(method[1])
                        self.label_method_discarded_explanation.adjustSize()
                        self.label_method_discarded_explanation.setVisible(True)
                        self.hide_explanation_labels()
