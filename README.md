# Question 12 – Electricity Bill Calculation

The sample tariff is illustrative only:
- First 100 units: ₹2 per unit
- Next 100 units: ₹3 per unit
- Above 200 units: ₹5 per unit

For 250 units, the bill is ₹750.

## Run locally
```bash
pip install -r requirements.txt
python app.py
```
Open `http://localhost:5000/bill?units=250`.

## Docker
```bash
docker build -t electricity-app .
docker run -d -p 5000:5000 --name electricity-container electricity-app
```

## Jenkins
Create a Pipeline job connected to this GitHub repository. Select **Pipeline script from SCM**, choose Git, enter the repository URL, and set Script Path to `Jenkinsfile`. Ensure the Jenkins agent has Docker installed and permission to run it.

## GitHub
```bash
git init
git add .
git commit -m "Add electricity bill calculator"
git branch -M main
git remote add origin https://github.com/USERNAME/REPOSITORY.git
git push -u origin main
```
