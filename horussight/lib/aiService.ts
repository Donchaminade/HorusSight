import { GoogleGenerativeAI } from '@google/generative-ai';


// Instantiation is moved inside functions to avoid crash if env var is missing in browser
function getAiClient() {
  const apiKey = process.env.GEMINI_API_KEY || process.env.NEXT_PUBLIC_GEMINI_API_KEY;
  if (!apiKey) return null;
  return new GoogleGenerativeAI(apiKey);
}

export interface VulnSolution {
  category: string;
  description: string;
  simplifiedSummary: string;
  action: string;
  responsibleParty: 'User' | 'Developer' | 'Security Expert';
  priorityLevel: number;
  precautions: string;
  contactAdvice: string;
  contactChannels: string[];
  contactTemplate?: string;
  remediationChecklist: string[];
}

export interface AIRiskAnalysis {
  overallRiskScore: number;
  businessImpactSummary: string;
  simplifiedRiskSummary: string;
  remediationRoadmap: {
    immediate: string[];
    shortTerm: string[];
    longTerm: string[];
  };
  severityClassification: 'Critical' | 'High' | 'Medium' | 'Low' | 'Info';
  exhaustiveSolutions: VulnSolution[];
}

export async function analyzeVulnerabilities(target: string, vulnerabilities: any[]): Promise<AIRiskAnalysis> {
  const ai = getAiClient();
  
  if (!ai) {
    // Return high-quality mock data if API key is missing
    return {
      overallRiskScore: 78,
      severityClassification: 'High',
      businessImpactSummary: "The absence of security headers exposes your infrastructure to injection and clickjacking attacks. This could compromise the integrity of user sessions and allow attackers to retrieve sensitive information via unauthorized third-party domains.",
      simplifiedRiskSummary: "Your site is like a house with closed doors but unlocked windows. It's easy to protect, but right now, any prowler can see what's happening inside.",
      remediationRoadmap: {
        immediate: ["Configure Content-Security-Policy (CSP) headers", "Enable HSTS to force HTTPS"],
        shortTerm: ["Audit exposed endpoints", "Implement a Web Application Firewall (WAF)"],
        longTerm: ["Implement automatic API key rotation", "OWASP Top 10 training for developers"]
      },
      exhaustiveSolutions: vulnerabilities.map((v, i) => ({
        category: v.category || "Security Configuration",
        description: `Fixing vulnerability: ${v.type}`,
        simplifiedSummary: "Locking unauthorized access",
        action: `Add the '${v.type.toLowerCase()}' directive in the server configuration (Nginx/Apache) or via a security middleware.`,
        responsibleParty: 'Developer',
        priorityLevel: i + 1,
        precautions: "Test first on a staging environment to avoid blocking legitimate scripts (especially with CSP).",
        contactAdvice: "Contact your DevOps team or hosting provider to apply these rules at the server level.",
        contactChannels: ["Email", "Support Ticket", "Slack #devops"],
        contactTemplate: `[SECURITY ADVISORY - URGENT]\n\nSubject: Critical Security Vulnerability Detected on ${target}\n\nDear Infrastructure Team,\n\nDuring a recent security audit conducted by HorusSight, we identified a high-risk vulnerability on our production assets: ${v.type}.\n\nIMPACT: This flaw exposes our infrastructure to unauthorized data exfiltration and session hijacking.\n\nREQUIRED ACTION:\n- Implementation of ${v.type} headers\n- Validation of the security handshake\n- Recursive scan of all sub-paths\n\nTechnical documentation for the patch is available in the HorusSight Dashboard.\n\nBest regards,\nSecurity Operations Center (SOC)`,
        remediationChecklist: ["Identify configuration file", "Add the header", "Restart the server", "Verify with curl -I"]
      }))
    };
  }

  const model = ai.getGenerativeModel({ model: 'gemini-2.0-flash' });
  const prompt = `Perform an EXHAUSTIVE security analysis for ${target} based on these vulnerabilities: ${JSON.stringify(vulnerabilities)}. 
  IMPORTANT: ALL TEXT CONTENT IN THE JSON (summaries, actions, templates, checklists) MUST BE IN ENGLISH.
  Return valid JSON conform to AIRiskAnalysis interface.`;
  
  try {
    const result = await model.generateContent(prompt);
    const text = result.response.text();
    // Basic cleanup in case Gemini returns markdown blocks
    const jsonStr = text.replace(/```json|```/g, '').trim();
    return JSON.parse(jsonStr);
  } catch (error) {
    console.error('Gemini Analysis Failed:', error);
    throw error;
  }
}

export async function analyzeSecurityLogs(logs: any[]) {
  const ai = getAiClient();
  if (!ai) {
    return {
      detectedPatterns: [
        {
          patternType: "Suspected Brute Force",
          description: "Rapid sequence of failed login attempts from the same IP address.",
          threatActorProfile: "Automated botnet prospecting for vulnerable targets.",
          severity: "High",
          recommendedImmediateAction: "Ban the IP address via the firewall and enable 2FA."
        }
      ],
      overallSecurityHealth: "Attention required - Suspicious activity detected on authentication endpoints.",
      intelligenceBrief: "The attacks appear coordinated but have not yet successfully targeted specific accounts."
    };
  }
  
  const model = ai.getGenerativeModel({ model: 'gemini-2.0-flash' });
  const prompt = `Analyze these security logs and detect patterns: ${JSON.stringify(logs)}. Return JSON brief. ALL TEXT MUST BE IN ENGLISH.`;
  const result = await model.generateContent(prompt);
  return JSON.parse(result.response.text().replace(/```json|```/g, '').trim());
}

export async function assessSecurityPosture(scanHistory: any[]) {
  const ai = getAiClient();
  if (!ai) {
    return {
      scoreTrend: 'Stable',
      currentPostureSummary: "Your security is generally healthy but has room for improvement. The basics are in place, but defense-in-depth lacks maturity.",
      keyStrengths: ["Fast incident response", "Good access management"],
      primaryWeaknesses: ["Incomplete HTTP configuration", "Absence of detailed application logs"],
      strategicRecommendations: ["Invest in a SIEM monitoring solution", "Automate vulnerability scans."]
    };
  }
  
  const model = ai.getGenerativeModel({ model: 'gemini-2.0-flash' });
  const prompt = `Assess security posture from history: ${JSON.stringify(scanHistory)}. Return JSON brief. ALL TEXT MUST BE IN ENGLISH.`;
  const result = await model.generateContent(prompt);
  return JSON.parse(result.response.text().replace(/```json|```/g, '').trim());
}

export async function askAboutVulnerability(vuln: any, context: string): Promise<string> {
  const ai = getAiClient();
  if (!ai) {
    return `As Ewaba Intelligence, I can tell you that this vulnerability (${vuln.type}) is like leaving your keys in the lock. It's convenient for you, but it is also convenient for thieves. \n\nTo fix this, I recommend moving these "keys" to a safe place (like environment variable secrets) and restricting who can access them. Alternatively, you can use a secret management service like Vault or AWS Secrets Manager.`;
  }
  
  const model = ai.getGenerativeModel({ model: 'gemini-2.0-flash' });
  const prompt = `As EWABA security mentor, explain ${JSON.stringify(vuln)} to a user asking: ${context}. Keep it educational and premium.`;
  const result = await model.generateContent(prompt);
  return result.response.text();
}
