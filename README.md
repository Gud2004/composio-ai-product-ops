# AI Product Operations Research Agent

This project was developed for the **Composio AI Product Operations Internship Assignment**.

## Overview

The project automates research for **100 SaaS applications** by collecting structured information about:

- Category
- Authentication methods
- Self-service vs gated onboarding
- API surface
- MCP support
- Buildability
- Main blockers
- Supporting evidence from official documentation

Instead of researching applications manually, the pipeline generates structured JSON reports automatically and aggregates the results for analysis.

---

## Features

- Automated research pipeline
- Researches 100 SaaS applications
- Generates one JSON report per application
- Resumable execution
- Aggregated analysis
- Manual verification support
- HTML case study report

---

## Project Structure

```
composio-ai-product-ops/

├── agents/
│   └── research_agent.py
│
├── analysis/
│   └── analyze.py
│
├── verification/
│   └── verify.py
│
├── data/
│   └── apps.csv
│
├── output/
│   ├── *.json
│   ├── all_results.json
│   └── failed_apps.json
│
├── report/
│   └── index.html
│
├── screenshots/
│
├── main.py
├── requirements.txt
└── README.md
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/Gud2004/composio-ai-product-ops.git

cd composio-ai-product-ops
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file:

```env
OPENROUTER_API_KEY=your_api_key_here
```

---

## Run the Research Pipeline

```bash
python main.py
```

The pipeline will:

- Read applications from `data/apps.csv`
- Research each application
- Generate one JSON report per application
- Save results inside the `output/` directory
- Generate `all_results.json`
- Support resumable execution

---

## Run Analysis

```bash
python analysis/analyze.py
```

This generates aggregated insights such as:

- Authentication distribution
- Category distribution
- Buildability
- Common blockers
- MCP support

---

## Verification

```bash
python verification/verify.py
```

The verification step compares selected applications against official documentation to improve confidence in the generated research.

---

## Technologies Used

- Python
- OpenRouter API
- Pandas
- JSON
- HTML & CSS
- Git
- GitHub

---

## Repository

https://github.com/Gud2004/composio-ai-product-ops

---

## Author

**Sanskriti Gupta**
