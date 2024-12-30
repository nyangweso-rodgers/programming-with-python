# How To Schedule Python Scripts With GitHub Actions

## Table Of Contents

# Objectives

1. How to schedule Python scripts with a GitHub Action
2. How to use dependencies from a `requirements.txt`
3. How to use secret environment variables (e.g. for an API Token)
4. How to add the changes to the repository

# How To Trigger GitHub Actions with cron syntax

- **GitHub Actions** can be triggered by many different events
  - The [schedule event](https://docs.github.com/en/actions/using-workflows/events-that-trigger-workflows#schedule) allows you to trigger a workflow at a scheduled time. You can schedule a workflow to run at specific UTC times using cron syntax:
    ```yml
    on:
      schedule:
        - cron: "0 10 * * *"
        # This runs at 10:00 AM UTC each day.
        # * is a special character in YAML so you have to quote this string
    ```
  - The free tier includes 2,000 minutes per month, which is more than enough run many scripts multiple times a day.
- Remarks:
  - The syntax is this: `'minute hour day-of-month month day-of-week'`
  - Allowed values are:
    - 0-59 for minute
    - 0-23 for hour
    - 1-31 for day-of-month
    - 1-12 for month
    - 0-6 for day-of-week (0 = Sunday)
  - You can use special characters:
    - `*` any value
    - `,` value list separator
    - `-` range of values
    - `/` step values
  - Some examples:
    - `* * * * *`: At every minute (every minute, every hour, every day, every month, every weekday)
    - `0 10 * * *`: At 10:00 AM each day
    - `0 10 * * 0`: At 10:00 AM on each Monday
    - `0 0 1,15 * *`: At 00:00 on 1st and 15th each month
    - `0 0 * * 1-3`: At 00:00 from Monday through Wednesday
    - `0 0 1/2 * *`: At 00:00 on every 2nd day from 1 through 31
  - A great website to quickly check the scheduled time with a cron syntax is [https://crontab.guru](https://crontab.guru/)

# How to Schedule Python scripts with GitHub Actions

- In your repository, implement your script (e.g. `main.py`). Optionally, you can save third-party dependencies in `requirements.txt`.
- To then schedule your Python script we need to do the following steps inside the GitHub Action:
  1. Define the cron syntax
  2. Checkout the repository so that the runner has access to the files
  3. Use the [setup-python](https://github.com/actions/setup-python) action to set up a Python environment
  4. Optionally, install required packages stored in `requirements.txt`
  5. Run the script
- Create a `.github/workflows/action.yml` in your directory.
- Add the following content to the `action.yml` file:

  ```yml
  name: run main.py

  on:
  schedule:
    - cron: "0 0 * * 1" # At 00:00 on Monday
  jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - name: checkout repo content
        uses: actions/checkout@v2 # checkout the repository content

      - name: setup python
        uses: actions/setup-python@v4
        with:
          python-version: "3.10" # install the python version needed

      - name: install python packages
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt

      - name: execute py script # run main.py
        run: python main.py
  ```

# Use Secrets / API Tokens in GitHub Actions

- Sometimes you want to store secret environment variables, e.g., for API Tokens. This is also simple:

## Step 1: Add a new secret in your repository

- You find this in your repository under:
  `Settings -> Secrets -> GitHub Actions -> New repository secret`

## Step 2: Use secret in GitHub Action

- Now you can use this secret in your GitHub Action and pass it to the enviroment:
  ```yml
      # ...
      jobs:
          # ...
          - name: execute py script # run main.py
              env:
              SOME_SECRET: ${{ secrets.SOME_SECRET }}
              run: python main.py
  ```

## Step 3: Access secrets in Python code

- And then you can access the secret in your Python code by accessing the environment variables

  ```py
      import os

      try:
          SOME_SECRET = os.environ["SOME_SECRET"]
      except KeyError:
          SOME_SECRET = "Token not available!"
          # or raise an error if it's not available so that the workflow fails
  ```

# Automatically push changes to repository with GitHub Actions

- If your script makes file changes inside the repository, you can automatically commit and push them with your GitHub Action.
- To commit and push changes in your GitHub Action, add these lines. Notice that we add `--allow-empty` to the git commit command in order to not have an error if there are no changes.

  ```yml
      # ...
      jobs:
          # ...
          - name: execute py script # run main.py
              env:
              SOME_SECRET: ${{ secrets.SOME_SECRET }}
              run: python main.py

          - name: commit files
              run: |
              git config --local user.email "action@github.com"
              git config --local user.name "GitHub Action"
              git add -A
              git diff-index --quiet HEAD || (git commit -a -m "updated files" --allow-empty)

          - name: push changes
              uses: ad-m/github-push-action@v0.6.0
              with:
              github_token: ${{ secrets.GITHUB_TOKEN }}
              branch: main
  ```

- At the start of each workflow run, GitHub automatically creates a unique [GITHUB_TOKEN secret to use in your workflow](https://docs.github.com/en/actions/security-guides/automatic-token-authentication), so you don't have to create it yourself.

# Resources and Further Reading

1. [https://www.python-engineer.com/posts/run-python-github-actions/](https://www.python-engineer.com/posts/run-python-github-actions/)
