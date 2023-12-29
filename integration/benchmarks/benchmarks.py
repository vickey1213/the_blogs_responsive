"""Runs the benchmarks and inserts the results into the database."""

import json
import os
import sys

import pytest
from helpers import insert_benchmarking_data


def get_lighthouse_scores(directory_path: str) -> dict:
    """Extracts the Lighthouse scores from the JSON files in the specified directory.

    Args:
        directory_path (str): The path to the directory containing the JSON files.

    Returns:
        dict: The Lighthouse scores.
    """
    scores = {}

    try:
        for filename in os.listdir(directory_path):
            if filename.endswith(".json") and filename != "manifest.json":
                file_path = os.path.join(directory_path, filename)
                with open(file_path, "r") as file:
                    data = json.load(file)
                    # Extract scores and add them to the dictionary with the filename as key
                    scores[data["finalUrl"].replace("http://localhost:3000/", "")] = {
                        "performance_score": data["categories"]["performance"]["score"],
                        "accessibility_score": data["categories"]["accessibility"][
                            "score"
                        ],
                        "best_practices_score": data["categories"]["best-practices"][
                            "score"
                        ],
                        "seo_score": data["categories"]["seo"]["score"],
                        "pwa_score": data["categories"]["pwa"]["score"],
                    }
    except Exception as e:
        print(e)
        return {"error": "Error parsing JSON files"}

    return scores


def run_pytest_and_get_results(test_path=None) -> dict:
    """Runs pytest and returns the results.

    Args:
        test_path: The path to the tests to run.

    Returns:
        dict: The results of the tests.
    """
    # Set the default path to the current directory if no path is provided
    if not test_path:
        test_path = os.getcwd()
    # Ensure you have installed the pytest-json plugin before running this
    pytest_args = ["-v", "--benchmark-json=benchmark_report.json", test_path]

    # Run pytest with the specified arguments
    pytest.main(pytest_args)

    # Print ls of the current directory
    print(os.listdir())

    with open("benchmark_report.json", "r") as file:
        pytest_results = json.load(file)

    return pytest_results


def extract_stats_from_json(json_data) -> list[dict]:
    """Extracts the stats from the JSON data and returns them as a list of dictionaries.

    Args:
        json_data: The JSON data to extract the stats from.

    Returns:
        list[dict]: The stats for each test.
    """
    # Load the JSON data if it is a string, otherwise assume it's already a dictionary
    data = json.loads(json_data) if isinstance(json_data, str) else json_data

    # Initialize an empty list to store the stats for each test
    test_stats = []

    # Iterate over each test in the 'benchmarks' list
    for test in data.get("benchmarks", []):
        stats = test.get("stats", {})
        test_name = test.get("name", "Unknown Test")
        min_value = stats.get("min", None)
        max_value = stats.get("max", None)
        mean_value = stats.get("mean", None)
        stdev_value = stats.get("stddev", None)

        test_stats.append(
            {
                "test_name": test_name,
                "min": min_value,
                "max": max_value,
                "mean": mean_value,
                "stdev": stdev_value,
            }
        )

    return test_stats


def main():
    """Runs the benchmarks and inserts the results into the database."""
    # Get the commit SHA and JSON directory from the command line arguments
    commit_sha = sys.argv[1]
    json_dir = sys.argv[2]

    # Get the PR title and database URL from the environment variables
    pr_title = os.environ.get("PR_TITLE")
    db_url = os.environ.get("DATABASE_URL")

    if db_url is None or pr_title is None:
        sys.exit("Missing environment variables")

    # Run pytest and get the results
    results = run_pytest_and_get_results()
    cleaned_results = extract_stats_from_json(results)

    # Get the Lighthouse scores
    lighthouse_scores = get_lighthouse_scores(json_dir)

    # Insert the data into the database
    insert_benchmarking_data(
        db_url, lighthouse_scores, cleaned_results, commit_sha, pr_title
    )


if __name__ == "__main__":
    main()
