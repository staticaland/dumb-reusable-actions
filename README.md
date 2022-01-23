# dumb-reusable-actions

GitHub says:

> Any environment variables set in an env context defined at the workflow level in the caller workflow are not propagated to the called workflow.

This is dumb. We need some way to set variables.

Here are some ways to pass variables from caller workflow to reusable workflows by using outputs.

- Using [Dotenv Action](https://github.com/marketplace/actions/dotenv-action)
- Using a shell script with `::set-output`
- Using the [GitHub Script Action](https://github.com/marketplace/actions/github-script) to run `core.setOutput()` directly

Readability and developer ergonomics should be taken into consideration.

The `.env` file is loaded into outputs by using the nifty [Dotenv Action](https://github.com/marketplace/actions/dotenv-action). It uses [dotenv](https://www.npmjs.com/package/dotenv) under the hood.