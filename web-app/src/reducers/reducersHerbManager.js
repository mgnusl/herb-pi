import { SET_SELECTED_HERB, SET_TOP_CONTAINER_CONTENT, SET_CONTROL_BUTTON } from '../constants/ActionTypes';

const topContentInitialState = {
	contentIndex: 0,
	selected: -1
}

export function topContent(state = topContentInitialState, action) {
	switch(action.type) {
		case SET_TOP_CONTAINER_CONTENT:
			return Object.assign({}, state, {
				contentIndex: action.index
		});
	  	case SET_SELECTED_HERB:
	  		if(action.clickedHerb == state.selected) {
			    return Object.assign({}, state, {
			    	selected: -1
			    });
	  		} else {
	  			return Object.assign({}, state, {
	  				selected: action.clickedHerb
	  			});
	  		}
		default:
			return state;
	}
}


const bottomContentInitialState = {
	buttonIndex: 0
}

export function bottomContent(state = bottomContentInitialState, action) {
	switch(action.type) {
		case SET_CONTROL_BUTTON:
			return Object.assign({}, state, {
				buttonIndex: action.index
		});
		default:
			return state;	
	}
}