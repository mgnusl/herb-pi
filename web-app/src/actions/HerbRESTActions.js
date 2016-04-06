import { REQUEST_HERBS, RECEIVE_HERBS } from '../constants/ActionTypes.js';
import fetch from 'isomorphic-fetch';


/**
 * REST Actions - commanding the data flow back and forth between client and server
 * http://redux.js.org/docs/advanced/AsyncActions.html
 */

export function requestHerbs() {
	return {
		type: REQUEST_HERBS
	}
}

export function receiveHerbs(json) {
	return {
		type: RECEIVE_HERBS,
	    posts: json,
	    receivedAt: Date.now()
	}
}

/**
 * Thunks do not need to be pure.
 * See Redux docs for more information on thunks
 */

export function fetchHerbs() {

	return function(dispatch) {

		/* Pre-fetch dispatch so we can notify the user about fetching */
		dispatch(requestHerbs())
		
		return fetch('http://127.0.0.1:8000/plants')
			.then(response => response.json())
			.then(json =>

				/* Do any number of dispatches if needed */
				dispatch(receiveHerbs(json))
			)
	}
}