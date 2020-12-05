import React, { useState} from 'react';
import { useHistory, NavLink } from 'react-router-dom';



const SearchBar = () => {
    let history = useHistory();
    const [input, setInput] = useState('')

    const handleChange = e => {
        setInput(e.target.value)
    }

    const handleSubmit = () => {
        console.log(input)
        history.push('/search')
    }

    return (
        <div className='search__component'>
            <input type='text' className='search__value' value={input} onChange={handleChange} />
            <button className='search__label' className='search__button nav-link' placeholder='healthcare worker' onClick={handleSubmit}>search</button>
        </div>
    )
}

export default SearchBar;
