import { HERB_FORM_CHANGE } from '../constants/ActionTypes.js';


export function herbFormChange(formValue) {
	return {
		type: HERB_FORM_CHANGE,
		formValue
	}
}