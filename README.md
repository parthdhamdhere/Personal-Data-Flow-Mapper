
 🔐 Personal Data Flow Mapper

> Enterprise-grade static analysis for detecting and tracing sensitive data movement across Python applications.

Track how emails, phone numbers, passwords, user IDs, and other personal information travel through your codebase — from assignment to external exposure — using Python AST-powered analysis with zero runtime execution.

---

# Overview

Modern applications process massive amounts of user data, but most engineering teams lack visibility into:

- Where sensitive data originates
- How it propagates through the application
- Which APIs, databases, or logs expose it
- Whether compliance boundaries are violated

**Personal Data Flow Mapper** automates this analysis using static code inspection.

It scans Python source files, detects personal data variables, follows their movement through function calls, and identifies high-risk sink operations such as:

- External API requests
- Database writes
- Logging statements
- File persistence
- Messaging systems

All without executing a single line of code.

---

# Key Features

## 🔍 AST-Based Static Analysis
Uses Python’s built-in `ast` module to safely analyze source code structure.

## 🧠 Sensitive Data Detection
Automatically identifies variables related to:

- Emails
- Phone numbers
- Passwords
- IP addresses
- National IDs
- Addresses
- Birth dates
- Authentication tokens

## 🚨 Sink Detection
Detects when sensitive data reaches:

- HTTP requests
- Database queries
- Logs
- Storage layers
- External integrations

## 📊 Risk Classification
Every finding is categorized by severity:

| Level | Meaning |
|---|---|
| LOW | Sensitive data source detected |
| HIGH | Sensitive data exposed to a sink |

## 📁 Multi-Project Scanning
Analyze:

- Single files
- Entire repositories
- Monorepos
- CI/CD pipelines

## 📦 Zero Runtime Dependencies
Core engine relies entirely on Python standard libraries.

---

# Architecture


```

```text
File created.

```text
Python Source Code
        │
        ▼
┌────────────────────┐
│    AST Parser      │
└─────────┬──────────┘
          │
          ▼
┌────────────────────┐
│   Source Detector  │
└─────────┬──────────┘
          │
          ▼
┌────────────────────┐
│    Flow Tracker    │
└─────────┬──────────┘
          │
          ▼
┌────────────────────┐
│    Sink Analyzer   │
└─────────┬──────────┘
          │
          ▼
┌────────────────────┐
│   Risk Classifier  │
└─────────┬──────────┘
          │
          ▼
 Terminal Report / JSON Export

```

# Installation

**Clone Repository**

```bash
git clone [https://github.com/yourusername/data-flow-mapper.git](https://github.com/yourusername/data-flow-mapper.git)
cd data-flow-mapper

```

**Requirements**

* Python 3.8+
* No external dependencies required

# Quick Start

**Scan a Sample Project**

```bash
python main.py sample_app

```

**Scan Your Own Codebase**

```bash
python main.py /path/to/project

```

**Scan a Single File**

```bash
python main.py app/services/user_service.py

```

**Export Results as JSON**

```bash
python main.py src/ --json

```

# Sample Output

**Terminal Report**

```text
============================================================
 PERSONAL DATA FLOW MAPPER — SCAN REPORT
============================================================

 Total Findings : 8
 Sources Found  : 3
 Sinks Found    : 5
 Risk Level     : HIGH

============================================================
 SOURCES
============================================================

[LOW] sample_app/user_service.py:12
 Variable: user_email

[LOW] sample_app/user_service.py:13
 Variable: user_name

[LOW] sample_app/user_service.py:14
 Variable: phone

============================================================
 SINKS
============================================================

[HIGH] sample_app/user_service.py:17
 Variable : user_email
 Sink     : requests.post

[HIGH] sample_app/user_service.py:23
 Variable : phone
 Sink     : cursor.execute

```

**JSON Output**

```json
[
  {
    "type": "SOURCE",
    "variable": "user_email",
    "line": 12,
    "file": "sample_app/user_service.py",
    "risk": "LOW"
  },
  {
    "type": "SINK",
    "variable": "user_email",
    "sink": "requests.post",
    "line": 17,
    "file": "sample_app/user_service.py",
    "risk": "HIGH"
  }
]

```

# Supported Detection Patterns

**Personal Data Keywords**

* email
* phone
* name
* address
* dob
* birth
* ssn
* password
* ip_address
* location
* gender
* user_id
* national_id

**Sink Keywords**

* requests.post
* requests.get
* cursor.execute
* send_mail
* print
* log
* insert
* save

# Project Structure

```text
data-flow-mapper/
│
├── mapper/
│   ├── __init__.py
│   ├── scanner.py
│   ├── patterns.py
│   └── reporter.py
│
├── sample_app/
│   └── user_service.py
│
├── main.py
├── requirements.txt
└── README.md

```

# CI/CD Integration

```bash
python main.py src/ --json > findings.json

```

```python
import json
import sys

findings = json.load(open("findings.json"))

high_risk = any(
    item["risk"] == "HIGH"
    for item in findings
)

if high_risk:
    print("Sensitive data exposure detected.")
    sys.exit(1)

```
