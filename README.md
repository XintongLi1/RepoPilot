# RepoPilot

RepoPilot is a powerful tool for static code analysis that provides an overview of code quality trends and summaries across repositories. Leveraging data scraped from GitHub repositories, RepoPilot gathers comprehensive information on the repository and performs effective code analysis. The tool has already scraped numerous popular repositories and added them to the dataset. Users can also add specific repository links of their choice, expanding the dataset with new insights.

## Installation
1. Create a venv
2. From root dir, run `pip install -r requirements.txt`
3. Go to frontend
4. Run `npm i`

## Running it
### Backend
From root, run `python -m flask --app backend run -p 3001`
### Frontend
From frontend folder, run `npm start`
