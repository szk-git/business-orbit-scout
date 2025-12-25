# Project: Business Orbit Scout

## Goal
Build a Python-based system that discovers businesses via the Google API, organizes them in a circular collection flow, and expands functionality to:
- Scrape each business website.
- Detect and extract the Careers page (or hiring-related pages).
- Send extracted data to DeepSeek for analysis.
- Return structured results.

## Core Requirements
- Use Python for the data pipeline and scraping functions.
- Maintain a left-side navigation UI for managing sources, jobs, and results.
- Implement a "circle" collection process (continuous loop or ring buffer) to gather and enrich businesses.
- Add extensible functions for site crawling and careers discovery.
- Integrate DeepSeek for analysis and summarization of findings.

## Deliverables
- A modular Python codebase with clear entry points and testable components.
- Scraper functions and a careers-page finder.
- A DeepSeek integration layer with retry/error handling.
- A results output format (JSON or database-ready).
- Left-side navigation UI scaffolding.
