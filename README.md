## Web Crawler

### Overview
This is a short web app using web scraping to filter a news page to get only required and necessary news

### Tech stack
- Python 3.10.12
- React
- TypeScript
- FastAPI
- MaterialUI

### Features
- **Web Scraping**: Get only the content that the user wants from a webpage
- **User interface**: Simple UI to display the results
- **API Integration**: Comunication between front-end and back-end

## Setup

### Prerequisites
- **Python 3.10.x**
- **Nodejs** Ensure having the lts version

### Run the project
1. Clone the repository:
```
git clone https://github.com/MarcoAguirre/web-crawler.git
```
2. Install the dependencies (You only ned to do this one time):
```
make setup-api
```
then
```
make setup-ui
```
3. Run the project:

**Front-end**:
```
make run-ui
```
**Back-end**
```
make run-api
```

### Create .env file
```
cp .env-example .env
```
