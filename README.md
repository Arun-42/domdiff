## domdiff
Get difference betweent two states of DOM.

### Usage
The two states are provided as HTML to an LLM
1. `python run.py` will ask for the two html components to be pasted as input
2. on the site to diff DOMs, paste the contents of `getdom.js` into the console. This will create a button to right top corner to copy current HTML
3. copy the HTML for two different states and provide as stdin to `run.py`
