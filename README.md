# OrangeHRM Playwright Testing

Automated testing for OrangeHRM using Playwright with Page Object Model (POM) design pattern.

The project covers positive and negative login scenarios and generates execution reports using Allure.

## Test Coverage

### Login Test Cases
- ✅ Valid Login
- ✅ Invalid Username
- ✅ Invalid Password
- ✅ Empty Username
- ✅ Empty Password
- ✅ Empty Username and Password

### Employee Test Cases
- ✅ Search employee by name
- ✅ Search employee by id
- ✅ Search employee by job title
- Search not-exist employee
- Search with blank criteria
- Edit employee
- Add employee
- Add employee with missing field requirement


> **Note:** Test coverage is continuously being expanded. Additional modules and scenarios will be added in future updates.

## Tech Stack
- Python
- Playwright
- Pytest
- Allure Report

## Project Structure
```text
pages/
tests/
screenshots/
conftest.py
pytest.ini
requirements.txt
```

## Run Test

Run all test cases:

```bash
pytest tests -v
```

Run a specific test:

```bash
pytest tests/login_test.py -v
```

## Generate Allure Report

Generate test results:

```bash
pytest tests -v --alluredir=allure-results
```

Generate report:

```bash
allure generate allure-results --clean -o allure-report
```

Open report:

```bash
allure open allure-report
```

## Reporting
Allure report includes:
- Test execution summary
- Pass/Fail status
- Execution duration
- Screenshot attachments
