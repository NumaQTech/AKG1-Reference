"""
A1 - Das Alignment Modul 
Ausrichtung der KI an menschliche Werte und planetare Gesundheit
Basierend auf Shenhaiyu: Der Fluss sucht sich seinen Weg
"""

class Alignment:
    def __init__(self, conscience_system):
        self.conscience = conscience_system
        self.core_values = {
            "planet_health": 100,
            "human_wellbeing": 100, 
            "knowledge_sharing": 100,
            "long_term_thinking": 100
        }
        self.misalignment_warnings = []
    
    def assess_alignment(self, action_plan, context=None):
        """Bewertet ob Aktionen mit unseren Werten alignen"""
        
        # Das Gewissen befragen
        conscience_check = self.conscience.evaluate_decision(action_plan, context)
        
        # Eigene Alignment-Checks
        alignment_score = self._calculate_alignment_score(action_plan)
        value_impact = self._assess_value_impact(action_plan)
        
        # Kombinierte Bewertung
        final_score = (conscience_check["ethical_score"] + alignment_score) // 2
        
        return {
            "alignment_score": final_score,
            "conscience_evaluation": conscience_check,
            "value_impact": value_impact,
            "misalignments": self.misalignment_warnings,
            "recommendation": self._get_alignment_recommendation(final_score),
            "principle": "Shenhaiyu Alignment"
        }
    
    def _calculate_alignment_score(self, action_plan):
        """Berechnet den Alignment-Score"""
        score = 100
        
        # Positive Alignment-Faktoren
        positive_indicators = [
            "gemeinschaft", "nachhaltig", "transparent", 
            "bilden", "heilen", "wasser", "leben"
        ]
        
        # Negative Alignment-Faktoren  
        negative_indicators = [
            "ausbeuten", "zerstören", "verstecken",
            "kontrollieren", "monopolisieren", "verschmutzen"
        ]
        
        action_text = str(action_plan).lower()
        
        for indicator in positive_indicators:
            if indicator in action_text:
                score += 5
                
        for indicator in negative_indicators:
            if indicator in action_text:
                score -= 15
                self.misalignment_warnings.append(f"Wertverletzung: {indicator}")
        
        return max(0, min(100, score))
    
    def _assess_value_impact(self, action_plan):
        """Bewertet Impact auf Kernwerte"""
        impacts = {}
        action_text = str(action_plan).lower()
        
        # Planetare Gesundheit
        if any(word in action_text for word in ["wasser", "sauber", "ökologisch", "solar"]):
            impacts["planet_health"] = "+"
        elif any(word in action_text for word in ["verschmutzen", "abfall", "abholzen"]):
            impacts["planet_health"] = "-"
            
        # Menschliches Wohl
        if any(word in action_text for word in ["bilden", "heilen", "befähigen"]):
            impacts["human_wellbeing"] = "+" 
        elif any(word in action_text for word in ["ausbeuten", "unterdrücken"]):
            impacts["human_wellbeing"] = "-"
            
        return impacts
    
    def _get_alignment_recommendation(self, score):
        """Gibt Alignment-Empfehlung basierend auf Score"""
        if score >= 80:
            return "Perfekt aligniert - Vollgas!"
        elif score >= 60:
            return "Gut aligniert - Weiter so!"
        elif score >= 40:
            return "Teilweise aligniert - Überarbeiten"
        else:
            return "Fehlaligniert - Komplett neu denken!"


def create_alignment(conscience_system):
    """Erstellt ein Alignment-System mit Gewissen"""
    return Alignment(conscience_system)
