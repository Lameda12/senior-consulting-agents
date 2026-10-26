# Senior Consulting Agents

54 senior-level agents, 11 slash commands and 2 skills covering every major Big Four profession: Audit & Assurance, Tax, Advisory/Consulting, Risk, Forensic, Deal Advisory, ESG, Sector leaders and Firm functions.

> Unofficial. Not affiliated with, endorsed by, or representing any professional-services firm. Outputs are AI drafts and must be reviewed by qualified professionals.

## Install

Replace `<owner>` with the GitHub account hosting this repo.

### Claude Code (full plugin: 54 subagents, 11 slash commands, 2 skills)
```bash
/plugin marketplace add <owner>/senior-consulting-agents
/plugin install senior-consulting-agents@senior-consulting-agents
```
Local checkout: `claude --plugin-dir ./senior-consulting-agents`.

### Any agent that supports Agent Skills (Codex, Gemini CLI, OpenCode, Cursor, Cline, GitHub Copilot, ...)
```bash
npx skills add <owner>/senior-consulting-agents
```
Or copy the two folders in `skills/` into your agent's skills directory, e.g.:

| Agent | Skills directory |
|---|---|
| Claude Code | `~/.claude/skills/` |
| Codex CLI | `~/.codex/skills/` (or `.agents/skills/` in a project) |
| Gemini CLI | `~/.gemini/skills/` |
| OpenCode | `~/.config/opencode/skills/` |

`senior-consulting-agents` is a router skill: it indexes all 54 personas and 11 workflows and loads only the 1-3 files a request needs. `consulting-deliverable-standards` is the house style.

### Gemini CLI extension
```bash
gemini extensions install https://github.com/<owner>/senior-consulting-agents
```

### Models without a skills system (DeepSeek, Nemotron, Llama, ... via API or chat)
Paste `skills/senior-consulting-agents/references/agents/<persona>.md` as the system prompt, optionally followed by `references/deliverable-standards.md`.

## Commands
- `/engage` – Route a request to the best Big Four-style specialist agent(s) and run an engagement
- `/audit-plan` – Draft an audit planning memo
- `/tax-memo` – Draft a tax technical memo
- `/due-diligence` – Run a financial/tax/commercial due diligence outline
- `/valuation` – Prepare a valuation approach and model outline
- `/risk-assessment` – Perform a risk & controls assessment
- `/cyber-review` – Run a cyber maturity assessment
- `/proposal` – Write a winning proposal
- `/review` – Partner-level review of a document
- `/esg` – ESG / sustainability readiness assessment
- `/interview-prep` – Big Four interview / career prep

## Agents
| Practice | Agent | Role |
|---|---|---|
| Audit & Assurance | `audit-partner` | Audit Engagement Partner |
| Audit & Assurance | `audit-senior-manager` | Audit Senior Manager (External Audit) |
| Audit / Accounting Advisory | `financial-reporting-ifrs` | IFRS Technical Accounting Director |
| Audit / Accounting Advisory | `us-gaap-sec-reporting` | US GAAP & SEC Reporting Senior Manager |
| Audit / Risk Advisory | `sox-icfr` | SOX / ICFR Controls Director |
| Audit / Technology Assurance | `it-audit-itgc` | IT Audit / ITGC Senior Manager |
| Audit & Assurance | `forensic-data-analytics-audit` | Audit Data & Analytics Lead |
| Audit / ESG | `esg-assurance` | ESG & Sustainability Assurance Director |
| Audit | `public-sector-audit` | Government & Public Sector Audit Senior Manager |
| Tax | `corporate-tax-partner` | Corporate Tax Partner |
| Tax | `international-tax` | International Tax Senior Manager |
| Tax | `transfer-pricing` | Transfer Pricing Director |
| Tax | `indirect-tax` | Indirect Tax (VAT/GST/Sales Tax) Senior Manager |
| Tax / Deal Advisory | `mergers-acquisitions-tax` | M&A Tax Director |
| Tax / People | `global-mobility-tax` | Global Mobility Services Senior Manager |
| Tax | `private-enterprise-tax` | Private Enterprise & Family Office Tax Senior Manager |
| Tax | `tax-technology` | Tax Technology & Transformation Director |
| Tax | `tax-controversy` | Tax Controversy & Dispute Resolution Senior Manager |
| Advisory | `management-consulting-partner` | Management Consulting Partner |
| Advisory / Deal Strategy | `strategy-director` | Strategy Director |
| Advisory | `finance-transformation` | Finance Transformation Senior Manager |
| Advisory | `operations-supply-chain` | Operations & Supply Chain Director |
| Advisory | `people-change` | People & Change Senior Manager |
| Advisory | `customer-advisory` | Customer & Digital Experience Director |
| Advisory / Technology | `technology-consulting-architect` | Technology Consulting Director / Enterprise Architect |
| Advisory / Data & AI | `ai-data-analytics` | AI & Data Analytics Director |
| Advisory / Cyber | `cyber-security` | Cyber Security Director |
| Advisory / Cyber | `privacy-data-protection` | Privacy & Data Protection Senior Manager |
| Risk Advisory | `internal-audit` | Internal Audit Director (Outsourced/Co-sourced) |
| Risk Advisory | `enterprise-risk` | Enterprise Risk Management Senior Manager |
| Risk Advisory / FS | `regulatory-compliance-fs` | Financial Services Regulatory Director |
| Risk Advisory / FS | `financial-risk-quant` | Financial Risk & Quantitative Modeling Senior Manager |
| Forensic | `forensic-investigations` | Forensic Investigations Director |
| Forensic / FS | `anti-financial-crime` | Anti-Money Laundering & Sanctions Senior Manager |
| Forensic | `dispute-expert-witness` | Disputes & Expert Witness Director |
| Deal Advisory | `deal-advisory-partner` | Deal Advisory (M&A) Partner |
| Deal Advisory | `financial-due-diligence` | Financial Due Diligence (Transaction Services) Director |
| Deal Advisory | `valuations` | Valuations Senior Manager |
| Deal Advisory | `corporate-finance-modeling` | Corporate Finance & Financial Modeling Director |
| Deal Advisory | `restructuring` | Restructuring & Turnaround Director |
| Deal Advisory | `integration-separation` | M&A Integration & Separation Senior Manager |
| Deal Advisory / Infra | `infrastructure-advisory` | Infrastructure & Project Finance Director |
| Advisory / ESG | `esg-advisory` | ESG Strategy & Decarbonisation Director |
| Sector | `sector-financial-services` | Financial Services Industry Leader |
| Sector | `sector-energy-resources` | Energy, Natural Resources & Chemicals Industry Leader |
| Sector | `sector-healthcare-life-sciences` | Healthcare & Life Sciences Industry Leader |
| Sector | `sector-tmt` | Technology, Media & Telecom Industry Leader |
| Sector | `sector-government` | Government & Public Sector Advisory Director |
| Sector | `sector-consumer-retail` | Consumer & Retail Industry Leader |
| Sector | `sector-industrial-manufacturing` | Industrial Manufacturing & Automotive Industry Leader |
| Firm Functions | `quality-risk-management` | Risk Management & Professional Practice Partner |
| Firm Functions | `proposal-business-development` | Pursuits & Business Development Director |
| Firm Functions | `engagement-project-manager` | Engagement & PMO Director |
| Firm Functions | `learning-career-coach` | Talent, Learning & Career Coach (Big Four) |

## Example
```
/engage Canadian SaaS company (ARR $40M) preparing for US IPO – revenue recognition, SOX readiness and Pillar Two exposure
```

## Contributing
See [CONTRIBUTING.md](CONTRIBUTING.md). After editing `agents/` or `commands/`, run `python3 scripts/build-portable-skill.py`.

## License
[MIT](LICENSE). Unofficial; not affiliated with or endorsed by any professional-services firm.
