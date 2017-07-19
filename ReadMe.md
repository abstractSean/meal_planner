# Meal Planner

This is a learning project to design a meal planning application to be run as a web application.

## Initial plans
### Modules
- foods:
	- Maintains food database.
	- tracks overall food consumption, real & planned.
	- Different food classes, general to more specific.
- groceries:
	- Maintains grocery lists.
	- Customizale per store layout (WinCo, Safeway, Walmart, etc.)
- meals:
	- Generates psuedo random weekly/bi-weekly/monthly meal plans from recipes.
	- References existing pantry and generates required gorcery lists.
	- Accounts for effort/resources required for meal and checks against schedule.
	- Implements agent based algorithm scheduling/weighting (machine learning/AI).
	- Tracks individual taste/preference/rating as feedback (machine learning)
	- Tracks actual meals for analysis/feedback.
- pantry:
	- Maintains database of pantry foods.
	- Used in generating meal plans and gorcery lists.
	- Tracks "staples".
	- Tracks brands and individual taste/preference/ratings of food types.
- recipes:
	- Maintains recipe database.
	- Tracks individual taste/preference/rating.
	- Scrapes online recipe databases and guesses/suggests new recipes.
- stores:
	- Maintains store database.
	- Includes brands carried, and layout of store for grocery list optimization.
	- Tracks shopping trip times for analysis.

### Tools
- Github hosted source code and git version control following [Conventional Commits](https://conventionalcommits.org/)
- Free Python Anywhere account hosting.
- Flask & bootstrap framework for front end development.
- MySQL
- SQLAlchemy

	
## Future plans	
### Tools
- AWS for hosting, aim for free/low cost account.
- Transition to non-relational databases where appropriate.


## Things I hope to learn:
Again, this is a learning project, this is what I hope to learn.
### Wider concepts
- Object oriented vs functional programming
- File parsing with regular expressions
- Version control
- Automated testing
- Relational databases
- ORMs
- Web application hosting/front end development
- Non-relational databases
- Machine Learning
- Complex system, agent based programming
- Data analysis


### Specific tools
- Python
- Git/Github
- Automated testing?
- Relational databases
	-MySQL
	-SQLlite?
- ORMs
	- SQLAlchemy
	- peewee?
	- PonyORM?
- Web application hosting
	- Python Anywhere
	- AWS
	- home server
- Web application front end development frameworks
	- Flask
	- Bootstrap
	- Django
- non-relational databases (no SQL)
	-Postgre (sp?)
	


