import { SET_TOP_CONTAINER_CONTENT, SET_CONTROL_BUTTON } from '../constants/ActionTypes.js';

export function setTopContainerContent(index) {
	return {
		type: SET_TOP_CONTAINER_CONTENT,
		index
	}
}

export function setControlButton(index) {
	return {
		type: SET_CONTROL_BUTTON,
		index
	}
}