import React, { useState, useContext } from 'react';
import { AuthContext } from '../../context';
import { useHistory, NavLink } from 'react-router-dom';



function Signup({setSignupOpen}) {
  let [email, setEmail] = useState('');
  let [password, setPassword] = useState('');
  let [firstName, setFirstName] = useState('');
  let [lastName, setLastName] = useState('');
  let errors = useState([]);
  const setErrors = errors[1]
  const { fetchWithCSRF, setCurrentUserId } = useContext(AuthContext);
  let history = useHistory();

  const handleChange = (e) => {
    const { id, value } = e.target;
    switch (id) {
      case "email":
        setEmail(value);
        return;
      case "password":
        setPassword(value);
        return;
      case "firstName":
        setFirstName(value);
        return;
      case "lastName":
        setLastName(value);
        return;
      default:
        return;
    }
  }

  async function signupUser() {
    const response = await fetchWithCSRF('/api-user/', {
      method: 'POST',
      headers: {
        "Content-Type": "application/json",
      },
      credentials: 'include',
      body: JSON.stringify({
        email,
        password,
        firstName,
        lastName,
      })
    });

    const responseData = await response.json();
    if (!response.ok) {
      setErrors(responseData.errors);
    } else {
      setCurrentUserId(responseData.current_user_id)
      history.push(`/`)
    }
  };

  const handleSignUp = (e) => {
    e.preventDefault();
    signupUser();
  }

  const handleClose = () => {
    setSignupOpen(false)
  }

  return (
    <div className='auth__con'>
      <div className='auth__dialog'>
        <div>
          <button onClick={handleClose} className='exit-sign'>x</button>
          <h1 className='auth__title'>
            Welcome! Who are you?
              </h1>
          <form className='auth__form'>
            <label className='form-label' htmlFor="email">Email</label>
            <input
              id='email'
              type='email'
              className='auth__input'
              onChange={handleChange}
            />
            <label className='form-label' htmlFor="password">Password</label>
            <input
              id='password'
              type='password'
              className='auth__input'
              onChange={handleChange}
            />
            <label className='form-label' htmlFor="firstName">First Name</label>
            <input
              id='firstName'
              type='text'
              className='auth__input'
              onChange={handleChange}
            />
            <label className='form-label' htmlFor="lastName">Last Name</label>
            <input
              id='lastName'
              type='text'
              className='auth__input'
              onChange={handleChange}
            />
            <div className='auth_btns'>
              <button onClick={handleSignUp} className='auth__btn left'>Sign Up</button>
            </div>
          </form>
        </div>
      </div>
    </div>
  );
}
export default Signup;
