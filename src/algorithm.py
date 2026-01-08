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

    for evaluation_method in evaluation_methods:
        discarded = False

        # Check if measurement and prerequisite matches, otherwise place into discarded methods list  with the specific explanation
        if requirements.measurement in evaluation_method.measurements:
            if evaluation_method.prerequisite:
                for name, value in requirements.__dict__.items():
                    if type(value) == type(evaluation_method.prerequisite):
                        if value != evaluation_method.prerequisite:
                            discarded_methods.append([evaluation_method.name, "This method has been discarded because the necessary prerequisites are not met."])
                            discarded = True
                            break
        else:
            discarded_methods.append([evaluation_method.name, "This method has been discarded because the measurement criteria does not match your requirements."])
            discarded = True
        # Check if human involvement option is submitted and if it doesn't align with the method, discard it
        if not discarded and requirements.human_participants and requirements.human_participants != evaluation_method.human_participants:
            discarded_methods.append([evaluation_method.name, "This method has been discarded because the human involvement criteria does not match your requirements."])
            discarded = True

        if discarded: continue

        # For every method that remains, calculate suitability score and add the name of the method and the score to a list

        scores = []
        scores_explanation = {}

        # Calculate score for the resulting type of data
        if requirements.data_type:
            score = 10
            if requirements.data_type == RequirementsDataType.QUALITATIVE and evaluation_method.data_type == DataType.QUANTITATIVE:
                score = 0
            elif requirements.data_type == RequirementsDataType.QUANTITATIVE and evaluation_method.data_type == DataType.QUALITATIVE:
                score = 0
            scores.append(score)
            scores_explanation["Resulting Data"] = score

        # Calculate score for the automation of the method
        if requirements.automated:
            score = 10
            if requirements.automated == Automated.YES and evaluation_method.automated == Automated.NO:
                score = 0
            scores.append(score)
            scores_explanation["Automation"] = score

        # Calculate score for the method being parallelizable
        if requirements.parallelizable:
            score = 10
            if requirements.parallelizable == Parallelizable.YES and evaluation_method.parallelizable == Parallelizable.NO:
                score = 0
            scores.append(score)
            scores_explanation["Parallelizable"] = score

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
            else:
                score = requirements.recruitable_participants / participants_recommended * 10
            scores.append(score)
            scores_explanation["Available Participants"] = score

        # Calculate score for the iterative potential of the methods
        if requirements.iterative_improvements:
            score = 10
            if requirements.iterative_improvements == IterativeImprovements.YES:
                if evaluation_method.iterative_potential == Scale.LOW:
                    score = 0
                elif evaluation_method.iterative_potential == Scale.MEDIUM:
                    score = 5
                else:
                    score = 10
            scores.append(score)
            scores_explanation["Iterative Potential"] = score

        # Calculate score for the budget
        if requirements.budget:
            score = 10
            if requirements.budget == Budget.MEDIUM:
                if evaluation_method.cost == Scale.HIGH:
                    score = 5
            elif requirements.budget == Budget.LOW:
                if evaluation_method.cost == Scale.MEDIUM:
                    score = 5
                elif evaluation_method.cost == Scale.HIGH:
                    score = 0
            scores.append(score)
            scores_explanation["Budget"] = score

        # Calculate score for the required time
        if requirements.time:
            score = 10
            if requirements.time == Time.MEDIUM:
                if evaluation_method.required_time == Scale.HIGH:
                    score = 5
            elif requirements.time == Time.LOW:
                if evaluation_method.required_time == Scale.MEDIUM:
                    score = 5
                elif evaluation_method.required_time == Scale.HIGH:
                    score = 0
            scores.append(score)
            scores_explanation["Required Time"] = score

        # Calculate score regarding the difficulty of each method
        if requirements.difficult_methods:
            score = 10
            if requirements.difficult_methods == DifficultMethods.NO:
                if evaluation_method.difficulty == Scale.LOW:
                    score = 10
                elif evaluation_method.difficulty == Scale.MEDIUM:
                    score = 5
                else:
                    score = 0
            scores.append(score)
            scores_explanation["Difficulty"] = score

        # Calculate average score from all the scores
        suitable_methods[evaluation_method.name] = sum(scores) / len(scores)
        method_score_explanations[evaluation_method.name] = scores_explanation

    # Sort by score and print every method
    """print("*** Valid Methods: ***\n")
    for key, value in sorted(suitable_methods.items(), key=lambda item: item[1], reverse=True):
        explanations = method_score_explanations[key]
        print(key + " -> " + str(value) + f" / 10.0   -> {explanations}")
    print("\n\n*** Discarded Methods: ***\n")
    for method in discarded_methods:
        print(method[0] + " -> Reason: " + method[1])"""

    return suitable_methods, discarded_methods, method_score_explanations



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
