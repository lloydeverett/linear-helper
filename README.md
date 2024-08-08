
A little tool to create Linear tickets from the command line because doing it in the UI sometimes feels a bit slow.

Be warned: this is a *super* hacky amalgamation of JS, bash and python and the author makes no apologies.

## Setup

Create `config.js` as follows

```javascript
export const apiKey = 'YOUR_API_KEY_HERE';
```

Then grab the data

```bash
npm install
./get-teams > data-teams
./get-projects > data-projects
./get-users > data-users
./get-labels > data-labels
./team Squirrels # any substring of your team name; should give you your teamId
./get-states `./team Squirrels` > data-states # grab workflow states for your team
```

## Usage

```
# ./create-issue.py <team> <title> <assignee> <state> <project> <estimate> <tags>
./create-issue.py Psych "Do the needful" Lloyd "Todo" NA 1.0 "Development" "Review"
```

Team, assignee, etc. will be looked up based on substring match, so you don't have to be exact.

The program will read a line from stdin where you can write an issue description. Just hit enter if you don't want one.

