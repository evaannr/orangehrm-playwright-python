# OrangeHRM Playwright Testing

Automation testing project untuk OrangeHRM menggunakan Playwright dan pytest.

## Project Structure

```
test_orangehrm_playwright/
├── pages/              # Page Object Model classes
├── tests/              # Test cases
├── utils/              # Utility functions and helpers
├── screenshots/        # Screenshot captures during test execution
├── reports/            # Test reports and results
├── conftest.py         # Pytest configuration and fixtures
├── pytest.ini          # Pytest settings
├── requirements.txt    # Python dependencies
└── README.md           # This file
```

## Setup

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Install Playwright Browsers
```bash
playwright install
```

## Running Tests

### Run all tests
```bash
pytest
```

### Run specific test
```bash
pytest tests/test_login.py
```

### Run with specific markers
```bash
pytest -m smoke
pytest -m regression
```

### Run with verbose output
```bash
pytest -v
```

### Generate HTML report
```bash
pytest --html=reports/report.html --self-contained-html
```

## Project Details

- **Framework**: Playwright (async)
- **Test Runner**: pytest
- **Language**: Python
