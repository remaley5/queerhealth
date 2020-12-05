import React, { useContext, useState, useEffect } from 'react';
import Nav from './Nav'
import { AuthContext } from '../context'



const Home = () => {
    const { fetchWithCSRF, currentUserId } = useContext(AuthContext);

    return (
        <div className='page'>
            <div className='page-header'>
                <div></div>
                <div className='nav'>
                    <>Hello</>
                </div>
            </div>
        </div>
    )
}

export default Home;
