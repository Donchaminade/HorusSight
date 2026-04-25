import os
import json
from google import genai
from google.genai import types
from dotenv import load_dotenv

# Chargement de l'environnement
# BASE_DIR = horussight/ (parent de engine/)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# Cherche .env dans horussight/ puis dans HorusSight/ (racine du projet)
load_dotenv(os.path.join(BASE_DIR, '.env'))
load_dotenv(os.path.join(os.path.dirname(BASE_DIR), '.env'), override=False)

class EWABAAnalyzer:
    """
    Expert Web-Application Brain Assistant (EWABA)
    Moteur d'intelligence expert pour HorusSight.
    """
    def __init__(self, api_key=None, model_id="gemini-2.0-flash"):
        self.api_key = api_key or os.getenv("GEMINI_API_KEY")
        self.model_id = model_id
        
        if self.api_key:
            self.client = genai.Client(api_key=self.api_key)
        else:
            self.client = None
            print("LOG:[!] EWABA Error: GEMINI_API_KEY non trouvée. Mode dégradé activé.")

    def analyze_vulnerabilities(self, target: str, findings: list) -> dict:
        """
        Effectue une analyse de risque globale et détaillée sur les résultats du scan.
        """
        if not self.client:
            return self._get_mock_analysis(target, findings)

        prompt = f"""
        As a world-class cybersecurity expert (Ewaba Intelligence), perform a comprehensive risk analysis 
        for the target {target} based on these detected vulnerabilities: {json.dumps(findings)}.
        
        YOUR OBJECTIVE: Communicate clearly to TWO audiences (the technical developer and the non-technical executive/business owner).
        
        Required Output: Strictly valid JSON object matching this exact structure:
        {{
          "overallRiskScore": integer (0-100),
          "businessImpactSummary": "string describing professional business impact in English",
          "simplifiedRiskSummary": "a SIMPLE and METAPHORICAL analogy (e.g., using a house, a car, or a vault) for a non-technical person",
          "remediationRoadmap": {{
            "immediate": ["Action 1", "Action 2"],
            "shortTerm": ["Action 3"],
            "longTerm": ["Action 4"]
          }},
          "severityClassification": "Critical" | "High" | "Medium" | "Low",
          "exhaustiveSolutions": [
            {{
              "category": "string (e.g., XSS, SQLi, Security Headers)",
              "description": "Precise technical explanation of the vulnerability",
              "simplifiedSummary": "Simplified explanation for someone with no IT background",
              "action": "Precise technical instructions (Include code snippets or configuration examples if possible)",
              "responsibleParty": "Developer" | "System Admin" | "Security Expert",
              "priorityLevel": integer (1-10, 1=Urgent),
              "precautions": "Precautions to take before applying the fix",
              "contactAdvice": "Who should be informed about this issue?",
              "contactChannels": ["Email", "Slack", "Meeting"],
              "contactTemplate": "Ready-to-use professional message template to report the issue",
              "remediationChecklist": [
                 "Step 1: Technical verification",
                 "Step 2: Business validation"
              ]
            }}
          ]
        }}
        """

        try:
            response = self.client.models.generate_content(
                model=self.model_id,
                contents=prompt,
                config=types.GenerateContentConfig(
                    response_mime_type='application/json'
                )
            )
            
            # Directly parse the JSON if response_mime_type is respected
            return json.loads(response.text)
            
        except Exception as e:
            print(f"[!] EWABA Analysis Failed: {str(e)}")
            return self._get_mock_analysis(target, findings)

    def _get_mock_analysis(self, target, findings) -> dict:
        """
        Returns a high-quality fallback analysis in case of API error or missing key.
        """
        return {
            "overallRiskScore": 65 if findings else 10,
            "businessImpactSummary": "The lack of security headers or the presence of injection vulnerabilities exposes your infrastructure to critical attacks.",
            "simplifiedRiskSummary": "Your perimeter is like a fortress with high walls but unencrypted public communication corridors.",
            "remediationRoadmap": {
                "immediate": ["Apply missing security headers", "Sanitize user inputs"],
                "shortTerm": ["Architecture audit", "Implement a WAF"],
                "longTerm": ["CI/CD Security Scanning integration"]
            },
            "severityClassification": "High" if findings else "Low",
            "exhaustiveSolutions": [
                {
                    "category": findings[0]['type'] if findings else "Configuration",
                    "description": "Technical correction of the detected vulnerability.",
                    "simplifiedSummary": "Locking down access points",
                    "action": "Use prepared statements or strict Content Security Policies.",
                    "responsibleParty": "Developer",
                    "priorityLevel": 1,
                    "precautions": "Test in staging environment first.",
                    "contactAdvice": "Inform the CTO or IT Lead.",
                    "contactChannels": ["Email"],
                    "contactTemplate": "Hello, a security vulnerability has been detected...",
                    "remediationChecklist": ["Fix", "Test", "Deploy"]
                }
            ]
        }
