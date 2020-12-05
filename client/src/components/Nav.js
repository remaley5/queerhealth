import React, { useContext, useState, useEffect } from 'react';
import { AuthContext } from '../context';
import { NavLink } from 'react-router-dom';
import SearchBar from './search/SearchBar'
import Login from './auth/Login';
import Signup from './auth/Signup'


const Nav = () => {
    const { setCurrentUserId, currentUserId, fetchWithCSRF } = useContext(AuthContext);
    let [loginOpen, setLoginOpen] = useState(false);
    let [signupOpen, setSignupOpen] = useState(false);

    const handleLoginOpen = () => {
        setLoginOpen(true);
    }

    const handleSignupOpen = () => {
        setSignupOpen(true);
    }

    const logoutUser = async () => {
        const response = await fetchWithCSRF('/logout', {
            method: 'POST',
            credentials: 'include'
        });
        if (response.ok) {
            setCurrentUserId(null)
        }
    }

    return (
        <div className='nav-bar'>
            { currentUserId ?
                <>
                    <NavLink to='/'><button className='nav-link'>home</button></NavLink>
                    <NavLink to='/discover'><button className='nav-link'>discover</button></NavLink>
                    <NavLink to='/profile'><button className='nav-link'>profile</button></NavLink>
                </> : null
            }
            <SearchBar />
            { currentUserId ?
                <button onClick={logoutUser} className='nav-link'>Logout</button>
                :
                <>
                    <div className='landing__btns'>
                        <button className='login__btn landing__btn' onClick={handleLoginOpen}>Sign in</button>
                        <button className='login__btn landing__btn' onClick={handleSignupOpen}>Sign up</button>
                    </div>
                    <dialog className='landing__dialog page-mask' open={loginOpen}>
                        <Login setLoginOpen={setLoginOpen} />
                    </dialog>
                    <dialog className='landing__dialog page-mask' open={signupOpen}>
                        <Signup setSignupOpen={setSignupOpen} />
                    </dialog>
                </>
            }
        </div>
    )
}

export default Nav;
