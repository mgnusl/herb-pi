import { SET_SELECTED_HERB } from '../constants/ActionTypes';


const initialState = {
	selectedHerb: -1
}

export default function selectedHerb(state = initialState, action) {
  switch (action.type) {
  case SET_SELECTED_HERB:
    return Object.assign({}, state, {
    	selectedHerb: action.clickedHerb
    });
  default:
    return state;
  }
}
