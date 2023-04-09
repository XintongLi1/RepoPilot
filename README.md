# RepoPilot

RepoPilot is a powerful tool for static code analysis that provides an overview of code quality trends and summaries across repositories. Leveraging data scraped from GitHub repositories, RepoPilot gathers comprehensive information on the repository and performs effective code analysis. The tool has already scraped numerous popular repositories and added them to the dataset. Users can also add specific repository links of their choice, expanding the dataset with new insights.


## System Design and Implementation

The project's frontend has been developed using the React library, while the backend is built using Python with Flask as the web framework. To implement the database management system, the project employs MySQL.
Additionally, [SemGrep](https://semgrep.dev/), an open-source static analysis engine for finding bugs and detecting dependency vulnerabilities, is used for code analysis. 

### Database Schema

* Owner (<u>name</u>, followers) 
* User(<u>name</u>, following)
  * FK: name references Owner
* Organization(<u>name</u>)
  * FK: name references Owner
* OrganizationUser(<u>user_name</u>, <u>organization_name</u>)
  * FK: user_name references User(name)
  * FK: orgnization_name references Organization(name)
* Repository(<u>name</u>, <u>owner</u>, stars, forks, watching)
  * FK: owner references Owner(name)
* File(<u>path</u>, <u>repo_name</u>, <u>owner</u>, name, language)
  * FK: (repo_name, owner) references Repository (name, owner)
* Issue(<u>id</u>, <u>path</u>, <u>repo_name</u>, <u>owner</u>, check_id, start_line, end_line, category, impact)
  * FK: (path, repo_name, owner) references File (path, repo_name, owner)
* Contributor(<u>user_name</u>, <u>owner</u>, <u>repo_name</u>)
  * FK: user_name references User (name)
  * FK: (owner, repo_name) references Repository (owner, name)
* RepositoryQueue(<u>owner</u>, <u>repo_name</u>, date_inserted)
  * FK: (owner, repo_name) references Repository (owner, name)

### Features


## Installation
1. Create a virtual environment
2. From root dir, run `pip install -r requirements.txt`
3. Go to frontend
4. Run `npm i`

## How to Run it
### Backend

From root, run `python -m flask --app backend run -p 3001`.

Run mysql and create a database called `repopilot`

### Frontend
From frontend folder, run `npm start`
