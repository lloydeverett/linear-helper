import { apiKey } from './config.js'
import { LinearClient } from '@linear/sdk'

const client = new LinearClient({
	apiKey
});

const COUNTER_MAX = 5;

function processPage(after, counter) {
	eval('client.' + process.argv[2]).then(
		r => {
			const output = eval(process.argv[3])
			if (output === null ||
			    typeof output === 'string' ||
			    typeof output[Symbol.iterator] !== 'function') {
				console.log(r);
			} else {
				output.forEach(e => console.log(e));
			}

			if ('pageInfo' in r && r.pageInfo.hasNextPage) {
				if (counter > COUNTER_MAX) {
					console.error('Max number of pages fetched and hasNextPage is still true; giving up.')
					process.exit(1);
				}
				processPage(r.pageInfo.endCursor, counter + 1);
			}
		}
	);
}
processPage(null, 0)

