# aws-billing-notifier
AWS Lambda scripts for notification of aws billing.

## 1. Setup

### Setup Python environment for development

#### Install pyenv

```
$ brew install pyenv
```

```
export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init -)"
```

#### Install Python

This project is using Python 3.6

```
$ pyenv install 3.6
$ pyenv global 3.6
```

#### Install pipenv

```
$ pip install pipenv
```

Or via Homebrew

```
$ brew install pipenv
```

#### Sync pipenv in project

```
$ pipenv sync --dev
```

### Install package manager

```
$ brew install yarn
```

### Setup serverless

```
$ yarn install
$ ./node_modules/serverless/bin/serverless config credentials --provider aws --key 'YOUR_AWS_ACCESS_KEY_ID' --secret 'YOUR_AWS_SECRET_ACCESS_KEY'
```

#### Use below steps If you have troubles above

```
$ mkdir ~/.aws
$ vim ~/.aws/credentials 
[default]
aws_access_key_id=[your key here]
aws_secret_access_key=[your secret here]
```

## 2. Usage
You can set slack notification url and channel in `serverless.yml`.  
Please modify `functions.billing_estimate.events.schedule.input` .  
The default corn job is set on Sundays and Wednesdays.   
You can also change the frequency.  

## 2. Deploy

Make sure you pull recent changes.

```
$ ./node_modules/serverless/bin/serverless deploy -v --stage production
```

