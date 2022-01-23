GitHub says:

> Any environment variables set in an env context defined at the workflow level in the caller workflow are not propagated to the called workflow.

So let's use a `.env` file loaded into outputs instead by using the nifty [Dotenv Action](https://github.com/marketplace/actions/dotenv-action). It uses [dotenv](https://www.npmjs.com/package/dotenv) under the hood.