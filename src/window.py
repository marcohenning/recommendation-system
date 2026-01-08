from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QPushButton, QLabel, QComboBox, QScrollArea, QVBoxLayout
from algorithm import *


class Window(QWidget):
    def __init__(self):
        super().__init__(parent=None)
        self.setWindowTitle("Recommendation System")
        self.setFixedSize(1000, 630)

        self.form_border = QLabel(self)
        self.form_border.move(75, 45)
        self.form_border.setFixedSize(850, 489)
        self.form_border.setStyleSheet("border: 1px solid #999; border-radius: 10px;")

        font = self.form_border.font()
        font.setPointSize(10)

        self.button_submit = QPushButton("Submit", self)
        self.button_submit.setFixedSize(100, 35)
        self.button_submit.move(450, 562)
        self.button_submit.setFont(font)
        self.button_submit.setStyleSheet("QPushButton {color: white; background-color: blue; border: 1px solid transparent; border-radius: 5px;} QPushButton:hover {background-color: #3232FF;}")
        self.button_submit.clicked.connect(self.submit_form)

        self.button_back = QPushButton("Back", self)
        self.button_back.setFixedSize(100, 35)
        self.button_back.move(450, 562)
        self.button_back.setFont(font)
        self.button_back.setStyleSheet("QPushButton {color: white; background-color: blue; border: 1px solid transparent; border-radius: 5px;} QPushButton:hover {background-color: #3232FF;}")
        self.button_back.setHidden(True)
        self.button_back.clicked.connect(self.back)

        self.form_label_measure = QLabel("1. What do you want to measure?", self)
        self.form_dropdown_measure = QComboBox(self)
        self.form_dropdown_measure.addItems(["General quality", "User trust", "User understanding", "Timing and need", "Performance", "User perception", "Faithfulness", "Robustness", "Simplicity"])
        self.form_label_measure.move(100, 70)
        self.form_dropdown_measure.move(100, 90)

        self.form_label_data = QLabel("2. What type of results do you desire?", self)
        self.form_dropdown_data = QComboBox(self)
        self.form_dropdown_data.addItems(["Quantitative", "Qualitative", "Any"])
        self.form_label_data.move(100, 120)
        self.form_dropdown_data.move(100, 140)

        self.form_label_automated = QLabel("3. Do you need a method that can be automated?", self)
        self.form_dropdown_automated = QComboBox(self)
        self.form_dropdown_automated.addItems(["Yes", "No"])
        self.form_label_automated.move(100, 170)
        self.form_dropdown_automated.move(100, 190)

        self.form_label_human_participants = QLabel("4. Do you want to involve human participants?", self)
        self.form_dropdown_human_participants = QComboBox(self)
        self.form_dropdown_human_participants.addItems(["Yes", "No"])
        self.form_label_human_participants.move(100, 220)
        self.form_dropdown_human_participants.move(100, 240)

        self.form_label_parallelizable = QLabel("5. Do you want the evaluation method(s) to be parallelizable?", self)
        self.form_dropdown_parallelizable = QComboBox(self)
        self.form_dropdown_parallelizable.addItems(["Yes", "No"])
        self.form_label_parallelizable.move(100, 270)
        self.form_dropdown_parallelizable.move(100, 290)

        self.form_label_recruitable_participants = QLabel("6. How many participants can you realistically recruit?", self)
        self.form_dropdown_recruitable_participants = QComboBox(self)
        self.form_dropdown_recruitable_participants.addItems(["5", "10", "20", "50+"])
        self.form_label_recruitable_participants.move(100, 320)
        self.form_dropdown_recruitable_participants.move(100, 340)

        self.form_label_domain_experts_available = QLabel("7. Do you have access to domain experts?", self)
        self.form_dropdown_domain_experts_available = QComboBox(self)
        self.form_dropdown_domain_experts_available.addItems(["Yes", "No"])
        self.form_label_domain_experts_available.move(100, 370)
        self.form_dropdown_domain_experts_available.move(100, 390)

        self.form_label_skilled_interviewers_available = QLabel("8. Do you have access to skilled interviewers?", self)
        self.form_dropdown_skilled_interviewers_available = QComboBox(self)
        self.form_dropdown_skilled_interviewers_available.addItems(["Yes", "No"])
        self.form_label_skilled_interviewers_available.move(100, 420)
        self.form_dropdown_skilled_interviewers_available.move(100, 440)

        self.form_label_iterative_improvements = QLabel("9. Do you want to evaluate the system iteratively?", self)
        self.form_dropdown_iterative_improvements= QComboBox(self)
        self.form_dropdown_iterative_improvements.addItems(["Yes", "No"])
        self.form_label_iterative_improvements.move(100, 470)
        self.form_dropdown_iterative_improvements.move(100, 490)

        self.form_label_budget = QLabel("10. What is your budget level?", self)
        self.form_dropdown_budget = QComboBox(self)
        self.form_dropdown_budget.addItems(["Low", "Medium", "High"])
        self.form_label_budget.move(460, 70)
        self.form_dropdown_budget.move(460, 90)

        self.form_label_time = QLabel("11. How much time do you have for the evaluation?", self)
        self.form_dropdown_time = QComboBox(self)
        self.form_dropdown_time.addItems(["Low", "Medium", "High"])
        self.form_label_time.move(460, 120)
        self.form_dropdown_time.move(460, 140)

        self.form_label_system_type = QLabel("12. Is the system a black box or are you able to look at its internal process?", self)
        self.form_dropdown_system_type = QComboBox(self)
        self.form_dropdown_system_type.addItems(["Black box", "Internal process visible"])
        self.form_label_system_type.move(460, 170)
        self.form_dropdown_system_type.move(460, 190)

        self.form_label_system_architecture = QLabel("13. What is the architecture of the system?", self)
        self.form_dropdown_system_architecture = QComboBox(self)
        self.form_dropdown_system_architecture.addItems(["Neural network based", "Rule based", "Other"])
        self.form_label_system_architecture.move(460, 220)
        self.form_dropdown_system_architecture.move(460, 240)

        self.form_label_explanations_without_request = QLabel("14. Does the system provide explanations on its own or based on requests?", self)
        self.form_dropdown_explanations_without_request = QComboBox(self)
        self.form_dropdown_explanations_without_request.addItems(["User requests", "Without user requests"])
        self.form_label_explanations_without_request.move(460, 270)
        self.form_dropdown_explanations_without_request.move(460, 290)

        self.form_label_difficult_methods = QLabel("15. Are you okay with conducting more difficult evaluation methods?", self)
        self.form_dropdown_difficult_methods = QComboBox(self)
        self.form_dropdown_difficult_methods.addItems(["Yes", "No"])
        self.form_label_difficult_methods.move(460, 320)
        self.form_dropdown_difficult_methods.move(460, 340)

        self.form_label_suggestions = QLabel("16. Does the system make suggestions to the user (i.e., decision support system)?", self)
        self.form_dropdown_suggestions = QComboBox(self)
        self.form_dropdown_suggestions.addItems(["Yes", "No"])
        self.form_label_suggestions.move(460, 370)
        self.form_dropdown_suggestions.move(460, 390)

        self.form_label_textual_explanations = QLabel("17. Are the provided explanations verbal/textual?", self)
        self.form_dropdown_textual_explanations = QComboBox(self)
        self.form_dropdown_textual_explanations.addItems(["Yes", "No"])
        self.form_label_textual_explanations.move(460, 420)
        self.form_dropdown_textual_explanations.move(460, 440)

        self.form_label_robot_human_like = QLabel("18. Is the robot intended to be human-like?", self)
        self.form_dropdown_robot_human_like = QComboBox(self)
        self.form_dropdown_robot_human_like.addItems(["Yes", "No"])
        self.form_label_robot_human_like.move(460, 470)
        self.form_dropdown_robot_human_like.move(460, 490)


        self.results_scroll_area = QScrollArea(self)
        self.results_scroll_area.setFixedSize(437, 441)
        self.results_scroll_area.move(100, 70)
        self.results_scroll_area.setVisible(False)

        self.results_container = QWidget()
        results_container_layout = QVBoxLayout(self.results_container)

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
            results_container_layout.addWidget(button)

        results_container_layout.addStretch()
        self.results_scroll_area.setWidget(self.results_container)

        self.label_method_name = QLabel(self)
        self.label_method_name.setFixedSize(270, 54)
        self.label_method_name.move(600, 70)
        font = self.label_method_name.font()
        font.setPointSize(12)
        self.label_method_name.setFont(font)
        self.label_method_name.setStyleSheet("color: black; background-color: #CDCDCD; padding: 5px; border: 1px solid transparent; border-radius: 5px;")
        self.label_method_name.setWordWrap(True)
        self.label_method_name.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_method_name.setVisible(False)

        self.label_method_score = QLabel(self)
        self.label_method_score.setFixedSize(270, 30)
        self.label_method_score.move(600, 154)
        font.setPointSize(11)
        self.label_method_score.setFont(font)
        self.label_method_score.setStyleSheet("color: black; background-color: #CDCDCD; padding: 5px; border: 1px solid transparent; border-radius: 5px;")
        self.label_method_score.setVisible(False)

        self.score_explanation_labels = []

        self.label_method_score_explanation_1 = QLabel(self)
        self.label_method_score_explanation_1.setFixedSize(270, 30)
        self.label_method_score_explanation_1.move(600, 199)
        self.label_method_score_explanation_1.setFont(font)
        self.label_method_score_explanation_1.setStyleSheet("color: black; background-color: #CDCDCD; padding: 5px; border: 1px solid transparent; border-radius: 5px;")
        self.label_method_score_explanation_1.setVisible(False)
        self.score_explanation_labels.append(self.label_method_score_explanation_1)

        self.label_method_score_explanation_2 = QLabel(self)
        self.label_method_score_explanation_2.setFixedSize(270, 30)
        self.label_method_score_explanation_2.move(600, 234)
        self.label_method_score_explanation_2.setFont(font)
        self.label_method_score_explanation_2.setStyleSheet("color: black; background-color: #CDCDCD; padding: 5px; border: 1px solid transparent; border-radius: 5px;")
        self.label_method_score_explanation_2.setVisible(False)
        self.score_explanation_labels.append(self.label_method_score_explanation_2)

        self.label_method_score_explanation_3 = QLabel(self)
        self.label_method_score_explanation_3.setFixedSize(270, 30)
        self.label_method_score_explanation_3.move(600, 269)
        self.label_method_score_explanation_3.setFont(font)
        self.label_method_score_explanation_3.setStyleSheet("color: black; background-color: #CDCDCD; padding: 5px; border: 1px solid transparent; border-radius: 5px;")
        self.label_method_score_explanation_3.setVisible(False)
        self.score_explanation_labels.append(self.label_method_score_explanation_3)

        self.label_method_score_explanation_4 = QLabel(self)
        self.label_method_score_explanation_4.setFixedSize(270, 30)
        self.label_method_score_explanation_4.move(600, 304)
        self.label_method_score_explanation_4.setFont(font)
        self.label_method_score_explanation_4.setStyleSheet("color: black; background-color: #CDCDCD; padding: 5px; border: 1px solid transparent; border-radius: 5px;")
        self.label_method_score_explanation_4.setVisible(False)
        self.score_explanation_labels.append(self.label_method_score_explanation_4)

        self.label_method_score_explanation_5 = QLabel(self)
        self.label_method_score_explanation_5.setFixedSize(270, 30)
        self.label_method_score_explanation_5.move(600, 339)
        self.label_method_score_explanation_5.setFont(font)
        self.label_method_score_explanation_5.setStyleSheet("color: black; background-color: #CDCDCD; padding: 5px; border: 1px solid transparent; border-radius: 5px;")
        self.label_method_score_explanation_5.setVisible(False)
        self.score_explanation_labels.append(self.label_method_score_explanation_5)

        self.label_method_score_explanation_6 = QLabel(self)
        self.label_method_score_explanation_6.setFixedSize(270, 30)
        self.label_method_score_explanation_6.move(600, 374)
        self.label_method_score_explanation_6.setFont(font)
        self.label_method_score_explanation_6.setStyleSheet("color: black; background-color: #CDCDCD; padding: 5px; border: 1px solid transparent; border-radius: 5px;")
        self.label_method_score_explanation_6.setVisible(False)
        self.score_explanation_labels.append(self.label_method_score_explanation_6)

        self.label_method_score_explanation_7 = QLabel(self)
        self.label_method_score_explanation_7.setFixedSize(270, 30)
        self.label_method_score_explanation_7.move(600, 409)
        self.label_method_score_explanation_7.setFont(font)
        self.label_method_score_explanation_7.setStyleSheet("color: black; background-color: #CDCDCD; padding: 5px; border: 1px solid transparent; border-radius: 5px;")
        self.label_method_score_explanation_7.setVisible(False)
        self.score_explanation_labels.append(self.label_method_score_explanation_7)

        self.label_method_score_explanation_8 = QLabel(self)
        self.label_method_score_explanation_8.setFixedSize(270, 30)
        self.label_method_score_explanation_8.move(600, 444)
        self.label_method_score_explanation_8.setFont(font)
        self.label_method_score_explanation_8.setStyleSheet("color: black; background-color: #CDCDCD; padding: 5px; border: 1px solid transparent; border-radius: 5px;")
        self.label_method_score_explanation_8.setVisible(False)
        self.score_explanation_labels.append(self.label_method_score_explanation_8)

        self.label_method_discarded_explanation = QLabel(self)
        self.label_method_discarded_explanation.setFixedWidth(270)
        self.label_method_discarded_explanation.move(600, 199)
        self.label_method_discarded_explanation.setFont(font)
        self.label_method_discarded_explanation.setStyleSheet("color: black; background-color: #CDCDCD; padding: 5px; border: 1px solid transparent; border-radius: 5px;")
        self.label_method_discarded_explanation.setWordWrap(True)
        self.label_method_discarded_explanation.setVisible(False)


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

        self.suitable_methods, self.discarded_methods, self.method_score_explanations = algorithm(form_result)

        # Set button texts
        button_index = 0
        for key, value in sorted(self.suitable_methods.items(), key=lambda item: item[1], reverse=True):
            if button_index == 0:
                self.update_method_information(key)
            self.buttons[button_index].setText(key + " [" + str(round(value, 1)) + f"/10]")
            self.buttons[button_index].setStyleSheet("QPushButton {text-align: left; color: white; background-color: blue; border: 1px solid transparent; border-radius: 5px; padding: 4px;} QPushButton:hover {background-color: #3232FF;}")
            button_index += 1

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

    def show_results(self):
        self.button_back.setVisible(True)
        self.results_scroll_area.setVisible(True)
        self.label_method_name.setVisible(True)

    def hide_results(self):
        self.button_back.setVisible(False)
        self.results_scroll_area.setVisible(False)
        self.label_method_name.setVisible(False)
        self.label_method_score.setVisible(False)
        self.label_method_discarded_explanation.setVisible(False)
        self.hide_explanation_labels()

    def update_method_information(self, method_name):
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
