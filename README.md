# Weather ETL Pipeline

The Weather ETL Pipeline is a full Python-based project that implements an automated ETL (Extract, Transform, Load) workflow for weather data. The pipeline fetches hourly temperature data from the Open-Meteo API, transforms raw JSON files into CSV format, stores the data in a SQLite database, and generates charts for the next 48 hours, providing clear and easy-to-read visualizations.

The project is organized into modular folders for better maintainability and scalability:

- **extract/**: Scripts for fetching raw weather data.
- **transform/**: Scripts to process and transform raw data into CSV.
- **load/**: Scripts to store transformed data into a SQLite database.
- **visualize/**: Scripts to create charts and visualizations.
- **docker/**: Dockerfile and docker-compose.yml for containerized execution.
- **data/**: Stores raw JSON and transformed CSV files.
- **screenshot_example/**: Example screenshots of visualizations.

This structure allows easy extension, including interactive dashboards with Plotly or Dash, alerts for extreme temperatures, logging for monitoring, and historical data analysis. The pipeline can be automated with cron jobs or Docker Compose to continuously update with the latest weather forecasts.

The Weather ETL Pipeline is perfect for portfolios, learning purposes, or as a foundation for larger data engineering projects. It uses Python 3, Pandas, Matplotlib, SQLite, Docker, and Docker Compose, providing a complete solution for weather data processing and visualization. Example screenshots are included to clearly demonstrate the pipeline functionality and chart quality.
