import React from 'react'
import { Redirect } from 'react-router-dom'
const Auth = (props) => {
	return (localStorage.getItem("needsstation-token") ? props.children : <Redirect to={'/login'}/>);
}
export default Auth;
