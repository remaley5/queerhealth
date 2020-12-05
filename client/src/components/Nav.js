import React, {useContext, useState, useEffect} from 'react';
import {AuthContext} from '../context';
import { NavLink } from 'react-router-dom';


const Nav = () => {
    const { setCurrentUserId, fetchWithCSRF } = useContext(AuthContext);
    const logoutUser = async () => {
        const response = await fetchWithCSRF('/logout', {
            method: 'POST',
            credentials: 'include'
        });
        if(response.ok) {
            setCurrentUserId(null)
        }
    }

    return (
        <div className='nav-bar'>
            <NavLink to='/'><button className='nav-link'>home</button></NavLink>
            <button onClick={logoutUser} className='nav-link'>Logout</button>
        </div>
    )
}

export default Nav;
