# Python Web Scraping Learning Repository

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![Web Scraping](https://img.shields.io/badge/Web-Scraping-orange.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

This repository contains my journey of learning web scraping techniques using Python. It covers various methods from basic scraping to handling AJAX content and pagination.

## 📂 Project Structure

.
├── ajax/                  - Scraping dynamic AJAX content
│   └── main.py
├── basic/                 - Basic web scraping fundamentals
│   ├── countries.csv
│   └── main.py
├── header-spoofing/       - Using headers to avoid detection
│   └── main.py
├── pagination/            - Handling paginated content
│   ├── football.csv
│   └── main.py

## Technologies Used

- Python 3.x
- BeautifulSoup4
- Requests
- Pandas (for data handling)
- Other scraping-related libraries

## Getting Started

### Prerequisites
- Python 3.x installed
- Pip package manager

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/Zulhaditya/web-scraping-python.git
   cd web-scraping-python
   ```

2. Install required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Learning Modules

### 1. Basic Web Scraping
- Introduction to BeautifulSoup
- Extracting data from static pages
- Saving data to CSV
- File: `basic/main.py`

### 2. Header Spoofing
- Modifying request headers
- Avoiding basic bot detection
- Simulating different browsers
- File: `header-spoofing/main.py`

### 3. AJAX Content Handling
- Dealing with dynamically loaded content
- Analyzing XHR requests
- Using browser developer tools
- File: `ajax/main.py`

### 4. Pagination Handling
- Scraping across multiple pages
- Building URL patterns
- Combining data from multiple sources
- File: `pagination/main.py`

## Important Notes

- Always check a website's `robots.txt` before scraping
- Respect websites' terms of service
- Implement delays between requests to avoid overloading servers
- Consider using proxies for large-scale scraping

## Contributing

Contributions are welcome! Please follow these steps:
1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some your-feature'`)
4. Push to the branch (`git push origin feature/your-feature`)
5. Open a Pull Request