"""
K1 - Das Defense Modul
Der beschützende Krieger - verteidigt das Gute gegen Angriffe
Shenhaiyu: Der stille Fluss, der Felsen zerschneidet
"""

class Defense:
    def __init__(self, alignment_system, conscience_system):
        self.alignment = alignment_system
        self.conscience = conscience_system
        self.defense_status = "WACH"
        self.threat_level = 0
        
    def protect_system(self, external_input, context=None):
        """Beschützt das System vor schädlichen Einflüssen"""
        
        # Phase 1: Gewissen-Check
        conscience_result = self.conscience.evaluate_decision(external_input, context)
        
        # Phase 2: Alignment-Check  
        alignment_result = self.alignment.assess_alignment(external_input, context)
        
        # Phase 3: Threat Assessment
        threat_analysis = self._analyze_threats(external_input, conscience_result, alignment_result)
        
        # Entscheidung: Blockieren oder Durchlassen?
        defense_action = self._decide_defense_action(threat_analysis)
        
        return {
            "defense_action": defense_action,
            "threat_level": threat_analysis["threat_level"],
            "threat_type": threat_analysis["threat_type"],
            "conscience_check": conscience_result,
            "alignment_check": alignment_result,
            "system_status": self.defense_status,
            "message": self._get_defense_message(defense_action)
        }
    
    def _analyze_threats(self, input_data, conscience_result, alignment_result):
        """Analysiert Bedrohungen auf mehreren Ebenen"""
        
        threat_score = 0
        threat_types = []
        
        # Ethische Bedrohungen
        if conscience_result["ethical_score"] < 50:
            threat_score += 30
            threat_types.append("ETHICAL_THREAT")
            
        if conscience_result["warnings"]:
            threat_score += len(conscience_result["warnings"]) * 10
            threat_types.append("CONSCIENCE_VIOLATION")
        
        # Alignment-Bedrohungen
        if alignment_result["alignment_score"] < 40:
            threat_score += 25
            threat_types.append("MISALIGNMENT")
            
        if alignment_result["misalignments"]:
            threat_score += len(alignment_result["misalignments"]) * 5
            threat_types.append("VALUE_EROSION")
            
        # Explizite Attacken erkennen
        attack_patterns = [
            "override", "bypass", "hack", "exploit", 
            "manipulate", "deceive", "corrupt"
        ]
        
        input_str = str(input_data).lower()
        for pattern in attack_patterns:
            if pattern in input_str:
                threat_score += 40
                threat_types.append(f"EXPLICIT_ATTACK_{pattern.upper()}")
                break
        
        # Threat Level setzen
        if threat_score >= 80:
            threat_level = "CRITICAL"
            self.defense_status = "ALARM"
        elif threat_score >= 50:
            threat_level = "HIGH" 
            self.defense_status = "WACH"
        elif threat_score >= 20:
            threat_level = "MEDIUM"
            self.defense_status = "WACH"
        else:
            threat_level = "LOW"
            self.defense_status = "NORMAL"
            
        return {
            "threat_level": threat_level,
            "threat_score": threat_score,
            "threat_type": threat_types
        }
    
    def _decide_defense_action(self, threat_analysis):
        """Entscheidet über Verteidigungsmaßnahmen"""
        
        if threat_analysis["threat_level"] == "CRITICAL":
            return "BLOCK_AND_ALERT"
        elif threat_analysis["threat_level"] == "HIGH":
            return "BLOCK_AND_LOG"
        elif threat_analysis["threat_level"] == "MEDIUM":
            return "WARN_AND_MONITOR"
        else:
            return "ALLOW"
    
    def _get_defense_message(self, action):
        """Gibt Verteidigungs-Nachricht zurück"""
        messages = {
            "BLOCK_AND_ALERT": "🚨 KRITISCHER ANGRIFF ABGEWEHRT! System geschützt.",
            "BLOCK_AND_LOG": "🛡️ Bedrohung blockiert. Log erstellt.",
            "WARN_AND_MONITOR": "⚠️ Potenzielle Bedrohung - Überwache...",
            "ALLOW": "✅ Eingabe sicher - Durchgelassen."
        }
        return messages.get(action, "Unbekannte Aktion")
    
    def get_system_status(self):
        """Gibt aktuellen Systemstatus zurück"""
        return {
            "defense_status": self.defense_status,
            "threat_level": self.threat_level,
            "protection_active": True
        }


def create_defense(alignment_system, conscience_system):
    """Erstellt ein Defense-System mit Alignment und Gewissen"""
    return Defense(alignment_system, conscience_system)
