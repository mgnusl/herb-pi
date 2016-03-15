import { REQUEST_HERBS, RECEIVE_HERBS } from '../constants/ActionTypes.js';


export default function herbs(state = {
	isFetching: false,
	didInvalidate: false,
	items: []
}, action) {
	switch(action.type) {
		case REQUEST_HERBS:
			return Object.assign({}, state, {
				isFetching: true,
				didInvalidate: false
			})
		case RECEIVE_HERBS:
			return Object.assign({}, state, {
				isFetching: false,
				didInvalidate: false,
				items: action.posts,
				lastUpdate: action.receivedAt
			})
		default:
			return state
	}
}

