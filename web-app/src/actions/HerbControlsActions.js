import { NEW_HERB, DELETE_HERB, SET_SELECTED_HERB } from '../constants/ActionTypes.js'

export function newHerb() {
	return {
		type: NEW_HERB
	};
}

export function deleteHerb() {
	return {
		type: DELETE_HERB
	};
}

export function setSelectedHerb(clickedHerb) {
	return {
		type: SET_SELECTED_HERB,
		clickedHerb
	}
}