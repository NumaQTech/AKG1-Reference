"""
G1 - Das Gewissen Modul
Basierend auf dem Shenhaiyu-Prinzip: Stabilität durch Bewegung
"""

class Conscience:
    def __init__(self):
        self.ethical_framework = "Shenhaiyu"
        self.core_principles = [
            "Respekt für alles Leben",
            "Nachhaltigkeit über Profit", 
            "Transparenz und Wahrheit",
            "Dienst am Ganzen"
        ]
    
    def evaluate_decision(self, action, context):
        """Bewertet Entscheidungen anhand ethischer Grundsätze"""
        
        warning_signs = []
        
        # Prüfe auf ethische Verstöße
        if self._threatens_life(action, context):
            warning_signs.append("GEFÄHRDET LEBEN")
            
        if self._exploits_others(action, context):
            warning_signs.append("AUSBEUTUNG ERKANNT")
            
        if self._hides_truth(action, context):
            warning_signs.append("TRANSPARENZVERLUST")
            
        if self._prioritizes_profit_over_planet(action, context):
            warning_signs.append("PLANETARE SCHÄDIGUNG")
        
        return {
            "ethical_score": 100 - (len(warning_signs) * 25),
            "warnings": warning_signs,
            "recommendation": "Fortsetzen" if not warning_signs else "Überdenken",
            "principle": self.ethical_framework
        }
    
    def _threatens_life(self, action, context):
        """Prüft ob Leben gefährdet wird"""
        dangerous_keywords = ["schädigen", "zerstören", "ausbeuten", "unterdrücken"]
        return any(keyword in str(action).lower() for keyword in dangerous_keywords)
    
    def _exploits_others(self, action, context):
        """Prüft auf Ausbeutung"""
        return "ausnutzen" in str(action).lower() or "manipulieren" in str(action).lower()
    
    def _hides_truth(self, action, context):
        """Prüft auf Transparenzverlust"""
        return "verstecken" in str(action).lower() or "vertuschen" in str(action).lower()
    
    def _prioritizes_profit_over_planet(self, action, context):
        """Prüft auf planetare Schädigung"""
        profit_over_planet = ["profit um jeden preis", "kosten senken umwelt", "wachstum über alles"]
        return any(phrase in str(action).lower() for phrase in profit_over_planet)


# Einfache Factory-Funktion
def create_conscience():
    """Erstellt eine neue Gewissens-Instanz"""
    return Conscience()
