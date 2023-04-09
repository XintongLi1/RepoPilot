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

1. **Summary**
    This tool provides an overview summary of all the repositories or search for a specific one.
2. **Rank by impact**
   This feature allows you to view all high impact repositories.  
   Repositories are scored based on the severity of their issues, and those with more severe issues are ranked higher. Repositories must have at least 20 issues and one HIGH level issue to be listed as "high impact".
   It is a useful feature to identify repositories with good code quality.
3. **Add new repo**
   Users can submit a GitHub URL for that repo to be analysed and added to the database.
4. **Update**
   While ranking all repositories, you can click on the "Update" button to update their metadata.
5. **Pagination**
   Results returned by a query can be paginated for better display.
6. **URL Sanitization**
   Uploaded URLs are sanitized to prevent malicious code execution.
7. **AutoComplete Search**
   Search results appear in real-time as users type in the summary section of the app.
   Allows users to find and view repositories with the same prefix easily. 

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
