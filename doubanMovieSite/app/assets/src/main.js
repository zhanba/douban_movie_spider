import React from 'react';
import ReactDom from 'react-dom';
import App from './components/App';

import injectTapEventPlugin from 'react-tap-event-plugin';

// Needed for onTouchTap
// http://stackoverflow.com/a/34015469/988941
injectTapEventPlugin();

ReactDom.render(<App />, document.getElementById('app'));
