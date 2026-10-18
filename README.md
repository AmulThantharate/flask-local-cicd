# Flask Local CI/CD & Jenkins Groovy Pipeline

A minimal Flask task management API with automated test suite and Jenkins CI/CD pipeline written in Groovy.

---

## Project Structure

```
flask-local-cicd/
├── app.py              # Flask application with /health and /tasks endpoints
├── requirements.txt    # Project dependencies (flask, pytest)
├── pytest.ini          # Pytest configuration with pythonpath = .
├── test/
│   └── test_app.py     # Pytest test suite
├── Jenkinsfile         # Jenkins CI/CD pipeline (Groovy DSL)
└── .gitignore          # Git ignore rules for Python, venv, and cache
```

---

## Local Development & Testing

1. **Activate virtual environment:**
   ```bash
   source venv/bin/activate
   ```

2. **Run tests:**
   ```bash
   pytest -v test/test_app.py
   ```

3. **Run Flask application:**
   ```bash
   python3 app.py
   ```

---

## Learning Groovy with Jenkins

Jenkins pipelines use **Groovy** syntax under the hood. There are two primary pipeline styles:

### 1. Declarative Pipeline (Recommended)
Defined using the `pipeline { ... }` block (see [`Jenkinsfile`](file:///home/f33/linux-homework/flask-local-cicd/Jenkinsfile)). It provides a structured schema while supporting raw Groovy scripts inside `script { ... }` blocks.

Key Groovy concepts demonstrated in [`Jenkinsfile`](file:///home/f33/linux-homework/flask-local-cicd/Jenkinsfile):
- **Groovy Methods / Functions**:
  ```groovy
  def printBanner(String message) {
      echo ">>> ${message}"
  }
  ```
- **Dynamic Typing (`def`)**:
  ```groovy
  def appName = 'flask-local-cicd'
  ```
- **String Interpolation (GStrings with double quotes)**:
  ```groovy
  echo "Project: ${appName}"
  ```
- **Collections & Closures**:
  ```groovy
  ['Flask', 'Pytest', 'Jenkins'].each { item ->
      echo "  * ${item}"
  }
  ```
- **Maps (Key-Value pairs)**:
  ```groovy
  def meta = [author: 'Amul', tool: 'Jenkins']
  echo meta.tool
  ```

---

## Setting up in Jenkins (Local `http://localhost:8080`)

1. Open Jenkins at `http://localhost:8080`.
2. Click **New Item** -> select **Pipeline** -> enter a name (e.g. `flask-local-cicd`).
3. Under the **Pipeline** configuration section:
   - **Definition**: Choose *Pipeline script from SCM*.
   - **SCM**: Select *Git*.
   - **Repository URL**: Your GitHub repository URL (`git@github.com:AmulThantharate/flask-local-cicd.git`).
   - **Branch Specifier**: `*/main`.
   - **Script Path**: `Jenkinsfile`.
4. Click **Save** and then **Build Now** to run the pipeline!
