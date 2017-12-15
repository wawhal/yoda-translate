# Yoda Translate Slack Bot

![](https://media.giphy.com/media/3oxHQI3RRfRJoNcz4c/giphy.gif)

This is a slack bot that will convert any sentence to a Yoda style sentence. For example:

```
Input: This app is so cool.
Output: So cool this app is.
```

## Requirements

To get this app running, you need to have:

1. [hasura CLI tool](https://docs.hasura.io/0.15/manual/install-hasura-cli.html)
2. A project on [Google Cloud Platform](https://console.cloud.google.com/home/). You can create one for free :)
3. Some Slack workspace

## Deployment Guide

*The app will be **ready and working** in just 9 steps. This app requires several secret tokens to be set up. If you are stuck anywhere for more than 5 minutes, contact me at rishichandra.wawhal@gmail.com*

1. Get this project.

```
$ hasura quickstart rishi/yoda-translate-slackbot
```

2. Make an app in your slack workspace. Copy your slack token and add it to your hasura project secrets so that you do not have to explicitly mention it in the code.

```
$ hasura secret update slack.token '<slack_token>'
```

3. Add a slash command to your workspace (say /yodify). Add the URL to be `https://yoda.<cluster-name>.hasura-app.io/echo`. Run `hasura cluster status` to get your cluster name.
4. Go to interactive components. Add the URL as `https://yoda.<cluster-name>.hasura-app.io/confirm`.
5. Add a bot user. Name it whatever you want; preferably Yoda.
6. Go to `OAuth and Permissions` and add the following permission scope.

![Scope](https://github.com/coco98/python-slack-bot/raw/master/readme-assets/scope.png)

7. Scroll up and install the app to the workspace. Once you install, copy the Bot-Access-Token and add it to your secrets.

```
$ hasura secret update bot.access.token '<bot_access_token>'
```

8. Finally, enable the  [Google Cloud Natural Language API](https://console.cloud.google.com/home/) for your project and get your API key. Add this to your secrets. Check how to [get API key](https://support.google.com/cloud/answer/6158862?hl=en)

```
$ hasura secret update google.api.key <google_api_key>
```

9. Just push this project to your Hasura cluster and you are set. Run the following from project directory.

```
$ git add . && git commit -m "First commit"
$ git push hasura master
```

## Usage

Once the app is live, you can see it in action in any of your channels of your slack workspace. Just run `/yodify This app is so cool`. You will get your result :)

## Modification

If you want to make any changes to the code, the source code for this application lives in `microservices/yoda/app/src` directory. Modify whatever you wish to and repeat *step 9* of the deployment guide to see the changes live.

