# dumb-reusable-actions

[GitHub says](https://docs.github.com/en/actions/using-workflows/reusing-workflows#limitations):

> Any environment variables set in an env context defined at the workflow level in the caller workflow are not propagated to the called workflow.

This is dumb. We need some way to set variables.

Here are some ways to pass variables from caller workflow to reusable workflows by using outputs.

Readability and developer ergonomics is taken into consideration.

- Using [Dotenv Action](https://github.com/marketplace/actions/dotenv-action)
    - The `.env` file can be used locally ➕
    - Dependencies ➖
- Using a shell script with `::set-output`
    - Ugly syntax which decreases readability ➖
    - Not possible to use `shfmt` on the code ➖
- Using a Python script
    - Very easy to read ➕
    - Programmable ➕
    - Built in JSON library ➕
- Using the [GitHub Script Action](https://github.com/marketplace/actions/github-script) to run `core.setOutput()` directly
    - Familiar Javascript syntax ➕
    - Programmable
    - Dependencies ➖

The `.env` file is loaded into outputs by using the nifty [Dotenv Action](https://github.com/marketplace/actions/dotenv-action). It uses [dotenv](https://www.npmjs.com/package/dotenv) under the hood.

## Other caveats

Readability and developer ergonomics should be taken into consideration.
[act](https://github.com/nektos/act) [does not support reusable workflows](https://github.com/nektos/act/issues/826).

The `.env` file is loaded into outputs by using the nifty [Dotenv Action](https://github.com/marketplace/actions/dotenv-action). It uses [dotenv](https://www.npmjs.com/package/dotenv) under the hood.

## Considerations

Get rid of the shackles and use https://jsonnet.org/ or https://cuelang.org/ instead.
