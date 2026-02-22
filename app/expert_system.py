from typing import List, Dict, Any
from .schemas import UserSymptom
from .models import Rule

def calculate_diagnosis(user_symptoms: List[UserSymptom], all_rules: List[Rule]) -> Dict[int, float]:
    """
    Calculates the Certainty Factor for diseases based on user symptoms and expert rules.
    Returns a dictionary of {disease_id: certainty_factor}.
    """

    # Group rules by disease
    rules_by_disease: Dict[int, List[Rule]] = {}
    for rule in all_rules:
        if rule.disease_id not in rules_by_disease:
            rules_by_disease[rule.disease_id] = []
        rules_by_disease[rule.disease_id].append(rule)

    # Map user symptoms for quick lookup: {symptom_id: confidence}
    user_symptom_map = {s.symptom_id: s.confidence for s in user_symptoms}

    results = {}

    for disease_id, rules in rules_by_disease.items():
        cf_combined = 0.0

        for rule in rules:
            if rule.symptom_id in user_symptom_map:
                user_cf = user_symptom_map[rule.symptom_id]
                expert_cf = rule.expert_cf

                # CF for this specific evidence
                cf_current = expert_cf * user_cf

                # Combine using CF formula: CF_new = CF_old + CF_current * (1 - CF_old)
                # This assumes positive CFs. If negative, formula differs slightly (CF1 + CF2) / (1 - min(|CF1|, |CF2|)) etc.
                # For this expert system, we assume positive correlation (symptom implies disease).

                if cf_current > 0:
                    cf_combined = cf_combined + cf_current * (1 - cf_combined)

        if cf_combined > 0:
            results[disease_id] = cf_combined

    return results
