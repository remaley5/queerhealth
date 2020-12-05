import React, { useState, useEffect } from 'react'
import { Switch } from 'react-router-dom';

import { AuthContext } from './context';
import { ProtectedRoute, AuthRoute } from './Routes'
import LandingPage from './components/LandingPage'
import HomePage from './components/HomePage'
import Nav from './components/Nav'
import SearchPage from './components/SearchPage'
import ProfilePage from './components/ProfilePage'
import DiscoverPage from './components/DiscoverPage';

const App = () => {
    const [fetchWithCSRF, setFetchWithCSRF] = useState(() => fetch);
    const [currentUserId, setCurrentUserId] = useState(null);
    const [loading, setLoading] = useState(true);
    const [otherUserId, setOtherUserId] = useState(null);

    const authContextValue = {
        fetchWithCSRF,
        currentUserId,
        setCurrentUserId,
        otherUserId,
        setOtherUserId
    }

    useEffect(() => {
        async function restoreCSRF() {
            const response = await fetch('/api/csrf/restore', {
                method: 'GET',
                credentials: 'include'
            });
            if (response.ok) {
                const authData = await response.json();
                setFetchWithCSRF(() => {
                    return (resource, init) => {
                        if (init.headers) {
                            init.headers['X-CSRFToken'] = authData.csrf_token;
                        } else {
                            init.headers = {
                                'X-CSRFToken': authData.csrf_token,
                            };
                        }
                        return fetch(resource, init);
                    };
                });
                if (authData.current_user_id) {
                    setCurrentUserId(authData.current_user_id);
                }
            }
            setLoading(false);
        }
        restoreCSRF();
    }, []);

    if (loading) {
        return null;
    }

    return (
        <AuthContext.Provider value={authContextValue}>
            <div className='nav' currentUserId={currentUserId}>
                <Nav />
            </div>
            <Switch >
                <AuthRoute
                    path='/landing'
                    component={LandingPage}
                    currentUserId={currentUserId}
                />
                <ProtectedRoute
                    path="/"
                    exact
                    component={HomePage}
                    currentUserId={currentUserId}
                />
                <ProtectedRoute
                    path="/search"
                    exact
                    component={SearchPage}
                    currentUserId={currentUserId}
                />
                <ProtectedRoute
                    path="/profile"
                    exact
                    component={ProfilePage}
                    currentUserId={currentUserId}
                />
                <ProtectedRoute
                    path="/discover"
                    exact
                    component={DiscoverPage}
                    currentUserId={currentUserId}
                />
            </Switch>
        </AuthContext.Provider>
    )
}


export default App;
