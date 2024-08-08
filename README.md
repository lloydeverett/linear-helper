
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
./team Squirrels # any substring of your team name; should give you your teamId
./get-states `./team Squirrels` > data-states # grab workflow states for your team
```

## Usage

```
# ./create-issue.py <team> <title> <assignee> <state> <project> <estimate> <tags>
./create-issue.py Psych "Review Standard REST Inlet changes" Lloyd "Todo" NA 1.0 "Development" "Review"
```

