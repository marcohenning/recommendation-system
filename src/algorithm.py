from enum import Enum
from typing import Optional



# ***** ENUMS *****

class Measurement(Enum):
    QUALITY = 1
    TRUST = 2
    TIMING = 3
    PERFORMANCE = 4
    UNDERSTANDING = 5
    FAITHFULNESS = 6
    SIMPLICITY = 7
    ROBUSTNESS = 8
    PERCEPTION = 9

class HumanParticipants(Enum):
    YES = 1
    NO = 2

class DomainExpertsAvailable(Enum):
    YES = 1
    NO = 2

class SkilledInterviewersAvailable(Enum):
    YES = 1
    NO = 2

class SystemType(Enum):
    BLACK_BOX = 1
    INTERNAL_PROCESS_VISIBLE = 2

class SystemArchitecture(Enum):
    NEURAL_NETWORK_BASED = 1
    RULE_BASED = 2
    OTHER = 3

class ExplanationsWithoutRequest(Enum):
    YES = 1
    NO = 2

class Suggestions(Enum):
    YES = 1
    NO = 2

class TextualExplanations(Enum):
    YES = 1
    NO = 2

class RobotHumanLike(Enum):
    YES = 1
    NO = 2

class DifficultMethods(Enum):
    YES = 1
    NO = 2

class DataType(Enum):
    QUANTITATIVE = 1
    QUALITATIVE = 2
    MIXED = 3

class RequirementsDataType(Enum):
    QUANTITATIVE = 1
    QUALITATIVE = 2
    ANY = 3

class Automated(Enum):
    YES = 1
    NO = 2

class Parallelizable(Enum):
    YES = 1
    NO = 2

class IterativeImprovements(Enum):
    YES = 1
    NO = 2

class Budget(Enum):
    LOW = 1
    MEDIUM = 2
    HIGH = 3

class Time(Enum):
    LOW = 1
    MEDIUM = 2
    HIGH = 3

class Scale(Enum):
    LOW = 1
    MEDIUM = 2
    HIGH = 3



# ***** CLASSES *****

class EvaluationMethod:
    def __init__(
        self,
        name,
        measurements: list[Measurement],
        human_participants: HumanParticipants,
        subject_amount: Optional[Scale],
        data_type: DataType,
        parallelizable: Optional[Parallelizable],
        cost: Scale,
        required_time: Scale,
        difficulty: Scale,
        automated: Automated,
        iterative_potential: Scale,
        prerequisite: Optional[Enum]
    ):
        self.name = name
        self.measurements = measurements
        self.human_participants = human_participants
        self.subject_amount = subject_amount
        self.data_type = data_type
        self.parallelizable = parallelizable
        self.cost = cost
        self.required_time = required_time
        self.difficulty = difficulty
        self.automated = automated
        self.iterative_potential = iterative_potential
        self.prerequisite = prerequisite


class Requirements:
    def __init__(
        self,
        measurement: Measurement,
        data_type: RequirementsDataType,
        automated: Automated,
        human_participants: Optional[HumanParticipants],
        parallelizable: Optional[Parallelizable],
        recruitable_participants: int, # 5 / 10 / 20 / 50+
        domain_experts_available: DomainExpertsAvailable,
        skilled_interviewers_available: SkilledInterviewersAvailable,
        iterative_improvements: IterativeImprovements,
        budget: Budget,
        time: Time,
        system_type: SystemType,
        system_architecture: SystemArchitecture,
        explanations_without_request: ExplanationsWithoutRequest,
        difficult_methods: DifficultMethods,
        suggestions: Suggestions,
        textual_explanations: TextualExplanations,
        robot_human_like: RobotHumanLike
    ):
        self.measurement = measurement
        self.data_type = data_type
        self.automated = automated
        self.human_participants = human_participants
        self.parallelizable = parallelizable
        self.recruitable_participants = recruitable_participants
        self.domain_experts_available = domain_experts_available
        self.skilled_interviewers_available = skilled_interviewers_available
        self.iterative_improvements = iterative_improvements
        self.budget = budget
        self.time = time
        self.system_type = system_type
        self.system_architecture = system_architecture
        self.explanations_without_request = explanations_without_request
        self.difficult_methods = difficult_methods
        self.suggestions = suggestions
        self.textual_explanations = textual_explanations
        self.robot_human_like = robot_human_like



# ***** ALGORITHM *****

def algorithm(requirements: Requirements):
    discarded_methods = []
    suitable_methods = {}
    method_score_explanations = {}
    method_score_explanations_descriptions = {}

    for evaluation_method in evaluation_methods:
        discarded = False

        # Check if measurement and prerequisite matches, otherwise place into discarded methods list  with the specific explanation
        if requirements.measurement in evaluation_method.measurements:
            if evaluation_method.prerequisite:
                for name, value in requirements.__dict__.items():
                    if type(value) == type(evaluation_method.prerequisite):
                        if value != evaluation_method.prerequisite:
                            if type(evaluation_method.prerequisite) == TextualExplanations:
                                discarded_methods.append([evaluation_method.name, "This method has been discarded because the method requires explanations to be textual or verbal but they are not."])
                            elif type(evaluation_method.prerequisite) == SkilledInterviewersAvailable:
                                discarded_methods.append([evaluation_method.name, "This method has been discarded because the method requires skilled interviewers to be available but they are not."])
                            elif type(evaluation_method.prerequisite) == Suggestions:
                                discarded_methods.append([evaluation_method.name, "This method has been discarded because the method requires the system to make suggestions to the user but it does not."])
                            elif type(evaluation_method.prerequisite) == DomainExpertsAvailable:
                                discarded_methods.append([evaluation_method.name, "This method has been discarded because the method requires domain experts to be available but they are not."])
                            elif type(evaluation_method.prerequisite) == RobotHumanLike:
                                discarded_methods.append([evaluation_method.name, "This method has been discarded because the method requires the robot to be intended to be human-like but it is not."])
                            elif evaluation_method.prerequisite == ExplanationsWithoutRequest.YES:
                                discarded_methods.append([evaluation_method.name, "This method has been discarded because the method requires the system to provide explanations without the user requesting them but it does not."])
                            elif evaluation_method.prerequisite == ExplanationsWithoutRequest.NO:
                                discarded_methods.append([evaluation_method.name, "This method has been discarded because the method requires the system to provide explanations specifically after the user requests them but it does not."])
                            elif evaluation_method.prerequisite == SystemType.INTERNAL_PROCESS_VISIBLE:
                                discarded_methods.append([evaluation_method.name, "This method has been discarded because the method requires the system's internal process to be visible but it is not."])
                            elif evaluation_method.prerequisite == SystemArchitecture.RULE_BASED:
                                discarded_methods.append([evaluation_method.name, "This method has been discarded because the method requires the system's architecture to be rule-based but it is not."])

                            discarded = True
                            break
        else:
            discarded_methods.append([evaluation_method.name, "This method has been discarded because you want to measure {} but the method measures something different.".format(requirements.measurement.name.lower())])
            discarded = True
        # Check if human involvement option is submitted and if it doesn't align with the method, discard it
        if not discarded and requirements.human_participants and requirements.human_participants != evaluation_method.human_participants:
            if requirements.human_participants == HumanParticipants.YES and evaluation_method.human_participants == HumanParticipants.NO:
                discarded_methods.append([evaluation_method.name, "This method has been discarded because you want to involve human participants but the method is performed without them."])
            else:
                discarded_methods.append([evaluation_method.name, "This method has been discarded because you don't want to involve human participants but the method requires them."])
            discarded = True

        if discarded: continue

        # For every method that remains, calculate suitability score and add the name of the method and the score to a list

        scores = []
        scores_explanation = {}
        scores_explanation_description = {}

        # Calculate score for the resulting type of data
        if requirements.data_type:
            score = 10
            description = "The type of data you want to collect from the evaluation ({}) matches the type of data produced by this method.".format(requirements.data_type.name.lower())
            if requirements.data_type == RequirementsDataType.QUALITATIVE and evaluation_method.data_type == DataType.QUANTITATIVE:
                score = 0
                description = "You want to collect qualitative data from the evaluation but this method produces quantitative data."
            elif requirements.data_type == RequirementsDataType.QUANTITATIVE and evaluation_method.data_type == DataType.QUALITATIVE:
                score = 0
                description = "You want to collect quantitative data from the evaluation but this method produces qualitative data."
            scores.append(score)
            scores_explanation["Resulting Data"] = score
            scores_explanation_description["Resulting Data"] = description

        # Calculate score for the automation of the method
        if requirements.automated:
            score = 10
            description = "You want the method to be automated and the method is automated."
            if requirements.automated == Automated.YES and evaluation_method.automated == Automated.NO:
                score = 0
                description = "You want the method to be automated but the method is not automated."
            elif requirements.automated == Automated.NO and evaluation_method.automated == Automated.YES:
                description = "You don't require the method to be automated but the method is automated (this doesn't have any negative effect so it still scores well)."
            elif requirements.automated == Automated.NO and evaluation_method.automated == Automated.NO:
                description = "You don't require the method to be automated and the method isn't automated."
            scores.append(score)
            scores_explanation["Automation"] = score
            scores_explanation_description["Automation"] = description

        # Calculate score for the method being parallelizable
        if requirements.parallelizable:
            score = 10
            description = "You want the method to be parallelizable and the method is parallelizable."
            if requirements.parallelizable == Parallelizable.YES and evaluation_method.parallelizable == Parallelizable.NO:
                score = 0
                description = "You want the method to be parallelizable but the method is not parallelizable."
            elif requirements.parallelizable == Parallelizable.NO and evaluation_method.parallelizable == Parallelizable.YES:
                description = "You don't require the method to be parallelizable but the method is parallelizable (this doesn't have any negative effect so it still scores well)."
            elif requirements.parallelizable == Parallelizable.NO and evaluation_method.parallelizable == Parallelizable.NO:
                description = "You don't require the method to be parallelizable and the method isn't parallelizable."
            scores.append(score)
            scores_explanation["Parallelizable"] = score
            scores_explanation_description["Parallelizable"] = description

        # Calculate score for the amount of people you can recruit
        if requirements.recruitable_participants:
            if evaluation_method.subject_amount == Scale.LOW:
                participants_recommended = 12
            elif evaluation_method.subject_amount == Scale.MEDIUM:
                participants_recommended = 20
            else:
                participants_recommended = 50

            if requirements.recruitable_participants >= participants_recommended:
                score = 10
                description = "The amount of participants you can realistically recruit ({}) is equal to, or higher than the recommended amount of participants ({}) for this method.".format(requirements.recruitable_participants, participants_recommended)
            else:
                score = requirements.recruitable_participants / participants_recommended * 10
                description = "The amount of participants you can realistically recruit ({}) is lower than the recommended amount of participants ({}) for this method.".format(requirements.recruitable_participants, participants_recommended)
            scores.append(score)
            scores_explanation["Available Participants"] = score
            scores_explanation_description["Available Participants"] = description

        # Calculate score for the iterative potential of the methods
        if requirements.iterative_improvements:
            score = 10
            description = "You don't want to make iterative improvements to the system and evaluate it each time, so the iterative potential of the method is not relevant."
            if requirements.iterative_improvements == IterativeImprovements.YES:
                if evaluation_method.iterative_potential == Scale.LOW:
                    score = 0
                    description = "You want to make iterative improvements to the system and evaluate it each time but this method is not well-suited for iterative use."
                elif evaluation_method.iterative_potential == Scale.MEDIUM:
                    score = 5
                    description = "You want to make iterative improvements to the system and this method has decent iterative potential."
                else:
                    score = 10
                    description = "You want to make iterative improvements to the system and this method has very high iterative potential."
            scores.append(score)
            scores_explanation["Iterative Potential"] = score
            scores_explanation_description["Iterative Potential"] = description

        # Calculate score for the budget
        if requirements.budget:
            user_budget = "0 € - 500 €"
            if requirements.budget == Budget.MEDIUM:
                user_budget = "500 € - 3000 €"
            elif requirements.budget == Budget.HIGH:
                user_budget = "3000+ €"

            method_budget = "0 € - 500 €"
            if evaluation_method.cost == Scale.MEDIUM:
                method_budget = "500 € - 3000 €"
            elif evaluation_method.cost == Scale.HIGH:
                method_budget = "3000+ €"

            score = 10
            description = "Your budget of {} is equal to or higher than the required budget of this method ({}).".format(user_budget, method_budget)

            if requirements.budget == Budget.MEDIUM:
                if evaluation_method.cost == Scale.HIGH:
                    score = 5
                    description = "Your budget of {} is lower than the required budget of this method ({}).".format(user_budget, method_budget)
            elif requirements.budget == Budget.LOW:
                if evaluation_method.cost == Scale.MEDIUM:
                    score = 5
                    description = "Your budget of {} is lower than the required budget of this method ({}).".format(user_budget, method_budget)
                elif evaluation_method.cost == Scale.HIGH:
                    score = 0
                    description = "Your budget of {} is much lower than the required budget of this method ({}).".format(user_budget, method_budget)
            scores.append(score)
            scores_explanation["Budget"] = score
            scores_explanation_description["Budget"] = description

        # Calculate score for the required time
        if requirements.time:
            user_time = "1 Week"
            if requirements.time == Time.MEDIUM:
                user_time = "2-3 Weeks"
            elif requirements.time == Time.HIGH:
                user_time = "4+ Weeks"

            method_time = "1 Week"
            if evaluation_method.required_time == Scale.MEDIUM:
                method_time = "2-3 Weeks"
            elif evaluation_method.required_time == Scale.HIGH:
                method_time = "4+ Weeks"

            score = 10
            description = "Your available time of {} is equal to or higher than the required time for this method ({}).".format(user_time, method_time)

            if requirements.time == Time.MEDIUM:
                if evaluation_method.required_time == Scale.HIGH:
                    score = 5
                    description = "Your available time of {} is lower than the required time for this method ({}).".format(user_time, method_time)
            elif requirements.time == Time.LOW:
                if evaluation_method.required_time == Scale.MEDIUM:
                    score = 5
                    description = "Your available time of {} is lower than the required time for this method ({}).".format(user_time, method_time)
                elif evaluation_method.required_time == Scale.HIGH:
                    score = 0
                    description = "Your available time of {} is much lower than the required time for this method ({}).".format(user_time, method_time)
            scores.append(score)
            scores_explanation["Required Time"] = score
            scores_explanation_description["Required Time"] = description

        # Calculate score regarding the difficulty of each method
        if requirements.difficult_methods:
            score = 10
            description = "You are okay with performing more difficult methods."
            if requirements.difficult_methods == DifficultMethods.NO:
                if evaluation_method.difficulty == Scale.LOW:
                    score = 10
                    description = "You are not okay with performing more difficult methods but this method is of low difficulty."
                elif evaluation_method.difficulty == Scale.MEDIUM:
                    score = 5
                    description = "You are not okay with performing more difficult methods and this method is of medium difficulty."
                else:
                    score = 0
                    description = "You are not okay with performing more difficult methods and this method is of high difficulty."
            scores.append(score)
            scores_explanation["Difficulty"] = score
            scores_explanation_description["Difficulty"] = description

        # Calculate average score from all the scores
        suitable_methods[evaluation_method.name] = sum(scores) / len(scores)
        method_score_explanations[evaluation_method.name] = scores_explanation
        method_score_explanations_descriptions[evaluation_method.name] = scores_explanation_description

    # Sort by score and print every method
    """print("*** Valid Methods: ***\n")
    for key, value in sorted(suitable_methods.items(), key=lambda item: item[1], reverse=True):
        explanations = method_score_explanations[key]
        print(key + " -> " + str(value) + f" / 10.0   -> {explanations}")
    print("\n\n*** Discarded Methods: ***\n")
    for method in discarded_methods:
        print(method[0] + " -> Reason: " + method[1])"""

    return suitable_methods, discarded_methods, method_score_explanations, method_score_explanations_descriptions



# ***** DATABASE OF EVALUATION METHODS *****
evaluation_methods: list[EvaluationMethod] = []

goodness_checklist = EvaluationMethod(
    "Explanation Goodness Checklist (Checklist for Researchers)",
    [Measurement.QUALITY],
    HumanParticipants.NO,
    None,
    DataType.QUANTITATIVE,
    None,
    Scale.LOW,
    Scale.LOW,
    Scale.LOW,
    Automated.NO,
    Scale.HIGH,
    None
)
evaluation_methods.append(goodness_checklist)

satisfaction_scale = EvaluationMethod(
    "Explanation Satisfaction Scale",
    [Measurement.QUALITY],
    HumanParticipants.YES,
    Scale.HIGH,
    DataType.QUANTITATIVE,
    Parallelizable.YES,
    Scale.MEDIUM,
    Scale.MEDIUM,
    Scale.LOW,
    Automated.NO,
    Scale.MEDIUM,
    None
)
evaluation_methods.append(satisfaction_scale)

system_causability_scale = EvaluationMethod(
    "System Causability Scale (SCS)",
    [Measurement.QUALITY],
    HumanParticipants.YES,
    Scale.HIGH,
    DataType.QUANTITATIVE,
    Parallelizable.YES,
    Scale.MEDIUM,
    Scale.MEDIUM,
    Scale.LOW,
    Automated.NO,
    Scale.MEDIUM,
    None
)
evaluation_methods.append(system_causability_scale)

matching_human_explanations = EvaluationMethod(
    "Matching Human Explanations",
    [Measurement.QUALITY],
    HumanParticipants.NO,
    None,
    DataType.QUANTITATIVE,
    None,
    Scale.LOW,
    Scale.LOW,
    Scale.LOW,
    Automated.YES,
    Scale.HIGH,
    TextualExplanations.YES
)
evaluation_methods.append(matching_human_explanations)

interview = EvaluationMethod(
    "Interview",
    [Measurement.QUALITY, Measurement.TRUST, Measurement.UNDERSTANDING, Measurement.TIMING],
    HumanParticipants.YES,
    Scale.LOW,
    DataType.QUALITATIVE,
    Parallelizable.NO,
    Scale.HIGH,
    Scale.HIGH,
    Scale.HIGH,
    Automated.NO,
    Scale.MEDIUM,
    SkilledInterviewersAvailable.YES
)
evaluation_methods.append(interview)

trust_scale = EvaluationMethod(
    "Trust Scale for Robots",
    [Measurement.TRUST],
    HumanParticipants.YES,
    Scale.HIGH,
    DataType.QUANTITATIVE,
    Parallelizable.YES,
    Scale.MEDIUM,
    Scale.MEDIUM,
    Scale.LOW,
    Automated.NO,
    Scale.MEDIUM,
    None
)
evaluation_methods.append(trust_scale)

user_following_suggestions = EvaluationMethod(
    "Likelihood of users following the agent’s suggestions",
    [Measurement.TRUST],
    HumanParticipants.YES,
    Scale.HIGH,
    DataType.QUANTITATIVE,
    Parallelizable.YES,
    Scale.MEDIUM,
    Scale.MEDIUM,
    Scale.LOW,
    Automated.NO,
    Scale.MEDIUM,
    Suggestions.YES
)
evaluation_methods.append(user_following_suggestions)

user_interactions = EvaluationMethod(
    "Number of interactions between the user and the agent",
    [Measurement.TRUST],
    HumanParticipants.YES,
    Scale.HIGH,
    DataType.QUANTITATIVE,
    Parallelizable.YES,
    Scale.MEDIUM,
    Scale.MEDIUM,
    Scale.LOW,
    Automated.NO,
    Scale.MEDIUM,
    None
)
evaluation_methods.append(user_interactions)

domain_expert_experiment = EvaluationMethod(
    "Domain expert experiment with the exact application task",
    [Measurement.PERFORMANCE],
    HumanParticipants.YES,
    Scale.MEDIUM,
    DataType.QUANTITATIVE,
    Parallelizable.NO,
    Scale.HIGH,
    Scale.HIGH,
    Scale.HIGH,
    Automated.NO,
    Scale.LOW,
    DomainExpertsAvailable.YES
)
evaluation_methods.append(domain_expert_experiment)

domain_expert_experiment_simplified = EvaluationMethod(
    "Domain expert experiment with a simpler or partial task",
    [Measurement.PERFORMANCE],
    HumanParticipants.YES,
    Scale.MEDIUM,
    DataType.QUANTITATIVE,
    Parallelizable.NO,
    Scale.HIGH,
    Scale.HIGH,
    Scale.HIGH,
    Automated.NO,
    Scale.LOW,
    DomainExpertsAvailable.YES
)
evaluation_methods.append(domain_expert_experiment_simplified)

forward_simulation = EvaluationMethod(
    "Forward simulation",
    [Measurement.UNDERSTANDING],
    HumanParticipants.YES,
    Scale.HIGH,
    DataType.QUANTITATIVE,
    Parallelizable.YES,
    Scale.MEDIUM,
    Scale.MEDIUM,
    Scale.LOW,
    Automated.NO,
    Scale.MEDIUM,
    None
)
evaluation_methods.append(forward_simulation)

counterfactual_simulation = EvaluationMethod(
    "Counterfactual simulation",
    [Measurement.UNDERSTANDING],
    HumanParticipants.YES,
    Scale.HIGH,
    DataType.QUANTITATIVE,
    Parallelizable.YES,
    Scale.MEDIUM,
    Scale.MEDIUM,
    Scale.LOW,
    Automated.NO,
    Scale.MEDIUM,
    None
)
evaluation_methods.append(counterfactual_simulation)

diagramming_task = EvaluationMethod(
    "Diagramming task",
    [Measurement.UNDERSTANDING],
    HumanParticipants.YES,
    Scale.MEDIUM,
    DataType.QUALITATIVE,
    Parallelizable.YES,
    Scale.LOW,
    Scale.MEDIUM,
    Scale.MEDIUM,
    Automated.NO,
    Scale.MEDIUM,
    None
)
evaluation_methods.append(diagramming_task)

curiosity_checklist = EvaluationMethod(
    "Curiosity Checklist",
    [Measurement.TIMING],
    HumanParticipants.YES,
    Scale.MEDIUM,
    DataType.MIXED,
    Parallelizable.YES,
    Scale.MEDIUM,
    Scale.MEDIUM,
    Scale.LOW,
    Automated.NO,
    Scale.MEDIUM,
    ExplanationsWithoutRequest.NO
)
evaluation_methods.append(curiosity_checklist)

questioning_user_after_explanation = EvaluationMethod(
    "Questioning the user after each provided explanation",
    [Measurement.TIMING],
    HumanParticipants.YES,
    Scale.MEDIUM,
    DataType.QUALITATIVE,
    Parallelizable.NO,
    Scale.MEDIUM,
    Scale.MEDIUM,
    Scale.LOW,
    Automated.NO,
    Scale.MEDIUM,
    ExplanationsWithoutRequest.YES
)
evaluation_methods.append(questioning_user_after_explanation)

sagat = EvaluationMethod(
    "Situation awareness-based global assessment technique (SAGAT)",
    [Measurement.UNDERSTANDING, Measurement.TIMING],
    HumanParticipants.YES,
    Scale.LOW,
    DataType.QUALITATIVE,
    Parallelizable.NO,
    Scale.MEDIUM,
    Scale.HIGH,
    Scale.MEDIUM,
    Automated.NO,
    Scale.MEDIUM,
    None
)
evaluation_methods.append(sagat)

concurrent_think_aloud = EvaluationMethod(
    "Concurrent think-aloud",
    [Measurement.UNDERSTANDING, Measurement.TIMING],
    HumanParticipants.YES,
    Scale.LOW,
    DataType.QUALITATIVE,
    Parallelizable.NO,
    Scale.MEDIUM,
    Scale.HIGH,
    Scale.MEDIUM,
    Automated.NO,
    Scale.MEDIUM,
    None
)
evaluation_methods.append(concurrent_think_aloud)

concurrent_think_aloud_questions = EvaluationMethod(
    "Concurrent think-aloud with added question answering",
    [Measurement.UNDERSTANDING, Measurement.TIMING],
    HumanParticipants.YES,
    Scale.LOW,
    DataType.QUALITATIVE,
    Parallelizable.NO,
    Scale.HIGH,
    Scale.HIGH,
    Scale.HIGH,
    Automated.NO,
    Scale.MEDIUM,
    SkilledInterviewersAvailable.YES
)
evaluation_methods.append(concurrent_think_aloud_questions)

retrospective_think_aloud = EvaluationMethod(
    "Retrospective think-aloud",
    [Measurement.UNDERSTANDING, Measurement.TIMING],
    HumanParticipants.YES,
    Scale.LOW,
    DataType.QUALITATIVE,
    Parallelizable.NO,
    Scale.MEDIUM,
    Scale.HIGH,
    Scale.MEDIUM,
    Automated.NO,
    Scale.MEDIUM,
    None
)
evaluation_methods.append(retrospective_think_aloud)

godspeed_questionnaire = EvaluationMethod(
    "Godspeed Questionnaire",
    [Measurement.PERCEPTION],
    HumanParticipants.YES,
    Scale.HIGH,
    DataType.QUANTITATIVE,
    Parallelizable.YES,
    Scale.MEDIUM,
    Scale.MEDIUM,
    Scale.LOW,
    Automated.NO,
    Scale.MEDIUM,
    RobotHumanLike.YES
)
evaluation_methods.append(godspeed_questionnaire)

consistency_and_sufficiency = EvaluationMethod(
    "Consistency and sufficiency",
    [Measurement.FAITHFULNESS],
    HumanParticipants.NO,
    None,
    DataType.QUANTITATIVE,
    None,
    Scale.LOW,
    Scale.LOW,
    Scale.LOW,
    Automated.YES,
    Scale.HIGH,
    None
)
evaluation_methods.append(consistency_and_sufficiency)

internal_trace_comparison = EvaluationMethod(
    "Comparison of internal trace and explanation",
    [Measurement.FAITHFULNESS],
    HumanParticipants.NO,
    None,
    DataType.QUANTITATIVE,
    None,
    Scale.LOW,
    Scale.HIGH,
    Scale.LOW,
    Automated.NO,
    Scale.HIGH,
    SystemType.INTERNAL_PROCESS_VISIBLE
)
evaluation_methods.append(internal_trace_comparison)

input_perturbation = EvaluationMethod(
    "Input Perturbation",
    [Measurement.ROBUSTNESS],
    HumanParticipants.NO,
    None,
    DataType.QUANTITATIVE,
    None,
    Scale.LOW,
    Scale.LOW,
    Scale.LOW,
    Automated.YES,
    Scale.HIGH,
    None
)
evaluation_methods.append(input_perturbation)

number_of_rules = EvaluationMethod(
    "Number of rules used in an explanation",
    [Measurement.SIMPLICITY],
    HumanParticipants.NO,
    None,
    DataType.QUANTITATIVE,
    None,
    Scale.LOW,
    Scale.LOW,
    Scale.LOW,
    Automated.YES,
    Scale.HIGH,
    SystemArchitecture.RULE_BASED
)
evaluation_methods.append(number_of_rules)

number_of_features = EvaluationMethod(
    "Number of features inputted to create an explanation",
    [Measurement.SIMPLICITY],
    HumanParticipants.NO,
    None,
    DataType.QUANTITATIVE,
    None,
    Scale.LOW,
    Scale.LOW,
    Scale.LOW,
    Automated.YES,
    Scale.HIGH,
    SystemArchitecture.NEURAL_NETWORK_BASED
)
evaluation_methods.append(number_of_features)



# ***** TESTING *****

form_result_1 = Requirements(
    Measurement.QUALITY,
    RequirementsDataType.ANY,
    Automated.YES,
    HumanParticipants.YES,
    Parallelizable.YES,
    50,
    DomainExpertsAvailable.NO,
    SkilledInterviewersAvailable.NO,
    IterativeImprovements.NO,
    Budget.MEDIUM,
    Time.MEDIUM,
    SystemType.BLACK_BOX,
    SystemArchitecture.RULE_BASED,
    ExplanationsWithoutRequest.YES,
    DifficultMethods.YES,
    Suggestions.NO,
    TextualExplanations.YES,
    RobotHumanLike.NO
)

form_result_2 = Requirements(
    Measurement.UNDERSTANDING,
    RequirementsDataType.ANY,
    Automated.NO,
    HumanParticipants.YES,
    Parallelizable.YES,
    20,
    DomainExpertsAvailable.NO,
    SkilledInterviewersAvailable.YES,
    IterativeImprovements.NO,
    Budget.MEDIUM,
    Time.HIGH,
    SystemType.BLACK_BOX,
    SystemArchitecture.RULE_BASED,
    ExplanationsWithoutRequest.YES,
    DifficultMethods.YES,
    Suggestions.NO,
    TextualExplanations.YES,
    RobotHumanLike.NO
)

form_result_3 = Requirements(
    Measurement.TRUST,
    RequirementsDataType.QUALITATIVE,
    Automated.NO,
    HumanParticipants.YES,
    Parallelizable.NO,
    5,
    DomainExpertsAvailable.NO,
    SkilledInterviewersAvailable.YES,
    IterativeImprovements.NO,
    Budget.HIGH,
    Time.HIGH,
    SystemType.BLACK_BOX,
    SystemArchitecture.RULE_BASED,
    ExplanationsWithoutRequest.YES,
    DifficultMethods.NO,
    Suggestions.YES,
    TextualExplanations.YES,
    RobotHumanLike.NO
)
