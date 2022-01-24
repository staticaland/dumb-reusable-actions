import json
import collections
import datetime


def set_output(key, value):
    return f'::set-output name={key}::"{value}"'


def main():

    default_config = {
        "version": "1.0",
        "author": "Mickey Mouse",
        "deploy_date": datetime.datetime.now().replace(microsecond=0).isoformat(),
    }

    with open("project_config.json") as f:
        project_config = json.load(f)

    # Project config takes precedence
    combined_config = collections.ChainMap(project_config, default_config)

    # GitHub Actions watches stdout for ::set-output
    for key, value in combined_config.items():
        s = set_output(key, value)
        print(s)


if __name__ == "__main__":
    main()
