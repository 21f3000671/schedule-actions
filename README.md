# Daily IMDb Scraper GitHub Action

This repository contains a GitHub Action that automatically scrapes the IMDb Top 250 movies daily and commits the data to the repository.

## Workflow Details

- **Schedule**: Runs daily at 14:30 UTC
- **Trigger**: Can also be manually triggered via workflow_dispatch
- **Email**: Uses email `21f3000671@ds.study.iitm.ac.in` in the Git configuration
- **Output**: Creates a JSON file with daily IMDb Top 250 data

## Files

- `.github/workflows/daily-scrape.yml`: The GitHub Actions workflow
- `scrape.py`: Python script that scrapes IMDb Top 250 movies
- `imdb-top250-YYYY-MM-DD.json`: Daily data files

## Manual Trigger

You can manually trigger the workflow by:
1. Going to the Actions tab in your GitHub repository
2. Selecting "Daily IMDb Scraper" workflow
3. Clicking "Run workflow"

## Data Format

Each JSON file contains:
```json
{
  "timestamp": "2025-06-22T14:30:00+00:00",
  "movies": [
    {
      "title": "1. The Shawshank Redemption",
      "year": "1994",
      "rating": "9.3"
    }
  ]
}
```
