import React, { useState, useContext } from 'react';
import { useHistory } from 'react-router-dom';
import {AuthContext} from '../../context';


const Login = ({ setLoginOpen }) => {
    let [email, setEmail] = useState('')
    let [password, setPassword] = useState('')
    let [errors, setErrors] = useState([])
    const { fetchWithCSRF, setCurrentUserId} = useContext(AuthContext);
    let history = useHistory();

    const handlePasswordChange = e => {
        setPassword(e.target.value)
    }

    const handleEmailChange = (e) => {
        setEmail(e.target.value)
    }

    const handleSubmit = e => {
        e.preventDefault();
        loginUser(email, password);
    }

    const handleDemoSubmit = (e) => {
        e.preventDefault();
        loginUser("demo@aa.io", "password");
    }

    const handleClose = () => {
        setLoginOpen(false)
    }

    async function loginUser(email, password) {
        const response = await fetchWithCSRF('/login', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            credentials: 'include',
            body: JSON.stringify({
                email,
                password
            })
        })

        const responseData = await response.json();
        if (!response.ok) {
            setErrors(responseData.errors);
        } else {
            setLoginOpen(false);
            setCurrentUserId(responseData.current_user_id)
            history.push('/')
        }
    }

    return (
        <div className='auth__con'>
            <div className='auth__dialog'>
                <div>
                    <button onClick={handleClose} className='exit-sign'>x</button>
                    <h1 className='auth__title'>
                        Sign in
              </h1>
                    <div className='auth__errors' id="form-title" onClose={handleClose}>
                        {errors.length ? errors.map((err) => <li key={err}>{err}</li>) : ''}
                    </div>
                    <div className='auth__form'>
                        <label className='form-label' htmlFor="email">Email</label>
                        <input
                            className='auth__text'
                            id="email"
                            type="email"
                            placeholder="Email"
                            onChange={handleEmailChange}
                        />
                        <label className='form-label' htmlFor="password">Password</label>
                        <input
                            className='auth__text'
                            id="password"
                            type="password"
                            placeholder="Password"
                            onChange={handlePasswordChange}
                        />
                    </div>
                    <div className='auth__btns'>
                        <button className='auth__btn left' onClick={handleSubmit}>login</button>
                        <button className='auth__btn right' onClick={handleDemoSubmit}>Demo</button>
                    </div>
                </div>
            </div>
        </div>
    )
}

export default Login;
